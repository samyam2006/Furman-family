# Content to replace

The site is fully built and styled — only the real copy and details need to be
dropped in. Every editable spot is marked in the HTML with an `<!-- EDIT -->`
comment and/or bracketed text like `[Attorney Name]`. Below is the full checklist.

Tip: most of these repeat across pages (header, footer). Do a project-wide
find-and-replace for the bracketed tokens to update them everywhere at once.

## Global (appears in the header/footer of every page)
- `(000) 000-0000` → real phone number (also in `href="tel:+10000000000"`)
- `hello@furmanfamilylaw.com` → real email (also in `href="mailto:..."`)
- `[Street Address]`, `[City, State ZIP]` → office address
- `Mon–Fri, 9–5 (by appt.)` → real office hours
- Firm statement under the footer wordmark

## index.html (Home)
- Hero headline + intro paragraph
- Hero meta: `[City & Region]` served
- Firm intro (two paragraphs)
- Stats: `25+`, `1000+`, `1`, `24h` → real figures (edit the `data-count` values)
- Practice-area blurbs (6) — adjust names/descriptions if needed
- Approach teaser copy
- Attorney quote + `[Attorney Name]` + short bio line
- Client testimonial

## about.html (About)
- Intro paragraph
- `[Attorney Name]` (appears several times) + title
- Full attorney bio (three paragraphs) — replace `[their]` with correct pronoun
- Credentials block: education, admissions, courts, memberships, languages
- Honors/associations pills (4)
- Values cards (3) — optional to edit

## practice-areas.html (Practice Areas)
- Intro paragraph
- Six practice-area descriptions + tag chips
- FAQ answers (5) — especially the consultation fee/policy

## approach.html (Approach)
- Intro paragraph
- Five process steps
- "Our Promise" pull quote
- "What to Expect" cards (3)

## contact.html (Contact)
- Intro paragraph
- Contact details (phone, email, office, hours)
- Office photo or map embed (replace the `.photo-slot`)
- The form currently shows a front-end confirmation only. To make it live,
  connect it to your intake system, an email service (e.g. Formspree), or a
  backend endpoint — see `data-contact-form` handling in `assets/js/main.js`.

## Photos
Elegant placeholder "photo slots" are in place for:
- Attorney portrait (home + about)
- Office photo / map (contact)
Drop an `<img>` inside each `.figure` (there is a `photo-slot` helper you can
remove once a real image is added).
