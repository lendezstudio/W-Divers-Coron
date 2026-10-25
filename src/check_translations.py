"""Report text a translation is missing (it would fall back to English).

Usage: python src/check_translations.py [code ...]
"""
import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config  # noqa: E402
import media  # noqa: E402

# Structure inherited from English, not text to translate.
STRUCTURAL = {"to", "img", "interest", "related", "slug", "type", "id", "hash", "inline_img", "inline_video"}
# The inquiry message sent to W Divers keeps English labels on purpose, so the team can always read it.
# Wreck names ("name") stay in their original romanized form unless a translation overrides them.
KEEP_ENGLISH = {"msg_intro", "msg_labels", "email_subject", "name"}


def leaves(obj, path=()):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in STRUCTURAL or k in KEEP_ENGLISH:
                continue
            yield from leaves(v, path + (k,))
    elif isinstance(obj, list) and obj and all(isinstance(x, dict) for x in obj):
        for i, v in enumerate(obj):
            yield from leaves(v, path + (i,))
    else:
        yield path


def check(code):
    en = importlib.import_module("content.en")
    mod = importlib.import_module(f"content.{code.replace('-', '_')}")
    problems = []
    for name in ("UI", "ROUTE_NAMES", "PAGES", "SITES", "ARTICLES"):
        want = set(leaves(getattr(en, name)))
        have = set(leaves(getattr(mod, name, {})))
        problems += [f"{name}: missing {'.'.join(map(str, p))}" for p in sorted(want - have, key=str)]
    alt = getattr(mod, "ALT", {})
    used = [k for k in media.MEDIA]
    problems += [f"ALT: missing {k}" for k in used if k not in alt and code not in media.MEDIA[k]["alt"]]
    for attr in ("LANG", "LANG_NAME", "SHORT", "OG_LOCALE"):
        if not hasattr(mod, attr):
            problems.append(f"missing {attr}")
    return problems


if __name__ == "__main__":
    codes = sys.argv[1:] or [c for c in config.LOCALES if c != "en"]
    bad = 0
    for c in codes:
        p = check(c)
        bad += len(p)
        print(f"{c}: {'complete' if not p else str(len(p)) + ' gaps'}")
        for line in p[:40]:
            print("   ", line)
    sys.exit(1 if bad else 0)
