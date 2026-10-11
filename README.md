# cookie-scope-witness

Explain host-only/domain, slash-boundary path and secure eligibility for each supplied cookie and request.

For web developers debugging which cookie reaches a route. Same cookie names at several domains and paths obscure why a request sees different state.

## Quickstart

Python 3.10 or newer. No runtime dependencies or service account. Build tooling downloads require access to PyPI; this repository is not published on PyPI.

```bash
git clone https://github.com/nripankadas07/cookie-scope-witness.git
cd cookie-scope-witness
python -m venv .venv
.venv/bin/python -m pip install .
.venv/bin/cookie-scope-witness example.json
```

Windows: use `.venv\Scripts\python.exe` and `.venv\Scripts\cookie-scope-witness.exe` instead. Windows is not part of the tested CI matrix.

The supplied example is synthetic. JSON success exits 0, including valid findings such as unmet quorum, ineligible cookie or an ordering cycle; malformed or unsupported input exits 2 with an `error` field. Argument usage errors use argparse's stderr. No input files or live services are modified.

## Scope and limits

Only already-normalized cookie records: no Set-Cookie parsing, public suffix list, SameSite, expiry, partitioning, prefix acceptance, IDNA or browser conformance. IDs must not contain cookie values. URLs and domains remain visible in local output.

Input limits: 256 KiB JSON; at most 200 cookies and 200 requests; request URLs at most 4,096 characters.

## Inspectable evidence

- [Demo and input schema](DEMO.md)
- [Candidate brief and comparisons](RESEARCH.md)
- [Validation and untested behavior](VALIDATION.md)
- [Build instructions](BUILDING.md)
- [Security reporting](SECURITY.md) and [support/contribution guidance](SUPPORT.md)

MIT; original implementation. No competitor code or branding copied. No speed, adoption or superiority claim. CI executes core regressions, the demo, a fresh wheel installation outside source and the documented source installation on Python 3.10, 3.12 and 3.14.
