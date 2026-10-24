"""Check the generated site, including the print layout, without extra packages."""
from html.parser import HTMLParser
from pathlib import Path


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.policy = None
        self.referrer = None
        self.scripts = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'meta':
            if attrs.get('http-equiv', '').lower() == 'content-security-policy':
                self.policy = attrs['content']
            if attrs.get('name') == 'referrer':
                self.referrer = attrs.get('content')
        if tag == 'script':
            self.scripts.append(attrs)
            if not self.policy:
                self.errors.append('script appears before CSP')
            if 'src' not in attrs and attrs.get('type') != 'application/ld+json':
                self.errors.append('executable inline script')
        if any(key.lower().startswith('on') for key in attrs):
            self.errors.append('inline event handler')
        for key in ('src', 'href'):
            if attrs.get(key, '').strip().lower().startswith('javascript:'):
                self.errors.append('JavaScript URL')
        if tag == 'a' and attrs.get('target') == '_blank':
            if 'noopener' not in attrs.get('rel', '').split():
                self.errors.append('new tab without explicit noopener')


pages = list(Path('_site').rglob('*.html'))
assert pages, 'Build the site first'
for path in pages:
    page = Page()
    page.feed(path.read_text())
    assert page.policy, f'{path}: missing CSP'
    directives = dict(part.strip().split(' ', 1) for part in page.policy.split(';') if ' ' in part.strip())
    for key, value in [('default-src', "'self'"), ('base-uri', "'none'"),
                       ('object-src', "'none'"), ('frame-src', "'none'"),
                       ('form-action', "'none'")]:
        assert directives.get(key) == value, f'{path}: {key}'
    assert "'unsafe-inline'" not in directives['script-src'], path
    assert "'unsafe-eval'" not in page.policy, path
    assert page.referrer == 'strict-origin-when-cross-origin', path
    assert not page.errors, f'{path}: {page.errors}'
    for script in page.scripts:
        src = script.get('src')
        if src and src.startswith('/'):
            asset = Path('_site') / src.lstrip('/').split('?')[0]
            assert asset.is_file(), f'{path}: missing {src}'
for name in ('Gemfile', 'Gemfile.lock', 'docker-compose.yml', 'SECURITY.md',
             'scripts', 'tests', 'docs', 'vendor', 'README.html', 'LICENSE.html'):
    assert not (Path('_site') / name).exists(), f'Build tool/document published: {name}'
assert not Path('_site/assets/plugins/bootstrap/js/bootstrap.js').exists()
print(f'Security checks passed for {len(pages)} generated HTML pages')
