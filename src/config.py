"""Site-wide configuration. Edit values here, then run `python src/build.py`."""

# Set to the full URL of the site root (no trailing slash, including any
# BASE_PATH) once the domain is confirmed, e.g. "https://www.example.com".
# While empty, canonical URLs, hreflang
# alternates, og:url and sitemap.xml are not generated, because publishing
# them for a domain the business does not own would be wrong.
SITE_URL = ""

# URL prefix when the site is served from a sub-folder. GitHub Pages project
# sites live at https://<user>.github.io/<repo>/, so this is "/W-Divers-Coron".
# Set to "" when the site moves to its own domain.
BASE_PATH = "/W-Divers-Coron"

LOCALES = ["en", "ko"]
DEFAULT_LOCALE = "en"

BUSINESS_NAME = "W Divers Coron"

# Authoritative contact configuration supplied by Lyneth on 25 October 2026
# (Instagram updated the same day to @wdiverscoronpalawan). Pages show channel
# names, not usernames.
CONTACT = {
    "facebook": "https://www.facebook.com/Wdiverscoronpalawan",
    "instagram": "https://www.instagram.com/wdiverscoronpalawan/",
    "whatsapp_display": "+82 10 8621 8096",
    "whatsapp_number": "821086218096",
    "email": "wdiverscoron@gmail.com",
    "maps": "https://www.google.com/maps/place/?q=place_id:ChIJy1EoZNQdujMRmLH0eY9EEXw",
    "naver": "https://blog.naver.com/redscandle",
}

# KakaoTalk IDs as printed on the business's own contact cards
# (assets/images/513276370_...jpg and 808897143_...jpg). IDs only: no channel
# URL or QR code was found, so the site offers copy-ID actions.
KAKAO_IDS = [
    {"id": "redscandle3384", "label_key": "kakao_kr"},
    {"id": "wdiverscoron", "label_key": "kakao_ph"},
]

# Address wording from the earlier internal brief and Google listing.
# The meeting point is NOT confirmed; pages tell visitors to confirm it.
ADDRESS = {
    "street": "Barangay Poblacion 5, National Highway",
    "locality": "Coron Town Proper, Coron",
    "region": "Palawan",
    "postal": "5316",
    "country": "PH",
}

STUDIO_URL = "https://lendezstudio.com/"

DAN_FLYING_URL = "https://dan.org/health-medicine/health-resources/diseases-conditions/flying-after-diving/"
