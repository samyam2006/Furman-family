# Launch-blocker checklist — confirm before going live

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

## Portrait
- [ ] Provide a **real, licensed** professional portrait of Angela Furman, OR keep the
      current intentional typographic (no-photo) composition. The source's stock image
      was **not** used — do not present a stock model as Angela.

## Contact form (make it real)
- [ ] The form is a **clearly-labeled non-production stub** — it does not send anything.
      Wire it to an approved secure endpoint or form provider (see the submit handler in
      `assets/js/main.js`). Requirements: HTTPS, server-side validation, spam protection,
      encrypted transport, least-privilege storage, documented retention/deletion.
- [ ] Provide firm-approved **success copy** and the desired recipient / response process.
- [ ] Never send the `message` field to analytics, ad pixels, heatmaps, or session replay.
- [ ] Add a **privacy policy** link if personal data is collected.

## SEO / production readiness
- [ ] Set the **canonical URL** and Open Graph `og:url` / `og:image` once the production
      domain + SSL are verified (placeholders are commented out in `<head>`).
- [ ] Replace the inline SVG **favicon** with a real firm favicon; add `robots.txt` / sitemap.
- [ ] Enable the **LegalService structured data** block (commented in `<head>`) only after
      the firm confirms name, address, phone, hours, and service area. No invented
      ratings, prices, specialties, or awards.
- [ ] No preview-only artifacts (e.g. "Made with Emergent" badge) are present — keep it that way.
