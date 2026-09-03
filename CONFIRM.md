# Launch-blocker checklist — confirm before going live

## ⚠️ Highest priority — DMV / multi-state service
- [ ] **Confirm licensure before advertising service in D.C. and Virginia.** The home page
      now has an "Areas We Serve" section and the schema lists Washington, D.C. and Northern
      Virginia. Our copy states Angela is **licensed in Maryland**. Practicing (or advertising
      that you practice) in D.C./VA generally requires admission to those bars or a proper
      co-counsel/pro hac vice arrangement. If Angela is **not** admitted in D.C./VA, either
      remove those jurisdictions from the "Areas We Serve" section (in `build.py` → `home_main`)
      and from `areaServed` in `SITE_JSONLD`, or reword to reflect referral/co-counsel. A note
      to that effect is already shown under the section — have counsel approve or revise it.

## Recently added (verify)
- [x] Real **logo + favicon set** generated from `assets/angela.png` (header mark
      `assets/img/logo-mark.png`, `favicon.ico`, PNG icons, apple-touch, `site.webmanifest`).
- [x] **Privacy Policy** and **Disclaimer** pages — *drafts for attorney review*; confirm they
      match the firm's actual practices, provider(s), and law, and update the "Last updated" date.
- [x] **Insights** scaffold (footer-linked) with one sample post; replace/expand with real articles.
- [x] **Consultation checklist** page + downloadable `assets/consultation-checklist.pdf`
      (regenerate the PDF if you edit the checklist).
- [x] **View Transitions** + `netlify.toml` security headers / CSP. If you use a form provider
      other than Netlify/Formspree, add it to the CSP `connect-src`/`form-action` in `netlify.toml`.

---

This site was built to the PRD ("Black-and-White Family Law Website Rebuild").
All copy comes from the audited source and is treated as **pending attorney
approval**, not independently verified. Every item below is marked in the HTML
with a `CONFIRM` or `pending` comment. Resolve all of them before connecting a
production domain.

## Business facts (verify exact values)
- [ ] Phone — currently `(410) 635-4910` (also in `tel:+14106354910`)
- [ ] Email — currently `angela.furman@alfurmanlaw.com`
- [ ] Office address — `8850 Columbia 100 Pkwy, Suite 303, Columbia, MD 21045`;
      confirm the office is suitable for public display / whether to add a map link
- [ ] Hours — resolved to **"Mon–Fri · Until 5:00 PM · By appointment"** everywhere
      (the source mixed "Closes 5 PM" and "Open until 5:00 PM"). Confirm exact times.
- [ ] Attorney credential + licensing line — "Angela Furman, Esq. · Founding Attorney · Licensed in Maryland"
- [ ] Copyright year — rendered dynamically via JS (currently the live year). Confirm.

## Legal content (attorney must approve)
- [ ] All eight Maryland-law **FAQ answers** (timeframes, custody factors, support
      guidelines, separation framing, protective-order courts/timing)
- [ ] Footer **disclaimer** wording (Attorney Advertising / no legal advice / no
      attorney–client relationship)
- [ ] Form **submission disclaimer** wording
- [ ] Protective-order **emergency language** — a "call 911" note is included in FAQ #6;
      confirm wording and whether to add an approved local resource. Do not invent a hotline.

## Testimonials (do not publish without authorization)
- [ ] Written permission for the two testimonials (Rebecca M., David T.)
- [ ] Confirm initials + location are intentional and wording is unedited
      (no ratings or outcome claims were added)

## Portrait & imagery
- [ ] Provide a **real, licensed** professional portrait of Angela Furman for the About
      page (currently an intentional typographic slot). The source's stock image was
      **not** used — do not present a stock model as Angela.
- [ ] The home **hero background** (`assets/img/hero.svg`) is a self-made black-and-white
      illustration standing in for a real photo. Swap it for a licensed B&W office/
      architectural photograph when available (update the `.hero__bg` background URL).

## Contact form (make it live)
The form is now **wired for real submission** and works two ways:
- **Netlify Forms** (default): it already has `data-netlify`, a hidden `form-name`, and a
  honeypot. Deploy the site to Netlify and submissions arrive automatically — no code needed.
- **Formspree / other**: change the form's `action="/"` to your endpoint URL (in
  `build.py` `contact_main`, then regenerate) — the JS posts to whatever `action` you set.
- [ ] Pick the provider and confirm the **recipient inbox** + response process.
- [ ] On any host that is **not** Netlify and has no endpoint set, the form shows a
      "please call/email" message instead of sending — confirm that's acceptable, or set an endpoint.
- [ ] Requirements to satisfy with the provider: HTTPS, spam protection, encrypted transport,
      least-privilege storage, documented retention/deletion, and a **privacy policy** link.
- [ ] Never send the `message` field to analytics, ad pixels, heatmaps, or session replay.

## SEO / production readiness
- [ ] **Set the production domain.** Everything points at `https://alfurmanlaw.com` via the
      `BASE_URL` constant in `build.py` (canonical, `og:url`, sitemap, robots). Change it to the
      real domain and regenerate before launch.
- [x] Canonical, Open Graph, Twitter tags, and a branded 1200×630 **OG image**
      (`assets/img/og.png`) are in place. — verify the domain resolves.
- [x] `robots.txt` + `sitemap.xml` generated.
- [x] **LegalService** structured data on every page and **FAQPage** schema on the FAQ page.
      Verify the business name, address, phone, and service area are correct — no ratings,
      prices, specialties, or awards are asserted.
- [x] Fonts are **self-hosted** (`assets/fonts/`) — no third-party font requests.
- [ ] Replace the inline SVG **favicon** with a real firm favicon/logo when available.
- [x] Custom **404 page**, **print stylesheet**, and reduced-motion support are in place.
- [x] No preview-only artifacts (e.g. "Made with Emergent" badge) are present.
