# Instant Server — Landing Page

Marketing landing page for **Instant Server** (cloud server & object storage).
Static single page, bilingual (Bahasa Indonesia / English) with a language
switcher, dark luxury theme.

## Structure

- `index.html` — the whole page (inline CSS + i18n dictionary + JS).
- `nginx.conf` — static serving with gzip and security headers.
- `Dockerfile` — nginx:alpine image serving the page on port 80.

## Deploy

Coolify application (dockerfile build pack), domain
`instantserver.5.223.60.108.sslip.io` until the real `instantserver.*` domain is live.

## Editing

- Prices, specs and copy live in `index.html`.
- All user-facing strings are in the `I18N` object at the bottom of the file;
  every element carries a `data-i18n="key"` attribute, and both `id` and `en`
  dictionaries must contain the same keys.
- Buy buttons link to the billing portal checkout:
  `https://paymenter-<uuid>.5.223.60.108.sslip.io/products/<category>/<product>/checkout`.
