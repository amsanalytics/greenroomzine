"""Check the static export without third-party Python packages."""
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).parent
class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.refs, self.anchors = set(), [], []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'): self.ids.add(a['id'])
        for name in ('src', 'data-src', 'data-image', 'poster'):
            if a.get(name): self.refs.append(a[name])
        if tag == 'link' and a.get('href'): self.refs.append(a['href'])
        if tag == 'a' and a.get('href', '').startswith('#'): self.anchors.append(a['href'][1:])

page = Page()
page.feed((ROOT / 'index.html').read_text(encoding='utf-8'))
missing = []
for ref in page.refs:
    u = urlsplit(ref)
    if not u.scheme and not u.netloc and u.path and not (ROOT / unquote(u.path)).is_file():
        missing.append(ref)
for url, entry in json.loads((ROOT / 'asset-manifest.json').read_text(encoding='utf-8')).items():
    if not (ROOT / entry['path']).is_file(): missing.append(entry['path'])
bad_anchors = sorted(set(page.anchors) - page.ids)
assert not missing, f'Missing local assets: {missing}'
assert not bad_anchors, f'Missing anchor targets: {bad_anchors}'
assert (ROOT / 'assets/umbrellas.mp4').stat().st_size > 100000
print(f'PASS: {len(page.refs)} asset references, {len(page.anchors)} anchor links, and the asset manifest.')
