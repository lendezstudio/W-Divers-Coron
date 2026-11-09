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
NOV = os.path.join(IMG, "November 9, 2026")
NOV10 = os.path.join(IMG, "Enhanced Nov 10")

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
        "kind": "business", "focus": "50% 75%", "cats": ["moments"],
        "alt": {"en": "Guests pose under the W Divers Coron sign.",
                "ko": "게스트들이 W Divers Coron 간판 아래에서 포즈를 취하고 있습니다."},
    },
    "shop-guests-2": {
        "src": (IMG, "598559289_3831762660289274_2309205698229230351_n.jpg"),
        "kind": "business", "focus": "50% 75%", "cats": ["moments"],
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
    # Business photos supplied 9 November 2026 (assets/images/November 9, 2026)
    "lagoon-boats": {
        "src": (NOV, "Aerial Lagoon with Limestone Cliffs and Boats-6.png"),
        "kind": "business", "focus": "60% 60%", "cats": ["islands"],
        "alt": {"en": "Aerial view of a blue W Divers boat in a lagoon between limestone cliffs.",
                "ko": "석회암 절벽 사이 라군에 떠 있는 W Divers의 파란 보트를 위에서 본 모습입니다."},
    },
    "dive-boat": {
        "src": (NOV, "Blue W Divers Outrigger Boat at Sea-4.png"),
        "kind": "business", "focus": "45% 50%", "cats": ["islands", "moments"],
        "alt": {"en": "The blue W Divers outrigger dive boat at sea, seen from above.",
                "ko": "바다 위의 파란색 W Divers 아웃리거 다이빙 보트를 위에서 본 모습입니다."},
    },
    "dean": {
        "src": (IMG, "Scuba instructor portrait on a pink boat.png"),
        "kind": "business", "focus": "50% 22%", "cats": [],
        "alt": {"en": "Dean Kang, head instructor of W Divers Coron, in a Scubapro wetsuit on a boat in Coron.",
                "ko": "코론의 보트 위에서 스쿠버프로 슈트를 입은 W Divers Coron 대표 강사 강덕환."},
    },
    "ssi-shop": {
        "src": (os.path.join(IMG, "SSI"), "67dbf144db423_DC_Image_763270_shop_outside.png"),
        "kind": "business", "focus": "50% 60%", "cats": [],
        "alt": {"en": "Guests and Dean Kang outside the W Divers Coron shop and free diving centre on Coron's main street.",
                "ko": "코론 중심가의 W Divers Coron 샵과 프리다이빙 센터 앞에 선 손님들과 강덕환 강사."},
    },
    "ssi-jungle": {
        "src": (os.path.join(IMG, "SSI"), "67dbf1cbe0742_DC_Image_763270_shop_inside.png"),
        "kind": "business", "focus": "50% 50%", "cats": [],
        "alt": {"en": "Poster of W Divers' filming support for SBS Law of the Jungle in Coron, 21 to 23 January 2020, with photos and signed autographs.",
                "ko": "2020년 1월 21~23일 SBS 정글의 법칙 in 코론 촬영 지원 포스터. 사진과 출연진 사인이 담겨 있습니다."},
    },
    "inhan": {
        "src": (IMG, "Restored portrait of Inhan Kang-2.png"),
        "kind": "business", "focus": "50% 30%", "cats": [],
        "alt": {"en": "Portrait of Inhan Kang, instructor at W Divers Coron.",
                "ko": "W Divers Coron 강사 강인한의 인물 사진."},
    },
    "jex": {
        "src": (IMG, "Restored portrait of Jex Lenver Tabat-1.png"),
        "kind": "business", "focus": "50% 30%", "cats": [],
        "alt": {"en": "Portrait of Jex Lenver Tabat (GIGs), divemaster at W Divers Coron.",
                "ko": "W Divers Coron 다이브마스터 젝스 렌버 타밧(GIGs)의 인물 사진."},
    },
    "yacht-aerial": {
        "src": (NOV10, "Catamaran at anchor, wide (site version).png"),
        "kind": "business", "focus": "50% 55%", "cats": ["islands"],
        "alt": {"en": "A white sailing catamaran at anchor in calm blue water, seen from above.",
                "ko": "잔잔한 푸른 바다에 정박한 흰색 세일링 카타마란을 위에서 본 모습."},
    },
    "yacht-cabin": {
        "src": (NOV10, "Naturally Enhanced Underwater Dive Scene-15.png"),
        "kind": "business", "focus": "50% 50%", "cats": [],
        "alt": {"en": "A bright yacht cabin with a double bed and windows looking out to green islands.",
                "ko": "더블 침대와 초록 섬이 보이는 창이 있는 밝은 요트 객실."},
    },
    "dugong-diver": {
        "src": (NOV10, "Dugong and Diver Beneath Caustic Light-1.png"),
        "kind": "business", "focus": "40% 45%", "cats": ["underwater"],
        "alt": {"en": "A dugong swims in sunlit blue water as a diver watches from a respectful distance.",
                "ko": "햇살이 비치는 푸른 바다에서 헤엄치는 듀공과 거리를 두고 지켜보는 다이버."},
    },
    "calauit-zebras": {
        "src": (NOV10, "Natural underwater diving scene-8.png"),
        "kind": "business", "focus": "50% 60%", "cats": ["islands"],
        "alt": {"en": "Zebras graze near a ranger station at Calauit Safari Park on Busuanga.",
                "ko": "부수앙가 칼라위트 사파리 파크의 관리소 근처에서 풀을 뜯는 얼룩말들."},
    },
    "calauit-giraffes": {
        "src": (NOV10, "Underwater adventure in natural light-3.png"),
        "kind": "business", "focus": "50% 30%", "cats": ["islands"],
        "alt": {"en": "Two giraffes lean toward the camera under a blue sky at Calauit Safari Park.",
                "ko": "칼라위트 사파리 파크의 파란 하늘 아래 카메라 쪽으로 다가온 기린 두 마리."},
    },
    "boat-lunch": {
        "src": (NOV10, "Natural boat lunch spread-3.png"),
        "kind": "business", "focus": "50% 60%", "cats": ["moments"],
        "alt": {"en": "A lunch spread of grilled fish, chicken, vegetables, mussels and mango on a boat deck.",
                "ko": "보트 갑판에 차려진 생선구이, 닭고기, 채소, 홍합, 망고 점심."},
    },
    "w-coral-wreck": {
        "src": (NOV10, "Coral-covered wreck with schooling fish-7 (1).png"),
        "kind": "business", "focus": "55% 55%", "cats": ["underwater"],
        "alt": {"en": "A coral-covered shipwreck rises from blue water, surrounded by schooling fish.",
                "ko": "물고기 떼가 둘러싼, 산호로 덮인 난파선."},
    },
    "w-valves": {
        "src": (NOV10, "Silt-covered engine valves underwater-7.png"),
        "kind": "business", "focus": "50% 50%", "cats": ["underwater"],
        "alt": {"en": "A row of silt-covered engine valves inside a wreck.",
                "ko": "난파선 안에 줄지어 있는 퇴적물 덮인 엔진 밸브."},
    },
    "w-three-divers": {
        "src": (NOV10, "Three Divers at a Coral Wreck-5.png"),
        "kind": "business", "focus": "50% 45%", "cats": ["underwater"],
        "alt": {"en": "Three divers give a peace sign through an opening in a coral-covered wreck.",
                "ko": "산호로 덮인 난파선의 틈 사이로 브이를 하는 다이버 세 명."},
    },
    "w-engine-room": {
        "src": (NOV10, "Moody Underwater Wreck Engine Room-6.png"),
        "kind": "business", "focus": "50% 50%", "cats": ["underwater"],
        "alt": {"en": "Machinery inside the dim engine room of a wreck.",
                "ko": "어두운 난파선 기관실 안의 기계 장치."},
    },
    "w-machinery": {
        "src": (NOV10, "Fish Among Underwater Wreck Machinery-2.png"),
        "kind": "business", "focus": "50% 45%", "cats": ["underwater"],
        "alt": {"en": "Small fish swim past encrusted machinery on a wreck.",
                "ko": "난파선의 산호 덮인 기계 사이를 지나는 작은 물고기들."},
    },
    "fd-cave": {
        "src": (NOV10, "Natural underwater diving adventure-14.png"),
        "kind": "business", "focus": "50% 70%", "cats": ["islands"],
        "alt": {"en": "A limestone cave with stalactites reflected in still water.",
                "ko": "잔잔한 물에 비친 종유석이 있는 석회암 동굴."},
    },
    "fd-beam": {
        "src": (NOV10, "Natural underwater diving scene-11.png"),
        "kind": "business", "focus": "50% 58%", "cats": ["underwater"],
        "alt": {"en": "A freediver floats in a shaft of sunlight in deep blue water.",
                "ko": "깊고 푸른 물속, 햇살 줄기 속에 떠 있는 프리다이버."},
    },
    "dsd-sand": {
        "src": (NOV10, "Underwater adventure, naturally enhanced-1.png"),
        "kind": "business", "focus": "50% 40%", "cats": ["underwater"],
        "alt": {"en": "A diver glides over white sand toward the camera, with other divers behind.",
                "ko": "흰 모래 위를 카메라 쪽으로 미끄러지듯 다가오는 다이버와 뒤편의 다른 다이버들."},
    },
    "pool-lesson": {
        "src": (NOV10, "Poolside scuba lesson-2 (1).png"),
        "kind": "business", "focus": "50% 8%", "cats": ["moments"],
        "alt": {"en": "An instructor prepares scuba equipment with a student beside a swimming pool.",
                "ko": "수영장 옆에서 교육생과 함께 스쿠버 장비를 준비하는 강사."},
    },
    "gear-crates": {
        "src": (NOV10, "Colorful Scuba Gear Beside a Blue Vehicle-1 (1).png"),
        "kind": "business", "focus": "50% 62%", "cats": ["moments"],
        "alt": {"en": "Crates of fins, masks and dive gear ready to load beside a blue vehicle.",
                "ko": "파란 차량 옆에 싣기 위해 준비된 핀, 마스크, 다이빙 장비 상자."},
    },
    "van-transfer": {
        "src": (NOV10, "People boarding a silver van-6 (1).png"),
        "kind": "business", "focus": "50% 50%", "cats": ["moments"],
        "alt": {"en": "Guests with backpacks board a silver van for a transfer.",
                "ko": "배낭을 멘 손님들이 이동을 위해 은색 밴에 타는 모습."},
    },
    "crew-briefing": {
        "src": (NOV10, "Boat crew briefing on deck-4.png"),
        "kind": "business", "focus": "50% 40%", "cats": ["moments"],
        "alt": {"en": "Divers in wetsuits gather for a briefing on the deck of a blue dive boat.",
                "ko": "파란 다이빙 보트 갑판에서 브리핑을 위해 모인 슈트 차림의 다이버들."},
    },
    "harbor-group": {
        "src": (NOV10, "Eight-Person Harbor Portrait by Boats-4 (1).png"),
        "kind": "business", "focus": "50% 50%", "cats": ["moments"],
        "alt": {"en": "A group of eight guests poses on the harbour wall with boats and green hills behind.",
                "ko": "보트와 초록 언덕을 배경으로 항구 방파제에서 포즈를 취한 손님 여덟 명."},
    },
    "briefing-blue": {
        "src": (NOV10, "Dive briefing aboard a blue boat-6.png"),
        "kind": "business", "focus": "50% 40%", "cats": ["moments"],
        "alt": {"en": "Guests relax on a blue dive boat between dives.",
                "ko": "다이빙 사이에 파란 다이빙 보트에서 쉬고 있는 손님들."},
    },
    "heart-divers": {
        "src": (NOV10, "Smiling Divers Form a Heart Gesture-7.png"),
        "kind": "business", "focus": "50% 45%", "cats": ["moments"],
        "alt": {"en": "Two smiling divers make a heart sign at the surface beside the boat.",
                "ko": "보트 옆 수면에서 하트를 만들며 웃는 다이버 두 명."},
    },
    "under-boat": {
        "src": (NOV10, "Divers Beneath the Boat-3.png"),
        "kind": "business", "focus": "50% 55%", "cats": ["underwater"],
        "alt": {"en": "Divers descend over white sand beneath the hull of a boat.",
                "ko": "보트 아래 흰 모래 위로 내려가는 다이버들."},
    },
    "rope": {
        "src": (NOV10, "Encrusted Rope Beneath the Surface-5 (1).png"),
        "kind": "business", "focus": "50% 50%", "cats": ["underwater"],
        "alt": {"en": "A coral-encrusted mooring line hangs in clear blue water.",
                "ko": "맑고 푸른 물속에 늘어진 산호 덮인 계류 밧줄."},
    },
    "flags-bow": {
        "src": (NOV10, "Natural underwater travel scene-4.png"),
        "kind": "business", "focus": "50% 40%", "cats": ["islands"],
        "alt": {"en": "Korean and Philippine flags fly from a boat with green islands on the horizon.",
                "ko": "초록 섬이 보이는 바다 위 보트에 휘날리는 한국 국기와 필리핀 국기."},
    },
    "yacht-salon": {
        "src": (NOV10, "Refined Underwater Travel Photograph-19.png"),
        "kind": "business", "focus": "50% 55%", "cats": [],
        "alt": {"en": "The yacht's saloon with a galley, sofa seating and a dining table.",
                "ko": "주방, 소파, 식탁이 있는 요트 살롱."},
    },
    "fd-standing": {
        "src": (NOV10, "Natural underwater diving scene-16.png"),
        "kind": "business", "focus": "50% 62%", "cats": [],
        "alt": {"en": "A freediver stands on an underwater rock beneath rays of sunlight.",
                "ko": "햇살 아래 수중 바위 위에 선 프리다이버."},
    },
    "calauit-feeding": {
        "src": (NOV10, "Natural underwater travel scene-10.png"),
        "kind": "business", "focus": "50% 45%", "cats": ["islands"],
        "alt": {"en": "A guest reaches toward a giraffe at Calauit Safari Park on Busuanga.",
                "ko": "부수앙가 칼라위트 사파리 파크에서 기린에게 손을 뻗는 손님."},
    },
    "jungle-crew": {
        "src": (NOV, "Four divers posing aboard a boat-3.png"),
        "kind": "business", "focus": "50% 40%", "cats": ["moments"],
        "alt": {"en": "Four divers smile on a boat deck during the Law of the Jungle filming in Coron.",
                "ko": "코론에서 진행된 정글의 법칙 촬영 중 보트 갑판에서 웃고 있는 네 명의 다이버."},
    },
    "film-crew-3": {
        "src": (NOV, "Two Men Posing in a Warm Restaurant-2.png"),
        "kind": "business", "focus": "50% 35%", "cats": [],
        "alt": {"en": "Two men smile together in a restaurant in Coron.",
                "ko": "코론의 한 식당에서 함께 웃고 있는 두 사람."},
    },
    "film-crew": {
        "src": (NOV, "Outdoor Group Portrait with Straw Hat-5.png"),
        "kind": "business", "focus": "50% 100%", "cats": ["moments"],
        "alt": {"en": "A group portrait taken during W Divers' support for the film The Golden Holiday in Coron.",
                "ko": "코론에서 영화 '국제수사' 촬영을 지원할 때 찍은 단체 사진."},
    },
    "film-crew-2": {
        "src": (NOV, "Refined outdoor group portrait-1.png"),
        "kind": "business", "focus": "50% 35%", "cats": [],
        "alt": {"en": "Guests and the W Divers team pose together outdoors in Coron.",
                "ko": "코론 야외에서 게스트와 W Divers 팀이 함께 포즈를 취하고 있습니다."},
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
    "stock-fins": {
        "src": (PEX, "pexels-mcphotographer-1139603240-26860915.jpg"),
        "kind": "stock", "focus": "50% 45%", "cats": [],
        "alt": {"en": "A pair of dive fins resting in clear shallow water.",
                "ko": "맑고 얕은 물속에 다이빙 핀 한 쌍이 놓여 있습니다."},
    },
    # Google downloads supplied by Lyneth; thematic only, no location claimed
    "island-aerial": {
        "src": (IMG, "Apo-Reef.jpg"),
        "kind": "stock", "focus": "50% 55%", "cats": ["islands"],
        "alt": {"en": "Aerial view of a white-sand beach and turquoise shallows beside a forested island.",
                "ko": "숲이 우거진 섬 옆으로 하얀 모래사장과 청록빛 얕은 바다가 펼쳐진 항공 사진입니다."},
    },
    "island-small": {
        "src": (IMG, "images (1).jpg"),
        "kind": "stock", "focus": "50% 55%", "cats": ["islands"],
        "alt": {"en": "A small green island ringed by white sand and clear blue water, seen from above.",
                "ko": "하얀 모래와 맑은 바다로 둘러싸인 작은 초록 섬을 위에서 본 모습입니다."},
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
