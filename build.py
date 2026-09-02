# -*- coding: utf-8 -*-
import os, re, json
import html as htmlmod

OUT = "/home/user/Furman-family"

PHONE_TEL = "+14106354910"
PHONE = "(410) 635-4910"
EMAIL = "angela.furman@alfurmanlaw.com"

BASE_URL = "https://alfurmanlaw.com"  # CONFIRM production domain before launch

FONTS = ('<link rel="preload" href="assets/fonts/source-sans-3-400-normal-latin.woff2" as="font" type="font/woff2" crossorigin />\n'
         '  <link rel="preload" href="assets/fonts/libre-baskerville-700-normal-latin.woff2" as="font" type="font/woff2" crossorigin />\n'
         '  <link rel="stylesheet" href="assets/fonts/fonts.css" />')

# Site-wide structured data. CONFIRM business facts + domain before launch.
SITE_JSONLD = ('<script type="application/ld+json">'
    '{"@context":"https://schema.org","@type":"LegalService",'
    '"name":"Law Office of Angela Furman, LLC",'
    '"description":"Boutique family law practice in Columbia, Maryland — divorce, custody, support, and family matters.",'
    f'"url":"{BASE_URL}/","image":"{BASE_URL}/assets/img/og.png",'
    '"telephone":"+1-410-635-4910","email":"angela.furman@alfurmanlaw.com",'
    '"areaServed":["Columbia, MD","Howard County, MD"],'
    '"address":{"@type":"PostalAddress","streetAddress":"8850 Columbia 100 Pkwy, Suite 303",'
    '"addressLocality":"Columbia","addressRegion":"MD","postalCode":"21045","addressCountry":"US"}}'
    '</script>')

FAVICON = ("<link rel=\"icon\" href=\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Crect width='32' height='32' fill='%23ffffff'/%3E%3Ctext x='16' y='24' font-family='Georgia,serif' "
           "font-weight='700' font-size='22' fill='%2314140f' text-anchor='middle'%3EF%3C/text%3E%3C/svg%3E\" />")

NAV = [
    ("Home", "index.html"),
    ("Practice Areas", "practice-areas.html"),
    ("About", "about.html"),
    ("Process", "process.html"),
    ("Testimonials", "testimonials.html"),
    ("FAQ", "faq.html"),
    ("Contact", "contact.html"),
]

def head(title, desc, slug="index.html", extra_head=""):
    url = BASE_URL + "/" + ("" if slug == "index.html" else slug)
    extra = ("\n  " + extra_head) if extra_head else ""
    return f'''<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta name="theme-color" content="#ffffff" />
  <!-- CONFIRM production domain (BASE_URL) before relying on canonical / og:url -->
  <link rel="canonical" href="{url}" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Law Office of Angela Furman, LLC" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{BASE_URL}/assets/img/og.png" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{desc}" />
  <meta name="twitter:image" content="{BASE_URL}/assets/img/og.png" />
  {FAVICON}
  {FONTS}
  <link rel="stylesheet" href="assets/css/styles.css" />
  {SITE_JSONLD}{extra}
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>'''

def header(active):
    links = ""
    for label, href in NAV:
        cur = ' aria-current="true"' if href == active else ''
        links += f'          <li><a class="nav__link" href="{href}"{cur}>{label}</a></li>\n'
    drawer_links = ""
    for i, (label, href) in enumerate(NAV, 1):
        drawer_links += f'      <li><a href="{href}"><span class="idx">{i:02d}</span> {label}</a></li>\n'
    return f'''
  <!-- ===== TOP UTILITY BAR ===== -->
  <div class="topbar">
    <div class="container">
      <span class="tb-left">Boutique family law serving Columbia &amp; Howard County, Maryland</span>
      <div class="tb-right">
        <a href="tel:{PHONE_TEL}" aria-label="Call the firm at {PHONE}"><span aria-hidden="true">&#9742;</span> {PHONE}</a>
        <span class="tb-sep" aria-hidden="true"></span>
        <span class="tb-hours">Mon&ndash;Fri &middot; By Appointment</span>
      </div>
    </div>
  </div>

  <!-- ===== MAIN HEADER ===== -->
  <header class="site-header">
    <div class="container">
      <a class="brand" href="index.html" aria-label="Law Office of Angela Furman, LLC — home">
        <span class="brand__name">Law Office of Angela Furman</span>
        <span class="brand__sub">Family Law &middot; Columbia, Maryland</span>
      </a>
      <nav class="nav" aria-label="Primary">
        <ul class="nav__links">
{links}        </ul>
        <a class="btn btn--solid nav__cta" href="contact.html"><span class="btn__label">Consultation</span></a>
      </nav>
      <button class="burger" aria-label="Open menu" aria-expanded="false" aria-controls="drawer"><span></span><span></span><span></span></button>
    </div>
  </header>

  <!-- ===== MOBILE DRAWER ===== -->
  <div class="drawer" id="drawer" aria-hidden="true" aria-label="Mobile menu">
    <button class="drawer__close" aria-label="Close menu"></button>
    <ul class="drawer__links">
{drawer_links}    </ul>
    <a class="btn btn--solid drawer__cta" href="contact.html"><span class="btn__label">Schedule a Consultation</span><span class="btn__arrow">&rarr;</span></a>
    <div class="drawer__foot">
      <a href="tel:{PHONE_TEL}">{PHONE}</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
  </div>
'''

def cta_band():
    return f'''
    <!-- ===== CTA BAND ===== -->
    <section class="cta-band" aria-label="Contact call to action">
      <div class="container">
        <h2 class="cta-band__title" data-reveal>Ready to talk about what's next?</h2>
        <div class="cta-band__side" data-reveal data-delay="1">
          <span class="phone"><a href="tel:{PHONE_TEL}">{PHONE}</a></span>
          <a class="btn btn--solid" href="contact.html"><span class="btn__label">Schedule a Consultation</span><span class="btn__arrow">&rarr;</span></a>
        </div>
      </div>
    </section>'''

def footer():
    return f'''
  <!-- ===== FOOTER ===== -->
  <footer class="site-footer" aria-label="Footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <span class="brand__name display">Law Office of Angela Furman, LLC</span>
          <p>A boutique family law practice serving Columbia, Maryland and the surrounding area &mdash; built on relationships, not volume.</p>
        </div>
        <div>
          <h4>Explore</h4>
          <ul>
            <li><a href="practice-areas.html">Practice Areas</a></li>
            <li><a href="about.html">About</a></li>
            <li><a href="process.html">Process</a></li>
            <li><a href="testimonials.html">Testimonials</a></li>
            <li><a href="faq.html">FAQ</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>
        <div>
          <h4>Contact</h4>
          <ul>
            <li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
            <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li>8850 Columbia 100 Pkwy, Suite 303<br>Columbia, MD 21045</li>
            <li>Mon&ndash;Fri &middot; Until 5:00 PM &middot; By appointment</li>
          </ul>
        </div>
      </div>
      <div class="footer-legal">
        <p class="disclaimer"><strong>Attorney Advertising.</strong> Prior results do not guarantee a similar outcome. The information on this website is for general informational purposes only and does not constitute legal advice. No attorney&ndash;client relationship is formed by contacting this firm or submitting the contact form.</p>
      </div>
      <div class="footer-bottom">
        <span>&copy; <span id="year">2026</span> Law Office of Angela Furman, LLC. All rights reserved.</span>
        <span>Columbia, Maryland</span>
      </div>
    </div>
  </footer>

  <div class="callbar" data-callbar aria-hidden="true">
    <span class="cb-label">Speak with the firm<strong>{PHONE}</strong></span>
    <a class="cb-btn" href="tel:{PHONE_TEL}">Call Now</a>
  </div>
  <button class="to-top" aria-label="Back to top"><span aria-hidden="true">&uarr;</span></button>

  <script src="assets/js/main.js"></script>
</body>
</html>
'''

def page(active, title, desc, main_html, with_cta=True, extra_head=""):
    return (head(title, desc, slug=active, extra_head=extra_head) + header(active) + '\n  <main id="main">\n'
            + main_html + ('\n' + cta_band() if with_cta else '') + '\n  </main>\n' + footer())

def page_hero(crumb_label, title, lead):
    return f'''
    <!-- ===== PAGE HERO ===== -->
    <section class="page-hero" aria-label="Page introduction">
      <div class="page-hero__bg" aria-hidden="true"></div>
      <div class="page-hero__scrim" aria-hidden="true"></div>
      <div class="container">
        <nav class="page-hero__crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> <span aria-hidden="true">/</span> {crumb_label}</nav>
        <h1 class="page-hero__title">{title}</h1>
        <p class="lead measure">{lead}</p>
      </div>
    </section>'''

# Practice-area data
AREAS = [
    ("01", "Divorce", "Divorce",
     "Compassionate, strategic representation through contested and uncontested divorce — protecting what matters most.",
     ["Uncontested divorce", "Contested divorce", "High-asset divorce", "Legal separation", "Post-judgment"]),
    ("02", "Child Custody", "Child Custody",
     "Custody arrangements crafted around your child's best interests, with clarity, structure, and long-term stability.",
     ["Legal &amp; physical custody", "Parenting plans", "Relocation", "Modifications", "Enforcement"]),
    ("03", "Child &amp; Spousal Support", "Child / Spousal Support",
     "Fair, accurate support calculations and modifications — guided by Maryland law and your family's reality.",
     ["Child support", "Spousal support / alimony", "Enforcement", "Modification"]),
    ("04", "Property Division", "Property Division",
     "Marital and non-marital asset analysis to ensure an equitable division of property, retirement, and debts.",
     ["Marital estate", "Business interests", "Retirement / QDRO", "Real property", "Debt allocation"]),
    ("05", "Adoption", "Adoption",
     "Step-parent, relative, and independent adoptions handled with care, discretion, and meticulous attention to detail.",
     ["Step-parent adoption", "Relative adoption", "Independent adoption"]),
    ("06", "Protective Orders", "Protective Order",
     "Urgent, confidential help securing protective orders and safety for you and your children when it matters most.",
     ["Temporary orders", "Final protective orders", "Petition preparation", "Hearing representation"]),
    ("07", "Prenuptial Agreements", "Prenuptial Agreement",
     "Thoughtful, enforceable prenuptial and postnuptial agreements that protect both parties and start a marriage on solid ground.",
     ["Prenuptial", "Postnuptial", "Cohabitation agreements"]),
]

FAQS = [
    ("How long does a divorce take in Maryland?",
     "<p>An uncontested divorce in Maryland can be finalized in as little as 60&ndash;90 days after filing, depending on court availability. Contested divorces involving custody, property, or support disputes typically take 6&ndash;18 months. We work to keep things moving while protecting your interests at every step.</p>"),
    ("Do I need a lawyer for an uncontested divorce?",
     "<p>Even when both parties agree, the paperwork, financial disclosures, and court procedures must be done correctly the first time. A small mistake can delay the case for months. Most clients find peace of mind in having an attorney review or prepare the documents — even in an amicable separation.</p>"),
    ("How is child custody determined in Maryland?",
     "<p>Maryland courts decide custody based on the best interests of the child, weighing factors like each parent's caregiving history, the child's relationships, stability, work schedules, and the child's preferences when age-appropriate. We help present a clear, well-documented picture of what is truly best for your child.</p>"),
    ("What factors affect child support amounts?",
     "<p>Maryland uses statutory child support guidelines based on both parents' gross incomes, the number of overnights, health insurance costs, work-related childcare expenses, and any extraordinary needs. We calculate accurate numbers up front so there are no surprises.</p>"),
    ("What's the difference between legal separation and divorce?",
     "<p>Maryland does not have a formal &quot;legal separation&quot; status, but spouses can live separately and enter into a binding separation agreement covering custody, support, and property. Divorce legally ends the marriage. A separation agreement is often a foundation for a smooth divorce later.</p>"),
    ("How do I get a protective order in Maryland?",
     "<p>If you or your children are in danger, you can petition for a protective order at the District Court or Circuit Court. A temporary order can be granted the same day. We can help you prepare your petition, gather evidence, and represent you at the final protective order hearing.</p><p><strong>If you are in immediate danger, call 911.</strong> This website and its contact form are not monitored continuously and are not an emergency service.</p>"),
    ("Are consultations confidential?",
     "<p>Yes. Every consultation is confidential, whether or not you ultimately hire the firm. You can speak openly so we can give you honest, accurate guidance about your options.</p>"),
    ("How do you charge for your services?",
     "<p>Most family law matters are billed at an hourly rate against an initial retainer, with detailed monthly invoices so you always know where things stand. We discuss fees clearly and transparently before any engagement begins.</p>"),
]

def acc_html(faqs):
    out = '        <div class="acc" data-reveal>\n'
    for i, (q, a) in enumerate(faqs, 1):
        out += f'''          <div class="acc__item">
            <h3><button class="acc__head" aria-expanded="false" aria-controls="faq{i}"><span class="acc__q">{q}</span><span class="acc__toggle" aria-hidden="true"></span></button></h3>
            <div class="acc__body" id="faq{i}"><div class="acc__bodyinner">{a}</div></div>
          </div>
'''
    out += '        </div>\n'
    return out

def portrait(ar="ar-portrait", label="Attorney portrait — real photo pending", parallax=False):
    p = ' data-parallax' if parallax else ''
    return f'''<div class="figure photo-slot {ar}"{p}>
              <div class="photo-slot__mono" aria-hidden="true">AF</div>
              <span class="photo-slot__label">{label}</span>
            </div>'''

# ---------------- HOME ----------------
def home_main():
    # practice teaser: 6 cards
    cards = ""
    for num, title, matter, desc, tags in AREAS[:6]:
        cards += f'''          <div class="parea">
            <span class="parea__num">{num}</span><span class="parea__rule" aria-hidden="true"></span>
            <h3 class="parea__title">{title} <span class="arrow" aria-hidden="true">&rarr;</span></h3>
            <p class="parea__desc">{desc}</p>
            <a class="parea__link" href="practice-areas.html">{title}</a>
          </div>
'''
    marquee_items = "".join(f'<span class="marquee__item">{t}</span>' for _,t,_,_,_ in AREAS)
    marquee_items = marquee_items + marquee_items  # duplicate for seamless loop
    return f'''
    <!-- ===== HERO ===== -->
    <section class="hero hero--image" aria-label="Introduction">
      <div class="hero__bg" aria-hidden="true"></div>
      <div class="hero__scrim" aria-hidden="true"></div>
      <div class="container">
        <div class="hero--image__inner">
          <p class="overline"><span class="tick"></span> Family Law — Columbia, Maryland</p>
          <h1 class="h-hero display lines" style="margin-top: 1.4rem; max-width: 20ch;">
            <span class="ln"><span>Trusted Counsel.</span></span>
            <span class="ln"><span class="serif-italic">Exceptional Representation.</span></span>
          </h1>
          <p class="lead" data-reveal data-delay="2" style="margin-top: 1.6rem; max-width: 56ch;">
            A boutique family law practice in Columbia, Maryland — built on relationships, not
            volume. Direct access to your attorney from the first call to the final signature.
          </p>
          <div class="hero__cta" data-reveal data-delay="3">
            <a class="btn btn--solid" href="contact.html"><span class="btn__label">Schedule a Consultation</span><span class="btn__arrow">&rarr;</span></a>
            <a class="btn btn--ghost" href="practice-areas.html"><span class="btn__label">View Practice Areas</span></a>
          </div>
          <div class="hero__meta" data-reveal data-delay="4">
            <span class="m">Licensed in Maryland</span>
            <span class="m">Referral-based practice</span>
            <span class="m">Confidential &middot; By appointment</span>
          </div>
        </div>
      </div>
    </section>

    <!-- ===== TRUST BAND ===== -->
    <section class="section--tight bg-paper" id="trust" aria-label="Why clients choose the firm">
      <div class="container">
        <div class="trust__row trust-band" data-stagger>
          <div class="trust__item"><span class="mark" aria-hidden="true"></span><span class="n">Licensed in Maryland</span></div>
          <div class="trust__item"><span class="mark" aria-hidden="true"></span><span class="n">Personalized Attention</span></div>
          <div class="trust__item"><span class="mark" aria-hidden="true"></span><span class="n">Referral-Based Practice</span></div>
          <div class="trust__item"><span class="mark" aria-hidden="true"></span><span class="n">Confidential Consultations</span></div>
        </div>
      </div>
    </section>

    <!-- ===== PRACTICE TEASER ===== -->
    <section class="section bg-paper" aria-labelledby="pa-heading">
      <div class="container">
        <div class="split split--7-5 split--center sec-head" data-reveal style="margin-bottom: clamp(2rem,4vw,3.2rem); max-width:none;">
          <div>
            <p class="overline"><span class="tick"></span> What We Handle</p>
            <h2 class="h-xl display" id="pa-heading" style="margin-top: 1.1rem;">Focused expertise across the key areas of family law.</h2>
          </div>
          <div style="align-self:end;">
            <p class="muted" style="max-width:40ch;">Every family is different. Every case demands attention. These are the matters Angela handles personally.</p>
            <a class="link" href="practice-areas.html" style="margin-top:1rem;">All practice areas <span class="arrow" aria-hidden="true">&rarr;</span></a>
          </div>
        </div>
        <div class="parea-grid" data-stagger>
{cards}        </div>
      </div>
    </section>

    <!-- ===== STATS ===== -->
    <section class="section--tight bg-soft" aria-label="The firm at a glance">
      <div class="container">
        <div class="stats" data-reveal>
          <div class="stat"><div class="stat__num"><span data-count="7">0</span></div><div class="stat__label">Family law practice areas, handled personally</div></div>
          <div class="stat"><div class="stat__num"><span data-count="1">0</span></div><div class="stat__label">Attorney on your case, from first call to final signature</div></div>
          <!-- CONFIRM response-time claim -->
          <div class="stat"><div class="stat__num"><span data-count="24">0</span><span class="suf">h</span></div><div class="stat__label">Typical response to a new inquiry</div></div>
          <div class="stat"><div class="stat__num"><span data-count="100">0</span><span class="suf">%</span></div><div class="stat__label">Confidential consultations, every time</div></div>
        </div>
      </div>
    </section>

    <!-- ===== ABOUT TEASER ===== -->
    <section class="section bg-paper" aria-labelledby="about-t">
      <div class="container">
        <div class="split split--5-7" data-reveal>
          <div>{portrait()}</div>
          <div>
            <p class="overline"><span class="tick"></span> About the Firm</p>
            <h2 class="h-xl display" id="about-t" style="margin-top:1.1rem;">A practice built on trust.</h2>
            <div class="stack" style="margin-top:1.5rem; color:var(--ink-2);">
              <p>Angela Furman founded her practice on the belief that every client deserves direct access to their attorney. With a reputation built almost entirely on referrals, she brings a level of personal attention and professional integrity that larger firms simply cannot offer.</p>
              <p>Whether you're navigating a divorce, formalizing custody, or planning ahead with a prenuptial agreement, you will work directly with Angela — never handed off, never rushed.</p>
            </div>
            <a class="link" href="about.html" style="margin-top:1.6rem;">More about Angela <span class="arrow" aria-hidden="true">&rarr;</span></a>
          </div>
        </div>
      </div>
    </section>

    <!-- ===== PROCESS TEASER ===== -->
    <section class="section bg-soft" aria-labelledby="proc-t">
      <div class="container">
        <div class="sec-head" data-reveal>
          <p class="overline"><span class="tick"></span> How It Works</p>
          <h2 class="h-xl display" id="proc-t" style="margin-top:1.1rem;">Three thoughtful steps — no surprises.</h2>
        </div>
        <div class="steps" data-stagger>
          <div class="step"><div class="step__num">01</div><h3 class="step__title">Schedule a Consultation</h3><p class="step__text">We discuss your situation confidentially with no obligation. You leave with clarity, even if you don't hire us.</p></div>
          <div class="step"><div class="step__num">02</div><h3 class="step__title">Build Your Strategy</h3><p class="step__text">Angela personally reviews your case and outlines a clear, honest path forward — no jargon, no false promises.</p></div>
          <div class="step"><div class="step__num">03</div><h3 class="step__title">Move Forward</h3><p class="step__text">We handle the legal work, deadlines, and negotiations so you can focus on your family and what matters next.</p></div>
        </div>
        <a class="link" href="process.html" style="margin-top:2rem; display:inline-flex;">See the full process <span class="arrow" aria-hidden="true">&rarr;</span></a>
      </div>
    </section>

    <!-- ===== TESTIMONIALS TEASER ===== -->
    <section class="section bg-paper" aria-labelledby="tst-t">
      <div class="container">
        <div class="sec-head" data-reveal>
          <p class="overline"><span class="tick"></span> What Clients Say</p>
          <h2 class="h-xl display" id="tst-t" style="margin-top:1.1rem;">In the words of the people we've represented.</h2>
        </div>
        <div class="tgrid" data-stagger>
          <blockquote class="tcard"><span class="quote__mark" aria-hidden="true">&ldquo;</span><p class="quote">Angela was the steady hand I needed during the hardest year of my life. She returned every call, explained every step, and fought for my children without ever losing her grace.</p><footer class="quote__cite">Rebecca M. &middot; Columbia, MD</footer></blockquote>
          <blockquote class="tcard"><span class="quote__mark" aria-hidden="true">&ldquo;</span><p class="quote">I came to Angela on a referral and now I refer everyone I know. She is sharp, deeply prepared, and unfailingly kind. The kind of attorney you want in your corner.</p><footer class="quote__cite">David T. &middot; Columbia, MD</footer></blockquote>
        </div>
      </div>
    </section>'''

# ---------------- PRACTICE AREAS ----------------
def practice_main():
    arts = ""
    for i, (num, title, matter, desc, tags) in enumerate(AREAS):
        border = "border-block:1px solid var(--line);" if i == len(AREAS)-1 else "border-top:1px solid var(--line);"
        tag_html = "".join(f'<span class="tag" style="font-size:.76rem; border:1px solid var(--line); border-radius:999px; padding:.4em .9em; color:var(--muted);">{t}</span>' for t in tags)
        arts += f'''        <article class="split split--5-7" data-reveal style="padding-block: clamp(2.4rem,4.5vw,4rem); {border}">
          <div>
            <span class="parea__num" style="font-size:.8rem; letter-spacing:.14em;">{num} / 07</span>
            <h2 class="h-lg display" style="margin-top:.8rem;">{title}</h2>
          </div>
          <div>
            <p class="lead" style="max-width:58ch;">{desc}</p>
            <div style="display:flex; flex-wrap:wrap; gap:.6rem; margin-top:1.4rem;">{tag_html}</div>
            <a class="link" href="contact.html?matter={matter.replace(' ', '%20').replace('/', '%2F')}" style="margin-top:1.6rem;">Discuss a {title.replace('&amp;','&amp;').split(' ')[0].lower()} matter <span class="arrow" aria-hidden="true">&rarr;</span></a>
          </div>
        </article>
'''
    return page_hero("Practice Areas", "Family law, and only family law.",
        "Because we concentrate on a single field, we know it deeply — the statutes, the courts, the strategies, and the human realities behind each of these matters.") + f'''

    <section class="section--tight bg-paper">
      <div class="container">
{arts}      </div>
    </section>'''

# ---------------- ABOUT ----------------
def about_main():
    return page_hero("About", "Experience you can lean on.",
        "The Law Office of Angela Furman was built on a simple conviction: that people navigating the most personal legal matters of their lives deserve an attorney who is genuinely present — prepared, honest, and invested in the outcome.") + f'''

    <section class="section bg-paper" aria-labelledby="about-heading">
      <div class="container">
        <div class="split split--5-7" data-reveal>
          <div>{portrait()}</div>
          <div>
            <p class="overline"><span class="tick"></span> The Attorney</p>
            <h2 class="h-xl display" id="about-heading" style="margin-top:1.1rem;">Angela Furman, Esq.</h2>
            <p class="role" style="font-size:.78rem; font-weight:700; letter-spacing:.12em; text-transform:uppercase; color:var(--muted); margin-top:.6rem;">Founding Attorney &middot; Licensed in Maryland</p>
            <div class="stack" style="margin-top:1.8rem; color:var(--ink-2);">
              <p>Angela Furman founded her practice on the belief that every client deserves direct access to their attorney. With a reputation built almost entirely on referrals, she brings a level of personal attention and professional integrity that larger firms simply cannot offer.</p>
              <p>Family law touches the most important parts of a person's life — their children, their home, their future. Angela approaches every case with the discretion, preparation, and steady guidance her clients need during difficult moments.</p>
              <p>Whether you're navigating a divorce, formalizing custody, or planning ahead with a prenuptial agreement, you will work directly with Angela — never handed off, never rushed.</p>
            </div>
            <!-- CONFIRM: credentials + licensing statement -->
            <div class="cred-line"><div class="name">Angela Furman, Esq.</div><div class="role">Founding Attorney &middot; Licensed in Maryland</div></div>
          </div>
        </div>
      </div>
    </section>

    <section class="section bg-soft" aria-labelledby="values-h">
      <div class="container">
        <div class="sec-head" data-reveal>
          <p class="overline"><span class="tick"></span> What Guides Us</p>
          <h2 class="h-xl display" id="values-h" style="margin-top:1.1rem;">Principles behind every matter we take.</h2>
        </div>
        <div class="parea-grid" data-stagger style="grid-template-columns:repeat(3,1fr);">
          <div class="parea"><span class="parea__num">01</span><span class="parea__rule" aria-hidden="true"></span><h3 class="parea__title">Candor</h3><p class="parea__desc">Honest assessments — including the ones you may not want to hear. Good decisions require the truth.</p></div>
          <div class="parea"><span class="parea__num">02</span><span class="parea__rule" aria-hidden="true"></span><h3 class="parea__title">Discretion</h3><p class="parea__desc">Your circumstances are private. We handle them with the confidentiality and care they deserve.</p></div>
          <div class="parea"><span class="parea__num">03</span><span class="parea__rule" aria-hidden="true"></span><h3 class="parea__title">Preparation</h3><p class="parea__desc">Cases are built on groundwork. We arrive ready — anticipating the other side, not reacting to it.</p></div>
        </div>
      </div>
    </section>'''

# ---------------- PROCESS ----------------
def process_main():
    return page_hero("Process", "A clear path through an unclear time.",
        "You don't need more uncertainty right now. Our process is designed to give you footing fast — a clear understanding of where you stand, what your options are, and exactly what happens next.") + f'''

    <section class="section bg-paper" aria-labelledby="steps-h">
      <div class="container">
        <div class="sec-head" data-reveal>
          <p class="overline"><span class="tick"></span> How It Works</p>
          <h2 class="h-xl display" id="steps-h" style="margin-top:1.1rem;">Three thoughtful steps — no surprises.</h2>
        </div>
        <div class="steps" data-stagger>
          <div class="step"><div class="step__num">01</div><h3 class="step__title">Schedule a Consultation</h3><p class="step__text">We discuss your situation confidentially with no obligation. You leave with clarity about your options and a realistic sense of what's ahead — even if you don't hire us.</p></div>
          <div class="step"><div class="step__num">02</div><h3 class="step__title">Build Your Strategy</h3><p class="step__text">Angela personally reviews your case and outlines a clear, honest path forward — the outcome we're aiming for, the likely route there, and the timeline and costs you can expect. No jargon, no false promises.</p></div>
          <div class="step"><div class="step__num">03</div><h3 class="step__title">Move Forward With Confidence</h3><p class="step__text">We handle the legal work, deadlines, and negotiations — keeping you informed at every turn — so you can focus on your family and what matters next.</p></div>
        </div>
      </div>
    </section>

    <section class="section bg-soft" aria-labelledby="expect-h">
      <div class="container">
        <div class="sec-head" data-reveal>
          <p class="overline"><span class="tick"></span> What to Expect</p>
          <h2 class="h-xl display" id="expect-h" style="margin-top:1.1rem;">The details that make the difference.</h2>
        </div>
        <div class="parea-grid" data-stagger style="grid-template-columns:repeat(3,1fr);">
          <div class="parea"><span class="parea__num">01</span><span class="parea__rule" aria-hidden="true"></span><h3 class="parea__title">Responsiveness</h3><p class="parea__desc">Questions answered promptly, by someone who knows your file — not left waiting for days.</p></div>
          <div class="parea"><span class="parea__num">02</span><span class="parea__rule" aria-hidden="true"></span><h3 class="parea__title">Transparency</h3><p class="parea__desc">Clear billing and honest updates. You'll understand what each step involves before we take it.</p></div>
          <div class="parea"><span class="parea__num">03</span><span class="parea__rule" aria-hidden="true"></span><h3 class="parea__title">Composure</h3><p class="parea__desc">A calm, steady presence when emotions run high — and firm advocacy when it's needed most.</p></div>
        </div>
      </div>
    </section>'''

# ---------------- TESTIMONIALS ----------------
def testimonials_main():
    return page_hero("Testimonials", "In the words of the people we've represented.",
        "The measure of a family law practice is how its clients felt during the hardest moments — and whether they'd send the people they love.") + f'''

    <!-- CONFIRM before launch: written authorization for each testimonial; wording/initials/location approved. -->
    <section class="section bg-paper">
      <div class="container">
        <div class="tgrid" data-stagger>
          <blockquote class="tcard"><span class="quote__mark" aria-hidden="true">&ldquo;</span><p class="quote">Angela was the steady hand I needed during the hardest year of my life. She returned every call, explained every step, and fought for my children without ever losing her grace.</p><footer class="quote__cite">Rebecca M. &middot; Columbia, MD</footer></blockquote>
          <blockquote class="tcard"><span class="quote__mark" aria-hidden="true">&ldquo;</span><p class="quote">I came to Angela on a referral and now I refer everyone I know. She is sharp, deeply prepared, and unfailingly kind. The kind of attorney you want in your corner.</p><footer class="quote__cite">David T. &middot; Columbia, MD</footer></blockquote>
        </div>
        <p class="muted" data-reveal style="margin-top:2.4rem; font-size:.88rem; max-width:70ch;">Testimonials reflect the experience of individual clients. Every matter is different, and prior results do not guarantee a similar outcome.</p>
      </div>
    </section>'''

# ---------------- FAQ ----------------
def faq_main():
    return page_hero("FAQ", "Answers, in plain language.",
        "The questions clients ask us most often. Don't see yours? Reach out — Angela will get back to you personally.") + f'''

    <!-- CONFIRM before launch: attorney must approve every Maryland-law statement below. -->
    <section class="section bg-paper">
      <div class="container">
{acc_html(FAQS)}      </div>
    </section>'''

# ---------------- CONTACT ----------------
def contact_main():
    opts = "".join(f'<option>{m}</option>' for _,_,m,_,_ in AREAS)
    # unique matter labels in the select
    matter_opts = ["Divorce","Child Custody","Child / Spousal Support","Property Division","Adoption","Protective Order","Prenuptial Agreement","Other / Not Sure"]
    opts = "".join(f'                    <option>{m}</option>\n' for m in matter_opts)
    return page_hero("Contact", "Schedule a confidential consultation.",
        "Reach out by phone, email, or the form. Angela personally reviews every inquiry and will respond within one business day.") + f'''

    <section class="section bg-paper" id="contact">
      <div class="container">
        <div class="split split--5-7" data-reveal>
          <div>
            <div class="detail-row"><span class="k">Phone</span><span class="v"><a class="link" href="tel:{PHONE_TEL}">{PHONE}</a></span></div>
            <div class="detail-row"><span class="k">Email</span><span class="v"><a class="link" href="mailto:{EMAIL}">{EMAIL}</a></span></div>
            <div class="detail-row"><span class="k">Office</span><span class="v">8850 Columbia 100 Pkwy, Suite 303<small>Columbia, MD 21045</small></span></div>
            <div class="detail-row"><span class="k">Hours</span><span class="v">Mon&ndash;Fri &middot; Until 5:00 PM<small>By appointment</small></span></div>
            <p class="muted" style="margin-top:1.6rem; font-size:.9rem; max-width:40ch;">Prefer to talk it through? Call the office directly — Angela welcomes a confidential, no-obligation conversation.</p>
          </div>
          <div>
            <!-- Ready for Netlify Forms out of the box (data-netlify + hidden form-name + honeypot).
                 For Formspree/other providers, change action="/" to your endpoint URL. See CONFIRM.md. -->
            <form class="form-card" data-contact-form action="/" method="POST" name="consultation" data-netlify="true" netlify-honeypot="bot-field" novalidate aria-describedby="form-disclaimer">
              <input type="hidden" name="form-name" value="consultation" />
              <p class="hp" hidden aria-hidden="true"><label>Leave this field empty <input name="bot-field" tabindex="-1" autocomplete="off" /></label></p>
              <div class="form-row">
                <div class="field"><label for="name">Full Name <span class="req" aria-hidden="true">*</span></label><input id="name" name="name" type="text" autocomplete="name" required aria-required="true" aria-describedby="err-name" placeholder="Jane Doe" /><span class="field__error" id="err-name" role="alert"></span></div>
                <div class="field"><label for="phone">Phone <span class="req" aria-hidden="true">*</span></label><input id="phone" name="phone" type="tel" autocomplete="tel" required aria-required="true" aria-describedby="err-phone" placeholder="(410) 555-0100" /><span class="field__error" id="err-phone" role="alert"></span></div>
              </div>
              <div class="form-row">
                <div class="field"><label for="email">Email <span class="req" aria-hidden="true">*</span></label><input id="email" name="email" type="email" autocomplete="email" required aria-required="true" aria-describedby="err-email" placeholder="you@example.com" /><span class="field__error" id="err-email" role="alert"></span></div>
                <div class="field"><label for="matter">Practice Area <span class="req" aria-hidden="true">*</span></label><select id="matter" name="matter" required aria-required="true" aria-describedby="err-matter"><option value="">Select one&hellip;</option>
{opts}                  </select><span class="field__error" id="err-matter" role="alert"></span></div>
              </div>
              <div class="field"><label for="message">Brief Description <span class="req" aria-hidden="true">*</span></label><textarea id="message" name="message" required aria-required="true" aria-describedby="err-message note-message" placeholder="A short, confidential summary of the situation&hellip;"></textarea><span class="field__error" id="err-message" role="alert"></span><span class="form-note" id="note-message">Please don't include highly sensitive details — Social Security numbers, financial account numbers, passwords, or information about imminent danger.</span></div>
              <div class="field"><span id="pref-label" style="font-size:.72rem; font-weight:700; letter-spacing:.12em; text-transform:uppercase; color:var(--muted);">Preferred Contact</span><div class="radio-set" role="radiogroup" aria-labelledby="pref-label"><label class="radio"><input type="radio" name="preferred" value="Phone" checked /> Phone</label><label class="radio"><input type="radio" name="preferred" value="Email" /> Email</label></div></div>
              <button class="btn btn--solid" type="submit" style="width:100%;"><span class="btn__label">Request Consultation</span><span class="btn__arrow">&rarr;</span></button>
              <div class="form-status" data-form-status hidden role="status" aria-live="polite"></div>
              <p class="form-disclaimer" id="form-disclaimer">By submitting, you acknowledge that no attorney&ndash;client relationship is formed until a written engagement is signed. Information shared here will be treated confidentially.</p>
            </form>
          </div>
        </div>
      </div>
    </section>'''

def faq_jsonld(faqs):
    def clean(a):
        t = re.sub(r"<[^>]+>", " ", a)
        t = htmlmod.unescape(t)
        return re.sub(r"\s+", " ", t).strip()
    data = {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": htmlmod.unescape(q),
                            "acceptedAnswer": {"@type": "Answer", "text": clean(a)}} for q, a in faqs]}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + '</script>'

def notfound_main():
    return page_hero("Not Found", "This page could not be found.",
        "The page you're looking for may have moved or no longer exists. Use the links below, or head back to the homepage.") + '''
    <section class="section bg-paper">
      <div class="container" style="text-align:center;">
        <div class="hero__cta" style="justify-content:center;" data-reveal>
          <a class="btn btn--solid" href="index.html"><span class="btn__label">Back to home</span><span class="btn__arrow">&rarr;</span></a>
          <a class="btn btn--ghost" href="contact.html"><span class="btn__label">Contact the firm</span></a>
        </div>
      </div>
    </section>'''

PAGES = {
  "index.html": ("Law Office of Angela Furman, LLC | Family Law Attorney Columbia, MD",
                 "Angela Furman is a trusted family law attorney in Columbia, MD handling divorce, child custody, support, and more. Schedule a confidential consultation today.",
                 "index.html", home_main(), True),
  "practice-areas.html": ("Practice Areas | Law Office of Angela Furman, LLC",
                 "Divorce, child custody, support, property division, adoption, protective orders, and prenuptial agreements — family law in Columbia, MD.",
                 "practice-areas.html", practice_main(), True),
  "about.html": ("About Angela Furman | Family Law Attorney Columbia, MD",
                 "Meet Angela Furman, Esq. — a boutique, referral-based family law attorney in Columbia, Maryland offering direct, personal representation.",
                 "about.html", about_main(), True),
  "process.html": ("Our Process | Law Office of Angela Furman, LLC",
                 "A clear, three-step family law process — consultation, strategy, and resolution — with direct attorney access throughout.",
                 "process.html", process_main(), True),
  "testimonials.html": ("Testimonials | Law Office of Angela Furman, LLC",
                 "What clients say about working with Angela Furman — a steady, prepared, and personal family law advocate in Columbia, MD.",
                 "testimonials.html", testimonials_main(), True),
  "faq.html": ("Family Law FAQ | Law Office of Angela Furman, LLC",
                 "Answers to common Maryland family law questions about divorce timelines, custody, support, protective orders, fees, and confidentiality.",
                 "faq.html", faq_main(), True, faq_jsonld(FAQS)),
  "contact.html": ("Contact | Law Office of Angela Furman, LLC",
                 "Schedule a confidential family law consultation in Columbia, MD. Call (410) 635-4910, email, or send a message.",
                 "contact.html", contact_main(), False),
}

for fname, vals in PAGES.items():
    title, desc, active, main_html, with_cta = vals[:5]
    extra_head = vals[5] if len(vals) > 5 else ""
    html = page(active, title, desc, main_html, with_cta, extra_head=extra_head)
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", fname, len(html), "bytes")

# 404 page
nf = page("404.html", "Page Not Found | Law Office of Angela Furman, LLC",
          "Sorry — the page you were looking for could not be found.", notfound_main(), with_cta=False)
with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
    f.write(nf)
print("wrote 404.html", len(nf), "bytes")

# robots.txt + sitemap.xml
with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
    f.write("User-agent: *\nAllow: /\n\nSitemap: " + BASE_URL + "/sitemap.xml\n")

sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for fname in PAGES:
    loc = BASE_URL + "/" + ("" if fname == "index.html" else fname)
    pri = "1.0" if fname == "index.html" else "0.7"
    sitemap.append(f"  <url><loc>{loc}</loc><changefreq>monthly</changefreq><priority>{pri}</priority></url>")
sitemap.append("</urlset>\n")
with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write("\n".join(sitemap))
print("wrote robots.txt + sitemap.xml")

print("done")
