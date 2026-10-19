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
V = "12"  # cache bust for css/js

NAV = [
    ("index.html", "Digital Media"),
    ("digital-photography.html", "Digital Photography"),
    ("digital-arts.html", "Digital Arts"),
    ("teachers.html", "Our Teachers"),
    ("signup.html", "Sign Up"),
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
  <meta property="og:site_name" content="PVHS Digital Media">
  <meta property="og:image" content="https://www.schoolflo.org/pvhs/images/hero-home.jpg">
  <meta name="theme-color" content="#374545">
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
      <a class="brand" href="index.html" aria-label="PVHS Digital Media home">
        <img class="mark" src="images/pvhs-logo.png" alt="Pioneer Valley High School Panthers logo" width="74" height="80">
        <div>
          <div class="brand-name">PVHS Digital Media</div>
          <div class="brand-sub">Pioneer Valley High School<span class="brand-city"> &middot; Santa Maria, CA</span></div>
        </div>
      </a>
      <div class="mast-actions">
{lang_toggle(path, lang)}
        <a class="btn cta" href="signup.html?from={path.replace(".html", "")}">Sign Up</a>
      </div>
      <button class="navtoggle" aria-expanded="false" aria-controls="navlist" aria-label="Open menu"><span class="bars" aria-hidden="true"></span><span class="navtoggle-label">Menu</span></button>
    </div>
  </header>

  <nav class="mainnav" aria-label="Main">
    <div class="wrap">
      <a class="dock-logo" href="index.html" aria-label="PVHS Digital Media home" tabindex="-1"><img src="images/pvhs-logo.png" alt="" width="40" height="43"></a>
      <ul id="navlist">
{nav_items(path)}
        <li><a href="https://www.lightwriterz.org" target="_blank" rel="noopener">Light Writerz</a></li>
      </ul>
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
    rows = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == path else ""
        rows.append(f'        <li><a href="{href}"{cur}>{label}</a></li>')
    return "\n".join(rows)


def foot(extra_scripts=""):
    return f"""  </main>

  <footer class="site">
    <div class="wrap">
      <div class="cols">
        <div>
          <a href="index.html" aria-label="PVHS Digital Media home"><img class="foot-mark" src="images/pvhs-logo.png" alt="Pioneer Valley High School Panthers logo" width="89" height="96"></a>
          <p class="motto">Learn it. Make it.<br><span>Present it.</span></p>
          <p>Career Technical Education in Arts, Media, and Entertainment at Pioneer Valley High School. Design, Visual, and Media Arts pathway.</p>
        </div>
        <div>
          <h4>Digital Media</h4>
          <ul>
            <li><a href="index.html">Program Overview</a></li>
            <li><a href="digital-photography.html">Digital Photography</a></li>
            <li><a href="digital-arts.html">Digital Arts</a></li>
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
        <span>&copy; <span id="yr">2026</span> PVHS Digital Media &middot; Pioneer Valley High School</span>
        <span>Hosted on <a href="../">SchoolFlo</a> &middot; <a href="admin.html" rel="nofollow">Staff login</a></span>
      </div>
    </div>
  </footer>

  <script src="js/main.js?v={V}" defer></script>
{extra_scripts}</body>
</html>
"""

# ---------------------------------------------------------------- Home
HOME = """
    <section class="hero hero-home">
      <div class="wrap">
        <p class="eyebrow">Pioneer Valley High School &middot; CTE Pathway</p>
        <h1>Digital<br><span class="accent">Media</span></h1>
        <p>Real cameras. Industry software. Professional habits. Taught by CTE teachers with real industry experience, and it counts as your a-g &ldquo;F&rdquo; fine art.</p>
        <div class="actions">
          <a class="btn" href="digital-photography.html">Digital Photography</a>
          <a class="btn ghost" href="digital-arts.html">Digital Arts</a>
        </div>
      </div>
    </section>

    <div class="tiles">
      <div class="wrap">
        <ul>
          <li><a href="digital-photography.html"><span class="num">01</span><h2>Digital Photography</h2><span class="more">Photography 1 &amp; 2</span></a></li>
          <li><a href="digital-arts.html"><span class="num">02</span><h2>Digital Arts</h2><span class="more">Digital Arts 1 &amp; 2</span></a></li>
          <li><a href="teachers.html"><span class="num">03</span><h2>Our Teachers</h2><span class="more">Meet the team</span></a></li>
          <li><a href="https://www.lightwriterz.org" target="_blank" rel="noopener"><span class="num">04</span><h2>Light Writerz</h2><span class="more">The PVHS photo club</span></a></li>
        </ul>
      </div>
    </div>

    <section class="band">
      <div class="wrap split">
        <div>
          <p class="eyebrow">About the program</p>
          <h2 class="title">Hands on, not lectures</h2>
          <p class="lead" style="margin-top:18px">Digital Media at Pioneer Valley is a Career Technical Education program in the Arts, Media, and Entertainment sector, inside the Design, Visual, and Media Arts pathway.</p>
          <p class="muted">Students learn industry standard tools and professional habits through hands on projects. By the end of the pathway, a student can operate real equipment, run a professional edit and deliver workflow, and present finished creative work.</p>
          <ul class="checklist one">
            <li><strong>Bilingual materials.</strong> Project directions and handouts are offered in English and Spanish, and students may submit their work in either language.</li>
            <li><strong>A Mac lab.</strong> Students work on Macs, with a school iPad that doubles as a scanner for sketches and hand done work.</li>
            <li><strong>Fine arts credit.</strong> Courses satisfy the UC and CSU a-g &ldquo;F&rdquo; Visual and Performing Arts requirement.</li>
            <li><strong>Open to everyone.</strong> Photography 1 and Digital Arts 1 need no experience.</li>
          </ul>
        </div>
        <figure class="photo-fig"><img src="images/work/light-02.jpg" alt="Student work: a student in a blue sweater surrounded by loops of light, a light painting photograph" loading="lazy" width="900" height="600"><figcaption>Student work: writing with light, a long exposure project.</figcaption></figure>
      </div>
    </section>

    <section class="band ag" id="a-g">
      <div class="wrap split">
        <div class="ag-badge" aria-hidden="true"><span class="ag-top">UC / CSU a-g</span><span class="ag-letter">F</span><span class="ag-bot">Visual &amp; Performing Arts</span></div>
        <div>
          <p class="eyebrow" style="color:var(--gold)">College ready elective</p>
          <h2 class="title">The &ldquo;F&rdquo; in a-g</h2>
          <p class="lead" style="margin-top:18px">Our Photography and Digital Arts courses satisfy the UC and CSU a-g &ldquo;F&rdquo; Visual and Performing Arts requirement.</p>
          <p class="muted">To be eligible for the University of California and California State University, students need a year of Visual and Performing Arts. Digital Media covers that fine art requirement while building real career skills on industry tools, so one elective works toward college and career at the same time.</p>
          <ul class="checklist one">
            <li><strong>College:</strong> counts as fine art (&ldquo;F&rdquo;) for UC and CSU admission.</li>
            <li><strong>Career:</strong> a CTE pathway in Arts, Media, and Entertainment, with SkillsUSA.</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="band teal tight">
      <div class="wrap stats four">
        <div><div class="n">4</div><div class="l">Courses</div></div>
        <div><div class="n">35</div><div class="l">Years of industry experience</div></div>
        <div><div class="n word">a-g &ldquo;F&rdquo;</div><div class="l">Fine arts credit</div></div>
        <div><div class="n word">SkillsUSA</div><div class="l">Student organization</div></div>
      </div>
    </section>

    <section class="band">
      <div class="wrap">
        <div class="section-head">
          <h2>Two Pathways, Four Courses</h2>
          <span class="sub">Start with level 1, grow into level 2</span>
        </div>
        <div class="cards two">
          <article class="card program">
            <div class="cover" style="background-image:url('images/hero-photo-m.jpg')" role="img" aria-label="Student light painting photograph"></div>
            <div class="body">
              <p class="kicker">Program 01</p>
              <h3>Digital Photography</h3>
              <ul class="courses">
                <li>Photography 1<span>Foundation &middot; no experience needed</span></li>
                <li>Photography 2<span>Advanced &middot; lighting and studio</span></li>
              </ul>
              <p>Operate a real camera on Manual, see like a photographer, shape light on purpose, and finish images in Adobe Lightroom Classic and Photoshop.</p>
              <div class="card-actions"><a class="btn dark" href="digital-photography.html">Explore Photography</a><a class="text-link" href="signup.html?course=photography-1&amp;from=home">Sign up</a></div>
            </div>
          </article>
          <article class="card program gold-top">
            <div class="cover" style="background-image:url('images/hero-arts-m.jpg')" role="img" aria-label="Student magazine cover designs"></div>
            <div class="body">
              <p class="kicker">Program 02</p>
              <h3>Digital Arts</h3>
              <ul class="courses">
                <li>Digital Arts 1<span>Foundation &middot; no experience needed</span></li>
                <li>Digital Arts 2<span>Advanced &middot; brand and portfolio</span></li>
              </ul>
              <p>Learn the elements and principles of design, then use Adobe Illustrator and Photoshop to make clean, intentional graphics, brands, and portfolio work.</p>
              <div class="card-actions"><a class="btn dark" href="digital-arts.html">Explore Digital Arts</a><a class="text-link" href="signup.html?course=digital-arts-1&amp;from=home">Sign up</a></div>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="band skills" id="skillsusa">
      <div class="wrap split">
        <div>
          <p class="eyebrow" style="color:var(--gold)">Career Technical Student Organization</p>
          <h2 class="title">SkillsUSA</h2>
          <p class="lead" style="margin-top:18px">PVHS Digital Media is associated with SkillsUSA for both the Digital Photography and Digital Arts pathways.</p>
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
          <span class="sub">The same five steps in every course</span>
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
          <span class="sub">35 years of combined industry experience &middot; <a href="teachers.html">Meet the team</a></span>
        </div>
        <div class="team-mini">
          <a class="card" href="teachers.html#chris-silva" style="text-decoration:none;color:inherit"><img class="head" src="images/teachers/chris-silva.jpg" alt="Chris Silva" loading="lazy" width="84" height="84"><div><p class="kicker">Photography &amp; Digital Arts</p><h3>Chris Silva</h3><p>Photography 1 &amp; 2 &middot; Digital Arts 1<br><span class="exp-mini">14 years industry experience</span></p></div></a>
          <a class="card" href="teachers.html#laura-garcia" style="text-decoration:none;color:inherit"><img class="head" src="images/teachers/laura-garcia.jpg" alt="Laura Garcia" loading="lazy" width="84" height="84"><div><p class="kicker">Photography</p><h3>Laura Garcia</h3><p>Photography 1<br><span class="exp-mini">14 years industry experience</span></p></div></a>
          <a class="card" href="teachers.html#rileigh-mankin" style="text-decoration:none;color:inherit"><img class="head" src="images/teachers/rileigh-mankin.jpg" alt="Rileigh Mankin" loading="lazy" width="84" height="84"><div><p class="kicker">Digital Arts</p><h3>Rileigh Mankin</h3><p>Digital Arts 1 &amp; 2<br><span class="exp-mini">7 years industry experience</span></p></div></a>
        </div>
      </div>
    </section>

    <section class="band dark">
      <div class="wrap">
        <blockquote class="pull">Learn the concept. Make the work.<br><span class="accent">Present it like a professional.</span><cite>The PVHS Digital Media standard</cite></blockquote>
        <p class="cta-row" style="margin-top:36px"><a class="btn" href="signup.html?course=photography-1&amp;from=home">Sign up for Photography 1</a> <a class="btn dark" href="signup.html?course=digital-arts-1&amp;from=home">Sign up for Digital Arts 1</a></p>
        <p class="note" style="margin-top:18px">Interested? Fill out the sign up form so our teachers can follow up, and ask your counselor about adding the class to your schedule.</p>
      </div>
    </section>
"""

# ---------------------------------------------------------------- Photography
PHOTO = """
    <section class="hero page hero-photo">
      <div class="wrap">
        <p class="eyebrow">Digital Media &middot; Program 01</p>
        <h1>Digital<br>Photography</h1>
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
              <li><span class="k">a-g credit</span><span class="v">UC / CSU &ldquo;F&rdquo; Visual and Performing Arts</span></li>
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
              <li><span class="k">a-g credit</span><span class="v">UC / CSU &ldquo;F&rdquo; Visual and Performing Arts</span></li>
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
              <p class="k">SkillsUSA &middot; Concentrators &amp; Completers</p>
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
        <p class="eyebrow">Digital Media &middot; Program 02</p>
        <h1>Digital<br>Arts</h1>
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
              <li><span class="k">a-g credit</span><span class="v">UC / CSU &ldquo;F&rdquo; Visual and Performing Arts</span></li>
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
              <li><span class="k">a-g credit</span><span class="v">UC / CSU &ldquo;F&rdquo; Visual and Performing Arts</span></li>
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
              <p class="k">SkillsUSA &middot; Concentrators &amp; Completers</p>
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
        <p>Want to take Digital Photography or Digital Arts next school year? Fill out this short form and our teachers will follow up with you.</p>
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
          <p class="cta-row" style="margin-top:24px"><a class="btn" href="index.html">Back to Digital Media</a> <a class="btn dark" href="signup.html" id="againLink">Sign up another student</a></p>
        </div>

        <aside class="signup-side">
          <div class="card">
            <p class="kicker">Good to know</p>
            <ul class="checklist one">
              <li>Photography 1 and Digital Arts 1 are open to everyone. No experience needed.</li>
              <li>Every class counts toward the UC and CSU a-g &ldquo;F&rdquo; fine art requirement.</li>
            </ul>
          </div>
        </aside>
      </div>
    </section>
"""

# ---------------------------------------------------------------- Teachers
TEACH = """
    <section class="hero page hero-teachers">
      <div class="wrap">
        <p class="eyebrow">PVHS Digital Media</p>
        <h1>Our<br>Teachers</h1>
        <p>Every Digital Media teacher is a CTE teacher with real industry experience: 35 combined years of commercial and fine art work, brought into the classroom.</p>
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
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="band teal tight">
      <div class="wrap stats four">
        <div><div class="n">35</div><div class="l">Combined years in industry</div></div>
        <div><div class="n">14</div><div class="l">Chris Silva</div></div>
        <div><div class="n">14</div><div class="l">Laura Garcia</div></div>
        <div><div class="n">7</div><div class="l">Rileigh Mankin</div></div>
      </div>
    </section>

    <section class="band">
      <div class="wrap">
        <h2 class="title">Want to join a class?</h2>
        <p class="lead" style="margin-top:12px;max-width:720px">Photography 1 and Digital Arts 1 are open to every PVHS student, no experience needed, and they count toward the a-g &ldquo;F&rdquo; fine art requirement. Fill out the sign up form, then ask your counselor to add one to your schedule.</p>
        <p class="cta-row" style="margin-top:24px"><a class="btn" href="signup.html?from=teachers">Sign up</a> <a class="btn dark" href="index.html">Explore the program</a></p>
      </div>
    </section>
"""

ADMIN = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>Staff Admin | PVHS Digital Media</title>
  <meta name="robots" content="noindex, nofollow">
  <meta name="theme-color" content="#374545">
  <link rel="icon" type="image/png" sizes="64x64" href="images/favicon-64.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Oswald:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css?v={V}">
</head>
<body class="admin">
  <header class="masthead">
    <div class="wrap">
      <a class="brand" href="index.html" aria-label="PVHS Digital Media home">
        <img class="mark" src="images/pvhs-logo.png" alt="Pioneer Valley High School Panthers logo" width="74" height="80">
        <div>
          <div class="brand-name">PVHS Digital Media</div>
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
          <h1>PVHS Digital Media &middot; Interest form sign ups</h1>
          <p id="print-meta"></p>
        </div>
        <div class="admin-stats" id="stats"></div>
        <div class="admin-tools no-print">
          <label>Course <select id="flt-course"><option value="">All courses</option><option>Photography 1</option><option>Photography 2</option><option>Digital Arts 1</option><option>Digital Arts 2</option></select></label>
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
    ("index.html", "PVHS Digital Media | Pioneer Valley High School",
     "Digital Media at Pioneer Valley High School: Digital Photography and Digital Arts. Career Technical Education in Arts, Media, and Entertainment.",
     "hero-home", HOME),
    ("digital-photography.html", "Digital Photography | PVHS Digital Media",
     "Photography 1 and Photography 2 at Pioneer Valley High School: Manual mode, RAW, Lightroom Classic, lighting, and studio work.",
     "hero-photo", PHOTO),
    ("digital-arts.html", "Digital Arts | PVHS Digital Media",
     "Digital Arts 1 and Digital Arts 2 at Pioneer Valley High School: design foundations, Adobe Illustrator and Photoshop, branding, and portfolio work.",
     "hero-arts", ARTS),
    ("teachers.html", "Our Teachers | PVHS Digital Media",
     "Meet the Digital Media teachers at Pioneer Valley High School: Chris Silva, Laura Garcia, and Rileigh Mankin.",
     None, TEACH),
    ("signup.html", "Sign Up | PVHS Digital Media",
     "Interest form for Digital Photography and Digital Arts at Pioneer Valley High School.",
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
