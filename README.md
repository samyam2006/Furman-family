# Furman Family Law — Website

A professional, multi-page marketing website for a family law practice.
Black-and-white editorial theme with subtle, tasteful motion.

## Pages
| File | Page |
| --- | --- |
| `index.html` | Home |
| `about.html` | About the firm / attorney |
| `practice-areas.html` | Practice areas + FAQ |
| `approach.html` | How the firm works |
| `contact.html` | Contact details + inquiry form |

## Stack
- Plain, dependency-free **HTML + CSS + JavaScript** — no build step, hosts anywhere
  (GitHub Pages, Netlify, Vercel, S3, any static host).
- Typography: **Fraunces** (display serif) + **Inter** (sans), loaded from Google Fonts.
- All shared styling lives in `assets/css/styles.css`; interactions in `assets/js/main.js`.

## Design
- Strictly monochrome (near-black `#0b0b0c`, warm paper `#f4f2ee`, white) for a
  refined, non-generic law-firm feel.
- Editorial layout: asymmetric grids, section numbering, hairline rules,
  letter-spaced labels, large serif headlines.
- Subtle animation only (respects `prefers-reduced-motion`):
  - line-by-line hero headline reveal
  - scroll-reveal fade/rise on sections
  - sticky/condensing header
  - animated stat counters
  - a slow monochrome marquee of practice areas
  - hover states on links, buttons, cards, and the practice-area index
  - expanding practice-area rows and FAQ accordion
  - full-screen mobile menu

## Running locally
It's static — just open `index.html`, or serve the folder:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Making it yours
See **`CONTENT.md`** for the full checklist of copy, contact details, and
photos to replace. Every editable spot is marked with an `<!-- EDIT -->`
comment or bracketed `[placeholder]` text in the HTML.

The contact form currently shows a front-end confirmation only; wire it to your
intake system or an email service to receive submissions.
