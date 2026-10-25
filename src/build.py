"""Static site generator for W Divers Coron.

Usage:  python src/build.py
Output: dist/  (deploy this folder as the web root)
"""
import datetime
import html
import importlib
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config  # noqa: E402
import data  # noqa: E402
import media  # noqa: E402

SRC = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SRC)
DIST = os.path.join(ROOT, "dist")
YEAR = datetime.date.today().year
ASSET_V = datetime.datetime.now().strftime("%Y%m%d%H%M")

ROUTES = {
    "home": "", "diving": "diving/", "wreck": "diving/wreck-diving/", "reef": "diving/reef-diving/",
    "first": "first-time-divers/", "courses": "courses/", "sites": "dive-sites/",
    "island": "island-hopping/", "plan": "plan-your-trip/", "about": "about/", "gallery": "gallery/",
    "faq": "faq/", "journal": "journal/", "contact": "contact/", "privacy": "privacy/",
    "booking": "booking-information/", "sitemap": "sitemap/",
}
# Which top-level section each route belongs to, for aria-current in the header.
SECTION = {
    "diving": "diving", "wreck": "diving", "reef": "diving", "first": "diving", "courses": "diving",
    "island": "diving", "sites": "sites", "site": "sites", "plan": "plan", "faq": "plan",
    "gallery": "plan", "journal": "plan", "article": "plan", "about": "about", "contact": "contact",
}

SIZES = {}
e = html.escape


# ----------------------------------------------------------------- helpers

class Locale:
    def __init__(self, code):
        mod = importlib.import_module(f"content.{code}")
        self.code = code
        self.ui = mod.UI
        self.p = mod.PAGES
        self.names = mod.ROUTE_NAMES
        self.sites = mod.SITES
        self.articles = mod.ARTICLES
        self.lang_name = mod.LANG_NAME
        self.og_locale = mod.OG_LOCALE

    def site(self, slug):
        return next(s for s in self.sites if s["slug"] == slug)

    def article(self, slug):
        return next(a for a in self.articles if a["slug"] == slug)


def url(loc, key, slug=None):
    if key == "site":
        return f"/{loc}/dive-sites/{slug}/"
    if key == "article":
        return f"/{loc}/journal/{slug}/"
    return f"/{loc}/{ROUTES[key]}"


def contact_url(loc, interest=None, topic=None):
    q = []
    if interest:
        q.append(f"interest={interest}")
    if topic:
        q.append(f"topic={topic}")
    return url(loc, "contact") + ("?" + "&".join(q) if q else "") + "#inquiry"


def wa_url():
    return f"https://wa.me/{config.CONTACT['whatsapp_number']}"


def ext(href, label, cls="", L=None, extra=""):
    """External link that opens in a new tab with an accessible hint."""
    hint = f'<span class="vh"> {e(L.ui["new_tab"])}</span>' if L else ""
    c = f' class="{cls}"' if cls else ""
    return f'<a{c} href="{e(href)}" target="_blank" rel="noopener"{extra}>{label}{hint}</a>'


def picture(key, L, sizes="100vw", cls="", loading="lazy", fetchpriority=None, alt=None):
    m = media.MEDIA[key]
    w0, h0 = SIZES[key]
    widths = [w for w in media.WIDTHS if w <= w0] or [media.WIDTHS[0]]
    fb = 1280 if w0 >= 1280 else 640
    fw, fh = (fb, round(h0 * fb / w0)) if w0 >= fb else (w0, h0)
    srcset = ", ".join(f"/assets/img/{key}-{w}.webp {min(w, w0)}w" for w in widths)
    a = m["alt"][L.code] if alt is None else alt
    fp = f' fetchpriority="{fetchpriority}"' if fetchpriority else ""
    c = f' class="{cls}"' if cls else ""
    return (f'<picture{c}><source type="image/webp" srcset="{srcset}" sizes="{sizes}">'
            f'<img src="/assets/img/{key}-{fb}.jpg" alt="{e(a)}" width="{fw}" height="{fh}" '
            f'loading="{loading}" decoding="async"{fp} style="object-position:{m["focus"]}"></picture>')


ICONS = {
    "arrow": '<path d="M4 12h15M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>',
    "chev": '<path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>',
    "menu": '<path d="M4 8h16M4 16h16" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>',
    "close": '<path d="M6 6l12 12M18 6L6 18" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>',
    "facebook": '<path d="M14.5 3H12.8A3.8 3.8 0 0 0 9 6.8V9.5H7v3.3h2V21h3.4v-8.2h2.4l.5-3.3h-2.9V7.2c0-.6.4-1 1-1h1.1z" fill="currentColor"/>',
    "instagram": '<rect x="3.5" y="3.5" width="17" height="17" rx="5" fill="none" stroke="currentColor" stroke-width="1.6"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="1.6"/><circle cx="17.2" cy="6.8" r="1.1" fill="currentColor"/>',
    "whatsapp": '<path d="M4.5 19.5l1.2-3.6A8 8 0 1 1 8.4 18.5z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M9.2 8.3c.3-.4.7-.4 1-.1l.8 1.4c.2.3.1.6-.1.9l-.4.5c.5 1.1 1.4 2 2.5 2.5l.5-.4c.3-.2.6-.3.9-.1l1.4.8c.3.3.3.7-.1 1-.6.6-1.4.9-2.2.6a7.7 7.7 0 0 1-4.8-4.8c-.3-.8 0-1.6.5-2.3z" fill="currentColor"/>',
    "mail": '<rect x="3.5" y="5.5" width="17" height="13" rx="2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M4 7l8 6 8-6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>',
    "pin": '<path d="M12 21s-6.5-6.1-6.5-11A6.5 6.5 0 0 1 18.5 10c0 4.9-6.5 11-6.5 11z" fill="none" stroke="currentColor" stroke-width="1.6"/><circle cx="12" cy="10" r="2.3" fill="none" stroke="currentColor" stroke-width="1.6"/>',
    "naver": '<rect x="3.5" y="3.5" width="17" height="17" rx="3" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M8.5 8h2.3l2.9 4.3V8h2.3v8h-2.3l-2.9-4.3V16H8.5z" fill="currentColor"/>',
    "kakao": '<path d="M12 4.5c-4.7 0-8.5 3-8.5 6.6 0 2.3 1.5 4.3 3.8 5.5l-.9 3.3 3.8-2.5c.6.1 1.2.2 1.8.2 4.7 0 8.5-3 8.5-6.5S16.7 4.5 12 4.5z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>',
    "copy": '<rect x="8.5" y="8.5" width="11" height="11" rx="2" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M15.5 8.5V6a1.5 1.5 0 0 0-1.5-1.5H6A1.5 1.5 0 0 0 4.5 6v8A1.5 1.5 0 0 0 6 15.5h2.5" fill="none" stroke="currentColor" stroke-width="1.5"/>',
    "play": '<path d="M8 5.5v13l10.5-6.5z" fill="currentColor"/>',
    "globe": '<circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M3.5 12h17M12 3.5c2.4 2.3 3.6 5.1 3.6 8.5s-1.2 6.2-3.6 8.5c-2.4-2.3-3.6-5.1-3.6-8.5s1.2-6.2 3.6-8.5z" fill="none" stroke="currentColor" stroke-width="1.5"/>',
}


def icon(name, cls="ico"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{ICONS[name]}</svg>'


def arrow_link(href, label, cls="arrow-link"):
    return f'<a class="{cls}" href="{e(href)}"><span>{e(label)}</span>{icon("arrow")}</a>'


def btn(href, label, cls="btn"):
    return f'<a class="{cls}" href="{e(href)}">{e(label)}</a>'


def logo(L, cls="brand"):
    return (f'<a class="{cls}" href="{url(L.code, "home")}">'
            f'<img src="/assets/brand/logo-white.png" alt="W Divers Coron" width="150" height="150">'
            f'<span class="vh">{e(L.ui["home"])}</span></a>')


def other_locales(L):
    return [c for c in config.LOCALES if c != L.code]


def lang_links(L, route, cls="lang"):
    """Every language as a plain link; the current one is marked. Used in the menu panel and footer."""
    out = []
    for c in config.LOCALES:
        name = Locale.cache[c].lang_name
        cur = ' aria-current="true"' if c == L.code else ""
        out.append(f'<a class="{cls}" href="{url(c, *route)}" hreflang="{c}" lang="{c}" data-set-lang="{c}"{cur}>'
                   f'<span class="vh">{e(L.ui["lang_label"])}: </span>{e(name)}</a>')
    return "".join(out)


def lang_menu(L, route):
    """Compact language picker for the header: globe + current code, opening a list of all languages."""
    items = ""
    for c in config.LOCALES:
        name = Locale.cache[c].lang_name
        cur = ' aria-current="true"' if c == L.code else ""
        items += (f'<li><a href="{url(c, *route)}" hreflang="{c}" lang="{c}" data-set-lang="{c}"{cur}>'
                  f'<span class="lm-code">{c.upper()}</span>{e(name)}</a></li>')
    return (f'<details class="lang-menu" data-lang-menu><summary aria-label="{e(L.ui["lang_label"])}: {e(L.lang_name)}">'
            f'{icon("globe")}<span>{L.code.upper()}</span>{icon("chev", "ico chev")}</summary><ul>{items}</ul></details>')


def social_list(L, which=("facebook", "instagram", "whatsapp"), cls="social"):
    c = config.CONTACT
    hrefs = {"facebook": c["facebook"], "instagram": c["instagram"], "whatsapp": wa_url(),
             "mail": f"mailto:{c['email']}", "naver": c["naver"], "pin": c["maps"],
             "kakao": url(L.code, "contact") + "#kakao"}
    labels = {"facebook": L.ui["facebook"], "instagram": L.ui["instagram"], "whatsapp": L.ui["whatsapp"],
              "mail": L.ui["email"], "naver": L.ui["naver"], "pin": L.ui["maps"], "kakao": L.ui["kakao"]}
    items = []
    for w in which:
        if w in ("mail", "kakao"):
            items.append(f'<li><a href="{e(hrefs[w])}" aria-label="{e(labels[w])}">{icon(w)}</a></li>')
        else:
            items.append(f'<li><a href="{e(hrefs[w])}" target="_blank" rel="noopener" '
                         f'aria-label="{e(labels[w])} {e(L.ui["new_tab"])}">{icon(w)}</a></li>')
    return f'<ul class="{cls}" aria-label="{e(L.ui["social_label"])}">{"".join(items)}</ul>'


# ----------------------------------------------------------------- navigation

def nav_model(L):
    u = L.ui
    c = L.code
    return [
        ("diving", u["nav_diving"], url(c, "diving"), [
            (u["sub_trips"], url(c, "diving")), (u["sub_wreck"], url(c, "wreck")),
            (u["sub_reef"], url(c, "reef")), (u["sub_first"], url(c, "first")),
            (u["sub_courses"], url(c, "courses")), (u["sub_island"], url(c, "island"))]),
        ("sites", u["nav_sites"], url(c, "sites"), None),
        ("plan", u["nav_plan"], url(c, "plan"), [
            (u["sub_guide"], url(c, "plan")), (u["sub_faq"], url(c, "faq")),
            (u["sub_gallery"], url(c, "gallery")), (u["sub_journal"], url(c, "journal"))]),
        ("about", u["nav_about"], url(c, "about"), None),
        ("contact", u["nav_contact"], url(c, "contact"), None),
    ]


def header(L, route, current_path):
    key = route[0]
    sec = SECTION.get(key)
    items = []
    for k, label, href, sub in nav_model(L):
        cur = ' aria-current="true"' if k == sec else ""
        if sub:
            subs = "".join(
                f'<li><a href="{h}"{" aria-current=\"page\"" if h == current_path else ""}>{e(t)}</a></li>'
                for t, h in sub)
            items.append(f'<li class="has-sub"><a class="top" href="{href}"{cur}>{e(label)}{icon("chev", "ico chev")}</a>'
                         f'<ul class="sub">{subs}</ul></li>')
        else:
            items.append(f'<li><a class="top" href="{href}"{cur}>{e(label)}</a></li>')
    return f'''<header class="site-header" data-header>
  {logo(L)}
  <nav class="main-nav" aria-label="{e(L.ui["primary_nav"])}"><ul>{"".join(items)}</ul></nav>
  <div class="header-tools">
    {lang_menu(L, route)}
    {btn(url(L.code, "contact"), L.ui["plan_cta"], "btn btn-outline btn-sm header-cta")}
    <a class="menu-btn" href="#footer-nav" data-menu-open aria-controls="nav-panel">{icon("menu")}<span>{e(L.ui["menu"])}</span></a>
  </div>
</header>'''


def sticky_bar(L, route):
    return f'''<div class="sticky-bar" data-sticky aria-hidden="true">
  {logo(L, "brand brand-sm")}
  <div class="header-tools">
    {lang_menu(L, route)}
    {btn(url(L.code, "contact"), L.ui["plan_cta"], "btn btn-outline btn-sm")}
    <a class="menu-btn" href="#footer-nav" data-menu-open aria-controls="nav-panel" tabindex="-1">{icon("menu")}<span>{e(L.ui["menu"])}</span></a>
  </div>
</div>'''


def nav_panel(L, route, current_path):
    groups = []
    for k, label, href, sub in nav_model(L):
        if sub:
            links = "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h == current_path else ""}>{e(t)}</a></li>' for t, h in sub)
            groups.append(f'<li><details{" open" if SECTION.get(route[0]) == k else ""}><summary>{e(label)}{icon("chev", "ico chev")}</summary><ul>{links}</ul></details></li>')
        else:
            groups.append(f'<li><a class="panel-top" href="{href}"{" aria-current=\"page\"" if href == current_path else ""}>{e(label)}</a></li>')
    return f'''<div class="nav-panel" id="nav-panel" role="dialog" aria-modal="true" aria-label="{e(L.ui["menu"])}" hidden>
  <div class="nav-panel-inner">
    <div class="nav-panel-top">
      {logo(L, "brand brand-sm")}
      <button class="menu-btn" type="button" data-menu-close>{icon("close")}<span>{e(L.ui["close_menu"])}</span></button>
    </div>
    <nav aria-label="{e(L.ui["primary_nav"])}"><ul class="panel-list">{"".join(groups)}</ul></nav>
    <div class="nav-panel-foot">
      {btn(url(L.code, "contact"), L.ui["plan_cta"], "btn btn-solid")}
      {ext(wa_url(), e(L.ui["whatsapp_cta"]), "text-link", L)}
      <div class="panel-lang">{lang_links(L, route)}</div>
      {social_list(L, ("facebook", "instagram", "whatsapp", "kakao", "naver", "mail"))}
    </div>
  </div>
</div>'''


def footer(L, route):
    u = L.ui
    c = L.code
    C = config.CONTACT
    explore = [(u["nav_diving"], url(c, "diving")), (u["nav_sites"], url(c, "sites")),
               (u["nav_plan"], url(c, "plan")), (u["nav_about"], url(c, "about")),
               (u["nav_contact"], url(c, "contact")), (u["nav_faq"], url(c, "faq")),
               (u["sub_gallery"], url(c, "gallery")), (u["sub_journal"], url(c, "journal"))]
    legal = [(u["privacy"], url(c, "privacy")), (u["booking_info"], url(c, "booking")), (u["sitemap"], url(c, "sitemap"))]
    lis = lambda xs: "".join(f'<li><a href="{h}">{e(t)}</a></li>' for t, h in xs)  # noqa: E731
    return f'''<footer class="site-footer">
  <div class="wrap footer-grid">
    <div class="footer-brand">
      <img src="/assets/brand/logo-white.png" alt="" width="96" height="96" loading="lazy">
      <p class="footer-name">W Divers Coron</p>
      <p class="muted">{e(u["footer_desc"])}</p>
      <p class="muted small">{e(config.ADDRESS["street"])}, {e(config.ADDRESS["locality"])}, {e(config.ADDRESS["region"])} {e(config.ADDRESS["postal"])}</p>
    </div>
    <nav class="footer-col" id="footer-nav" aria-label="{e(u["footer_explore"])}">
      <h2 class="footer-h">{e(u["footer_explore"])}</h2><ul>{lis(explore)}</ul>
    </nav>
    <div class="footer-col">
      <h2 class="footer-h">{e(u["footer_contact"])}</h2>
      <ul class="footer-contacts">
        <li>{icon("whatsapp")}{ext(wa_url(), e(C["whatsapp_display"]), "", L)}</li>
        <li>{icon("mail")}<a href="mailto:{C["email"]}">{C["email"]}</a></li>
        <li>{icon("kakao")}<a href="{url(c, "contact")}#kakao">{e(u["kakao"])}</a></li>
        <li>{icon("facebook")}{ext(C["facebook"], e(u["facebook"]), "", L)}</li>
        <li>{icon("instagram")}{ext(C["instagram"], e(L.ui["instagram"]), "", L)}</li>
        <li>{icon("naver")}{ext(C["naver"], e(u["naver"]), "", L)}</li>
        <li>{icon("pin")}{ext(C["maps"], e(u["maps"]), "", L)}</li>
      </ul>
    </div>
    <div class="footer-col">
      <h2 class="footer-h">{e(u["footer_legal"])}</h2><ul>{lis(legal)}</ul>
      <div class="footer-lang">{lang_links(L, route)}</div>
    </div>
  </div>
  <div class="wrap footer-base">
    <p>&copy; <span data-year>{YEAR}</span> W Divers Coron. {e(u["rights"])}</p>
    <p class="credit">Designed by <a href="{config.STUDIO_URL}" target="_blank" rel="noopener">Lendez Studio</a></p>
  </div>
</footer>'''


# ----------------------------------------------------------------- layout

def head(L, route, title, meta, extra_head="", jsonld=None, og_image=None):
    path = url(L.code, *route)
    alt = ""
    if config.SITE_URL:
        alt = f'<link rel="canonical" href="{config.SITE_URL}{path}">\n'
        for c in config.LOCALES:
            alt += f'<link rel="alternate" hreflang="{c}" href="{config.SITE_URL}{url(c, *route)}">\n'
        alt += f'<link rel="alternate" hreflang="x-default" href="{config.SITE_URL}{url(config.DEFAULT_LOCALE, *route)}">\n'
        alt += f'<meta property="og:url" content="{config.SITE_URL}{path}">\n'
    og = og_image or "/assets/img/og-default.jpg"
    if config.SITE_URL:
        og = config.SITE_URL + og
    ld = ""
    for block in (jsonld or []):
        ld += f'<script type="application/ld+json">{json.dumps(block, ensure_ascii=False)}</script>\n'
    return f'''<!doctype html>
<html lang="{L.code}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(meta)}">
{alt}<meta property="og:type" content="website">
<meta property="og:site_name" content="W Divers Coron">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(meta)}">
<meta property="og:image" content="{og}">
<meta property="og:locale" content="{L.og_locale}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#04171E">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/brand/favicon-32.png">
<link rel="apple-touch-icon" href="/assets/brand/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/outfit-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css?v={ASSET_V}">
<script>document.documentElement.classList.add('js')</script>
{extra_head}{ld}</head>'''


def layout(L, route, title, meta, opening, body, extra_head="", jsonld=None, body_cls="", og_image=None):
    current = url(L.code, *route)
    return f'''{head(L, route, title, meta, extra_head, jsonld, og_image)}
<body class="{body_cls}">
<a class="skip" href="#main">{e(L.ui["skip"])}</a>
{sticky_bar(L, route)}
{nav_panel(L, route, current)}
{header(L, route, current)}
<main id="main" tabindex="-1">
{opening}
{body}
</main>
{footer(L, route)}
<script src="/assets/js/site.js?v={ASSET_V}" defer></script>
</body>
</html>
'''


def crumbs(L, trail):
    items = [f'<li><a href="{url(L.code, "home")}">{e(L.ui["home"])}</a></li>']
    for label, href in trail[:-1]:
        items.append(f'<li><a href="{href}">{e(label)}</a></li>')
    items.append(f'<li aria-current="page">{e(trail[-1][0])}</li>')
    return f'<nav class="crumbs" aria-label="{e(L.ui["breadcrumb"])}"><ol>{"".join(items)}</ol></nav>'


def opening(L, eyebrow, h1, intro, img=None, trail=None, extra="", note=None):
    """Framed opening for inner pages. With an image it is photographic; without, a plain dark panel."""
    media_html = ""
    cls = "page-open"
    if img:
        media_html = f'<div class="po-media">{picture(img, L, "(min-width: 900px) 88vw, 100vw", loading="eager", fetchpriority="high")}</div>'
        cls += " has-media"
    else:
        cls += " no-media"
    cr = crumbs(L, trail) if trail else ""
    nt = f'<p class="po-note">{e(note)}</p>' if note else ""
    return f'''<section class="{cls}">
  <div class="frame">
    {media_html}
    <div class="po-copy">
      {cr}
      <p class="eyebrow">{e(eyebrow)}</p>
      <h1 class="po-title">{e(h1)}</h1>
      <span class="rule" aria-hidden="true"></span>
      <p class="lead">{e(intro)}</p>
      {extra}
      {nt}
    </div>
  </div>
</section>'''


def cta_band(L, heading, text, label, interest=None, topic=None, note=None):
    t = f'<p class="cta-text">{e(text)}</p>' if text else ""
    n = f'<p class="cta-note muted small">{e(note)}</p>' if note else ""
    return f'''<section class="cta-band" id="contact-strip">
  <div class="wrap cta-inner reveal">
    <h2 class="cta-h">{e(heading)}</h2>
    {t}
    <div class="cta-actions">
      {btn(contact_url(L.code, interest, topic), label, "btn btn-solid")}
      {ext(wa_url(), icon("whatsapp") + "<span>" + e(L.ui["whatsapp_cta"]) + "</span>", "text-link with-ico", L)}
    </div>
    {n}
  </div>
</section>'''


def related(L, items):
    out = []
    for kind, slug in items:
        if kind == "article":
            a = L.article(slug)
            out.append((a["title"], url(L.code, "article", slug), L.names["journal"]))
        else:
            out.append((L.names[kind], url(L.code, kind), ""))
    lis = "".join(
        f'<li><a href="{h}">{f"<span class=\"rel-kind\">{e(k)}</span>" if k else ""}<span class="rel-t">{e(t)}</span>{icon("arrow")}</a></li>'
        for t, h, k in out)
    return f'<aside class="related wrap reveal" aria-labelledby="rel-h"><h2 class="related-h" id="rel-h">{e(L.ui["related"])}</h2><ul>{lis}</ul></aside>'


def paras(ps):
    return "".join(f"<p>{e(p)}</p>" for p in ps)


def business_ld(L):
    C = config.CONTACT
    A = config.ADDRESS
    ld = {
        "@context": "https://schema.org", "@type": "LocalBusiness", "name": "W Divers Coron",
        "description": L.p["home"]["meta"], "email": C["email"],
        "address": {"@type": "PostalAddress", "streetAddress": A["street"], "addressLocality": "Coron",
                    "addressRegion": A["region"], "postalCode": A["postal"], "addressCountry": A["country"]},
        "hasMap": C["maps"], "sameAs": [C["facebook"], C["instagram"], C["naver"]],
        "image": (config.SITE_URL or "") + "/assets/img/og-default.jpg",
    }
    if config.SITE_URL:
        ld["url"] = config.SITE_URL + url(L.code, "home")
    return ld


# ----------------------------------------------------------------- pages

def render_home(L):
    P = L.p["home"]
    c = L.code
    rail_ids = ["top", "routes", "feature", "sites", "planning", "contact-strip"]
    rail = "".join(f'<li><a href="#{i}" aria-label="{e(lbl)}"><span></span></a></li>' for i, lbl in zip(rail_ids, P["rail"]))
    hero = f'''<section class="hero" id="top">
  <div class="hero-backdrop" aria-hidden="true"></div>
  <div class="frame hero-frame">
    <div class="hero-media">{picture("hero-fish", L, "(min-width: 900px) 88vw, 100vw", loading="eager", fetchpriority="high")}</div>
    <div class="hero-soft" aria-hidden="true"></div>
    <span class="hero-divider" aria-hidden="true"></span>
    <div class="hero-copy">
      <p class="eyebrow">{e(P["eyebrow"])}</p>
      <h1 class="hero-title">{e(P["h1"])}</h1>
      <p class="hero-support">{e(P["support"])}</p>
      <span class="rule" aria-hidden="true"></span>
      <p class="hero-body">{e(P["body"])}</p>
      <div class="hero-actions">
        {btn(url(c, "contact"), L.ui["plan_cta"], "btn btn-outline")}
        {arrow_link(url(c, "sites"), P["secondary"], "arrow-link light")}
      </div>
    </div>
    <nav class="hero-rail" aria-label="{e(L.ui["section_nav"])}"><ul>{rail}</ul></nav>
    <a class="scroll-cue" href="#routes"><span>{e(L.ui["scroll"])}</span></a>
    {social_list(L, ("facebook", "instagram", "whatsapp", "kakao", "naver"), "social hero-social")}
  </div>
</section>'''

    routes = "".join(f'''<li class="route reveal">
      <a href="{url(c, r["to"])}">
        <span class="route-img frame">{picture(ROUTE_IMG[r["to"]], L, "(min-width: 640px) 200px, 92vw", alt="")}</span>
        <span class="route-n" aria-hidden="true">0{i + 1}</span>
        <span class="route-k">{e(r["k"])}</span>
        <span class="route-t">{e(r["t"])}</span>
        <span class="route-link">{e(r["link"])}{icon("arrow")}</span>
      </a></li>''' for i, r in enumerate(P["routes"]))

    sites = "".join(f'''<li class="reveal"><a href="{url(c, "site", s["slug"])}">
      <span class="site-img">{picture(s["img"], L, "(min-width: 900px) 40vw, 92vw", alt="")}</span>
      <span class="site-type">{e(L.ui["type_" + s["type"]])}</span>
      <span class="site-name">{e(s["name"])}</span>
      <span class="site-card">{e(s["card"])}</span>
      {icon("arrow")}</a></li>''' for s in L.sites)

    plan_items = "".join(
        f'<li><a href="{url(c, it["to"])}{"#" + it["hash"] if it.get("hash") else ""}">{e(it["t"])}{icon("arrow")}</a></li>'
        for it in P["plan_items"])

    body = f'''
<section class="home-routes wrap" id="routes" aria-labelledby="routes-h">
  <h2 class="section-h reveal" id="routes-h">{e(P["choose_h"])}</h2>
  <ol class="route-list">{routes}</ol>
</section>

<section class="feature" id="feature" aria-labelledby="feature-h">
  <div class="wrap feature-grid">
    <figure class="frame feature-media reveal">{picture("stock-descent", L, "(min-width: 900px) 40vw, 100vw")}</figure>
    <div class="feature-copy reveal">
      <h2 class="section-h" id="feature-h">{e(P["feature_h"])}</h2>
      <span class="rule" aria-hidden="true"></span>
      <p>{e(P["feature_t"])}</p>
      <div class="feature-links">
        {btn(url(c, "sites"), P["feature_link"], "btn btn-outline")}
        {arrow_link(url(c, "wreck"), P["feature_wreck"], "arrow-link light")}
        {arrow_link(url(c, "reef"), P["feature_reef"], "arrow-link light")}
      </div>
    </div>
  </div>
</section>

<section class="home-sites wrap" id="sites" aria-labelledby="sites-h">
  <div class="split-head reveal">
    <h2 class="section-h" id="sites-h">{e(P["sites_h"])}</h2>
    <p class="muted">{e(P["sites_t"])}</p>
  </div>
  <ul class="site-grid">{sites}</ul>
  <p class="img-note">{e(L.p["sites"]["img_note"])}</p>
  <p class="reveal">{arrow_link(url(c, "sites"), P["sites_all"], "arrow-link light")}</p>
</section>

<section class="paper planning" id="planning" aria-labelledby="planning-h">
  <div class="wrap planning-grid">
    <div class="reveal">
      <h2 class="section-h" id="planning-h">{e(P["plan_h"])}</h2>
      <p>{e(P["plan_t"])}</p>
      {btn(url(c, "plan"), P["plan_link"], "btn btn-dark")}
    </div>
    <ul class="plan-links reveal">{plan_items}</ul>
  </div>
</section>

<section class="moment" aria-label="{e(P["moment_caption"])}">
  <figure class="frame moment-frame reveal">
    {picture("boat-group", L, "(min-width: 900px) 88vw, 100vw")}
    <figcaption>{e(P["moment_caption"])}</figcaption>
  </figure>
</section>

{cta_band(L, P["contact_h"], P["contact_t"], P["contact_btn"])}
'''
    return layout(L, ("home",), P["title"], P["meta"], hero, body, jsonld=[business_ld(L)], body_cls="is-home")


def render_diving(L):
    P = L.p["diving"]
    c = L.code
    chooser = "".join(
        f'<li><a href="{contact_url(c, ch["interest"]) if ch["to"] == "contact" else url(c, ch["to"])}">{e(ch["t"])}{icon("arrow")}</a></li>'
        for ch in P["chooser"])
    extra = f'''<div class="chooser"><p class="chooser-h" id="chooser-h">{e(P["chooser_h"])}</p>
      <ul aria-labelledby="chooser-h">{chooser}</ul></div>'''
    op = opening(L, P["eyebrow"], P["h1"], P["intro"], "stock-wall", [(L.names["diving"], url(c, "diving"))], extra)
    big = "".join(f'''<article class="big-panel reveal">
      <a href="{url(c, b["to"])}" class="frame big-frame">
        {picture(b["img"], L, "(min-width: 900px) 44vw, 100vw")}
        <div class="big-copy"><h2>{e(b["h"])}</h2><p>{e(b["t"])}</p><span class="btn btn-outline btn-sm">{e(b["btn"])}</span></div>
      </a></article>''' for b in P["big"])
    small = "".join(f'''<li class="reveal"><h3>{e(s["h"])}</h3><p>{e(s["t"])}</p>{arrow_link(url(c, s["to"]), s["btn"], "arrow-link light")}</li>'''
                    for s in P["small"])
    checklist = "".join(f"<li>{e(x)}</li>" for x in P["practical"])
    body = f'''
<section class="wrap big-grid">{big}</section>
<section class="wrap"><ul class="small-list">{small}</ul></section>
<section class="paper">
  <div class="wrap practical reveal">
    <h2 class="section-h">{e(P["practical_h"])}</h2>
    <ul class="checklist">{checklist}</ul>
    <p>{e(P["practical_close"])}</p>
    {btn(contact_url(c, "unsure"), P["cta"], "btn btn-dark")}
  </div>
</section>
'''
    return layout(L, ("diving",), P["title"], P["meta"], op, body)


def render_service(L, key):
    P = L.p[key]
    c = L.code
    parent = [(L.names["diving"], url(c, "diving"))] if key in ("wreck", "reef") else []
    op = opening(L, P["eyebrow"], P["h1"], P["intro"], P["img"], parent + [(L.names[key], url(c, key))])
    S = P["summary"]
    summ = "".join(f"<li>{e(x)}</li>" for x in S["list"])
    secs = ""
    for i, s in enumerate(P["sections"]):
        secs += f'<section class="prose-sec reveal"><h2>{e(s["h"])}</h2>{paras(s["p"])}</section>'
        if i == 0 and P.get("inline_img"):
            secs += f'<figure class="frame inline-fig reveal">{picture(P["inline_img"], L, "(min-width: 900px) 56vw, 100vw")}</figure>'
        if i == 0 and P.get("inline_video"):
            secs += f'<div class="inline-video reveal">{video_figure(L, P["inline_video"])}</div>'
    catalog = ""
    if key == "courses":
        catalog = course_catalog(L)
    body = f'''
<div class="paper">
  <div class="wrap with-aside">
    <div class="prose">{secs}{catalog}</div>
    <aside class="summary reveal" aria-labelledby="sum-h">
      <h2 class="summary-h" id="sum-h">{e(S["h"])}</h2>
      <p class="summary-for">{e(S["for"])}</p>
      <ul class="checklist">{summ}</ul>
      {btn(contact_url(c, P["interest"]), P["cta"], "btn btn-dark")}
    </aside>
  </div>
</div>
{related(L, P["related"])}
{cta_band(L, P["cta"], "", L.ui["plan_cta"], P["interest"])}
'''
    return layout(L, (key,), P["title"], P["meta"], op, body)


def course_catalog(L):
    items = [co for co in data.COURSES if co.get("verified")]
    if not items:
        return ""
    cards = ""
    for co in items:
        inc = "".join(f"<li>{e(x)}</li>" for x in co["inclusions"][L.code])
        cards += f'''<article class="course"><p class="eyebrow">{e(co["agency"])}</p><h3>{e(co["name"][L.code])}</h3>
          <dl><dt>Min. age</dt><dd>{co["min_age"]}</dd><dt>Duration</dt><dd>{e(co["duration"][L.code])}</dd>
          <dt>Dives</dt><dd>{co["dives"]}</dd><dt>Languages</dt><dd>{e(", ".join(co["languages"]))}</dd>
          <dt>Price</dt><dd>PHP {co["price_php"]:,}</dd></dl><ul>{inc}</ul></article>'''
    return f'<section class="prose-sec"><h2>{e(L.p["courses"]["catalog_h"])}</h2><div class="courses">{cards}</div></section>'


def render_sites(L):
    P = L.p["sites"]
    c = L.code
    op = opening(L, P["eyebrow"], P["h1"], P["intro"], P["img"], [(L.names["sites"], url(c, "sites"))], note=P["img_note"])
    types = sorted({s["type"] for s in L.sites})
    filt = ""
    if len(types) > 1:
        b = [f'<button type="button" aria-pressed="true" data-filter="all">{e(L.ui["filter_all"])}</button>']
        b += [f'<button type="button" aria-pressed="false" data-filter="{t}">{e(L.ui["filter_" + t])}</button>' for t in types]
        filt = f'<div class="filters" role="group" aria-label="{e(L.ui["sites_filter"])}" data-filter-group="sites">{"".join(b)}</div>'
    rows = "".join(f'''<li class="site-row reveal" data-cat="{s["type"]}">
      <a href="{url(c, "site", s["slug"])}">
        <span class="sr-n" aria-hidden="true">{i + 1:02d}</span>
        <span class="sr-img frame">{picture(s["img"], L, "(min-width: 900px) 260px, 92vw", alt="")}</span>
        <span class="sr-main"><span class="site-type">{e(L.ui["type_" + s["type"]])}</span>
        <span class="sr-name">{e(s["name"])}</span>
        <span class="sr-card">{e(s["card"])}</span></span>
        <span class="sr-go">{e(L.ui["read_guide"])}{icon("arrow")}</span>
      </a></li>''' for i, s in enumerate(L.sites))
    reef_note = ""
    if "reef" not in types:
        reef_note = f'''<div class="note-panel reveal"><h2>{e(P["reef_note_h"])}</h2><p>{e(P["reef_note_t"])}</p>
          {arrow_link(url(c, "reef"), P["reef_note_link"], "arrow-link light")}</div>'''
    body = f'''
<section class="wrap sites-dir">{filt}<ol class="site-rows" data-filter-target="sites">{rows}</ol>{reef_note}</section>
{cta_band(L, L.p["wreck"]["cta"], "", L.ui["plan_cta"], "wreck")}
'''
    return layout(L, ("sites",), P["title"], P["meta"], op, body)


def render_site(L, s):
    P = L.p["site"]
    c = L.code
    meta = data.SITE_META[s["slug"]]
    reviewed = data.REVIEWED_LABEL[meta["reviewed"]][c]
    name_plain = s["name"]
    op = opening(L, P["eyebrow"], s["name"], s["card"], s["img"],
                 [(L.names["sites"], url(c, "sites")), (s["name"], url(c, "site", s["slug"]))], note=P["img_note"])
    ask = "".join(f"<li>{e(x)}</li>" for x in P["ask"])
    others = "".join(f'<li><a href="{url(c, "site", o["slug"])}"><span class="sr-name">{e(o["name"])}</span>{icon("arrow")}</a></li>'
                     for o in L.sites if o["slug"] != s["slug"])
    cta_label = P["cta"].format(name=name_plain)
    body = f'''
<div class="paper">
  <div class="wrap with-aside">
    <div class="prose">
      <section class="prose-sec reveal"><h2>{e(P["distinct_h"])}</h2>{paras(s["p"])}
        <p class="reviewed small">{e(L.ui["reviewed"])}: <time datetime="{meta["reviewed"]}">{e(reviewed)}</time></p></section>
      <section class="prose-sec reveal"><h2>{e(P["fit_h"])}</h2><p>{e(P["fit_t"])}</p></section>
    </div>
    <aside class="summary reveal" aria-labelledby="ask-h">
      <h2 class="summary-h" id="ask-h">{e(P["ask_h"])}</h2>
      <ul class="checklist">{ask}</ul>
      {btn(contact_url(c, "wreck", s["slug"]), cta_label, "btn btn-dark")}
      <p class="small summary-note">{e(P["cta_note"])}</p>
    </aside>
  </div>
</div>
<section class="wrap other-sites reveal" aria-labelledby="other-h"><h2 class="related-h" id="other-h">{e(P["other_h"])}</h2><ul>{others}</ul></section>
{cta_band(L, cta_label, "", L.ui["plan_cta"], "wreck", s["slug"], P["cta_note"])}
'''
    return layout(L, ("site", s["slug"]), s["title"], s["meta"], op, body)


def render_plan(L):
    P = L.p["plan"]
    c = L.code
    op = opening(L, P["eyebrow"], P["h1"], P["intro"], P["img"], [(L.names["plan"], url(c, "plan"))])
    toc = "".join(f'<li><a href="#{s["id"]}">{e(s["h"])}</a></li>' for s in P["steps"])
    steps = ""
    for i, s in enumerate(P["steps"]):
        link = ""
        if s.get("link"):
            link = f'<p>{ext(config.DAN_FLYING_URL, e(s["link"]), "text-link", L)}</p>'
        steps += f'''<li class="step reveal" id="{s["id"]}"><span class="step-n" aria-hidden="true">{i + 1:02d}</span>
          <div><h2>{e(s["h"])}</h2><p>{e(s["p"])}</p>{link}</div></li>'''
        if s["id"] == "packing":
            steps += f'<li class="step-fig reveal"><figure class="frame inline-fig">{picture("stock-fins", L, "(min-width: 900px) 60vw, 92vw")}</figure></li>'
    more = [("faq", None), ("booking", None), ("gallery", None), ("journal", None)]
    body = f'''
<div class="paper">
  <div class="wrap with-aside aside-left">
    <nav class="toc reveal" aria-label="{e(L.ui["section_nav"])}"><ol>{toc}</ol></nav>
    <ol class="steps">{steps}</ol>
  </div>
</div>
{related(L, more)}
{cta_band(L, P["cta"], "", L.ui["plan_cta"], P["interest"])}
'''
    return layout(L, ("plan",), P["title"], P["meta"], op, body)


def render_about(L):
    P = L.p["about"]
    c = L.code
    C = config.CONTACT
    op = opening(L, P["eyebrow"], P["h1"], P["intro"], P["img"], [(L.names["about"], url(c, "about"))])
    channels = [
        (icon("facebook"), L.ui["facebook"], C["facebook"]),
        (icon("instagram"), L.ui["instagram"], C["instagram"]),
        (icon("naver"), L.ui["naver"], C["naver"]),
    ]
    ch = "".join(f'<li>{ext(h, i + "<span>" + e(t) + "</span>", "chan", L)}</li>' for i, t, h in channels)
    ch += f'<li><a class="chan" href="{url(c, "contact")}">{icon("arrow")}<span>{e(P["contact_link"])}</span></a></li>'
    body = f'''
<section class="wrap about-intro">
  <div class="about-copy reveal">
    <h2 class="section-h">{e(P["s1_h"])}</h2>
    <p>{e(P["s1_t"])}</p>
  </div>
  <div class="about-strip">
    <figure class="frame reveal">{picture("shop-guests", L, "(min-width: 900px) 30vw, 100vw")}</figure>
    <figure class="frame reveal">{picture("boat-briefing", L, "(min-width: 900px) 30vw, 100vw")}</figure>
    <figure class="frame reveal">{picture("diver-sand", L, "(min-width: 900px) 30vw, 100vw")}</figure>
  </div>
</section>
<section class="paper">
  <div class="wrap about-grid">
    <div class="reveal">
      <h2 class="section-h">{e(P["s2_h"])}</h2>
      <p>{e(P["s2_t"])}</p>
      <ul class="chan-list">{ch}</ul>
      <p>{arrow_link(url(c, "gallery"), P["gallery_link"], "arrow-link")}</p>
    </div>
    <div class="reveal lang-note">
      <h2 class="section-h">{e(P["lang_h"])}</h2>
      <p>{e(P["lang_t"])}</p>
    </div>
  </div>
</section>
{cta_band(L, L.p["home"]["contact_h"], L.p["home"]["contact_t"], L.p["home"]["contact_btn"])}
'''
    return layout(L, ("about",), P["title"], P["meta"], op, body, jsonld=[business_ld(L)])


# Photo for each homepage route row, keyed by the route's destination page.
ROUTE_IMG = {"diving": "stock-wall", "first": "stock-pair", "courses": "pool-pair", "island": "island-aerial"}


# Curated gallery: (media key, tile size). Sizes are chosen so each section
# fills complete rows of a 4-column grid: lg = 2x2, wide = 2x1, "" = 1x1.
GALLERY = [
    ("underwater", [("stock-turtle", "lg"), ("hero-fish", ""), ("rock-walls", ""), ("wreck-bow", ""),
                    ("stock-reef-snake", ""), ("stock-wall", ""), ("stock-pair", ""), ("wreck-mast", ""),
                    ("stock-descent", "")]),
    ("video", "dugong"),
    ("islands", [("island-aerial", "lg"), ("flag-boat", ""), ("island-small", ""), ("beach-walk", ""),
                 ("boat-group", "")]),
    ("moments", [("shop-guests", "wide"), ("boat-briefing", ""), ("diver-sand", ""), ("pool-skills", ""),
                 ("seabed-group", ""), ("shop-guests-2", "wide")]),
]


def video_figure(L, key, cls="frame video-fig"):
    v = media.VIDEOS[key]
    return f'''<figure class="{cls}">
  <video controls preload="none" playsinline poster="/assets/video/{key}-poster.jpg" width="640" height="360">
    <source src="/assets/video/{key}.mp4" type="video/mp4">{e(L.ui["video_fallback"])}</video>
  <figcaption>{e(v["caption"][L.code])}</figcaption>
</figure>'''


def render_gallery(L):
    P = L.p["gallery"]
    c = L.code
    op = opening(L, P["eyebrow"], P["h1"], P["intro"], P["img"], [(L.names["gallery"], url(c, "gallery"))])
    nav = "".join(f'<li><a href="#g-{k}">{e(P["sections"][k][0])}</a></li>' for k, _ in GALLERY)
    secs = ""
    for k, items in GALLERY:
        h, t = P["sections"][k]
        head = f'<div class="gal-head reveal"><h2 class="section-h">{e(h)}</h2><p class="muted">{e(t)}</p></div>'
        if k == "video":
            secs += f'''<section class="gal-sec gal-video" id="g-{k}" aria-labelledby="g-{k}-h">
  <div class="gal-video-grid">{video_figure(L, items)}
    <div class="gal-video-copy reveal"><h2 class="section-h" id="g-{k}-h">{e(h)}</h2><p class="muted">{e(t)}</p>
      {arrow_link(url(c, "reef"), P["video_link"], "arrow-link light")}</div></div></section>'''
            continue
        tiles = ""
        for key, size in items:
            w0, _ = SIZES[key]
            full = f"/assets/img/{key}-{1920 if w0 >= 1920 else (1280 if w0 >= 1280 else 640)}.webp"
            sz = "(min-width: 900px) 46vw, 92vw" if size == "lg" else "(min-width: 900px) 23vw, 46vw"
            tiles += f'''<li class="tile {size} reveal"><a class="frame" href="{full}" data-lightbox data-caption="{e(media.MEDIA[key]["alt"][c])}">{picture(key, L, sz)}</a></li>'''
        secs += f'''<section class="gal-sec" id="g-{k}" aria-labelledby="g-{k}-h">
  {head.replace('class="section-h"', f'class="section-h" id="g-{k}-h"', 1)}
  <ul class="gal-grid">{tiles}</ul></section>'''
    lightbox = f'''<dialog class="lightbox" aria-label="{e(L.ui["lb_label"])}" data-lightbox-dialog>
  <figure><img alt="" src="data:," data-lb-img><figcaption data-lb-cap></figcaption></figure>
  <button type="button" class="lb-btn lb-prev" data-lb-prev aria-label="{e(L.ui["lb_prev"])}">{icon("arrow", "ico flip")}</button>
  <button type="button" class="lb-btn lb-next" data-lb-next aria-label="{e(L.ui["lb_next"])}">{icon("arrow")}</button>
  <button type="button" class="lb-btn lb-close" data-lb-close aria-label="{e(L.ui["lb_close"])}">{icon("close")}</button>
</dialog>'''
    body = f'''
<div class="wrap gallery">
  <nav class="gal-nav" aria-label="{e(P["nav_label"])}"><ul>{nav}</ul></nav>
  {secs}
  <p class="gallery-more">{ext(config.CONTACT["instagram"], icon("instagram") + "<span>" + e(P["insta"]) + "</span>", "btn btn-outline with-ico", L)}</p>
</div>
{lightbox}
{cta_band(L, P["cta"], L.p["home"]["contact_t"], L.ui["plan_cta"])}
'''
    return layout(L, ("gallery",), P["title"], P["meta"], op, body)


def render_faq(L):
    P = L.p["faq"]
    c = L.code
    op = opening(L, P["eyebrow"], P["h1"], P["intro"], "diver-sand", [(L.names["faq"], url(c, "faq"))])
    groups = ""
    qa = []
    for g in P["groups"]:
        items = "".join(f'''<details class="qa" id="{fid}"><summary><span>{e(q)}</span>{icon("chev", "ico chev")}</summary><div class="qa-a"><p>{e(a)}</p></div></details>'''
                        for fid, q, a in g["items"])
        qa += [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for _, q, a in g["items"]]
        groups += f'<section class="faq-group reveal"><h2>{e(g["h"])}</h2>{items}</section>'
    body = f'''
<div class="paper"><div class="wrap faq-wrap">{groups}</div></div>
{cta_band(L, P["cta_h"], "", P["cta"])}
'''
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": qa}
    return layout(L, ("faq",), P["title"], P["meta"], op, body, jsonld=[ld])


def render_journal(L):
    P = L.p["journal"]
    c = L.code
    op = opening(L, P["eyebrow"], P["h1"], P["intro"], "stock-split", [(L.names["journal"], url(c, "journal"))])
    cards = "".join(f'''<li class="j-item reveal"><a href="{url(c, "article", a["slug"])}">
        <span class="j-media frame">{picture(a["img"], L, "(min-width: 900px) 30vw, 100vw")}</span>
        <span class="j-title">{e(a["title"])}</span>
        <span class="j-meta">{e(a["meta"])}</span>
        <span class="arrow-link light"><span>{e(L.ui["read_article"])}</span>{icon("arrow")}</span></a></li>'''
                    for a in L.articles)
    body = f'''<section class="wrap journal"><ul class="j-grid">{cards}</ul></section>
{cta_band(L, L.p["home"]["contact_h"], L.p["home"]["contact_t"], L.ui["plan_cta"])}'''
    return layout(L, ("journal",), P["title"], P["meta"], op, body)


def render_article(L, a):
    c = L.code
    op = opening(L, L.p["journal"]["eyebrow"], a["title"], a["meta"], a["img"],
                 [(L.names["journal"], url(c, "journal")), (a["title"], url(c, "article", a["slug"]))])
    secs = "".join(f'<section class="prose-sec reveal"><h2>{e(h)}</h2>{paras(ps)}</section>' for h, ps in a["body"])
    body = f'''
<div class="paper"><article class="wrap article">{secs}
  <p class="article-cta reveal">{btn(contact_url(c, a["interest"]), a["cta"], "btn btn-dark")}</p>
</article></div>
{related(L, a["related"])}
{cta_band(L, a["cta"], "", L.ui["plan_cta"], a["interest"])}
'''
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["meta"],
          "inLanguage": c, "publisher": {"@type": "Organization", "name": "W Divers Coron"}}
    return layout(L, ("article", a["slug"]), f'{a["title"]} | W Divers Coron', a["meta"], op, body, jsonld=[ld])


def render_contact(L):
    P = L.p["contact"]
    c = L.code
    C = config.CONTACT
    op = opening(L, P["eyebrow"], P["h1"], P["intro"], "boat-group", [(L.names["contact"], url(c, "contact"))],
                 extra=f'''<div class="po-actions">{ext(wa_url(), icon("whatsapp") + "<span>" + e(L.ui["whatsapp_cta"]) + "</span>", "btn btn-outline with-ico", L)}
                 <a class="arrow-link light" href="mailto:{C["email"]}"><span>{e(L.ui["email_cta"])}</span>{icon("arrow")}</a></div>''')
    req = f'<span class="req">({e(P["required"])})</span>'
    opt = lambda opts: "".join(f'<option value="{e(v)}">{e(t)}</option>' for v, t in opts)  # noqa: E731
    topics = {s["slug"]: s["name"] for s in L.sites}
    cfg = {
        "wa": C["whatsapp_number"], "email": C["email"], "subject": P["email_subject"],
        "intro": P["msg_intro"], "labels": P["msg_labels"], "hints": P["f_detail_hint"],
        "topics": topics, "copied": P["copied"], "copyFailed": P["copy_failed"], "handoff": P["handoff_note"],
        "errors": {k: P[k] for k in ("err_name", "err_method", "err_detail", "err_email", "err_interest", "err_message")},
    }
    kakao = "".join(f'''<li class="kakao-id"><span class="kakao-label">{e(L.ui[k["label_key"]])}</span>
        <code>{e(k["id"])}</code>
        <button type="button" class="btn btn-ghost btn-sm" data-copy="{e(k["id"])}" data-copied="{e(L.ui["copied"])}" data-failed="{e(L.ui["copy_failed"])}">{icon("copy")}<span>{e(L.ui["copy_id"])}</span></button></li>'''
                    for k in config.KAKAO_IDS)
    body = f'''
<div class="paper">
  <div class="wrap contact-grid">
    <section class="composer reveal" id="inquiry" aria-labelledby="form-h">
      <h2 class="section-h" id="form-h">{e(P["form_h"])}</h2>
      <p class="muted-dark">{e(P["form_intro"])}</p>
      <noscript><p class="notice">{e(P["noscript"])}</p></noscript>
      <form class="inquiry" data-inquiry novalidate>
        <div class="err-summary" data-err-summary tabindex="-1" hidden><p>{e(P["error_summary"])}</p><ul></ul></div>
        <div class="field"><label for="f-name">{e(P["f_name"])} {req}</label>
          <input id="f-name" name="name" type="text" autocomplete="name" required>
          <p class="f-err" id="f-name-err" hidden></p></div>
        <div class="field-row">
          <div class="field"><label for="f-method">{e(P["f_method"])} {req}</label>
            <select id="f-method" name="method" required><option value="">{e(P["f_choose"])}</option>{opt(P["f_method_opts"])}</select>
            <p class="f-err" id="f-method-err" hidden></p></div>
          <div class="field"><label for="f-detail">{e(P["f_detail"])} {req}</label>
            <input id="f-detail" name="detail" type="text" required aria-describedby="f-detail-hint">
            <p class="hint" id="f-detail-hint"></p>
            <p class="f-err" id="f-detail-err" hidden></p></div>
        </div>
        <div class="field"><label for="f-interest">{e(P["f_interest"])} {req}</label>
          <select id="f-interest" name="interest" required><option value="">{e(P["f_choose"])}</option>{opt(P["f_interest_opts"])}</select>
          <p class="f-err" id="f-interest-err" hidden></p></div>
        <div class="field"><label for="f-message">{e(P["f_message"])} {req}</label>
          <textarea id="f-message" name="message" rows="5" required aria-describedby="f-message-hint"></textarea>
          <p class="hint" id="f-message-hint">{e(P["f_message_hint"])}</p>
          <p class="f-err" id="f-message-err" hidden></p></div>
        <fieldset class="optional"><legend>{e(P["optional_h"])}</legend>
          <div class="field-row">
            <div class="field"><label for="f-dates">{e(P["f_dates"])}</label>
              <input id="f-dates" name="dates" type="text" aria-describedby="f-dates-hint"><p class="hint" id="f-dates-hint">{e(P["f_dates_hint"])}</p></div>
            <div class="field"><label for="f-guests">{e(P["f_guests"])}</label>
              <input id="f-guests" name="guests" type="number" min="1" max="99" inputmode="numeric"></div>
          </div>
          <div class="field-row">
            <div class="field"><label for="f-experience">{e(P["f_experience"])}</label>
              <input id="f-experience" name="experience" type="text" aria-describedby="f-exp-hint"><p class="hint" id="f-exp-hint">{e(P["f_experience_hint"])}</p></div>
            <div class="field"><label for="f-last">{e(P["f_last"])}</label>
              <input id="f-last" name="last" type="text" aria-describedby="f-last-hint"><p class="hint" id="f-last-hint">{e(P["f_last_hint"])}</p></div>
          </div>
          <div class="field"><label for="f-lang">{e(P["f_lang"])}</label>
            <select id="f-lang" name="lang">{opt(P["f_lang_opts"])}</select></div>
        </fieldset>
        <input type="hidden" name="topic" value="">
        <p class="small muted-dark">{e(P["no_sensitive"])}</p>
        <p class="small muted-dark">{e(P["privacy_micro"])} <a href="{url(c, "privacy")}">{e(P["privacy_link"])}</a></p>
        <div class="form-actions">
          <button type="submit" class="btn btn-dark with-ico" data-action="whatsapp">{icon("whatsapp")}<span>{e(P["btn_whatsapp"])}</span></button>
          <button type="button" class="btn btn-line" data-action="email">{icon("mail")}<span>{e(P["btn_email"])}</span></button>
          <button type="button" class="btn btn-line" data-action="copy">{icon("copy")}<span>{e(P["btn_copy"])}</span></button>
        </div>
        <p class="small muted-dark">{e(P["btn_whatsapp_help"])} {e(P["handoff_note"])}</p>
        <p class="form-status" data-status role="status" aria-live="polite"></p>
        <textarea class="copy-fallback" data-copy-fallback readonly hidden aria-label="{e(P["btn_copy"])}"></textarea>
      </form>
      <script type="application/json" data-inquiry-config>{json.dumps(cfg, ensure_ascii=False).replace("</", "<\\/")}</script>
    </section>
    <aside class="direct reveal" aria-labelledby="direct-h">
      <h2 class="summary-h" id="direct-h">{e(P["direct_h"])}</h2>
      <p class="small">{e(P["direct_t"])}</p>
      <ul class="chan-list">
        <li>{ext(wa_url(), icon("whatsapp") + "<span>" + e(L.ui["whatsapp"]) + " · " + e(C["whatsapp_display"]) + "</span>", "chan", L)}</li>
        <li><a class="chan" href="mailto:{C["email"]}">{icon("mail")}<span>{C["email"]}</span></a></li>
        <li>{ext(C["instagram"], icon("instagram") + "<span>" + e(L.ui["instagram"]) + "</span>", "chan", L)}</li>
        <li>{ext(C["facebook"], icon("facebook") + "<span>" + e(L.ui["facebook"]) + "</span>", "chan", L)}</li>
        <li>{ext(C["naver"], icon("naver") + "<span>" + e(L.ui["naver"]) + "</span>", "chan", L)}</li>
      </ul>
      <div class="kakao" id="kakao">
        <h3>{icon("kakao")}<span>{e(P["kakao_h"])}</span></h3>
        <ul>{kakao}</ul>
        <p class="small">{e(L.ui["kakao_help"])}</p>
        <p class="small">{e(P["kakao_tip"])}</p>
        <p class="small copy-msg" data-copy-msg role="status" aria-live="polite"></p>
      </div>
      <div class="directions">
        <h3>{icon("pin")}<span>{e(P["directions_h"])}</span></h3>
        <p class="small">{e(config.ADDRESS["street"])}, {e(config.ADDRESS["locality"])}, {e(config.ADDRESS["region"])} {e(config.ADDRESS["postal"])}</p>
        <p class="small">{e(P["directions_t"])}</p>
        {ext(C["maps"], e(P["directions_btn"]), "btn btn-line btn-sm", L)}
      </div>
    </aside>
  </div>
</div>
'''
    return layout(L, ("contact",), P["title"], P["meta"], op, body, jsonld=[business_ld(L)], body_cls="is-contact")


def render_booking(L):
    P = L.p["booking"]
    c = L.code
    op = opening(L, P["eyebrow"], P["h1"], P["intro"], "stock-fins", [(L.names["booking"], url(c, "booking"))])
    steps = "".join(f'<li class="step reveal"><span class="step-n" aria-hidden="true">{i + 1:02d}</span><div><h2>{e(s["h"])}</h2><p>{e(s["p"])}</p></div></li>'
                    for i, s in enumerate(P["steps"]))
    body = f'''
<div class="paper"><div class="wrap narrow"><ol class="steps">{steps}</ol>
  <p class="reveal">{btn(contact_url(c, P["interest"]), P["cta"], "btn btn-dark")}</p></div></div>
{related(L, [("faq", None), ("plan", None), ("privacy", None)])}
'''
    return layout(L, ("booking",), P["title"], P["meta"], op, body)


def render_privacy(L):
    P = L.p["privacy"]
    c = L.code
    em = config.CONTACT["email"]
    op = opening(L, P["eyebrow"], P["h1"], P["intro"], None, [(L.names["privacy"], url(c, "privacy"))])
    secs = ""
    for s in P["sections"]:
        ps = "".join("<p>" + e(p).replace("{email}", f'<a href="mailto:{em}">{em}</a>') + "</p>" for p in s["p"])
        secs += f'<section class="prose-sec"><h2>{e(s["h"])}</h2>{ps}</section>'
    body = f'<div class="paper"><div class="wrap narrow prose">{secs}</div></div>'
    return layout(L, ("privacy",), P["title"], P["meta"], op, body)


def render_sitemap(L):
    P = L.p["sitemap"]
    c = L.code
    n = L.names
    op = opening(L, P["eyebrow"], P["h1"], P["intro"], None, [(n["sitemap"], url(c, "sitemap"))])
    g = P["groups"]
    groups = [
        (g[0], [(n[k], url(c, k)) for k in ("home", "diving", "wreck", "reef", "first", "courses", "island")]),
        (g[1], [(n["sites"], url(c, "sites"))] + [(s["name"], url(c, "site", s["slug"])) for s in L.sites]),
        (g[2], [(n[k], url(c, k)) for k in ("plan", "faq", "gallery", "booking")]),
        (g[3], [(n["journal"], url(c, "journal"))] + [(a["title"], url(c, "article", a["slug"])) for a in L.articles]),
        (g[4], [(n[k], url(c, k)) for k in ("about", "contact", "privacy")]),
    ]
    cols = "".join(f'<section><h2>{e(h)}</h2><ul>{"".join(f"<li><a href=\"{u}\">{e(t)}</a></li>" for t, u in items)}</ul></section>'
                   for h, items in groups)
    body = f'<div class="paper"><div class="wrap sitemap-grid">{cols}</div></div>'
    return layout(L, ("sitemap",), P["title"], P["meta"], op, body)


def render_404():
    blocks = ""
    for c in config.LOCALES:
        L = Locale.cache[c]
        P = L.p["404"]
        links = "".join(f'<li><a href="{url(c, k)}">{e(L.names[k])}</a></li>' for k in ("diving", "sites", "plan", "contact"))
        blocks += f'''<section class="nf-block" lang="{c}" data-nf="{c}">
      <p class="eyebrow">404</p><h1 class="po-title">{e(P["h1"])}</h1><span class="rule" aria-hidden="true"></span>
      <p class="lead">{e(P["t"])}</p><ul class="nf-links">{links}</ul>
      {btn(url(c, "home"), P["home"], "btn btn-outline")}</section>'''
    L = Locale.cache[config.DEFAULT_LOCALE]
    return f'''<!doctype html>
<html lang="{L.code}">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(L.p["404"]["title"])}</title><meta name="robots" content="noindex">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/brand/favicon-32.png">
<link rel="stylesheet" href="/assets/css/site.css?v={ASSET_V}">
<script>document.documentElement.classList.add('js')</script></head>
<body class="is-404">
<main id="main" class="nf">
  <a class="brand" href="/">{'<img src="/assets/brand/logo-white.png" alt="W Divers Coron" width="110" height="110">'}</a>
  <div class="frame nf-frame">{blocks}</div>
</main>
<script>
(function(){{var m=location.pathname.match(/\\/(ko|en)\\//);var l=m?m[1]:null;
try{{l=l||localStorage.getItem('wd-lang')}}catch(e){{}}
if(l){{document.documentElement.lang=l;document.querySelectorAll('[data-nf]').forEach(function(b){{if(b.getAttribute('data-nf')!==l)b.hidden=true}})}}}})();
</script>
</body></html>'''


def render_root():
    en = Locale.cache["en"]
    ko = Locale.cache["ko"]
    return f'''<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>W Divers Coron | Coron, Palawan</title>
<meta name="description" content="{e(en.p["home"]["meta"])}">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/brand/favicon-32.png">
<link rel="stylesheet" href="/assets/css/site.css?v={ASSET_V}">
<script>
(function(){{var l=null;try{{l=localStorage.getItem('wd-lang')}}catch(e){{}}
if(l!=='en'&&l!=='ko'){{var n=(navigator.languages||[navigator.language||'']).join(',').toLowerCase();l=/(^|,)ko/.test(n)?'ko':'en'}}
location.replace('{config.BASE_PATH.rstrip("/")}/'+l+'/');}})();
</script></head>
<body class="is-404"><main class="nf">
<img src="/assets/brand/logo-white.png" alt="W Divers Coron" width="110" height="110">
<div class="frame nf-frame"><div class="lang-choose">
<a class="btn btn-outline" href="/en/" hreflang="en" lang="en">English</a>
<a class="btn btn-outline" href="/ko/" hreflang="ko" lang="ko">{e(ko.lang_name)}</a></div></div>
</main></body></html>'''


# ----------------------------------------------------------------- build

def with_base(content):
    """Prefix root-relative URLs with BASE_PATH so the site works from a sub-folder."""
    b = config.BASE_PATH.rstrip("/")
    if not b:
        return content
    content = re.sub(r'(\s(?:href|src|content|poster)=")/(?!/)', rf"\1{b}/", content)
    content = re.sub(r'srcset="[^"]*"', lambda m: m.group(0).replace("/assets/", f"{b}/assets/"), content)
    return content.replace('"image": "/assets/', f'"image": "{b}/assets/')


def write(path, content):
    content = with_base(content)
    full = os.path.join(DIST, path.lstrip("/"))
    if full.endswith("/") or full.endswith(os.sep):
        full = os.path.join(full, "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def copy_static():
    for sub in ("css", "js", "fonts"):
        src = os.path.join(SRC, "static", sub)
        dst = os.path.join(DIST, "assets", sub)
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)


def main():
    global SIZES
    os.makedirs(DIST, exist_ok=True)
    SIZES = media.process(DIST)
    copy_static()
    Locale.cache = {c: Locale(c) for c in config.LOCALES}
    pages = []
    for c in config.LOCALES:
        L = Locale.cache[c]
        out = [
            (("home",), render_home(L)), (("diving",), render_diving(L)),
            (("sites",), render_sites(L)), (("plan",), render_plan(L)), (("about",), render_about(L)),
            (("gallery",), render_gallery(L)), (("faq",), render_faq(L)), (("journal",), render_journal(L)),
            (("contact",), render_contact(L)), (("booking",), render_booking(L)),
            (("privacy",), render_privacy(L)), (("sitemap",), render_sitemap(L)),
        ]
        out += [((k,), render_service(L, k)) for k in ("wreck", "reef", "first", "courses", "island")]
        out += [(("site", s["slug"]), render_site(L, s)) for s in L.sites]
        out += [(("article", a["slug"]), render_article(L, a)) for a in L.articles]
        for route, content in out:
            write(url(c, *route), content)
            pages.append(route)
    write("/404.html", render_404())
    write("/index.html", render_root())

    robots = "User-agent: *\nAllow: /\n"
    sm = os.path.join(DIST, "sitemap.xml")
    if config.SITE_URL:
        robots += f"\nSitemap: {config.SITE_URL}/sitemap.xml\n"
        seen = []
        rows = []
        for route in pages:
            if route in seen:
                continue
            seen.append(route)
            for c in config.LOCALES:
                alts = "".join(f'<xhtml:link rel="alternate" hreflang="{o}" href="{config.SITE_URL}{url(o, *route)}"/>' for o in config.LOCALES)
                rows.append(f"<url><loc>{config.SITE_URL}{url(c, *route)}</loc>{alts}</url>")
        with open(sm, "w", encoding="utf-8") as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                    'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(rows) + "\n</urlset>\n")
    elif os.path.exists(sm):
        os.remove(sm)
    with open(os.path.join(DIST, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)
    # Serve files as-is on GitHub Pages (no Jekyll processing)
    open(os.path.join(DIST, ".nojekyll"), "w").close()
    print(f"Built {len(pages)} pages in {config.LOCALES} -> {DIST}")


if __name__ == "__main__":
    main()
