"""November 2026 additions for each language: Pro's, Special Trips, DSD, Scuba Courses,
TDI, Free Diving, the About story, new slides and new photo descriptions.

Each <code>.json holds only text. apply() overlays it onto a language module's
UI, ROUTE_NAMES, PAGES, TRIPS and ALT; links, images and ids still come from en.py.
"""
import json
import os

HERE = os.path.dirname(__file__)


def apply(code, ns):
    path = os.path.join(HERE, f"{code}.json")
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as f:
        n = json.load(f)
    ns["UI"].update(n["UI"])
    ns["ROUTE_NAMES"].update(n["ROUTE_NAMES"])
    pages = ns["PAGES"]
    for key, value in n["PAGES"].items():
        if key == "about" and key in pages:
            pages[key].update(value)      # keep the older About text that is still in use
        else:
            pages[key] = value            # new pages, and pages rewritten since the last pass
    pages["home"].update(n["HOME"])
    pages["contact"]["f_interest_opts"] = [tuple(x) for x in n["CONTACT_INTEREST"]]
    pages["sitemap"]["groups"] = n["SITEMAP_GROUPS"]
    ns["TRIPS"] = n["TRIPS"]
    ns.setdefault("ALT", {}).update(n["ALT"])
