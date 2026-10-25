"""Media manifest and image processing.

Every image used on the site is listed here with its provenance:
  business  = supplied W Divers media (Facebook-sourced files in assets/images)
  stock     = Pexels download (assets/Images from pexels); thematic only,
              never captioned as a specific Coron site or as W Divers guests.

`focus` is a CSS object-position used when an image is cropped.
`cats` drive the gallery filters. Images without cats are not in the gallery.
"""
import os
import shutil
import subprocess

from PIL import Image, ImageFilter, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "images")
PEX = os.path.join(ROOT, "assets", "Images from pexels")

WIDTHS = [640, 1280, 1920]

MEDIA = {
    # Business media
    "hero-fish": {
        "src": (IMG, "512086947_3635699019895640_5649272940320611113_n.jpg"),
        "kind": "business", "focus": "30% 45%", "cats": ["underwater", "moments"],
        "alt": {"en": "Two scuba divers swim beside a large school of yellow fish over a reef.",
                "ko": "두 명의 스쿠버 다이버가 산호초 위에서 노란 물고기 떼 옆을 헤엄치고 있습니다."},
    },
    "wreck-bow": {
        "src": (IMG, "510213720_3635699456562263_7327651866007780773_n.jpg"),
        "kind": "business", "focus": "50% 40%", "cats": ["underwater", "moments"],
        "alt": {"en": "Divers rise alongside a towering coral-covered underwater structure.",
                "ko": "다이버들이 산호로 뒤덮인 거대한 수중 구조물을 따라 올라가고 있습니다."},
    },
    "wreck-mast": {
        "src": (IMG, "513306213_3635685183230357_6108606527161640286_n.jpg"),
        "kind": "business", "focus": "50% 45%", "cats": ["underwater", "moments"],
        "alt": {"en": "A group of divers gathers around a tall structure rising from the seabed.",
                "ko": "다이버 그룹이 해저에서 솟은 높은 구조물 주위에 모여 있습니다."},
    },
    "seabed-group": {
        "src": (IMG, "510799567_3635699363228939_7030323817826810473_n.jpg"),
        "kind": "business", "focus": "60% 35%", "cats": ["underwater", "moments"],
        "alt": {"en": "A group of divers poses together on the seabed in blue water.",
                "ko": "푸른 바닷속 해저에서 다이버들이 함께 포즈를 취하고 있습니다."},
    },
    "diver-sand": {
        "src": (IMG, "511941640_3635659493232926_3980670975062492712_n.jpg"),
        "kind": "business", "focus": "45% 40%", "cats": ["underwater", "moments"],
        "alt": {"en": "A diver hovers over white sand and reaches toward the camera.",
                "ko": "다이버가 하얀 모래 위에 떠서 카메라를 향해 손을 뻗고 있습니다."},
    },
    "rock-walls": {
        "src": (IMG, "512629134_3635613533237522_1820492965256356325_n.jpg"),
        "kind": "business", "focus": "50% 50%", "cats": ["underwater"],
        "alt": {"en": "A diver descends between steep underwater rock walls.",
                "ko": "다이버가 가파른 수중 암벽 사이로 내려가고 있습니다."},
    },
    "tanks-boat": {
        "src": (IMG, "511821404_3635837136548495_9044966663120801297_n.jpg"),
        "kind": "business", "focus": "50% 60%", "cats": ["moments"],
        "alt": {"en": "Scuba cylinders lined up on a boat while divers prepare their equipment.",
                "ko": "다이버들이 장비를 준비하는 동안 보트 위에 공기탱크가 줄지어 놓여 있습니다."},
    },
    "flag-boat": {
        "src": (IMG, "509914197_3635685173230358_8931917923479836856_n.jpg"),
        "kind": "business", "focus": "50% 30%", "cats": ["islands"],
        "alt": {"en": "Korean and Philippine flags fly from a boat beside green islands.",
                "ko": "푸른 섬을 배경으로 보트에 태극기와 필리핀 국기가 휘날리고 있습니다."},
    },
    "boat-group": {
        "src": (IMG, "600463260_3838271042971769_4233433979847032296_n.jpg"),
        "kind": "business", "focus": "50% 45%", "cats": ["islands", "moments"],
        "alt": {"en": "Guests smile together on a boat deck with green islands behind them.",
                "ko": "푸른 섬을 배경으로 게스트들이 보트 갑판에서 함께 웃고 있습니다."},
    },
    "beach-walk": {
        "src": (IMG, "598580270_3834549283343945_4218312546923648951_n.jpg"),
        "kind": "business", "focus": "50% 50%", "cats": ["islands", "moments"],
        "alt": {"en": "A group walks along a palm-lined shore toward the water.",
                "ko": "야자수가 늘어선 해변을 따라 일행이 바다 쪽으로 걸어가고 있습니다."},
    },
    "boat-briefing": {
        "src": (IMG, "599704121_3830543943744479_292865907568992662_n.jpg"),
        "kind": "business", "focus": "50% 40%", "cats": ["moments"],
        "alt": {"en": "Divers in wetsuits gather on a boat deck before a dive.",
                "ko": "웻슈트를 입은 다이버들이 다이빙 전에 보트 갑판에 모여 있습니다."},
    },
    "shop-front": {
        "src": (IMG, "594398514_3822234311242109_3990147863346867374_n.jpg"),
        "kind": "business", "focus": "50% 30%", "cats": ["moments"],
        "alt": {"en": "Two people look over paperwork at the entrance of the W Divers Coron shop.",
                "ko": "W Divers Coron 샵 입구에서 두 사람이 서류를 함께 보고 있습니다."},
    },
    "shop-guests": {
        "src": (IMG, "598556110_3827640630701477_6349572359701715112_n.jpg"),
        "kind": "business", "focus": "50% 40%", "cats": ["moments"],
        "alt": {"en": "Guests pose under the W Divers Coron sign.",
                "ko": "게스트들이 W Divers Coron 간판 아래에서 포즈를 취하고 있습니다."},
    },
    "shop-guests-2": {
        "src": (IMG, "598559289_3831762660289274_2309205698229230351_n.jpg"),
        "kind": "business", "focus": "50% 45%", "cats": ["moments"],
        "alt": {"en": "A group of guests gives a thumbs up outside the W Divers Coron shop.",
                "ko": "W Divers Coron 샵 앞에서 게스트들이 엄지를 들어 보이고 있습니다."},
    },
    "pool-skills": {
        "src": (IMG, "595618777_3823228414476032_644015780038480087_n.jpg"),
        "kind": "business", "focus": "50% 50%", "cats": ["moments"],
        "alt": {"en": "Divers practise in the clear water of a swimming pool.",
                "ko": "다이버들이 맑은 수영장 물속에서 연습하고 있습니다."},
    },
    "pool-pair": {
        "src": (IMG, "594413277_3823228494476024_106924261345780453_n.jpg"),
        "kind": "business", "focus": "50% 50%", "cats": ["moments"],
        "alt": {"en": "Two divers face each other underwater in a pool.",
                "ko": "수영장 물속에서 두 다이버가 서로 마주 보고 있습니다."},
    },
    "pool-indoor": {
        "src": (IMG, "595664591_3823228457809361_8958770326082131438_n.jpg"),
        "kind": "business", "focus": "50% 60%", "cats": [],
        "alt": {"en": "Divers in an indoor pool gather at the surface in full equipment.",
                "ko": "실내 수영장에서 장비를 갖춘 다이버들이 수면에 모여 있습니다."},
    },
    "surface-group": {
        "src": (IMG, "594422673_3823228151142725_6523286380109604437_n.jpg"),
        "kind": "business", "focus": "50% 50%", "cats": [],
        "alt": {"en": "Divers float together at the surface of calm open water.",
                "ko": "잔잔한 바다 수면에 다이버들이 함께 떠 있습니다."},
    },
    # Stock (Pexels): thematic only
    "stock-pair": {
        "src": (PEX, "pexels-aomata-14565669.jpg"),
        "kind": "stock", "focus": "50% 55%", "cats": ["underwater"],
        "alt": {"en": "Two divers hover in deep blue water, one giving an OK sign.",
                "ko": "짙푸른 물속에서 두 다이버가 떠 있고 한 명이 OK 신호를 보내고 있습니다."},
    },
    "stock-reef-snake": {
        "src": (PEX, "pexels-graham-henderson-37078134-7169290.jpg"),
        "kind": "stock", "focus": "45% 50%", "cats": ["underwater"],
        "alt": {"en": "A banded sea snake crosses a colourful reef as a diver takes a photo.",
                "ko": "다이버가 사진을 찍는 동안 줄무늬 바다뱀이 화려한 산호초를 지나가고 있습니다."},
    },
    "stock-descent": {
        "src": (PEX, "pexels-harvey-clements-13141095-15763632.jpg"),
        "kind": "stock", "focus": "50% 50%", "cats": ["underwater"],
        "alt": {"en": "Divers descend through blue water under shafts of sunlight.",
                "ko": "햇살이 비치는 푸른 물속으로 다이버들이 하강하고 있습니다."},
    },
    "stock-clownfish": {
        "src": (PEX, "pexels-chris-solo-1254330416-25533540.jpg"),
        "kind": "stock", "focus": "40% 40%", "cats": ["underwater"],
        "alt": {"en": "Two clownfish shelter in a sea anemone.",
                "ko": "흰동가리 두 마리가 말미잘 사이에 숨어 있습니다."},
    },
    "stock-turtle": {
        "src": (PEX, "pexels-leonardo-lamas-32247393-7001716.jpg"),
        "kind": "stock", "focus": "45% 60%", "cats": ["underwater"],
        "alt": {"en": "A sea turtle rests on the sandy bottom.",
                "ko": "바다거북이 모래 바닥 위에서 쉬고 있습니다."},
    },
    "stock-wall": {
        "src": (PEX, "pexels-aydenzaki-8029908.jpg"),
        "kind": "stock", "focus": "60% 45%", "cats": ["underwater"],
        "alt": {"en": "A diver swims past a reef wall in deep blue water.",
                "ko": "다이버가 짙푸른 물속에서 산호 벽을 따라 헤엄치고 있습니다."},
    },
    "stock-mask": {
        "src": (PEX, "pexels-ian-panelo-25538747.jpg"),
        "kind": "stock", "focus": "50% 50%", "cats": [],
        "alt": {"en": "A dive mask lies on wet sand at the water's edge.",
                "ko": "물가의 젖은 모래 위에 다이빙 마스크가 놓여 있습니다."},
    },
    "stock-split": {
        "src": (PEX, "pexels-toulouse-3098973.jpg"),
        "kind": "stock", "focus": "50% 60%", "cats": [],
        "alt": {"en": "A diver below the waterline with a lighthouse on the shore above.",
                "ko": "수면 아래의 다이버와 그 위 해안의 등대가 함께 보입니다."},
    },
}

VIDEOS = {
    "dugong": {
        "src": (IMG, "AQPJd6pveLXFQfsJ6EH1b8jQf9avgDqhJ9seLV445InSa2Ou4j__2MXJMQ7QU9ZRDSlSkgVcD2w6o8gKvbL9OnA.mp4"),
        "poster_at": 18,
        "caption": {"en": "A dugong glides past divers. Wildlife encounters are never guaranteed.",
                    "ko": "듀공이 다이버들 곁을 유유히 지나갑니다. 야생동물과의 만남은 보장되지 않습니다."},
    },
}

LOGO_SRC = (IMG, "Restored divers coron logo, crisp and transparent.png")


def _fresh(out, src):
    return os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(src)


def _open(path):
    im = Image.open(path)
    return ImageOps.exif_transpose(im).convert("RGB")


def process(dist):
    """Write responsive WebP/JPEG derivatives, logo variants, icons and video."""
    out_dir = os.path.join(dist, "assets", "img")
    os.makedirs(out_dir, exist_ok=True)
    sizes = {}
    for key, m in MEDIA.items():
        src = os.path.join(*m["src"])
        im = None
        w0, h0 = Image.open(src).size
        if Image.open(src).getexif().get(274) in (5, 6, 7, 8):
            w0, h0 = h0, w0
        sizes[key] = (w0, h0)
        for w in WIDTHS:
            if w > w0 and w != WIDTHS[0]:
                continue
            for ext in ("webp", "jpg"):
                if ext == "jpg" and w != 1280 and not (w0 < 1280 and w == WIDTHS[0]):
                    continue
                out = os.path.join(out_dir, f"{key}-{w}.{ext}")
                if _fresh(out, src):
                    continue
                if im is None:
                    im = _open(src)
                r = im.copy()
                r.thumbnail((w, w * 3))
                if ext == "webp":
                    r.save(out, "WEBP", quality=78, method=5)
                else:
                    r.save(out, "JPEG", quality=80, optimize=True, progressive=True)

    # Blurred, darkened backdrop derived from the hero image
    hero_src = os.path.join(*MEDIA["hero-fish"]["src"])
    bd = os.path.join(out_dir, "hero-backdrop.webp")
    if not _fresh(bd, hero_src):
        im = _open(hero_src)
        im.thumbnail((960, 960))
        im = im.filter(ImageFilter.GaussianBlur(28))
        im = Image.blend(im, Image.new("RGB", im.size, (4, 23, 30)), 0.45)
        im.save(bd, "WEBP", quality=70)

    # Social sharing image
    og = os.path.join(out_dir, "og-default.jpg")
    if not _fresh(og, hero_src):
        im = _open(hero_src)
        ImageOps.fit(im, (1200, 630), centering=(0.3, 0.45)).save(og, "JPEG", quality=82)

    _logos(dist)
    _videos(dist)
    return sizes


def _logos(dist):
    src = os.path.join(*LOGO_SRC)
    out_dir = os.path.join(dist, "assets", "brand")
    os.makedirs(out_dir, exist_ok=True)
    white = os.path.join(out_dir, "logo-white.png")
    if _fresh(white, src):
        return
    lg = Image.open(src).convert("RGBA")
    lg = lg.crop(lg.getbbox())
    lg.thumbnail((480, 480))
    r, g, b, a = lg.split()
    # The supplied mark is black on transparent. The reversed version keeps the
    # same shape and transparency, only the fill changes to soft white.
    fill = Image.new("RGBA", lg.size, (241, 245, 242, 255))
    fill.putalpha(a)
    fill.save(white, optimize=True)
    lg.save(os.path.join(out_dir, "logo-black.png"), optimize=True)
    fill.save(os.path.join(out_dir, "logo-white.webp"), "WEBP", quality=90)

    # Icons: reversed mark on the darkest ocean colour
    for size, name in ((32, "favicon-32.png"), (180, "apple-touch-icon.png"), (512, "icon-512.png")):
        tile = Image.new("RGBA", (size, size), (4, 23, 30, 255))
        m = fill.copy()
        pad = int(size * 0.12)
        m.thumbnail((size - pad * 2, size - pad * 2), Image.LANCZOS)
        tile.alpha_composite(m, ((size - m.width) // 2, (size - m.height) // 2))
        tile.save(os.path.join(out_dir, name))


def _videos(dist):
    out_dir = os.path.join(dist, "assets", "video")
    os.makedirs(out_dir, exist_ok=True)
    for key, v in VIDEOS.items():
        src = os.path.join(*v["src"])
        mp4 = os.path.join(out_dir, f"{key}.mp4")
        if not _fresh(mp4, src):
            shutil.copy2(src, mp4)
        poster = os.path.join(out_dir, f"{key}-poster.jpg")
        if not os.path.exists(poster) and shutil.which("ffmpeg"):
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(v["poster_at"]), "-i", src,
                            "-frames:v", "1", "-q:v", "4", poster], check=False)
