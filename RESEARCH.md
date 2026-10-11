# Candidate brief and fair comparison — 11 October 2026

**User:** Web developers debugging which cookie reaches a route. **Painful task:** Same cookie names at several domains and paths obscure why a request sees different state.

**Current alternatives:** Browser DevTools, Requests cookie jars, curl and Tough Cookie. **Smallest useful capability:** Explain host-only/domain, slash-boundary path and secure eligibility for each supplied cookie and request.

**Demand evidence:** inferred from the documented protocol/workflow and established comparable projects, not a verified request for this new product. Current comparable READMEs, representative implementation/docs and recent issue/PR lists were reviewed. Those issues do not prove demand for our feature, and no competitor absence is asserted. See [portfolio research evidence](https://github.com/nripankadas07/nripankadas07/blob/main/docs/RESEARCH_2026-10-11.json) for exact observations and code/doc URLs.

**Acceptance:** the 16 core contract tests must pass, the demo must check its known output and malformed input, and a clean installed command outside source must reproduce both success and error behavior. Scope limits remain visible in README/output. LIVE additionally requires final default-branch CI and verified docs/install path.

**Discovery:** descriptive GitHub topics, the profile chronological index, and a reproducible linked demo. No promised growth, invented users or unsolicited third-party issue promotion.

**Distinctness:** compared with all 158 existing owned repository names and today's other four briefs. Cookie routing is separate from CSP/cache/robots checks; SOA rollout arithmetic is separate from mail DNS topology and DNS blocking; expression alternatives are separate from SBOM inventory/dependency audits; startup pull-in versus ordering is separate from general migration plans; captured packet accounting is separate from live LAN delivery/network discovery. These are five independent capabilities, not subdivisions of one product.

## Live GitHub research

Queries: `cookie scope language:Python sort:stars`, `cookies sort:stars`. Observation date 2026-10-11 UTC. GitHub query results were relevance-screened; some broad queries include unrelated repositories. Highest-star relevant comparable **found** in this research: [psf/requests](https://github.com/psf/requests) (54563 stars). Coverage is limited; this is not an exhaustive global ranking. Additional established tools were inspected directly. Stars are discovery evidence, not performance.

| Comparable | Stars | Latest push observed (UTC) | Documented workflow |
| --- | ---: | --- | --- |
| [psf/requests](https://github.com/psf/requests) | 54563 | 2026-09-28T16:55:48Z | A simple, yet elegant, HTTP library. |
| [curl/curl](https://github.com/curl/curl) | 43151 | 2026-10-10T22:10:45Z | A command line tool and library for transferring data with URL syntax, supporting DICT, FILE, FTP, FTPS, GOPHER, GOPHERS, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, MQTT, MQTTS, POP3, POP3S, RTSP, SCP, SFTP, SMB, SMBS, SMTP, SMTPS, TELNET, TFTP, WS and WSS. libcurl offers a myriad of powerful features |
| [salesforce/tough-cookie](https://github.com/salesforce/tough-cookie) | 1064 | 2026-10-09T18:02:05Z | RFC6265 Cookies and CookieJar for Node.js |

## Workflow tradeoffs

Established alternatives have broader capabilities, documentation, examples and ecosystems; installability varies by language and platform. Ours offers a narrow one-command synthetic example and a zero-runtime-dependency Python source install. No competitor installation was timed or independently stress-tested in this run. No measured time-to-first-result, reliability, support responsiveness, performance or superiority claim. Current comparable licenses are recorded in linked research metadata; none of their implementation or prose was reused. Our license is MIT. Support is best-effort GitHub reports with no SLA.

**Limits and negative result:** Only already-normalized cookie records: no Set-Cookie parsing, public suffix list, SameSite, expiry, partitioning, prefix acceptance, IDNA or browser conformance. IDs must not contain cookie values. URLs and domains remain visible in local output. Broader production needs should use the established tools. Runnable local success demonstrates our behavior only.
