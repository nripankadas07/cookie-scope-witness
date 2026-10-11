"""Offline host/path/secure cookie routing witnesses; no browser access."""
import argparse, ipaddress, json, re, sys
from pathlib import Path
from urllib.parse import urlsplit

def host(value):
    if not isinstance(value,str) or not value or len(value)>253:
        raise ValueError('invalid host')
    value=value.lower().rstrip('.')
    try: return str(ipaddress.ip_address(value))
    except ValueError: pass
    if not all(re.fullmatch(r'[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?',p) for p in value.split('.')):
        raise ValueError('ASCII DNS host required')
    return value

def explain(data):
    if not isinstance(data,dict) or set(data)!={'cookies','requests'}: raise ValueError('expected cookies and requests')
    cs,rs=data['cookies'],data['requests']
    if not isinstance(cs,list) or not isinstance(rs,list) or len(cs)>200 or len(rs)>200: raise ValueError('at most 200 cookies and requests')
    cookies=[];ids=set()
    for c in cs:
        if not isinstance(c,dict) or set(c)!={'id','domain','path','host_only','secure'}: raise ValueError('invalid cookie fields')
        if not isinstance(c['id'],str) or not c['id'] or len(c['id'])>100 or c['id'] in ids: raise ValueError('unique nonempty cookie id required')
        ids.add(c['id'])
        if type(c['host_only']) is not bool or type(c['secure']) is not bool: raise ValueError('flags must be boolean')
        if not isinstance(c['path'],str) or not c['path'].startswith('/') or any(ord(x)<32 for x in c['path']): raise ValueError('absolute cookie path required')
        d=host(c['domain'].lstrip('.') if isinstance(c['domain'],str) else c['domain']);cookies.append((c,d))
    output=[]
    for u in rs:
        if not isinstance(u,str) or len(u)>4096 or any(ord(x)<33 for x in u): raise ValueError('invalid request URL')
        p=urlsplit(u)
        if p.scheme not in ('http','https') or not p.hostname or p.username is not None or p.password is not None: raise ValueError('HTTP(S) URL without credentials required')
        h=host(p.hostname);p.port;path=p.path or '/';rows=[]
        for c,d in cookies:
            try: ipaddress.ip_address(h); is_ip=True
            except ValueError: is_ip=False
            reasons=[]
            if not (h==d or (not c['host_only'] and not is_ip and h.endswith('.'+d))): reasons.append('domain')
            cp=c['path']
            if not (path==cp or (path.startswith(cp) and (cp.endswith('/') or path[len(cp):].startswith('/')))): reasons.append('path')
            if c['secure'] and p.scheme!='https': reasons.append('secure')
            rows.append({'id':c['id'],'eligible':not reasons,'blocked_by':reasons})
        output.append({'request':u,'cookies':rows,'eligible_ids':[x['id'] for x in rows if x['eligible']]})
    return {'requests':output,'scope':'domain/path/secure only; not browser acceptance or SameSite'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('snapshot');a=p.parse_args()
    try:
        with Path(a.snapshot).open('rb') as f: raw=f.read(262145)
        if len(raw)>262144: raise ValueError('snapshot exceeds 256 KiB')
        print(json.dumps(explain(json.loads(raw)),sort_keys=True));return 0
    except (ValueError,OSError,TypeError,KeyError,UnicodeError) as e: print(json.dumps({'error':str(e)}));return 2
if __name__=='__main__': sys.exit(main())
