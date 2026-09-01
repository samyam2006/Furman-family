# Law Office of Angela Furman, LLC — Website

A polished, responsive, **single-page** website for a boutique family law
practice in Columbia, Maryland. Black-and-white editorial theme (dark-dominant),
built to the project PRD.

## What it is
- **One long-form landing page** (`index.html`) with anchor navigation:
  `#practice-areas`, `#about`, `#process`, `#testimonials`, `#faq`, `#contact`.
- Dependency-free **HTML + CSS + JavaScript** — no build step, hosts on any static
  host (GitHub Pages, Netlify, Vercel, S3, …).
- Typography: **Cormorant Garamond** (display serif) + **Inter** (UI sans), via Google Fonts.
- Styling in `assets/css/styles.css`; interactions in `assets/js/main.js`.

## Design
- Strictly monochrome: near-black `#0B0B0B` / charcoal `#151515` grounds, warm
  paper `#F5F4F0` text, cool gray secondary. A muted antique-gold (`#B69A62`) is
  reserved as a *micro-accent only* (overline tick, active states, thin rules).
- Editorial layout — bounded container, asymmetric grids, hairline rules,
  letter-spaced overlines, large calm serif headlines. No stock legal iconography.
- **Restrained motion**, all gated by `prefers-reduced-motion`:
  line-by-line hero reveal, single fade/rise reveal pattern, transparent→solid
  scroll header, hover states on links/cards, accessible FAQ accordion, mobile drawer.

## Accessibility
- Skip link, semantic landmarks, single `h1`, logical headings.
- Keyboard-operable nav drawer (focus trap + return, `Esc` to close, `aria-expanded`/`aria-controls`).
- FAQ buttons expose `aria-expanded`/`aria-controls`; content is in the DOM for SEO.
- Labeled form controls, `autocomplete`, inline errors with `role="alert"`, and a
  polite live-region status. Targets WCAG 2.2 AA.

## Sections
Header → Hero → Credibility strip → Practice Areas (7) → About → Process (3 steps)
→ Testimonials (2) → FAQ (8) → Contact + form → Footer, plus a mobile-only "Call Now" bar.

## Running locally
Static — open `index.html`, or serve the folder:

```bash
python3 -m http.server 8000
# visit http://localhost:8000
```

## Before launch
The contact form is a **clearly-labeled non-production stub** and sends nothing —
wire it to an approved secure backend or form provider. All copy is from the audited
source and is **pending attorney approval**.

**See [`CONFIRM.md`](./CONFIRM.md)** for the full launch-blocker checklist (business
facts, legal-content approval, testimonial authorization, real portrait, secure form,
canonical URL, structured data).
