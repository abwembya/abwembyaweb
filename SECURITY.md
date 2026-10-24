# Security

This repository builds a static portfolio. Do not commit credentials, private
keys or private documents. Report a suspected vulnerability privately to
contact@abwembya.com; do not post credentials or exploit details in a public PR.

Local validation (Ruby 3.3 recommended):

```sh
bundle install
bundle exec bundler-audit check --update
JEKYLL_ENV=production bundle exec jekyll build --safe --strict_front_matter
python3 scripts/check-site-security.py
```

Use the Jekyll/Compose server only for local development. Production remains
GitHub Pages. See [the dated audit](docs/security-audit-2026-10-24.md) for findings,
validation limits and hosting/DNS checks that require account access.
