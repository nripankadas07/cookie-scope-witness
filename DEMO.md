# Runnable demo

```bash
python demo.py
python cookie_scope_witness.py example.json
```

`demo.py` checks a synthetic success and malformed-input rejection. The installed command uses the same arguments.

## Input contract

```text
{
  "cookies": [
    {
      "id": "session",
      "domain": "example.com",
      "path": "/app",
      "host_only": false,
      "secure": true
    },
    {
      "id": "local",
      "domain": "example.com",
      "path": "/",
      "host_only": true,
      "secure": false
    }
  ],
  "requests": [
    "https://api.example.com/app/item",
    "http://example.com/apple"
  ]
}
```

Inspect `test_contract.py` for independently specified expected outcomes, including boundary failures. Only already-normalized cookie records: no Set-Cookie parsing, public suffix list, SameSite, expiry, partitioning, prefix acceptance, IDNA or browser conformance. IDs must not contain cookie values. URLs and domains remain visible in local output.
