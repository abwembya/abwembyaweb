# Security audit — 24 October 2026

Scope: `abwembya/abwembyaweb` at `b306cad88def04f20c7ad493e6fb1b03cc00bc7e`, fetched Git history and public DNS for `abwembya.com`. Changes are proposed on a separate branch. No merge, deployment, DNS change, repository visibility change or settings mutation was performed.

## Findings and proposed fixes

| Finding | Exposure and evidence | Branch remediation |
| --- | --- | --- |
| Vulnerable Ruby dependencies in the committed lockfile | `bundler-audit` found 31 distinct package/advisory pairs across seven packages (50 results when Nokogiri's two platforms are counted). These are developer/build dependencies, not a public Ruby application. | Remove the unused `github-pages` umbrella dependency; update the remaining compatible dependencies and establish security floors. The resolved bundle passes the same audit with no ignored advisories. |
| Vendored Bootstrap JavaScript 3.3.6 | `assets/plugins/bootstrap/js/bootstrap.js` contains the legacy vulnerable JavaScript plugins. No current page loads it, so no working site XSS exploit was established. | Remove the unused JavaScript and its npm helper; keep Bootstrap CSS and all existing visual assets. |
| No source-defined CSP or referrer policy | Both normal and print pages use `_includes/head.html`. No untrusted visitor input, authentication, backend or form handler was found. This is missing defense in depth, not demonstrated injection. | Add an early CSP meta policy and referrer policy. Move theme initialization and optional analytics to local scripts; replace the print `onclick` with an event listener. Scripts do not require `unsafe-inline` or `unsafe-eval`. |
| Development server exposed on all interfaces | `_config.yml` used `host: 0.0.0.0`; Compose published port 4000 on every host interface. | Bind local Jekyll and the host side of Compose to `127.0.0.1`; enable safe mode. Container-internal binding remains necessary for the published port. |
| Some external links lacked explicit opener isolation | Template links used `target="_blank"` without `rel="noopener"`. Modern browsers usually isolate these implicitly. | Add explicit `noopener` for older browsers without changing destinations. |
| No repository-defined validation workflow or update bot | No workflow files existed at the reviewed head. | Add a build/security workflow with `contents: read`, immutable action SHAs, no persisted checkout credentials, a timeout, no secrets, no deployment permissions and no deployment steps. Add weekly Dependabot PRs. |

The old lock includes ActiveSupport 6.1.7.10, Addressable 2.8.7, concurrent-ruby 1.3.5, Faraday 2.8.1, Nokogiri 1.13.10, REXML 3.4.1 and rubyzip 2.4.1. ActiveSupport, Faraday, Nokogiri and rubyzip are removed along with unused plugins; Addressable resolves to 2.9.0, concurrent-ruby to 1.3.8 and REXML to 3.4.4.

Jekyll 3.10.0 matches the latest successful managed production build (see deployment evidence below). The existing Ruby Sass 3.7.4 engine is retained to preserve CSS output. It is end of life and deserves a separately tested future migration; an audit pass is not a support guarantee.

## Secrets and source review

Scanned 4,212 unique Git blobs across 465 commits reachable from all fetched branches. Signature checks covered private keys, GitHub tokens, AWS access-key IDs, Slack tokens, Google API keys and quoted credential assignments. No matches were found. This is a signature-based scan, not a guarantee against arbitrary passwords, encrypted secrets, unreachable objects, untracked files, provider-side secrets or secrets inside binary documents.

Reviewed layouts, includes, site configuration, JavaScript, dependency manifests and references to scripts, remote resources, inline handlers, HTTP assets and HTML injection sinks. `pdf-generator.js` contains `innerHTML` fed by a same-origin print-page fetch, but is not loaded by the site; no attacker-controlled input path was established. No speculative XSS fix was applied to it. Public contact information and analytics IDs are not credentials.

## DNS evidence

Queries used Google's DNS-over-HTTPS resolver on the audit date. These are public observations, not registrar-account settings.

| Record | Observed result |
| --- | --- |
| Apex A | `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` — GitHub Pages addresses |
| Apex AAAA | No records; IPv6 is optional |
| `www` CNAME | `abwembya.github.io.` |
| NS | `launch1.spaceship.net.`, `launch2.spaceship.net.` |
| DNSSEC | DS record present; resolver reports authenticated data (`AD: true`) |
| CAA | No records; this alone is not a vulnerability |
| `_github-pages-challenge-abwembya.abwembya.com` TXT | NXDOMAIN; expected verification record absent. Account verification status was inaccessible. |
| `security-audit-20261024.abwembya.com` A | NXDOMAIN; no wildcard response for this sampled hostname. This does not establish that every possible subdomain is safe. |

The apex and `www` records agree with the repository's `CNAME` (`abwembya.com`) and canonical URL. No dangling public target was established.

## GitHub Actions and deployment settings

The `master` branch API reports `protected: false`; the repository rulesets API returns an empty list. Direct inspection of branch-protection administration is denied to this integration. Require PR review and the new validation check on `master` as a follow-up setting change; the branch cannot enforce its own protection.

The latest successful existing workflow is [Pages run 38001568821](https://github.com/abwembya/abwembyaweb/actions/runs/38001568821), triggered dynamically from `master` on 9 October 2026. Its jobs build and deploy GitHub Pages. Build logs report managed `github-pages v232` / `jekyll v3.10.0` and explicitly warn that the old committed Gemfile cannot be satisfied. Consequently, updating this PR's lockfile fixes the reproducible local/CI bundle; it does **not** update the GitHub-managed Pages container or its dependencies. This PR retains the current deployment mechanism.

The connector cannot read the Pages configuration or account-level domain verification. Public unauthenticated Pages/settings API requests also did not grant access. Environment approvals, Actions default token permissions, allowed-action settings, repository secret names/values and the Enforce HTTPS checkbox remain unverified. The new workflow defines its own least-privilege token permissions regardless of repository defaults.

## HTTPS and response-header limitations

Requests to both HTTP and HTTPS are intercepted here with an environment-generated “Site Unavailable” response. An `envoy` response or proxy TLS certificate is not evidence about the origin. The independent web retrieval also failed. Therefore certificate validity/SANs/expiry, supported TLS versions, HTTP-to-HTTPS redirects, HSTS, CSP response headers, `X-Content-Type-Options`, framing headers and Permissions-Policy could not be independently confirmed. Do not interpret these as confirmed absent headers.

The source-level CSP/referrer policies apply to generated HTML after an approved deployment. HTML meta cannot enforce CSP `frame-ancestors`, HSTS, `X-Frame-Options`, `X-Content-Type-Options` or Permissions-Policy. No fake `_headers` file or ineffective meta substitute was added. CSP allows existing inline styles for visual compatibility, but executable inline scripts are disallowed.

Before production approval, verify:

1. GitHub account Settings → Pages: verify `abwembya.com` and retain GitHub's generated TXT challenge. Avoid wildcard records.
2. Repository Settings → Pages: confirm the existing `master` source, custom domain, certificate status and **Enforce HTTPS**. Do not remove/recreate the domain casually.
3. From an unrestricted network, inspect HTTP/HTTPS redirects and the certificate for apex and `www`; inspect actual response headers. If additional headers are needed, review a header-capable hosting/proxy configuration separately before changing DNS or deployment. Do not enable HSTS `includeSubDomains`/preload without checking every subdomain.
4. Protect `master` with required review/checks and inspect Pages environment protections and Actions permissions. Check that secret scanning/push protection is available and enabled; no secret-management endpoint was accessed.

WEBrick is a development server, not the production host. An unreviewed 2026 request-smuggling report exists for versions through 1.9.2 (GHSA-h4w6-wx8r-p68v) without an established fixed release in the available registry. The bundle audit database does not flag it. Localhost-only binding reduces exposure; do not put this development server behind a public proxy.

## Validation

- `bundle install` and strict safe Jekyll build: pass.
- `bundle exec bundler-audit check`: no vulnerabilities found against Ruby Advisory DB commit `03da937a9e171e3fedebde6620e203559b7a60c0`, with no exclusions.
- `python3 scripts/check-site-security.py`: all nine generated HTML pages pass; build/audit files are excluded from publication.
- Node syntax checks: theme initialization, interactions and analytics pass.
- Transient jsdom checks across all nine pages: dark-mode initialization/toggle/persistence, menu, print binding, filters, detail toggles and slideshow controls pass where present. This is DOM emulation, not a real browser test.
- Original-source baseline and changed-source builds compared with the same resolved toolchain: nine page bodies and 2,119 CSS/image/font/PDF assets unchanged after normalizing the intentional script, print binding and link-attribute edits.
- Full Chrome execution failed at startup in this environment; no screenshot comparison or real-browser CSP enforcement result is claimed. Optional analytics is disabled in the current configuration and was not tested against Google's service.
- `git diff --check`: pass.

## References

- [Ruby Advisory Database](https://github.com/rubysec/ruby-advisory-db)
- [Addressable advisory](https://github.com/sporkmonger/addressable/security/advisories/GHSA-h27x-rffw-24p4)
- [REXML advisory](https://github.com/ruby/rexml/security/advisories/GHSA-c2f4-jgmc-q2r5)
- [Bootstrap 3.4.0 security fixes](https://blog.getbootstrap.com/2018/12/13/bootstrap-3-4-0/)
- [GitHub Pages domain verification](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages)
- [GitHub Pages HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https)
