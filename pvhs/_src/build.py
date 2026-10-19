#!/usr/bin/env python3
"""Writes the static pages in schoolflo/pvhs/ (English) and schoolflo/pvhs/es/ (Spanish).

Run from anywhere:  python3 pvhs/_src/build.py
Header and footer are shared here so every page stays identical; the output is plain
HTML with no build step on the server. Spanish pages are made from the English pages
by translating every text segment through es.py (the build stops if a segment has no
translation). The _src folder is not published (GitHub Pages skips folders that start
with an underscore)."""
import os
import re
import sys
from html import escape
from html.parser import HTMLParser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from es import ES, KEEP  # noqa: E402

OUT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
V = "28"  # cache bust for css/js

# Teal bar: top level only. DM_PAGES highlight "Digital Media" too.
NAV = [
    ("index.html", "Visual Arts"),
    ("fine-art.html", "Art"),
    ("digital-media.html", "Digital Media"),
    ("teachers.html", "Our Teachers"),
    ("signup.html", "Sign Up"),
]
DM_PAGES = ("digital-media.html", "digital-photography.html", "digital-arts.html")

# Hamburger menu: every page and course. (level, href, label)
MENU = [
    (1, "index.html", "Visual Arts"),
    (1, "fine-art.html", "Art"),
    (2, "fine-art.html#intro-to-art", "Intro to Art"),
    (2, "fine-art.html#painting", "Painting 1"),
    (1, "digital-media.html", "Digital Media"),
    (2, "digital-photography.html", "Digital Photography"),
    (3, "digital-photography.html#photography-1", "Photography 1"),
    (3, "digital-photography.html#photography-2", "Photography 2"),
    (2, "digital-arts.html", "Digital Arts"),
    (3, "digital-arts.html#digital-arts-1", "Digital Arts 1"),
    (3, "digital-arts.html#digital-arts-2", "Digital Arts 2"),
    (1, "teachers.html", "Our Teachers"),
    (1, "signup.html", "Sign Up"),
]


def head(title, desc, path, preload=None, lang="en", noindex=False):
    pre = ""
    if preload:
        pre = (
            f'  <link rel="preload" as="image" href="images/{preload}-m.jpg" media="(max-width: 760px)" fetchpriority="high">\n'
            f'  <link rel="preload" as="image" href="images/{preload}.jpg" media="(min-width: 761px)" fetchpriority="high">\n'
        )
    page = "" if path == "index.html" else path
    url_en = "https://www.schoolflo.org/pvhs/" + page
    url_es = "https://www.schoolflo.org/pvhs/es/" + page
    url = url_es if lang == "es" else url_en
    robots = '  <meta name="robots" content="noindex">\n' if noindex else ""
    admin_href = "../admin.html" if lang == "es" else "admin.html"
    alts = "" if noindex else (
        f'  <link rel="alternate" hreflang="en" href="{url_en}">\n'
        f'  <link rel="alternate" hreflang="es" href="{url_es}">\n')
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{url}">
  <meta property="og:site_name" content="PVHS Visual Arts">
  <meta property="og:image" content="https://www.schoolflo.org/pvhs/images/hero-home.jpg">
  <meta name="theme-color" content="#0b0d0d">
  <meta name="format-detection" content="telephone=no">
{robots}{alts}  <link rel="icon" type="image/png" sizes="64x64" href="images/favicon-64.png">
  <link rel="apple-touch-icon" sizes="180x180" href="images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Oswald:wght@400;500;600;700&display=swap" rel="stylesheet">
{pre}  <link rel="stylesheet" href="css/style.css?v={V}">
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>

  <header class="masthead">
    <div class="wrap">
      <a class="brand" href="index.html" aria-label="PVHS Visual Arts home">
        <img class="mark" src="images/pvhs-logo.png" alt="Pioneer Valley High School Panthers logo" width="74" height="80">
        <div>
          <div class="brand-name">PVHS Visual Arts</div>
          <div class="brand-sub">Pioneer Valley High School<span class="brand-city"> &middot; Santa Maria, CA</span></div>
        </div>
      </a>
      <div class="mast-actions">
{lang_toggle(path, lang)}
        <div class="staffmenu">
          <button class="staffmenu-btn" type="button" aria-expanded="false" aria-controls="staffmenu-list" aria-label="More options"><span class="bars" aria-hidden="true"></span></button>
          <ul class="staffmenu-list" id="staffmenu-list" hidden>
{menu_items(path, admin_href, "staffmenu-list")}
          </ul>
        </div>
      </div>
      <button class="navtoggle" aria-expanded="false" aria-controls="navlist" aria-label="Open menu"><span class="bars" aria-hidden="true"></span><span class="navtoggle-label">Menu</span></button>
    </div>
  </header>

  <nav class="mainnav" aria-label="Main">
    <div class="wrap">
      <a class="dock-logo" href="index.html" aria-label="PVHS Visual Arts home" tabindex="-1"><img src="images/pvhs-logo.png" alt="" width="40" height="43"></a>
      <ul id="navlist">
{nav_items(path)}
{menu_items(path, admin_href, "navlist")}
      </ul>
      <div class="dock-tools">
{lang_toggle(path, lang)}
        <div class="staffmenu">
          <button class="staffmenu-btn" type="button" aria-expanded="false" aria-controls="dockmenu-list" aria-label="More options"><span class="bars" aria-hidden="true"></span></button>
          <ul class="staffmenu-list" id="dockmenu-list" hidden>
{menu_items(path, admin_href, "staffmenu-list")}
          </ul>
        </div>
      </div>
    </div>
  </nav>

  <main id="main">
"""


def lang_toggle(path, lang):
    """EN / ES switch. On English pages ES points into es/, on Spanish pages EN points back up.
    data-keep-href stops the Spanish path rewriter from touching these links."""
    en_href = f"../{path}" if lang == "es" else path
    es_href = path if lang == "es" else f"es/{path}"
    en_cur = ' aria-current="true"' if lang == "en" else ""
    es_cur = ' aria-current="true"' if lang == "es" else ""
    return (
        f'        <div class="langtoggle" role="group" aria-label="Language / Idioma">'
        f'<a href="{en_href}" hreflang="en" lang="en" data-lang="en" data-keep-href{en_cur}>EN</a>'
        f'<a href="{es_href}" hreflang="es" lang="es" data-lang="es" data-keep-href{es_cur}>ES</a></div>'
    )


def nav_items(path):
    """Teal bar links (desktop). Hidden on phones, where the full menu below shows instead."""
    rows = []
    for href, label in NAV:
        on = href == path or (href == "digital-media.html" and path in DM_PAGES)
        cur = ' aria-current="page"' if on else ""
        rows.append(f'        <li class="nav-top"><a href="{href}"{cur}>{label}</a></li>')
    return "\n".join(rows)


def menu_items(path, admin_href, where):
    """Full menu with every page and course, used by the top right menu (desktop) and the
    phone menu. Light Writerz only shows on the Digital Photography page."""
    pad = "            " if where == "staffmenu-list" else "        "
    cls = "menu" if where == "staffmenu-list" else "nav-full"
    rows = []
    for level, href, label in MENU:
        cur = ' aria-current="page"' if href == path else ""
        rows.append(f'{pad}<li class="{cls} lvl{level}"><a href="{href}"{cur}>{label}</a></li>')
        if href == "digital-photography.html#photography-2" and path == "digital-photography.html":
            rows.append(f'{pad}<li class="{cls} lvl3"><a href="https://www.lightwriterz.org" target="_blank" rel="noopener">Light Writerz</a></li>')
    rows.append(f'{pad}<li class="{cls} lvl1 staff"><a href="{admin_href}" data-keep-href>Teacher Login</a></li>')
    return "\n".join(rows)


def foot(extra_scripts=""):
    return f"""  </main>

  <footer class="site">
    <div class="wrap">
      <div class="cols">
        <div>
          <a href="index.html" aria-label="PVHS Visual Arts home"><img class="foot-mark" src="images/pvhs-logo.png" alt="Pioneer Valley High School Panthers logo" width="89" height="96"></a>
          <p class="motto">Learn it. Make it.<br><span>Present it.</span></p>
          <p>Visual Arts at Pioneer Valley High School: Digital Media, a Career Technical Education pathway in Arts, Media, and Entertainment, and Art.</p>
        </div>
        <div>
          <h4>Visual Arts</h4>
          <ul>
            <li><a href="index.html">Program Overview</a></li>
            <li><a href="digital-media.html">Digital Media</a></li>
            <li><a href="digital-photography.html">Digital Photography</a></li>
            <li><a href="digital-arts.html">Digital Arts</a></li>
            <li><a href="fine-art.html">Art</a></li>
            <li><a href="teachers.html">Our Teachers</a></li>
            <li><a href="signup.html?from=footer">Sign Up</a></li>
          </ul>
        </div>
        <div>
          <h4>Courses</h4>
          <ul>
            <li><a href="digital-photography.html#photography-1">Photography 1</a></li>
            <li><a href="digital-photography.html#photography-2">Photography 2</a></li>
            <li><a href="digital-arts.html#digital-arts-1">Digital Arts 1</a></li>
            <li><a href="digital-arts.html#digital-arts-2">Digital Arts 2</a></li>
            <li><a href="fine-art.html#intro-to-art">Intro to Art</a></li>
            <li><a href="fine-art.html#painting">Painting 1</a></li>
          </ul>
        </div>
        <div>
          <h4>Connect</h4>
          <ul>
            <li><a href="index.html#skillsusa">SkillsUSA</a></li>
            <li><a href="https://www.lightwriterz.org" target="_blank" rel="noopener">Light Writerz Photo Club</a></li>
            <li><a href="../">SchoolFlo</a></li>
            <li>Pioneer Valley High School<br>Santa Maria, CA</li>
          </ul>
        </div>
      </div>
      <div class="legal">
        <span>&copy; <span id="yr">2026</span> PVHS Visual Arts &middot; Pioneer Valley High School</span>
        <span>Hosted on <a href="../">SchoolFlo</a> &middot; <a href="admin.html" rel="nofollow">Staff login</a></span>
      </div>
    </div>
  </footer>

  <script src="js/main.js?v={V}" defer></script>
{extra_scripts}</body>
</html>
"""

# ---------------------------------------------------------------- Digital Media hub
DM = """
    <section class="hero page hero-photo">
      <div class="wrap">
        <p class="eyebrow">Visual Arts &middot; Digital Media</p>
        <h1>Digital<br><span class="accent">Media</span></h1>
        <p>A Career Technical Education program in the Design, Visual, and Media Arts pathway. Two pathways, Digital Photography and Digital Arts, built on real cameras and industry software.</p>
      </div>
    </section>

    <section class="band">
      <div class="wrap">
        <div class="section-head">
          <h2>Two Pathways</h2>
          <span class="sub">Start with level 1, grow into level 2</span>
        </div>
        <div class="cards two programs">
          <article class="card program">
            <div class="cover" style="background-image:url('images/hero-photo-m.jpg')" role="img" aria-label="Student light painting photograph"></div>
            <div class="body">
              <p class="kicker">Digital Media</p>
              <h3>Digital Photography</h3>
              <ul class="courses">
                <li>Photography 1<span>Foundation &middot; no experience needed</span></li>
                <li>Photography 2<span>Advanced &middot; lighting and studio</span></li>
              </ul>
              <p>Operate a real camera on Manual, see like a photographer, shape light on purpose, and finish images in Adobe Lightroom Classic and Photoshop.</p>
              <div class="card-actions"><a class="btn dark" href="digital-photography.html">Explore Photography</a><a class="text-link" href="signup.html?course=photography-1&amp;from=digital-media">Sign up</a></div>
            </div>
          </article>
          <article class="card program gold-top">
            <div class="cover" style="background-image:url('images/hero-arts-m.jpg')" role="img" aria-label="Student magazine cover designs"></div>
            <div class="body">
              <p class="kicker">Digital Media</p>
              <h3>Digital Arts</h3>
              <ul class="courses">
                <li>Digital Arts 1<span>Foundation &middot; no experience needed</span></li>
                <li>Digital Arts 2<span>Advanced &middot; brand and portfolio</span></li>
              </ul>
              <p>Learn the elements and principles of design, then use Adobe Illustrator and Photoshop to make clean, intentional graphics, brands, and portfolio work.</p>
              <div class="card-actions"><a class="btn dark" href="digital-arts.html">Explore Digital Arts</a><a class="text-link" href="signup.html?course=digital-arts-1&amp;from=digital-media">Sign up</a></div>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="band teal tight">
      <div class="wrap">
        <ul class="checklist one">
          <li><strong>Bilingual materials.</strong> In Digital Media, project directions and handouts are offered in English and Spanish, and students may submit their work in either language.</li>
          <li><strong>Fine arts credit.</strong> Every Visual Arts course satisfies the UC and CSU A-G &ldquo;F&rdquo; Visual and Performing Arts requirement.</li>
          <li><strong>Career:</strong> a CTE pathway in Arts, Media, and Entertainment, with SkillsUSA.</li>
        </ul>
        <p class="cta-row" style="margin-top:24px"><a class="btn dark btn-logo" href="index.html#skillsusa"><img src="images/skillsusa-gold.png" alt="SkillsUSA" width="598" height="292"></a> <a class="btn dark" href="teachers.html">Our Teachers</a></p>
      </div>
    </section>
"""

# ---------------------------------------------------------------- Home
HOME = """
    <section class="hero hero-home">
      <div class="wrap">
        <p class="eyebrow">Pioneer Valley High School &middot; Visual Arts</p>
        <h1>Visual<br><span class="accent">Arts</span></h1>
        <p>Photography, digital design, drawing, and painting. Learn on real cameras, industry software, and in the art studio, and build a portfolio of finished work.</p>
        <div class="actions">
          <a class="btn" href="#programs">Digital Media</a>
          <a class="btn ghost" href="fine-art.html">Art</a>
        </div>
      </div>
    </section>

    <div class="tiles">
      <div class="wrap">
        <ul>
          <li><a href="digital-media.html"><span class="num">01</span><h2>Digital Media</h2><span class="more">Photography &amp; Digital Arts</span></a></li>
          <li><a href="fine-art.html"><span class="num">02</span><h2>Art</h2><span class="more">Intro to Art &amp; Painting 1</span></a></li>
          <li><a href="teachers.html"><span class="num">03</span><h2>Our Teachers</h2><span class="more">Meet the team</span></a></li>
          <li><a href="signup.html?from=home"><span class="num">04</span><h2>Sign Up</h2><span class="more">Interest form</span></a></li>
        </ul>
      </div>
    </div>

    <section class="band">
      <div class="wrap split">
        <div>
          <p class="eyebrow">About the program</p>
          <h2 class="title taglines"><span class="tg"><small>Photography</small>Focus it. Capture it. Create it.</span><span class="tg"><small>Digital Arts</small>Imagine it. Design it. Create it.</span></h2>
          <p class="lead" style="margin-top:18px">PVHS Visual Arts brings together two areas: Digital Media, a Career Technical Education program in the Design, Visual, and Media Arts pathway, and Art, where students build drawing and painting skills by hand.</p>
          <p class="muted">In every class, students learn by making: real tools, clear steps, and finished work they can present. By the end of a course sequence, students have a body of work that shows what they can do.</p>
          <ul class="checklist one">
            <li><strong>Two areas, one program.</strong> Digital Media covers Digital Photography and Digital Arts. Art covers Intro to Art and Painting 1.</li>
            <li><strong>Bilingual materials.</strong> In Digital Media, project directions and handouts are offered in English and Spanish, and students may submit their work in either language.</li>
            <li><strong>Fine arts credit.</strong> Every Visual Arts course satisfies the UC and CSU A-G &ldquo;F&rdquo; Visual and Performing Arts requirement.</li>
            <li><strong>Open to everyone.</strong> Photography 1, Digital Arts 1, Intro to Art, and Painting 1 need no experience.</li>
          </ul>
        </div>
        <figure class="photo-fig"><img src="images/work/light-02.jpg" alt="Student work: a student in a blue sweater surrounded by loops of light, a light painting photograph" loading="lazy" width="900" height="600"><figcaption>Student work: writing with light, a long exposure project.</figcaption></figure>
      </div>
    </section>

    <section class="band ag" id="a-g">
      <div class="wrap split">
        <div class="ag-badge" aria-hidden="true"><span class="ag-top">UC / CSU A-G</span><span class="ag-letter">F</span><span class="ag-bot">Visual &amp; Performing Arts</span></div>
        <div>
          <p class="eyebrow" style="color:var(--gold)">College ready elective</p>
          <h2 class="title">The &ldquo;F&rdquo; in A-G</h2>
          <p class="lead" style="margin-top:18px">Every Visual Arts course, from Photography and Digital Arts to Intro to Art and Painting 1, satisfies the UC and CSU A-G &ldquo;F&rdquo; Visual and Performing Arts requirement.</p>
          <p class="muted">To be eligible for the University of California and California State University, students need a year of Visual and Performing Arts. Any Visual Arts course covers that requirement, and Digital Media also builds real career skills on industry tools, so one elective can work toward college and career at the same time.</p>
          <ul class="checklist one">
            <li><strong>College:</strong> counts as fine art (&ldquo;F&rdquo;) for UC and CSU admission.</li>
            <li><strong>Career:</strong> a CTE pathway in Arts, Media, and Entertainment, with SkillsUSA.</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="band teal tight">
      <div class="wrap stats four">
        <div><div class="n">6</div><div class="l">Courses</div></div>
        <div><div class="n">35+</div><div class="l">Years of industry experience</div></div>
        <div><div class="n word">A-G &ldquo;F&rdquo;</div><div class="l">Fine arts credit</div></div>
        <div><div class="n logo"><img src="images/skillsusa-gold.png" alt="SkillsUSA" width="598" height="292"></div><div class="l">Student organization</div></div>
      </div>
    </section>

    <section class="band" id="programs">
      <div class="wrap">
        <div class="section-head">
          <h2>Two Categories, Six Courses</h2>
          <span class="sub">Digital Media and Art &middot; start with level 1, grow into level 2</span>
        </div>
        <div class="prog-group">
          <h3 class="group-label"><a href="digital-media.html">Digital Media</a></h3>
          <div class="cards two programs">
          <article class="card program">
            <div class="cover" style="background-image:url('images/hero-photo-m.jpg')" role="img" aria-label="Student light painting photograph"></div>
            <div class="body">
              <h3>Digital Photography</h3>
              <p class="kicker">Photography 1 &amp; 2</p>
              <p>Operate a real camera on Manual, see like a photographer, shape light on purpose, and finish images in Adobe Lightroom Classic and Photoshop.</p>
              <div class="card-actions"><a class="btn dark" href="digital-photography.html">Explore Photography</a><a class="text-link" href="signup.html?course=photography-1&amp;from=home">Sign up</a></div>
            </div>
          </article>
          <article class="card program gold-top">
            <div class="cover" style="background-image:url('images/hero-arts-m.jpg')" role="img" aria-label="Student magazine cover designs"></div>
            <div class="body">
              <h3>Digital Arts</h3>
              <p class="kicker">Digital Arts 1 &amp; 2</p>
              <p>Learn the elements and principles of design, then use Adobe Illustrator and Photoshop to make clean, intentional graphics, brands, and portfolio work.</p>
              <div class="card-actions"><a class="btn dark" href="digital-arts.html">Explore Digital Arts</a><a class="text-link" href="signup.html?course=digital-arts-1&amp;from=home">Sign up</a></div>
            </div>
          </article>
          </div>
        </div>
        <div class="prog-group">
          <h3 class="group-label"><a href="fine-art.html">Art</a></h3>
          <div class="cards two programs">
          <article class="card program">
            <div class="cover cover-fineart" role="img" aria-label="Art: drawing and painting"></div>
            <div class="body">
              <h3>Intro to Art</h3>
              <p class="kicker">Foundation &middot; no experience needed</p>
              <p>The elements and principles of art, drawing from observation, color, and mixed media. Open to all students.</p>
              <div class="card-actions"><a class="btn dark" href="fine-art.html#intro-to-art">Explore Intro to Art</a><a class="text-link" href="signup.html?course=intro-to-art&amp;from=home">Sign up</a></div>
            </div>
          </article>
          <article class="card program gold-top">
            <div class="cover cover-fineart alt" role="img" aria-label="Art: drawing and painting"></div>
            <div class="body">
              <h3>Painting 1</h3>
              <p class="kicker">Studio &middot; no experience needed</p>
              <p>Watercolor and acrylic, color mixing, composition, and a personal style, building toward finished paintings ready to exhibit.</p>
              <div class="card-actions"><a class="btn dark" href="fine-art.html#painting">Explore Painting 1</a><a class="text-link" href="signup.html?course=painting&amp;from=home">Sign up</a></div>
            </div>
          </article>
          </div>
        </div>
      </div>
    </section>

    <section class="band skills" id="skillsusa">
      <div class="wrap split">
        <div>
          <p class="eyebrow" style="color:var(--gold)">Career Technical Student Organization</p>
          <h2 class="title skills-title"><img src="images/skillsusa-gold.png" alt="SkillsUSA" width="598" height="292"></h2>
          <p class="lead" style="margin-top:18px">The PVHS Digital Media program is associated with SkillsUSA for both the Digital Photography and Digital Arts pathways.</p>
          <p class="muted">SkillsUSA is a national organization for career and technical students. It helps students build leadership, teamwork, and workplace skills, and gives them a place to show their technical work beyond the classroom.</p>
          <p style="margin-top:26px"><a class="btn dark" href="https://www.skillsusa.org" target="_blank" rel="noopener">Visit SkillsUSA</a></p>
        </div>
        <div class="cards two status">
          <article class="card">
            <p class="kicker">Pathway status</p>
            <h3>Concentrator</h3>
            <p>A student who builds depth in one pathway by moving past the first course, for example Photography 1 into Photography 2, or Digital Arts 1 into Digital Arts 2.</p>
          </article>
          <article class="card gold-top">
            <p class="kicker">Pathway status</p>
            <h3>Completer</h3>
            <p>A student who finishes the full course sequence in a pathway. Completers leave with a body of finished work and real industry skills.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="band dark">
      <div class="wrap">
        <div class="section-head">
          <h2>How Every Project Runs</h2>
          <span class="sub">The same five steps in every Digital Media course</span>
        </div>
        <ol class="principles">
          <li><strong>Learn the concept</strong><span>A short, plain language overview introduces the idea and its key vocabulary.</span></li>
          <li><strong>Make or capture</strong><span>Photograph with a camera kit, or build a design in Adobe software.</span></li>
          <li><strong>Edit and finish</strong><span>Cull, edit, and export the work to a professional standard.</span></li>
          <li><strong>Turn it in</strong><span>Each step submits a clear deliverable to Canvas: a photo, a contact sheet, a design file, a high resolution export.</span></li>
          <li><strong>Reflect</strong><span>A short written reflection: what I did, what I learned, what I would change.</span></li>
        </ol>
        <p class="note" style="margin-top:26px">Students are graded on following the process and meeting the standard for each deliverable, not on being a &ldquo;natural.&rdquo; Clear, repeatable expectations are the point.</p>
      </div>
    </section>

    <section class="band gray">
      <div class="wrap">
        <div class="section-head">
          <h2>Our Teachers</h2>
          <span class="sub">Working photographers, designers, and artists &middot; <a href="teachers.html">Meet the team</a></span>
        </div>
        <div class="team-mini">
          <a class="card" href="teachers.html#chris-silva" style="text-decoration:none;color:inherit"><img class="head" src="images/teachers/chris-silva.jpg" alt="Chris Silva" loading="lazy" width="84" height="84"><div><p class="kicker">Photography &amp; Digital Arts</p><h3>Chris Silva</h3><p>Photography 1 &amp; 2 &middot; Digital Arts 1<br><span class="exp-mini">14 years industry experience</span></p></div></a>
          <a class="card" href="teachers.html#laura-garcia" style="text-decoration:none;color:inherit"><img class="head" src="images/teachers/laura-garcia.jpg" alt="Laura Garcia" loading="lazy" width="84" height="84"><div><p class="kicker">Photography</p><h3>Laura Garcia</h3><p>Photography 1<br><span class="exp-mini">14 years industry experience</span></p></div></a>
          <a class="card" href="teachers.html#rileigh-mankin" style="text-decoration:none;color:inherit"><img class="head" src="images/teachers/rileigh-mankin.jpg" alt="Rileigh Mankin" loading="lazy" width="84" height="84"><div><p class="kicker">Digital Arts</p><h3>Rileigh Mankin</h3><p>Digital Arts 1 &amp; 2<br><span class="exp-mini">7 years industry experience</span></p></div></a>
          <a class="card" href="teachers.html#stephanie-fikri" style="text-decoration:none;color:inherit"><span class="head logo-head"><img src="images/pvhs-logo.png" alt="" width="60" height="65"></span><div><p class="kicker">Art</p><h3>Stephanie Fikri</h3><p>Intro to Art &middot; Painting 1</p></div></a>
        </div>
      </div>
    </section>

    <section class="band dark">
      <div class="wrap">
        <blockquote class="pull">Learn the concept. Make the work.<br><span class="accent">Present it like a professional.</span><cite>The PVHS Visual Arts standard</cite></blockquote>
        <p class="cta-row" style="margin-top:36px"><a class="btn" href="signup.html?course=photography-1&amp;from=home">Sign up for Photography 1</a> <a class="btn dark" href="signup.html?course=digital-arts-1&amp;from=home">Sign up for Digital Arts 1</a> <a class="btn dark" href="signup.html?course=intro-to-art&amp;from=home">Sign up for Intro to Art</a></p>
        <p class="note" style="margin-top:18px">Interested? Fill out the sign up form so our teachers can follow up, and ask your counselor about adding the class to your schedule.</p>
      </div>
    </section>
"""

# ---------------------------------------------------------------- Photography
PHOTO = """
    <section class="hero page hero-photo">
      <div class="wrap">
        <p class="eyebrow">Visual Arts &middot; Digital Media</p>
        <h1>Digital<br>Photography</h1>
        <p class="tagline">Focus it. Capture it. Create it.</p>
        <p>From Manual mode to studio lighting. Two courses that teach students to see, capture, and finish photographs on purpose.</p>
      </div>
    </section>

    <section class="band tight">
      <div class="wrap">
        <div class="cards two">
          <a class="card" href="#photography-1" style="text-decoration:none;color:inherit"><p class="kicker">Foundation</p><h3>Photography 1</h3><p>Operate a real camera on Manual, see like a photographer, and finish images with professional editing software. Open to all students.</p></a>
          <a class="card gold-top" href="#photography-2" style="text-decoration:none;color:inherit"><p class="kicker">Advanced</p><h3>Photography 2</h3><p>Move from a good exposure to controlling light and telling a story on purpose, with flash, studio work, and a personal style.</p></a>
        </div>
      </div>
    </section>

    <section class="band">
      <div class="wrap">

        <article class="course" id="photography-1">
          <div class="course-side">
            <span class="course-level entry">Level 1 &middot; Foundation</span>
            <h2>Photography 1</h2>
            <p class="identity">The foundation photography course. Students learn to operate a real camera on Manual, see like a photographer, and finish their images with professional editing software.</p>
            <ul class="facts">
              <li><span class="k">A-G credit</span><span class="v">UC / CSU &ldquo;F&rdquo; Visual and Performing Arts</span></li>
              <li><span class="k">Taught by</span><span class="v"><a href="teachers.html#chris-silva">Chris Silva</a> &middot; <a href="teachers.html#laura-garcia">Laura Garcia</a></span></li>
              <li><span class="k">Who it is for</span><span class="v">Open to all students, no experience required. The entry point to the photography pathway.</span></li>
              <li><span class="k">Cameras</span><span class="v">Canon mirrorless camera kits: body, lenses, battery, charger, memory card.</span></li>
              <li><span class="k">Software</span><span class="v">Adobe Lightroom Classic, plus Adobe Photoshop near the end of the year.</span></li>
              <li><span class="k">Lab</span><span class="v">Mac computers, with the school iPad as a scanner.</span></li>
            </ul>
            <a class="btn signup-btn" href="signup.html?course=photography-1&amp;from=digital-photography">Sign up for Photography 1</a>
          </div>
          <div class="course-main">
            <h3>What students will be able to do</h3>
            <ul class="checklist one">
              <li>Operate a camera in Manual mode and capture in RAW, controlling aperture, shutter speed, and ISO.</li>
              <li>Read and use available light, and balance exposure across different settings.</li>
              <li>Apply composition: framing, the rule of thirds, leading lines, and point of view.</li>
              <li>Import, cull, and edit a set of photos, and build contact sheets of the full take and the final selections.</li>
              <li>Export finished, high resolution images and present them cleanly.</li>
            </ul>

            <h3>Core units</h3>
            <div class="units">
              <div class="unit"><strong>Camera fundamentals</strong><span>Manual mode, RAW, exposure (aperture, shutter, ISO), focus, and lens choice.</span></div>
              <div class="unit"><strong>Seeing &amp; composition</strong><span>Framing, the rule of thirds, leading lines, perspective, and finding images where others see none.</span></div>
              <div class="unit"><strong>Editing workflow</strong><span>Import, cull, edit for exposure and color, export, and contact sheets.</span></div>
              <div class="unit"><strong>Creative projects</strong><span>Themed photo walks and studio style challenges that put the skills to work.</span></div>
              <div class="unit"><strong>Intro to compositing</strong><span>A first Photoshop project that combines finished photos into one piece.</span></div>
            </div>

            <h3>Example projects</h3>
            <ul class="tags">
              <li>Self-Portrait</li><li>Composition Concepts</li><li>Leading Lines Photo Walk</li><li>Image Series Photo Walk</li><li>Lightroom Editing</li><li>Tiny Things</li><li>Balloon Pop</li><li>Aperture Portrait</li><li>Exposure Balance</li><li>Spell Your Name Photo Walk</li>
            </ul>

            <div class="callout">
              <p class="k">How the year builds</p>
              <p>Early projects teach one skill at a time: composition first, then the editing workflow, then a single camera control. Later projects combine skills. The year closes by moving finished photos into Photoshop, which sets up Photography 2 and the Digital Arts courses.</p>
            </div>
          </div>
        </article>

        <article class="course" id="photography-2">
          <div class="course-side">
            <span class="course-level">Level 2 &middot; Advanced</span>
            <h2>Photography 2</h2>
            <p class="identity">The advanced photography course. Students move from &ldquo;getting a good exposure&rdquo; to controlling light and telling a story on purpose.</p>
            <ul class="facts">
              <li><span class="k">A-G credit</span><span class="v">UC / CSU &ldquo;F&rdquo; Visual and Performing Arts</span></li>
              <li><span class="k">Taught by</span><span class="v"><a href="teachers.html#chris-silva">Chris Silva</a></span></li>
              <li><span class="k">Who it is for</span><span class="v">Students who completed Photography 1, or who can show the fundamentals: Manual mode, RAW, and the Lightroom workflow.</span></li>
              <li><span class="k">Lighting gear</span><span class="v">Speedlites and off camera flash, modifiers, backdrops, tripods, reflectors, and a studio setup.</span></li>
              <li><span class="k">Cameras</span><span class="v">Everything in Photography 1, plus camera kits reserved for the advanced course.</span></li>
            </ul>
            <a class="btn signup-btn" href="signup.html?course=photography-2&amp;from=digital-photography">Sign up for Photography 2</a>
          </div>
          <div class="course-main">
            <h3>What students will be able to do</h3>
            <ul class="checklist one">
              <li>Shape light on purpose: off camera flash, studio lighting, and mixed or available light.</li>
              <li>Plan and direct a session, and work with a subject to make an intentional portrait.</li>
              <li>Build and apply their own editing presets for a consistent personal style.</li>
              <li>Hold a higher creative bar: natural only constraints, series that read as a body of work, and refined final edits.</li>
            </ul>

            <h3>Core units</h3>
            <div class="units">
              <div class="unit"><strong>Lighting</strong><span>Off camera flash, studio sessions, modifiers, and controlling the look of light.</span></div>
              <div class="unit"><strong>Advanced exposure &amp; lenses</strong><span>Deliberate aperture and depth of field choices across the full lens kit.</span></div>
              <div class="unit"><strong>Style &amp; workflow</strong><span>Building custom presets and developing a consistent personal edit.</span></div>
              <div class="unit"><strong>Concept &amp; series</strong><span>Themed bodies of work with a tighter creative constraint.</span></div>
              <div class="unit"><strong>Portraiture</strong><span>Working with a subject, posing, and direction.</span></div>
            </div>

            <h3>Example projects</h3>
            <ul class="tags">
              <li>Composition Photo Walk</li><li>Off-Camera Flash</li><li>Studio Session</li><li>Build Your Own Preset</li><li>Tiny Things</li><li>Balloon Pop</li><li>Aperture Portrait</li><li>Exposure Balance</li><li>Spell Your Name Photo Walk</li>
            </ul>

            <div class="callout">
              <p class="k">Same rhythm, higher ceiling</p>
              <p>Photography 1 teaches one control at a time. Photography 2 adds lighting, often requires natural only or self directed work, and expects students to run the full capture to delivery pipeline on their own.</p>
            </div>
            <div class="callout skills-callout">
              <p class="k k-logo"><img src="images/skillsusa-gold.png" alt="SkillsUSA" width="598" height="292"><span>Concentrators &amp; Completers</span></p>
              <p>The Digital Photography pathway is associated with SkillsUSA. Students who continue past level 1 become pathway concentrators, and students who finish the full sequence become pathway completers. <a href="index.html#skillsusa">Learn more</a></p>
            </div>
          </div>
        </article>

      </div>
    </section>

    <section class="band gray">
      <div class="wrap">
        <div class="section-head">
          <h2>Student Work</h2>
          <span class="sub">Writing with light and multiple exposures</span>
        </div>
        <div class="work">
          <figure><img src="images/work/light-01.jpg" alt="Ribbons of light spiral around a student standing in the dark" loading="lazy" width="900" height="600"><figcaption><b>Writing with Light</b>Long exposure light painting</figcaption></figure>
          <figure><img src="images/work/light-04.jpg" alt="Dense scribbles of light across a dark frame, a face glowing behind them" loading="lazy" width="900" height="600"><figcaption><b>Writing with Light</b>Long exposure light painting</figcaption></figure>
          <figure><img src="images/work/light-02.jpg" alt="A student in a blue sweater surrounded by loops of light" loading="lazy" width="900" height="600"><figcaption><b>Writing with Light</b>Long exposure light painting</figcaption></figure>
        </div>
        <div class="work tall" style="margin-top:18px">
          <figure><img src="images/work/multiples-01.jpg" alt="Portrait of a student in a striped sweater under violet light" loading="lazy" width="900" height="1350"><figcaption><b>Multiples</b>Multiple exposure portrait</figcaption></figure>
          <figure><img src="images/work/multiples-02.jpg" alt="Black and white multiple exposure portrait of a student" loading="lazy" width="900" height="1350"><figcaption><b>Multiples</b>Multiple exposure portrait</figcaption></figure>
          <figure><img src="images/work/multiples-03.jpg" alt="Multiple exposure portrait of a student with glasses in violet and red" loading="lazy" width="900" height="1350"><figcaption><b>Multiples</b>Multiple exposure portrait</figcaption></figure>
        </div>
        <p style="margin-top:32px"><a class="btn dark" href="https://www.lightwriterz.org/gallery.html" target="_blank" rel="noopener">See more in the Light Writerz gallery</a></p>
      </div>
    </section>
"""

# ---------------------------------------------------------------- Digital Arts
ARTS = """
    <section class="hero page hero-arts">
      <div class="wrap">
        <p class="eyebrow">Visual Arts &middot; Digital Media</p>
        <h1>Digital<br>Arts</h1>
        <p class="tagline">Imagine it. Design it. Create it.</p>
        <p>Design with intention. Two courses that build from the elements of art to brand systems and portfolio quality work in Adobe Illustrator and Photoshop.</p>
      </div>
    </section>

    <section class="band tight">
      <div class="wrap">
        <div class="cards two">
          <a class="card" href="#digital-arts-1" style="text-decoration:none;color:inherit"><p class="kicker">Foundation</p><h3>Digital Arts 1</h3><p>The elements and principles of design, plus the industry standard Adobe tools to make clean, intentional graphics. Open to all students.</p></a>
          <a class="card gold-top" href="#digital-arts-2" style="text-decoration:none;color:inherit"><p class="kicker">Advanced</p><h3>Digital Arts 2</h3><p>Move from exercises to real, portfolio quality design work: brand systems, campaigns, layouts, and client briefs.</p></a>
        </div>
      </div>
    </section>

    <section class="band">
      <div class="wrap">

        <article class="course" id="digital-arts-1">
          <div class="course-side">
            <span class="course-level entry">Level 1 &middot; Foundation</span>
            <h2>Digital Arts 1</h2>
            <p class="identity">The foundation design course. Students learn the elements and principles of design and the industry standard Adobe tools to make clean, intentional graphics.</p>
            <ul class="facts">
              <li><span class="k">A-G credit</span><span class="v">UC / CSU &ldquo;F&rdquo; Visual and Performing Arts</span></li>
              <li><span class="k">Taught by</span><span class="v"><a href="teachers.html#chris-silva">Chris Silva</a> &middot; <a href="teachers.html#rileigh-mankin">Rileigh Mankin</a></span></li>
              <li><span class="k">Who it is for</span><span class="v">Open to all students, no experience required. The entry point to the design and graphic arts pathway.</span></li>
              <li><span class="k">Software</span><span class="v">Adobe Illustrator for vector art, logos, and type. Adobe Photoshop for image editing, compositing, and mockups.</span></li>
              <li><span class="k">Lab</span><span class="v">Mac computers, with the school iPad as a scanner for sketches and hand done work.</span></li>
            </ul>
            <a class="btn signup-btn" href="signup.html?course=digital-arts-1&amp;from=digital-arts">Sign up for Digital Arts 1</a>
          </div>
          <div class="course-main">
            <h3>What students will be able to do</h3>
            <ul class="checklist one">
              <li>Use the elements and principles of art and design on purpose: line, shape, color, form, balance, contrast, and type.</li>
              <li>Work the core Adobe tools: the Illustrator workspace, drawing and pen tools, type, layers, and exporting, plus Photoshop layers and placement.</li>
              <li>Take an idea from sketch to finished digital artwork, by vector tracing or by compositing.</li>
              <li>Apply color theory and typography to communicate a clear message.</li>
              <li>Produce finished, export ready graphics at a stated size and format.</li>
            </ul>

            <h3>Core units</h3>
            <div class="units">
              <div class="unit"><strong>Design foundations</strong><span>The elements and principles of art, color theory, and typography.</span></div>
              <div class="unit"><strong>Illustrator skills</strong><span>Workspace, drawing and pen tools, shapes, type, layers, and sketch to vector.</span></div>
              <div class="unit"><strong>Photoshop skills</strong><span>Layers, placing and sizing images, simple compositing, and export.</span></div>
              <div class="unit"><strong>Applied projects</strong><span>Posters, covers, pictograms and icons, character design, and brand graphics.</span></div>
              <div class="unit"><strong>Communication</strong><span>Making work that reads clearly and serves a purpose or a client.</span></div>
            </div>

            <h3>Example projects</h3>
            <ul class="tags">
              <li>Pictograms</li><li>Color Theory</li><li>Sketchbook Cover Art</li><li>Motivational Poster</li><li>Live Stream Graphic</li><li>Elements of Art / Character Design</li><li>Character Design (Form and Color)</li><li>Get to Know Illustrator</li>
            </ul>

            <div class="callout">
              <p class="k">How the year builds</p>
              <p>Start with design fundamentals and tool familiarity, then short applied projects that each target one or two principles. The year builds toward projects that combine skills into a finished, presentable piece.</p>
            </div>
          </div>
        </article>

        <article class="course" id="digital-arts-2">
          <div class="course-side">
            <span class="course-level">Level 2 &middot; Advanced</span>
            <h2>Digital Arts 2</h2>
            <p class="identity">The advanced design course. Students move from exercises to real, portfolio quality design work and brand projects.</p>
            <ul class="facts">
              <li><span class="k">A-G credit</span><span class="v">UC / CSU &ldquo;F&rdquo; Visual and Performing Arts</span></li>
              <li><span class="k">Taught by</span><span class="v"><a href="teachers.html#rileigh-mankin">Rileigh Mankin</a></span></li>
              <li><span class="k">Who it is for</span><span class="v">Students who completed Digital Arts 1, or who can show the fundamentals and comfort with Illustrator and Photoshop.</span></li>
              <li><span class="k">Software</span><span class="v">Illustrator and Photoshop together at a higher level, plus print and output tools.</span></li>
            </ul>
            <a class="btn signup-btn" href="signup.html?course=digital-arts-2&amp;from=digital-arts">Sign up for Digital Arts 2</a>
          </div>
          <div class="course-main">
            <h3>What students will be able to do</h3>
            <ul class="checklist one">
              <li>Design complete, multi piece projects: a brand system, a campaign, a layout set.</li>
              <li>Work from a brief or a client&rsquo;s needs, make deliberate design choices, and explain them.</li>
              <li>Combine Illustrator and Photoshop in a professional workflow, and prepare files for screen and print.</li>
              <li>Build a portfolio of finished work that shows range and craft.</li>
            </ul>

            <h3>Core units</h3>
            <div class="units">
              <div class="unit"><strong>Branding &amp; identity</strong><span>Logo systems, color and type systems, and a consistent visual language.</span></div>
              <div class="unit"><strong>Layout &amp; production</strong><span>Multi page and multi piece layouts, print and digital output, and file preparation.</span></div>
              <div class="unit"><strong>Client &amp; brief work</strong><span>Designing to a real or simulated client&rsquo;s needs and constraints.</span></div>
              <div class="unit"><strong>Advanced technique</strong><span>More complex Illustrator and Photoshop work, mockups, and presentation.</span></div>
              <div class="unit"><strong>Portfolio</strong><span>Curating and presenting a body of finished work.</span></div>
            </div>

            <div class="callout">
              <p class="k">Brief driven, portfolio focused</p>
              <p>Digital Arts 2 runs as a set of larger, brief driven projects that apply and deepen the Digital Arts 1 foundations. Same rhythm: concept, make, refine, deliver, reflect, with a higher bar on craft, independence, and finish.</p>
            </div>
            <div class="callout skills-callout">
              <p class="k k-logo"><img src="images/skillsusa-gold.png" alt="SkillsUSA" width="598" height="292"><span>Concentrators &amp; Completers</span></p>
              <p>The Digital Arts pathway is associated with SkillsUSA. Students who continue past level 1 become pathway concentrators, and students who finish the full sequence become pathway completers. <a href="index.html#skillsusa">Learn more</a></p>
            </div>
          </div>
        </article>

      </div>
    </section>

    <section class="band gray">
      <div class="wrap">
        <div class="section-head">
          <h2>Student Work</h2>
          <span class="sub">Magazine covers: photography meets design</span>
        </div>
        <div class="work five">
          <figure><img src="images/work/cover-vogue.jpg" alt="Vogue magazine cover by Ella Naoe" loading="lazy" width="900" height="1165"><figcaption><b>Ella Naoe</b>Vogue cover</figcaption></figure>
          <figure><img src="images/work/cover-rolling-stone.jpg" alt="Rolling Stone magazine cover by Gregorio Calleja" loading="lazy" width="900" height="1165"><figcaption><b>Gregorio Calleja</b>Rolling Stone cover</figcaption></figure>
          <figure><img src="images/work/cover-time.jpg" alt="Time magazine cover by Julio Marquez" loading="lazy" width="900" height="1165"><figcaption><b>Julio Marquez</b>Time cover</figcaption></figure>
          <figure><img src="images/work/cover-sports-illustrated.jpg" alt="Sports Illustrated magazine cover by Davina Royall Showalter" loading="lazy" width="900" height="1165"><figcaption><b>Davina Royall Showalter</b>Sports Illustrated cover</figcaption></figure>
          <figure><img src="images/work/cover-people.jpg" alt="People magazine cover by Jessica Valdez" loading="lazy" width="900" height="1165"><figcaption><b>Jessica Valdez</b>People cover</figcaption></figure>
        </div>
      </div>
    </section>
"""


SIGNUP = """
    <section class="hero page hero-signup">
      <div class="wrap">
        <p class="eyebrow">Interest Form</p>
        <h1>Sign Up</h1>
        <p>Want to take Digital Photography, Digital Arts, or Art next school year? Fill out this short form and our teachers will follow up with you.</p>
      </div>
    </section>

    <section class="band">
      <div class="wrap signup-wrap">
        <form class="form signup-form" id="signupForm" novalidate>
          <div class="field">
            <label for="f-name">Full name</label>
            <input id="f-name" name="name" type="text" autocomplete="name" maxlength="80" required placeholder="First and last name">
          </div>
          <div class="field">
            <label for="f-sid">Student ID number</label>
            <input id="f-sid" name="sid" type="text" inputmode="numeric" pattern="[0-9]{6}" maxlength="6" autocomplete="off" required placeholder="6 digits">
            <p class="hint">Your 6 digit PVHS student ID.</p>
          </div>
          <fieldset class="field">
            <legend id="grade-legend">What grade will you be in next school year?</legend>
            <div class="pills" role="radiogroup" aria-labelledby="grade-legend">
              <label class="pill"><input type="radio" name="grade" value="9" required><span>9th grade</span></label>
              <label class="pill"><input type="radio" name="grade" value="10"><span>10th grade</span></label>
              <label class="pill"><input type="radio" name="grade" value="11"><span>11th grade</span></label>
              <label class="pill"><input type="radio" name="grade" value="12"><span>12th grade</span></label>
            </div>
          </fieldset>
          <fieldset class="field">
            <legend>Which classes are you interested in?</legend>
            <p class="hint">Choose one or more.</p>
            <div class="options">
              <label class="option"><input type="checkbox" name="course" value="Photography 1" data-slug="photography-1"><span><b>Photography 1</b><small>Foundation &middot; no experience needed</small></span></label>
              <label class="option"><input type="checkbox" name="course" value="Photography 2" data-slug="photography-2"><span><b>Photography 2</b><small>Advanced &middot; after Photography 1</small></span></label>
              <label class="option"><input type="checkbox" name="course" value="Digital Arts 1" data-slug="digital-arts-1"><span><b>Digital Arts 1</b><small>Foundation &middot; no experience needed</small></span></label>
              <label class="option"><input type="checkbox" name="course" value="Digital Arts 2" data-slug="digital-arts-2"><span><b>Digital Arts 2</b><small>Advanced &middot; after Digital Arts 1</small></span></label>
              <label class="option"><input type="checkbox" name="course" value="Intro to Art" data-slug="intro-to-art"><span><b>Intro to Art</b><small>Foundation &middot; no experience needed</small></span></label>
              <label class="option"><input type="checkbox" name="course" value="Painting" data-slug="painting"><span><b>Painting 1</b><small>Studio &middot; no experience needed</small></span></label>
            </div>
          </fieldset>
          <div class="field">
            <label for="f-note">Questions or comments <span class="opt">(optional)</span></label>
            <textarea id="f-note" name="note" maxlength="500" rows="4"></textarea>
          </div>
          <div class="hp" aria-hidden="true"><label for="f-website">Website</label><input id="f-website" name="website" type="text" tabindex="-1" autocomplete="off"></div>
          <p class="form-msg" id="formMsg" role="alert" hidden></p>
          <button class="btn" type="submit" id="submitBtn">Send my sign up</button>
          <p class="note">This is an interest form, not your official schedule. Your counselor makes the final schedule.</p>
        </form>

        <div class="signup-done" id="signupDone" hidden tabindex="-1">
          <p class="eyebrow">Sent</p>
          <h2 class="title">You are on the list!</h2>
          <p class="lead" id="doneSummary"></p>
          <p class="muted">Our teachers will follow up with you. Remember to also ask your counselor about adding the class to your schedule.</p>
          <p class="cta-row" style="margin-top:24px"><a class="btn" href="index.html">Back to Visual Arts</a> <a class="btn dark" href="signup.html" id="againLink">Sign up another student</a></p>
        </div>

        <aside class="signup-side">
          <div class="card">
            <p class="kicker">Good to know</p>
            <ul class="checklist one">
              <li>Photography 1, Digital Arts 1, Intro to Art, and Painting 1 are open to everyone. No experience needed.</li>
              <li>Every class counts toward the UC and CSU A-G &ldquo;F&rdquo; fine art requirement.</li>
            </ul>
          </div>
        </aside>
      </div>
    </section>
"""

FINE = """
    <section class="hero page hero-fineart">
      <div class="wrap">
        <p class="eyebrow">Visual Arts &middot; Art</p>
        <h1>Art</h1>
        <p>Drawing, color, and painting by hand. Two courses that build observation skills, creative voice, and a body of finished artwork.</p>
      </div>
    </section>

    <section class="band tight">
      <div class="wrap">
        <div class="cards two">
          <a class="card" href="#intro-to-art" style="text-decoration:none;color:inherit"><p class="kicker">Foundation</p><h3>Intro to Art</h3><p>The elements and principles of art, drawing from observation, color, and mixed media. Open to all students.</p></a>
          <a class="card gold-top" href="#painting" style="text-decoration:none;color:inherit"><p class="kicker">Studio</p><h3>Painting 1</h3><p>Watercolor and acrylic, color mixing, composition, and a personal style, building toward finished paintings ready to exhibit.</p></a>
        </div>
        <p class="note" style="margin-top:20px">Course details are being finalized with our Art teacher and may change.</p>
      </div>
    </section>

    <section class="band">
      <div class="wrap">

        <article class="course" id="intro-to-art">
          <div class="course-side">
            <span class="course-level entry">Level 1 &middot; Foundation</span>
            <h2>Intro to Art</h2>
            <p class="identity">The foundation art course. Students learn the elements and principles of art and build core skills in drawing, color, and design by hand.</p>
            <ul class="facts">
              <li><span class="k">A-G credit</span><span class="v">UC / CSU &ldquo;F&rdquo; Visual and Performing Arts</span></li>
              <li><span class="k">Taught by</span><span class="v"><a href="teachers.html#stephanie-fikri">Stephanie Fikri</a></span></li>
              <li><span class="k">Who it is for</span><span class="v">Open to all students, no experience required. A starting point for art.</span></li>
              <li><span class="k">Materials</span><span class="v">Graphite, charcoal, ink, colored pencil, pastel, and paint, plus a personal sketchbook.</span></li>
            </ul>
            <a class="btn signup-btn" href="signup.html?course=intro-to-art&amp;from=fine-art">Sign up for Intro to Art</a>
          </div>
          <div class="course-main">
            <h3>What students will be able to do</h3>
            <ul class="checklist one">
              <li>Use the elements and principles of art on purpose: line, shape, value, color, texture, space, balance, and emphasis.</li>
              <li>Draw from observation using contour, value, proportion, and perspective.</li>
              <li>Mix and apply color using color theory.</li>
              <li>Work in a range of media, including collage, printmaking, and simple sculpture.</li>
              <li>Describe, analyze, and give feedback on artwork using art vocabulary.</li>
              <li>Keep a sketchbook to plan ideas and track growth.</li>
            </ul>

            <h3>Core units</h3>
            <div class="units">
              <div class="unit"><strong>Drawing fundamentals</strong><span>Line, contour, value, shading, and proportion.</span></div>
              <div class="unit"><strong>Color theory</strong><span>The color wheel, mixing, color schemes, and value scales.</span></div>
              <div class="unit"><strong>Perspective &amp; space</strong><span>One and two point perspective, overlapping, and creating depth.</span></div>
              <div class="unit"><strong>Mixed media &amp; design</strong><span>Collage, printmaking, pattern, and an introduction to 3D work.</span></div>
              <div class="unit"><strong>Art history &amp; critique</strong><span>Artists across cultures and eras, and how to talk about art.</span></div>
            </div>

            <h3>Example projects</h3>
            <ul class="tags">
              <li>Contour Line Drawing</li><li>Value Scale and Shaded Sphere</li><li>Color Wheel</li><li>One Point Perspective</li><li>Still Life Drawing</li><li>Self-Portrait Drawing</li><li>Collage</li><li>Printmaking</li>
            </ul>

            <div class="callout">
              <p class="k">How the year builds</p>
              <p>Start with observation and drawing basics, add color, then explore mixed media. The year closes with a finished piece ready to exhibit.</p>
            </div>
          </div>
        </article>

        <article class="course" id="painting">
          <div class="course-side">
            <span class="course-level entry">Level 1 &middot; Studio</span>
            <h2>Painting 1</h2>
            <p class="identity">The studio painting course. Students explore watercolor and acrylic, color mixing, and composition, and develop a personal style.</p>
            <ul class="facts">
              <li><span class="k">A-G credit</span><span class="v">UC / CSU &ldquo;F&rdquo; Visual and Performing Arts</span></li>
              <li><span class="k">Taught by</span><span class="v"><a href="teachers.html#stephanie-fikri">Stephanie Fikri</a></span></li>
              <li><span class="k">Who it is for</span><span class="v">Open to all students, no experience required.</span></li>
              <li><span class="k">Materials</span><span class="v">Watercolor, acrylic, brushes, palette knives, watercolor paper, and canvas.</span></li>
            </ul>
            <a class="btn signup-btn" href="signup.html?course=painting&amp;from=fine-art">Sign up for Painting 1</a>
          </div>
          <div class="course-main">
            <h3>What students will be able to do</h3>
            <ul class="checklist one">
              <li>Mix color with control over value, temperature, and intensity.</li>
              <li>Use painting techniques in watercolor and acrylic: washes, layering, blending, dry brush, and texture.</li>
              <li>Plan compositions with thumbnail sketches and studies.</li>
              <li>Paint from observation and imagination: still life, landscape, portrait, and abstraction.</li>
              <li>Study painters and art movements, and respond to them in their own work.</li>
              <li>Build a series and present finished paintings for exhibit.</li>
            </ul>

            <h3>Core units</h3>
            <div class="units">
              <div class="unit"><strong>Color &amp; mixing</strong><span>Color charts, value, temperature, and limited palettes.</span></div>
              <div class="unit"><strong>Watercolor</strong><span>Washes, wet on wet, layering, and lifting.</span></div>
              <div class="unit"><strong>Acrylic</strong><span>Blending, layering, texture, and painting on canvas.</span></div>
              <div class="unit"><strong>Composition &amp; subject</strong><span>Still life, landscape, portrait, and abstraction.</span></div>
              <div class="unit"><strong>Painters &amp; movements</strong><span>Master studies and art history connections.</span></div>
              <div class="unit"><strong>Series &amp; exhibition</strong><span>A cohesive body of work, artist statements, and display.</span></div>
            </div>

            <h3>Example projects</h3>
            <ul class="tags">
              <li>Color Mixing Chart</li><li>Watercolor Landscape</li><li>Monochromatic Painting</li><li>Still Life in Acrylic</li><li>Master Study</li><li>Self-Portrait Painting</li><li>Abstract Painting</li><li>Series for Exhibit</li>
            </ul>

            <div class="callout">
              <p class="k">Studio rhythm</p>
              <p>Every painting moves through the same steps: thumbnails, a color study, the final painting, and a short critique or reflection.</p>
            </div>
          </div>
        </article>

      </div>
    </section>

    <section class="band gray">
      <div class="wrap">
        <div class="section-head">
          <h2>Student Artwork</h2>
          <span class="sub">Coming soon</span>
        </div>
        <p class="lead" style="max-width:720px">A gallery of student drawings and paintings is on the way.</p>
        <p class="cta-row" style="margin-top:24px"><a class="btn" href="signup.html?course=intro-to-art&amp;from=fine-art">Sign up for Intro to Art</a> <a class="btn" href="signup.html?course=painting&amp;from=fine-art">Sign up for Painting 1</a> <a class="btn dark" href="teachers.html#stephanie-fikri">Meet Stephanie Fikri</a></p>
      </div>
    </section>
"""

# ---------------------------------------------------------------- Teachers
TEACH = """
    <section class="hero page hero-teachers">
      <div class="wrap">
        <p class="eyebrow">PVHS Visual Arts</p>
        <h1>Our<br>Teachers</h1>
        <p>Working photographers, designers, and artists. Our Digital Media teachers are CTE teachers who bring 35 combined years of commercial and fine art industry experience into the classroom.</p>
      </div>
    </section>

    <section class="band">
      <div class="wrap">
        <div class="people">
          <article class="person" id="chris-silva">
            <div class="ph"><img src="images/teachers/chris-silva.jpg" alt="Chris Silva" loading="lazy" width="800" height="1000"></div>
            <div class="body">
              <p class="role">Photography 1 &amp; 2 &middot; Digital Arts 1</p>
              <h3>Chris Silva</h3>
              <p class="exp">14 years industry experience</p>
              <p>Chris Silva is a fine art photographer and visual arts educator based in Santa Maria, California. He teaches Photography and Digital Arts at Pioneer Valley High School. Working mostly in black and white, across film, digital, and hybrid workflows, he makes documentary work, environmental portraits, and experimental images rooted in place and lived experience.</p>
              <p>Capturing light since age 13 on 35mm film, Chris studied Applied Arts and Design at Allan Hancock College and earned a BA in Photography from Southern New Hampshire University. He co-owns Cris &amp; Laura Inspired EYE Images and co-founded Light Writerz, the PVHS photography club.</p>
              <p class="person-link"><a href="https://www.creativesilva.com" target="_blank" rel="noopener">www.creativesilva.com</a></p>
            </div>
          </article>
          <article class="person" id="laura-garcia">
            <div class="ph"><img src="images/teachers/laura-garcia.jpg" alt="Laura Garcia" loading="lazy" width="800" height="1000"></div>
            <div class="body">
              <p class="role">Photography 1</p>
              <h3>Laura Garcia</h3>
              <p class="exp">14 years industry experience</p>
              <p>Laura Garcia is a professional photographer, photography educator, and co-founder of Light Writerz. Laura co-owns Cris &amp; Laura Inspired EYE Images, bringing years of professional industry experience to the next generation of Light Writers.</p>
              <p>Laura earned an Associate of Arts (A.A.) from Santa Barbara City College and a Bachelor of Arts (B.A.) in Photography from Southern New Hampshire University.</p>
              <p>As a Light Writerz advisor, Laura helps students build the discipline, technical skill, and creative confidence it takes to make photographs with intention.</p>
              <p class="person-link"><a href="https://www.chrisandlaura.com" target="_blank" rel="noopener">www.chrisandlaura.com</a></p>
            </div>
          </article>
          <article class="person" id="rileigh-mankin">
            <div class="ph"><img src="images/teachers/rileigh-mankin.jpg" alt="Rileigh Mankin" loading="lazy" width="800" height="1000"></div>
            <div class="body">
              <p class="role">Digital Arts 1 &amp; 2</p>
              <h3>Rileigh Mankin</h3>
              <p class="exp">7 years industry experience</p>
              <p>Hi there, nice to meet you! I&rsquo;m Rileigh. I&rsquo;m a tenacious designer who specializes in brand identity, apparel design, and pattern design. I thrive under pressure and strive to create meaningful designs through authentic storytelling.</p>
              <p>Outside of design, I love exploring and competing. You can find me traveling, camping, hiking, or challenging friends and family to a new board game.</p>
              <p>I studied at Corvin University and Laguna College of Art and Design, where I earned my bachelor&rsquo;s degree, and I now teach Digital Arts at Pioneer Valley High School.</p>
              <p class="person-link"><a href="https://rileighmankin.myportfolio.com/" target="_blank" rel="noopener">See Portfolio</a></p>
            </div>
          </article>
          <article class="person" id="stephanie-fikri">
            <div class="ph ph-logo"><img src="images/pvhs-logo.png" alt="Photo coming soon" loading="lazy" width="222" height="240"></div>
            <div class="body">
              <p class="role">Intro to Art &middot; Painting 1</p>
              <h3>Stephanie Fikri</h3>
              <p>Stephanie Fikri teaches Art at Pioneer Valley High School, including Intro to Art and Painting 1.</p>
              <p class="note">Full bio coming soon.</p>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="band teal tight">
      <div class="wrap stats four">
        <div><div class="n">35</div><div class="l">Digital Media combined years in industry</div></div>
        <div><div class="n">14</div><div class="l">Chris Silva</div></div>
        <div><div class="n">14</div><div class="l">Laura Garcia</div></div>
        <div><div class="n">7</div><div class="l">Rileigh Mankin</div></div>
      </div>
    </section>

    <section class="band">
      <div class="wrap">
        <h2 class="title">Want to join a class?</h2>
        <p class="lead" style="margin-top:12px;max-width:720px">Photography 1, Digital Arts 1, Intro to Art, and Painting 1 are open to every PVHS student, no experience needed. Fill out the sign up form, then ask your counselor to add one to your schedule.</p>
        <p class="cta-row" style="margin-top:24px"><a class="btn" href="signup.html?from=teachers">Sign up</a> <a class="btn dark" href="index.html">Explore the program</a></p>
      </div>
    </section>
"""

ADMIN = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>Staff Admin | PVHS Visual Arts</title>
  <meta name="robots" content="noindex, nofollow">
  <meta name="theme-color" content="#0b0d0d">
  <link rel="icon" type="image/png" sizes="64x64" href="images/favicon-64.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Oswald:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css?v={V}">
</head>
<body class="admin">
  <header class="masthead">
    <div class="wrap">
      <a class="brand" href="index.html" aria-label="PVHS Visual Arts home">
        <img class="mark" src="images/pvhs-logo.png" alt="Pioneer Valley High School Panthers logo" width="74" height="80">
        <div>
          <div class="brand-name">PVHS Visual Arts</div>
          <div class="brand-sub">Staff admin &middot; Interest form sign ups</div>
        </div>
      </a>
      <div class="mast-actions"><button class="btn dark" id="signout" type="button" hidden>Sign out</button></div>
    </div>
  </header>

  <main id="main">
    <section class="band" id="v-login">
      <div class="wrap admin-login">
        <h1 class="title">Staff login</h1>
        <p class="lead" style="margin-top:12px">Sign in with the program Google account to see interest form sign ups.</p>
        <p style="margin-top:24px"><button class="btn" id="signin" type="button">Sign in with Google</button></p>
        <p class="form-msg" id="login-err" role="alert" hidden></p>
      </div>
    </section>

    <section class="band admin-app" id="v-app" hidden>
      <div class="wrap">
        <div class="section-head no-print">
          <h2>Sign ups</h2>
          <span class="sub">Signed in as <b id="who"></b></span>
        </div>
        <div class="print-head print-only">
          <h1>PVHS Visual Arts &middot; Interest form sign ups</h1>
          <p id="print-meta"></p>
        </div>
        <div class="admin-stats" id="stats"></div>
        <div class="admin-tools no-print">
          <label>Course <select id="flt-course"><option value="">All courses</option><option>Photography 1</option><option>Photography 2</option><option>Digital Arts 1</option><option>Digital Arts 2</option><option>Intro to Art</option><option value="Painting">Painting 1</option></select></label>
          <label>Grade <select id="flt-grade"><option value="">All grades</option><option value="9">9th</option><option value="10">10th</option><option value="11">11th</option><option value="12">12th</option></select></label>
          <label>School year <select id="flt-year"><option value="">All years</option></select></label>
          <label class="grow">Search <input id="flt-q" type="search" placeholder="Name or student ID"></label>
          <div class="admin-btns">
            <button class="btn" id="btn-print" type="button">Print</button>
            <button class="btn dark" id="btn-csv" type="button">Download for Google Sheets</button>
            <button class="btn dark" id="btn-refresh" type="button">Refresh</button>
          </div>
        </div>
        <p class="note no-print" id="admin-note"></p>
        <div class="table-wrap">
          <table class="admin-table" id="table">
            <thead><tr><th>Submitted</th><th>Name</th><th>Student ID</th><th>Grade</th><th>School year</th><th>Classes</th><th>Signed up from</th><th>Lang</th><th>Note</th><th class="no-print"></th></tr></thead>
            <tbody id="rows"></tbody>
          </table>
        </div>
        <p class="note" id="empty" hidden>No sign ups match these filters yet.</p>
      </div>
    </section>
  </main>

  <script type="module" src="js/admin.js?v={V}"></script>
</body>
</html>
"""


# ---------------------------------------------------------------- Spanish
ASSET_RE = re.compile(r"^(css|js|images)/")


def es_path(v):
    """Rewrite one relative URL for a page that lives one folder deeper (pvhs/es/)."""
    if not v or v.startswith(("#", "http:", "https:", "mailto:", "sms:", "tel:", "data:", "/")):
        return v
    if ASSET_RE.match(v) or v.startswith("../") or v == "admin.html":
        return "../" + v
    return v  # sibling pages (index.html, signup.html?...) exist in es/ too


class Translator(HTMLParser):
    """Re-emits an English page with every text segment and user-facing attribute in Spanish."""
    TEXT_ATTRS = {"alt", "aria-label", "title", "placeholder"}

    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.out, self.raw, self.missing = path, [], 0, set()

    def tr(self, text):
        key = " ".join(text.split())
        if not key or not re.search(r"[A-Za-z]", key) or key in KEEP:
            return escape(text, quote=False)
        es = ES.get(f"{self.path}::{key}", ES.get(key))  # page-specific wording wins
        if es is None:
            self.missing.add(key)
            return escape(text, quote=False)
        lead = text[: len(text) - len(text.lstrip())]
        trail = text[len(text.rstrip()):]
        return lead + escape(es, quote=False) + trail

    def attrs(self, tag, attrs):
        d = dict(attrs)
        keep_href = "data-keep-href" in d
        parts = []
        for k, v in attrs:
            if v is None:
                parts.append(k)
                continue
            if k in self.TEXT_ATTRS:
                v = self.tr(v)
                v = v.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
            elif k == "content" and (d.get("name") == "description" or d.get("property") in ("og:title", "og:description")):
                v = self.tr(v).replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
            elif k in ("href", "src") and not keep_href:
                v = es_path(v)
            elif k == "style":
                v = re.sub(r"url\('([^']+)'\)", lambda m: "url('" + es_path(m.group(1)) + "')", v)
            parts.append(f'{k}="{escape(v)}"')
        return ("<" + tag + (" " + " ".join(parts) if parts else ""))

    def handle_starttag(self, tag, attrs):
        self.out.append(self.attrs(tag, attrs) + ">")
        if tag in ("script", "style"):
            self.raw += 1

    def handle_startendtag(self, tag, attrs):
        self.out.append(self.attrs(tag, attrs) + ">")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.raw -= 1
        self.out.append(f"</{tag}>")

    def handle_data(self, data):
        self.out.append(data if self.raw else self.tr(data))

    def handle_comment(self, data):
        self.out.append(f"<!--{data}-->")

    def handle_decl(self, decl):
        self.out.append(f"<!{decl}>")


def to_spanish(html, path, missing):
    t = Translator(path)
    t.feed(html)
    t.close()
    missing.update((path, m) for m in t.missing)
    return "".join(t.out)


PAGES = [
    ("index.html", "PVHS Visual Arts | Pioneer Valley High School",
     "Visual Arts at Pioneer Valley High School: Digital Photography, Digital Arts, Intro to Art, and Painting 1.",
     "hero-home", HOME),
    ("digital-media.html", "Digital Media | PVHS Visual Arts",
     "Digital Media at Pioneer Valley High School: a CTE program with two pathways, Digital Photography and Digital Arts.",
     "hero-photo", DM),
    ("digital-photography.html", "Digital Photography | PVHS Visual Arts",
     "Photography 1 and Photography 2 at Pioneer Valley High School: Manual mode, RAW, Lightroom Classic, lighting, and studio work.",
     "hero-photo", PHOTO),
    ("digital-arts.html", "Digital Arts | PVHS Visual Arts",
     "Digital Arts 1 and Digital Arts 2 at Pioneer Valley High School: design foundations, Adobe Illustrator and Photoshop, branding, and portfolio work.",
     "hero-arts", ARTS),
    ("fine-art.html", "Art | PVHS Visual Arts",
     "Intro to Art and Painting 1 at Pioneer Valley High School: drawing, color, watercolor, acrylic, and a portfolio of finished artwork.",
     None, FINE),
    ("teachers.html", "Our Teachers | PVHS Visual Arts",
     "Meet the Visual Arts teachers at Pioneer Valley High School: Chris Silva, Laura Garcia, Rileigh Mankin, and Stephanie Fikri.",
     None, TEACH),
    ("signup.html", "Sign Up | PVHS Visual Arts",
     "Interest form for Digital Photography, Digital Arts, and Art at Pioneer Valley High School.",
     None, SIGNUP),
]


SCRIPTS = {"signup.html": f'  <script type="module" src="js/signup.js?v={V}"></script>\n'}


def render(path, title, desc, pre, body, lang):
    return head(title, desc, path, pre, lang) + body.lstrip("\n") + "\n" + foot(SCRIPTS.get(path, ""))


def check(html, name):
    for bad in ("—", "–"):
        assert bad not in html, (name, "dash")


missing = set()
os.makedirs(os.path.join(OUT, "es"), exist_ok=True)
for path, title, desc, pre, body in PAGES:
    en = render(path, title, desc, pre, body, "en")
    es = to_spanish(render(path, title, desc, pre, body, "es"), path, missing)
    check(en, path)
    check(es, "es/" + path)
    with open(os.path.join(OUT, path), "w") as f:
        f.write(en)
    with open(os.path.join(OUT, "es", path), "w") as f:
        f.write(es)
    print("wrote", path, "and es/" + path)

admin = ADMIN.replace("{V}", V)
check(admin, "admin.html")
with open(os.path.join(OUT, "admin.html"), "w") as f:
    f.write(admin)
print("wrote admin.html")

miss_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "missing.txt")
if os.path.exists(miss_file):
    os.remove(miss_file)
if missing:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "missing.txt"), "w") as f:
        f.write("\n".join(sorted({m for _, m in missing})) + "\n")
    sys.exit(f"{len({m for _, m in missing})} text segments have no Spanish translation (see _src/missing.txt)")
