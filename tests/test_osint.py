"""Tests for the OSINT pipeline (build_clusters, infer_candidates, fetch_ct_candidates)
and the inferred=True API flag.
"""
from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import build_clusters  # noqa: E402
import fetch_ct_candidates  # noqa: E402
import infer_candidates  # noqa: E402

PKG_DIR = ROOT / "disposable_email"


# --------------------------------------------------------------------------
# Pure-function unit tests
# --------------------------------------------------------------------------

class TestSharedInfraMatching:
    def test_exact_match(self):
        assert build_clusters.is_shared("mx.cloudflare.net", ["mx.cloudflare.net"])

    def test_suffix_match(self):
        assert build_clusters.is_shared("route1.mx.cloudflare.net", ["mx.cloudflare.net"])

    def test_deep_suffix(self):
        assert build_clusters.is_shared(
            "deep.nested.route.mx.cloudflare.net", ["mx.cloudflare.net"]
        )

    def test_no_match(self):
        assert not build_clusters.is_shared("mail.mailinator.com", ["mx.cloudflare.net"])

    def test_case_insensitive(self):
        assert build_clusters.is_shared("ROUTE1.MX.CLOUDFLARE.NET", ["mx.cloudflare.net"])

    def test_trailing_dot_stripped(self):
        assert build_clusters.is_shared("route1.mx.cloudflare.net.", ["mx.cloudflare.net"])

    def test_empty_suffix_list(self):
        assert not build_clusters.is_shared("anything.com", [])

    def test_different_tld_not_match(self):
        assert not build_clusters.is_shared("mx.cloudflare.com", ["mx.cloudflare.net"])

    def test_partial_suffix_not_match(self):
        # 'foo.example.com' should NOT match suffix 'ample.com'
        assert not build_clusters.is_shared("foo.example.com", ["ample.com"])


class TestCTNormalize:
    def test_lowercase(self):
        assert fetch_ct_candidates.normalize_name("EXAMPLE.COM") == "example.com"

    def test_strip_wildcard(self):
        assert fetch_ct_candidates.normalize_name("*.example.com") == "example.com"

    def test_strips_whitespace(self):
        assert fetch_ct_candidates.normalize_name("  example.com\n") == "example.com"

    def test_reject_invalid_tld(self):
        assert fetch_ct_candidates.normalize_name("foo.bogusbogus") is None

    def test_reject_single_label(self):
        assert fetch_ct_candidates.normalize_name("invalid") is None

    def test_reject_with_space(self):
        assert fetch_ct_candidates.normalize_name("example .com") is None

    def test_reject_with_slash(self):
        assert fetch_ct_candidates.normalize_name("example.com/path") is None

    def test_normalize_leading_dot(self):
        # Leading dots are stripped (treated like wildcards).
        assert fetch_ct_candidates.normalize_name(".example.com") == "example.com"

    def test_reject_numeric_tld(self):
        assert fetch_ct_candidates.normalize_name("foo.123") is None

    def test_accept_freemail_tld(self):
        assert fetch_ct_candidates.normalize_name("trash.tk") == "trash.tk"


# --------------------------------------------------------------------------
# Pipeline integration tests using synthetic data
# --------------------------------------------------------------------------

@pytest.fixture
def synthetic_pipeline(tmp_path):
    """Build a synthetic resolution.sqlite with three clusters:
        - mail.fakedisp.com   : 6 disposables + 1 candidate (high-confidence)
        - mx.cloudflare.net   : 4 disposables (shared infra, should be excluded)
        - mail.smallsite.com  : 1 disposable (below threshold)
    Returns paths the test can use.
    """
    db = tmp_path / "resolution.sqlite"
    domains_file = tmp_path / "domains.txt"
    strict_file = tmp_path / "domains_strict.txt"
    candidates_file = tmp_path / "candidates.txt"
    shared_infra = tmp_path / "shared_infra.txt"
    out_inferred = tmp_path / "domains_inferred.txt"

    domains_file.write_text(
        "# disposable list\n"
        "fakedisp1.com\nfakedisp2.com\nfakedisp3.com\n"
        "fakedisp4.com\nfakedisp5.com\nfakedisp6.com\n"
        "cf-disposable1.com\ncf-disposable2.com\n"
        "cf-disposable3.com\ncf-disposable4.com\n"
        "tinydisp.com\n"
    )
    strict_file.write_text("# strict\n")
    candidates_file.write_text(
        "# candidates\n"
        "newdomain-suspect.com\n"     # shares MX with disposables -> should be inferred
        "legit-on-cloudflare.com\n"   # shares CF MX -> should NOT be inferred
        "isolated-candidate.com\n"    # not on any cluster -> should NOT be inferred
    )
    shared_infra.write_text(
        "# shared infra denylist\n"
        "mx.cloudflare.net\n"
    )

    conn = sqlite3.connect(str(db))
    conn.executescript("""
        CREATE TABLE domain_resolution (
            domain      TEXT PRIMARY KEY,
            resolved_at TEXT NOT NULL,
            status      TEXT NOT NULL,
            mx_hosts    TEXT,
            ips         TEXT
        );
    """)
    rows = [
        # Cluster A: mail.fakedisp.com — 6 disposables, high-confidence
        ("fakedisp1.com", "MX_OK", ["mail.fakedisp.com"], ["10.0.0.1"]),
        ("fakedisp2.com", "MX_OK", ["mail.fakedisp.com"], ["10.0.0.1"]),
        ("fakedisp3.com", "MX_OK", ["mail.fakedisp.com"], ["10.0.0.1"]),
        ("fakedisp4.com", "MX_OK", ["mail.fakedisp.com"], ["10.0.0.1"]),
        ("fakedisp5.com", "MX_OK", ["mail.fakedisp.com"], ["10.0.0.1"]),
        ("fakedisp6.com", "MX_OK", ["mail.fakedisp.com"], ["10.0.0.1"]),
        # Cluster B: route1.mx.cloudflare.net — 4 disposables, but shared infra
        ("cf-disposable1.com", "MX_OK", ["route1.mx.cloudflare.net"], ["172.66.1.1"]),
        ("cf-disposable2.com", "MX_OK", ["route2.mx.cloudflare.net"], ["172.66.1.2"]),
        ("cf-disposable3.com", "MX_OK", ["route1.mx.cloudflare.net"], ["172.66.1.1"]),
        ("cf-disposable4.com", "MX_OK", ["route1.mx.cloudflare.net"], ["172.66.1.1"]),
        # Cluster C: mail.smallsite.com — 1 disposable, below threshold
        ("tinydisp.com", "MX_OK", ["mail.smallsite.com"], ["10.99.99.99"]),
        # Candidate domains' resolutions
        ("newdomain-suspect.com", "MX_OK", ["mail.fakedisp.com"], ["10.0.0.1"]),
        ("legit-on-cloudflare.com", "MX_OK", ["route1.mx.cloudflare.net"], ["172.66.1.1"]),
        ("isolated-candidate.com", "MX_OK", ["mail.unknownhost.com"], ["192.168.1.1"]),
    ]
    for domain, status, mx, ips in rows:
        conn.execute(
            "INSERT INTO domain_resolution VALUES (?, ?, ?, ?, ?)",
            (domain, "2026-04-29T02:00:00+00:00", status,
             json.dumps(mx), json.dumps(ips)),
        )
    conn.commit()
    conn.close()

    return {
        "db": db,
        "domains": domains_file,
        "strict": strict_file,
        "candidates": candidates_file,
        "shared_infra": shared_infra,
        "out_inferred": out_inferred,
    }


def run_main(module, argv):
    """Run a script's main() with patched argv. Returns exit code."""
    with patch.object(sys, "argv", ["script"] + argv):
        return module.main()


class TestPipeline:
    def test_build_clusters_creates_tables(self, synthetic_pipeline):
        sp = synthetic_pipeline
        rc = run_main(build_clusters, [
            "--db", str(sp["db"]),
            "--domains", str(sp["domains"]),
            "--shared-infra", str(sp["shared_infra"]),
        ])
        assert rc == 0

        conn = sqlite3.connect(str(sp["db"]))
        # mail.fakedisp.com: 6 disposables + 1 candidate = 7 total domain_count, 6 disposable_count
        row = conn.execute(
            "SELECT domain_count, disposable_count, is_shared_infra"
            " FROM mx_cluster WHERE mx_host = 'mail.fakedisp.com'"
        ).fetchone()
        assert row == (7, 6, 0)

        # route1.mx.cloudflare.net: marked shared infra
        row = conn.execute(
            "SELECT is_shared_infra FROM mx_cluster"
            " WHERE mx_host = 'route1.mx.cloudflare.net'"
        ).fetchone()
        assert row == (1,)
        conn.close()

    def test_infer_promotes_only_correct_candidates(self, synthetic_pipeline):
        sp = synthetic_pipeline
        # Build clusters first
        run_main(build_clusters, [
            "--db", str(sp["db"]),
            "--domains", str(sp["domains"]),
            "--shared-infra", str(sp["shared_infra"]),
        ])
        # Then infer
        rc = run_main(infer_candidates, [
            "--db", str(sp["db"]),
            "--candidates", str(sp["candidates"]),
            "--domains", str(sp["domains"]),
            "--domains-strict", str(sp["strict"]),
            "--out", str(sp["out_inferred"]),
            "--min-disposable", "5",
        ])
        assert rc == 0

        body = sp["out_inferred"].read_text(encoding="utf-8")
        promoted = {
            line.strip() for line in body.splitlines()
            if line.strip() and not line.startswith("#")
        }
        # Exactly one candidate should be promoted
        assert promoted == {"newdomain-suspect.com"}
        # Cloudflare-shared candidate must NOT be promoted (shared-infra denylist)
        assert "legit-on-cloudflare.com" not in promoted
        # Isolated candidate must NOT be promoted (no cluster overlap)
        assert "isolated-candidate.com" not in promoted

    def test_infer_respects_min_disposable_threshold(self, synthetic_pipeline):
        sp = synthetic_pipeline
        # Tighten threshold to 7 — fakedisp cluster has only 6 disposables, no longer qualifies
        run_main(build_clusters, [
            "--db", str(sp["db"]),
            "--domains", str(sp["domains"]),
            "--shared-infra", str(sp["shared_infra"]),
        ])
        run_main(infer_candidates, [
            "--db", str(sp["db"]),
            "--candidates", str(sp["candidates"]),
            "--domains", str(sp["domains"]),
            "--domains-strict", str(sp["strict"]),
            "--out", str(sp["out_inferred"]),
            "--min-disposable", "7",
        ])
        body = sp["out_inferred"].read_text(encoding="utf-8")
        promoted = {
            line.strip() for line in body.splitlines()
            if line.strip() and not line.startswith("#")
        }
        assert promoted == set()  # threshold too tight, nothing promoted

    def test_infer_skips_already_listed(self, synthetic_pipeline):
        """A candidate that is already on the disposable list should not be re-promoted."""
        sp = synthetic_pipeline
        # Add 'newdomain-suspect.com' to the disposable list
        sp["domains"].write_text(
            sp["domains"].read_text() + "newdomain-suspect.com\n"
        )
        run_main(build_clusters, [
            "--db", str(sp["db"]),
            "--domains", str(sp["domains"]),
            "--shared-infra", str(sp["shared_infra"]),
        ])
        run_main(infer_candidates, [
            "--db", str(sp["db"]),
            "--candidates", str(sp["candidates"]),
            "--domains", str(sp["domains"]),
            "--domains-strict", str(sp["strict"]),
            "--out", str(sp["out_inferred"]),
            "--min-disposable", "5",
        ])
        body = sp["out_inferred"].read_text(encoding="utf-8")
        promoted = {
            line.strip() for line in body.splitlines()
            if line.strip() and not line.startswith("#")
        }
        assert "newdomain-suspect.com" not in promoted


# --------------------------------------------------------------------------
# API: inferred=True flag
# --------------------------------------------------------------------------

@pytest.fixture
def with_inferred_fixture():
    """Write a temporary domains_inferred.txt and reset module caches."""
    inferred_file = PKG_DIR / "domains_inferred.txt"
    backup = inferred_file.read_text(encoding="utf-8") if inferred_file.exists() else None
    inferred_file.write_text(
        "# test fixture\n"
        "test-inferred-domain.example\n"
        "shady.example\n",
        encoding="utf-8",
    )
    import disposable_email
    disposable_email._cache = {}
    disposable_email._inferred_cache = None
    yield
    if backup is not None:
        inferred_file.write_text(backup, encoding="utf-8")
    else:
        inferred_file.unlink()
    disposable_email._cache = {}
    disposable_email._inferred_cache = None


class TestInferredFlag:
    def test_default_does_not_include_inferred(self, with_inferred_fixture):
        from disposable_email import is_disposable
        assert is_disposable("test-inferred-domain.example") is False

    def test_inferred_flag_includes_inferred(self, with_inferred_fixture):
        from disposable_email import is_disposable
        assert is_disposable("test-inferred-domain.example", inferred=True) is True

    def test_inferred_flag_with_email(self, with_inferred_fixture):
        from disposable_email import is_disposable
        assert is_disposable("user@shady.example", inferred=True) is True

    def test_strict_and_inferred_combined(self, with_inferred_fixture):
        from disposable_email import is_disposable
        assert is_disposable(
            "test-inferred-domain.example", strict=True, inferred=True
        ) is True

    def test_get_domains_inferred_is_superset(self, with_inferred_fixture):
        from disposable_email import get_domains
        plain = get_domains()
        with_inf = get_domains(inferred=True)
        assert plain.issubset(with_inf)
        assert "test-inferred-domain.example" in with_inf
        assert "test-inferred-domain.example" not in plain

    def test_domain_count_inferred_larger(self, with_inferred_fixture):
        from disposable_email import domain_count
        assert domain_count(inferred=True) > domain_count()

    def test_inferred_subdomain_stripping(self, with_inferred_fixture):
        from disposable_email import is_disposable
        assert is_disposable("mail.shady.example", inferred=True) is True

    def test_is_valid_inverse_with_inferred(self, with_inferred_fixture):
        from disposable_email import is_disposable, is_valid
        for domain in ["test-inferred-domain.example", "gmail.com", "mailinator.com"]:
            assert is_valid(domain, inferred=True) is not is_disposable(domain, inferred=True)


class TestInferredFlagAbsentFile:
    """When domains_inferred.txt is absent, inferred=True should still work and add nothing."""

    def test_no_inferred_file_no_error(self):
        # No fixture used here — just test default state where the file may or may not exist.
        from disposable_email import is_disposable, domain_count
        # Should not raise even if file absent
        assert is_disposable("gmail.com", inferred=True) is False
        assert domain_count(inferred=True) >= domain_count()
