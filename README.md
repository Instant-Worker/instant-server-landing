# Instant Server: Landing Page

Marketing landing page for **Instant Server** (cloud server, object storage,
WhatsApp gateway). Static single page, bilingual (Indonesian / English) with a
language switcher, gold-on-ink dark theme.

Design direction lives in `DESIGN.md`. Read it before changing layout or copy.

## Structure

- `index.html`: the whole page (inline CSS + i18n dictionary + JS).
- `assets/legal.css`: styles for the legal and API-doc pages.
- `nginx.conf`: static serving, gzip, security headers.
- `Dockerfile`: nginx:alpine image serving the page on port 80.

## Deploy

Coolify application (Dockerfile build pack) on `https://instantserver.dev`.
Push to `master` and Coolify rebuilds.

## Editing

- Prices, specs, and copy live in `index.html`.
- Every user-facing string is in the `I18N` object at the bottom; the element
  carries `data-i18n="key"`, and both `id` and `en` must contain the same keys.
- Buy buttons point at the billing portal checkout:
  `https://panel.instantserver.dev/products/<category>/<product>/checkout`.
- No uptime figure, customer logo, testimonial, or datacenter claim that cannot
  be verified from the panel or the host. The servers run in Hetzner Singapore.
