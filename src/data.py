"""Language-neutral data: course catalog and dive-site editorial metadata."""

# Course catalog. Publish an entry only after the business confirms it is an
# active offering. Each entry needs every field below; text fields are keyed by
# locale. While the list is empty the Courses page shows its full guidance
# content and no catalog section.
#
# Example entry:
# {
#     "slug": "open-water",
#     "verified": True,
#     "agency": "SSI",                       # exact certifying agency
#     "name": {"en": "Open Water Diver", "ko": "오픈워터 다이버"},
#     "min_age": 10,
#     "prerequisites": {"en": "...", "ko": "..."},
#     "duration": {"en": "3 to 4 days", "ko": "3~4일"},
#     "dives": 4,
#     "languages": ["English", "Korean"],    # instructor languages
#     "inclusions": {"en": ["..."], "ko": ["..."]},
#     "price_php": 0,                        # total price in PHP
# }
COURSES = []

# Editorial provenance for the dive-site guides. Not displayed except the
# review date. Keep sources current when copy changes.
SITE_META = {
    "okikawa-maru": {
        "reviewed": "2026-10",
        "sources": ["PADI Coron dive-site guide [S2]",
                    "Historical record of the US Navy carrier air attack on Coron Bay, 24 September 1944"],
    },
    "akitsushima": {
        "reviewed": "2026-10",
        "sources": ["PADI Coron dive-site guide [S2]",
                    "Historical record of the Imperial Japanese Navy seaplane tender Akitsushima"],
    },
    "olympia-maru": {
        "reviewed": "2026-10",
        "sources": ["PADI Coron dive-site guide [S2]"],
        "note": "Brief card text said 'upright'. Orientation omitted until verified.",
    },
    "kogyo-maru": {
        "reviewed": "2026-10",
        "sources": ["PADI Coron dive-site guide [S2]"],
        "note": "Cargo described as 'reported' building materials; confirm wording with the team.",
    },
}

REVIEWED_LABEL = {"2026-10": {"en": "October 2026", "ko": "2026년 10월"}}
