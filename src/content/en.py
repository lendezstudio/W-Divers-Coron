"""English content source. Copy follows the 25 October 2026 brief (Part 4)."""

LANG = "en"
LANG_NAME = "English"
SHORT = "EN"
OG_LOCALE = "en_US"

UI = {
    "skip": "Skip to content",
    "home": "Home",
    "nav_diving": "Diving",
    "nav_sites": "Dive Sites",
    "nav_plan": "Plan Your Trip",
    "nav_about": "About",
    "nav_contact": "Contact",
    "nav_faq": "FAQs",
    "sub_trips": "Dive Trips",
    "sub_wreck": "Wreck Diving",
    "sub_reef": "Reef Diving",
    "sub_first": "DSD (Discover Scuba Diving)",
    "sub_courses": "Scuba Courses",
    "sub_tdi": "TDI Advanced Diver Course",
    "sub_free": "Free Diving",
    "nav_pros": "Pro's",
    "nav_special": "Special Trips",
    "sub_special_all": "All Special Trips",
    "sub_island": "Island Hopping",
    "sub_guide": "Planning Guide",
    "sub_faq": "FAQs",
    "sub_gallery": "Gallery",
    "sub_journal": "Journal",
    "menu": "Menu",
    "close_menu": "Close menu",
    "primary_nav": "Main navigation",
    "lang_label": "Language",
    "lm_site": "Choose a language",
    "plan_cta": "Plan Your Dive",
    "whatsapp_cta": "Message on WhatsApp",
    "kakao_cta": "Message on KakaoTalk",
    "email_cta": "Email W Divers",
    "scroll": "Scroll",
    "section_nav": "Page sections",
    "social_label": "W Divers Coron on social media",
    "footer_desc": "Diving and island adventures in Coron, Palawan.",
    "footer_explore": "Explore",
    "footer_contact": "Get in touch",
    "footer_legal": "Information",
    "privacy": "Privacy",
    "booking_info": "Booking Information",
    "sitemap": "Sitemap",
    "rights": "All rights reserved.",
    "breadcrumb": "Breadcrumb",
    "new_tab": "(opens in a new tab)",
    "facebook": "Facebook",
    "instagram": "Instagram",
    "whatsapp": "WhatsApp",
    "email": "Email",
    "maps": "Google Maps",
    "naver": "Naver Blog",
    "kakao": "KakaoTalk",
    "kakao_kr": "Korean phone account",
    "kakao_ph": "Philippine phone account",
    "copy_id": "Copy ID",
    "copied": "Copied",
    "copy_failed": "Copy failed. Select the ID and copy it manually.",
    "kakao_help": "Open KakaoTalk, choose Add Friend, then search by ID and paste the ID you copied.",
    "related": "Keep planning",
    "lb_close": "Close",
    "lb_prev": "Previous image",
    "lb_next": "Next image",
    "lb_label": "Image viewer",
    "video_fallback": "Your browser cannot play this video.",
    "sites_filter": "Filter dive sites",
    "filter_all": "All Sites",
    "filter_wreck": "Wrecks",
    "filter_lake": "Lakes & Caves",
    "filter_reef": "Reefs & Other Sites",
    "type_wreck": "Wreck",
    "type_lake": "Lake & Cave",
    "type_reef": "Reef",
    "video_caption": "A dugong glides past divers. Wildlife encounters are never guaranteed.",
    "reviewed_value": "November 2026",
    "reviewed": "Guide last reviewed",
    "read_guide": "Read the site guide",
    "read_article": "Read the article",
    "read_trip": "See the trip",
    "slides_label": "Highlights from W Divers Coron",
    "slide_n": "Slide {n} of {total}",
    "slide_show": "Show slide {n}",
    "slide_pause": "Pause the slideshow",
    "slide_play": "Play the slideshow",
}

ROUTE_NAMES = {
    "home": "Home", "diving": "Diving", "wreck": "Wreck Diving", "reef": "Reef Diving",
    "first": "DSD (Discover Scuba Diving)", "courses": "Scuba Courses", "sites": "Dive Sites",
    "tdi": "TDI Advanced Diver Course", "freediving": "Free Diving", "pros": "Pro's", "special": "Special Trips",
    "island": "Island Hopping", "plan": "Plan Your Trip", "about": "About", "gallery": "Gallery",
    "faq": "FAQs", "journal": "Journal", "contact": "Contact", "privacy": "Privacy",
    "booking": "Booking Information", "sitemap": "Sitemap",
}

PAGES = {}

PAGES["home"] = {
    "title": "W Divers Coron | Wreck and Reef Diving in Coron, Palawan",
    "meta": "Explore wreck diving, reef diving and island-hopping options in Coron, Palawan, then share your dates and experience with W Divers Coron to start planning.",
    "eyebrow": "Coron, Palawan · Since 2015",
    "h1": "Dive the wrecks of Coron.",
    "support": "Wrecks. Reefs. A different perspective.",
    "body": "Explore diving and island-hopping options with W Divers Coron. Share your dates and experience, and start planning your time on the water.",
    "trust": ["PADI · SSI · TDI instructors", "English and Korean", "Open daily, 7:00 to 21:00"],
    "secondary": "Explore the Dive Sites",
    "rail": ["Top", "Choose your route", "Wrecks and reefs", "Dive sites", "Planning", "Contact"],
    "choose_h": "Start with your kind of adventure.",
    "routes": [
        {"k": "Certified divers", "t": "Here for the wrecks, the reefs, or a little of both? Explore the options and share your certification and recent diving experience when you inquire.", "link": "Explore Dive Trips", "to": "diving"},
        {"k": "Discover Scuba Diving (DSD)", "t": "Never dived before? DSD is a supervised first taste of scuba with an instructor beside you. Ask which options suit your dates.", "link": "About DSD", "to": "first"},
        {"k": "Training", "t": "Scuba courses from your first certification to professional levels, plus TDI training for advanced wreck and technical divers.", "link": "See Scuba Courses", "to": "courses"},
        {"k": "Beyond diving", "t": "Looking for time above the surface too? Ask about island-hopping arrangements for your Coron stay.", "link": "Explore Island Hopping", "to": "island"},
    ],
    "feature_h": "The wrecks brought you here. The details help you plan.",
    "feature_t": "Learn about Coron's underwater destinations, then talk with W Divers about a plan that fits your experience. Site selection depends on conditions, your training and the arrangements available for your dates.",
    "feature_link": "Discover Coron's Dive Sites",
    "feature_wreck": "Wreck Diving",
    "feature_reef": "Reef Diving",
    "sites_h": "A few names you may already know.",
    "sites_t": "Short introductions to some of Coron's best-known wrecks. Each guide explains what to ask before you plan a visit.",
    "sites_all": "See the full dive-site directory",
    "plan_h": "Less guesswork before you arrive.",
    "plan_t": "From equipment questions to travel dates, a few details make the next conversation easier. Our planning guide helps you decide what to ask before confirming your trip.",
    "plan_link": "Plan Your Coron Trip",
    "plan_items": [
        {"t": "What's in a quotation", "to": "booking"},
        {"t": "Diving and flying", "to": "plan", "hash": "flying"},
        {"t": "Common questions", "to": "faq"},
    ],
    "moment_caption": "A day on the water with W Divers Coron guests.",
    "contact_h": "Have your dates in mind?",
    "contact_t": "Send your travel dates, group size and diving experience. If you're still deciding, tell us what you'd like to do.",
    "contact_btn": "Start a Dive Inquiry",
    "hero_more": [{"k": "Behind the camera", "h": "The crew behind the crew.", "s": "Dive and filming support for film and television in Coron."}, {"k": "Special trips", "h": "Further out, quieter waters.", "s": "Island hopping, Apo Reef and overnight trips beyond the usual routes."}, {"k": "Below the surface", "h": "Wrecks from 1944, a short boat ride away.", "s": "Reef dives and freediving too, planned around your level."}, {"k": "About W Divers", "h": "Your day on the water starts here.", "s": "PADI, SSI and TDI instructors. English and Korean spoken."}],
    "hero_ocean": [{"h": "Dive Coron's legendary wrecks.", "s": "Korean-run since 2015, with PADI, SSI and TDI instructors."}, {"k": "On set in Coron", "h": "Trusted by film and TV crews.", "s": "Dive support for SBS Law of the Jungle and the movie The Golden Holiday."}, {"k": "Special trips", "h": "Hidden lagoons and island escapes.", "s": "Island hopping, Apo Reef and overnight trips arranged by our team."}, {"k": "Wreck diving", "h": "Explore wrecks from 1944.", "s": "Wrecks, reefs and freediving, planned around your level."}, {"k": "Your dive boat", "h": "Gear up. Your boat is waiting.", "s": "Share your dates and experience, and we'll plan your days on the water."}],
    "boats_h": "Our dive boats.",
    "boats_t": "Traditional bangka dive boats with outriggers, run by the W Divers crew.",
    "boats": [{"img": "boat-1", "name": "W Divers Diving Boat 1", "tag": "Bangka dive boat"}, {"img": "boat-2", "name": "W Divers Diving Boat 2", "tag": "Bangka dive boat"}, {"img": "boat-3", "name": "W Divers Diving Boat 3", "tag": "Bangka dive boat"}, {"img": "boat-kwreck", "name": "K-WRECK", "tag": "Renovated dive boat"}],
    "slides": [
        ("Filming support for the movie \"The Golden Holiday\" (국제수사)\nFilming location: Teru Kaze Maru", "Meet our Pro's"),
        ("Filming support: SBS Law of the Jungle in Coron", "Meet our Pro's"),
        ("Lagoons, limestone cliffs and our boat", "Special Trips"),
        ("Wreck and reef diving around Coron", "Diving"),
        ("The W Divers Coron dive boat", "About us"),
    ],
    "slide_tabs": ["The Golden Holiday", "Law of the Jungle", "Lagoons", "Wrecks and reefs", "Our dive boat"],
    "special_h": "Special trips from Coron.",
    "special_t": "Longer days and overnight adventures, arranged by the W Divers team on selected dates.",
    "special_all": "See all special trips",
}

PAGES["diving"] = {
    "title": "Diving in Coron | Dive Trips with W Divers Coron",
    "meta": "Choose a starting point for diving in Coron: wreck diving, reef diving, a first scuba experience or training. Then ask W Divers Coron about your dates.",
    "eyebrow": "Diving with W Divers Coron",
    "h1": "Find your way into Coron's underwater world.",
    "intro": "A wreck-focused visit, a day around the reefs, or a first introduction to scuba: start with the experience you're looking for.",
    "chooser_h": "Where are you in your diving journey?",
    "chooser": [
        {"t": "I'm a certified diver", "to": "wreck"},
        {"t": "I'm new to scuba", "to": "first"},
        {"t": "I'm interested in training", "to": "courses"},
        {"t": "I'm planning for a group", "to": "contact", "interest": "unsure"},
    ],
    "big": [
        {"h": "Explore Coron's wrecks.", "t": "Discover the destination's historic underwater structures and talk through suitable diving options for your certification and experience.", "btn": "Wreck Diving", "to": "wreck", "img": "wreck-mast"},
        {"h": "Take a different route below the surface.", "t": "Explore the reef side of Coron and ask about trips that suit your interests and travel dates.", "btn": "Reef Diving", "to": "reef", "img": "stock-reef-snake"},
    ],
    "small": [
        {"h": "Begin with a conversation, then the basics.", "t": "Find out what an introductory scuba experience involves before deciding on your next step.", "btn": "First-Time Divers", "to": "first"},
        {"h": "Build skills for the diving you want to do.", "t": "Share your current level and goals, and ask about suitable training and instructor availability.", "btn": "Courses & Training", "to": "courses"},
        {"h": "Spend some time above the surface.", "t": "Ask about island-hopping arrangements for your group, including anyone who prefers to stay dry.", "btn": "Island Hopping", "to": "island"},
    ],
    "practical_h": "What should you confirm before booking?",
    "practical": ["Number of dives and approximate day length", "Suitable sites", "Equipment and rental charges", "Boat arrangements", "Meals and transfers", "Park or entrance fees", "Total price and booking terms"],
    "practical_close": "These details vary by arrangement. Ask for a clear quotation for your dates.",
    "cta": "Ask About a Dive Trip",
}

PAGES["wreck"] = {
    "inline_more": [[1, "c-irako-wheel"]],
    "title": "Wreck Diving in Coron | W Divers Coron",
    "meta": "Plan wreck diving in Coron around your certification and recent experience. Know what to share and what to confirm before you book with W Divers Coron.",
    "eyebrow": "Wreck diving",
    "h1": "Dive into Coron's underwater history.",
    "intro": "Coron's wrecks give the destination a character of its own. Explore the possibilities, then discuss a dive plan that fits your training, recent experience and comfort in the water.",
    "img": "wreck-bow",
    "summary": {
        "h": "Before you inquire",
        "for": "For certified divers.",
        "list": ["Certification level", "Approximate logged dives", "Date of your last dive", "Preferred dates", "Any wreck or deep-diving training"],
    },
    "sections": [
        {"h": "A site name is only the beginning.", "p": ["Different parts of a wreck can involve different depths and conditions. Seeing a wreck from the outside and entering an overhead environment are different activities. A guided trip does not replace the training required for penetration diving."]},
        {"h": "Help us understand your experience.", "p": ["Include your certification level, approximate logged dives, date of your last dive and preferred dates. Mention any relevant wreck or deep-diving training."]},
        {"h": "Confirm the details of your day.", "p": ["Ask which sites may suit you, how many dives are planned, and what is included in the quotation. Final site choices depend on conditions and the team's assessment."]},
    ],
    "inline_img": "w-three-divers",
    "cta": "Plan a Wreck-Diving Trip",
    "interest": "wreck",
    "related": [("sites", None), ("article", "wreck-diving-questions-before-booking"), ("faq", None)],
}

PAGES["reef"] = {
    "inline_more": [[0, "dugong-diver"]],
    "title": "Reef Diving in Coron | W Divers Coron",
    "meta": "Ask W Divers Coron about reef-diving options in Coron and a day shaped around your interests, experience and travel dates.",
    "eyebrow": "Reef diving",
    "h1": "Make room for Coron's reef side.",
    "intro": "There's more to a diving visit than shipwrecks. Ask about reef-diving options and a day shaped around your interests and experience.",
    "img": "stock-reef-snake",
    "summary": {
        "h": "Before you inquire",
        "for": "For divers who want variety, a relaxed pace or time with a camera.",
        "list": ["Your certification and recent dives", "What you enjoy underwater", "Preferred dates", "Equipment you plan to bring or rent"],
    },
    "sections": [
        {"h": "Tell us what draws you underwater.", "p": ["Whether you prefer a relaxed pace, underwater photography or a varied itinerary, mention it when you inquire. Wildlife encounters and visibility are never guaranteed."]},
        {"h": "Bring your questions with you.", "p": ["Ask about suitable sites, likely conditions, equipment arrangements and how a reef trip can fit into the rest of your visit."]},
    ],
    "inline_video": "dugong",
    "cta": "Ask About Reef Diving",
    "interest": "reef",
    "related": [("diving", None), ("plan", None), ("gallery", None)],
}

PAGES["first"] = {
    "inline_more": [[2, "heart-divers"]],
    "title": "Discover Scuba Diving (DSD) in Coron | W Divers Coron",
    "meta": "Try scuba for the first time with Discover Scuba Diving (DSD) at W Divers Coron: a supervised introduction with an instructor, no certification needed.",
    "eyebrow": "DSD · Discover Scuba Diving",
    "h1": "Your first breath underwater, with an instructor beside you.",
    "intro": "Discover Scuba Diving (DSD) is a supervised first taste of scuba for people who have never dived. Tell W Divers you're new to scuba, and ask which DSD options suit your dates.",
    "img": "dsd-sand",
    "summary": {
        "h": "Questions worth asking",
        "for": "For people who have never tried scuba, or tried it long ago.",
        "list": ["Minimum age and who can join", "Swimming or water-comfort expectations", "The medical questionnaire", "Where the session takes place", "How long it lasts and the total price"],
    },
    "sections": [
        {"h": "What a DSD involves.", "p": ["A Discover Scuba Diving session starts with a short briefing on the equipment and how to breathe underwater. You then practise a few basic skills in calm, shallow water before a guided dive with an instructor close by. No certification or previous experience is needed."]},
        {"h": "An introduction, not a certification.", "p": ["DSD lets you try scuba without committing to a course. If you enjoy it, ask how a scuba course could follow. The two are different steps, so ask which is right for your trip."]},
        {"h": "Before you book.", "p": ["Confirm the minimum age, swimming or water-comfort expectations, the medical questionnaire, where the session takes place, how long it lasts and what the price includes. Mention any health concerns to the team before your dive; an inquiry form is not a medical clearance."]},
        {"h": "No need to pretend you're confident already.", "p": ["It's fine to have questions about breathing underwater, equipment or being in the sea. Describe what you're comfortable with so the conversation starts in the right place."]},
    ],
    "inline_img": "pool-lesson",
    "cta": "Ask About DSD",
    "interest": "first",
    "related": [("courses", None), ("faq", None), ("article", "planning-your-first-coron-dive-trip")],
}

PAGES["courses"] = {
    "inline_more": [[1, "under-boat"]],
    "title": "Scuba Courses in Coron | W Divers Coron",
    "meta": "Learn to dive or keep progressing in Coron: scuba courses from beginner to professional levels with W Divers Coron's PADI and SSI instructors.",
    "eyebrow": "Scuba courses",
    "h1": "Learn to dive, then keep going.",
    "intro": "From your first certification to professional levels, W Divers Coron's instructors teach scuba courses with PADI and SSI. Share your experience, the course you're interested in and how much time you have in Coron.",
    "img": "pool-pair",
    "summary": {
        "h": "Courses to ask about",
        "for": "Taught by our PADI and SSI instructors:",
        "list": ["Open Water Diver", "Advanced Open Water Diver", "Rescue Diver and Emergency First Response", "Divemaster", "Specialties: Deep, Enriched Air (Nitrox), Sidemount, Wreck, Peak Performance Buoyancy", "AWARE Coral Reef Conservation"],
    },
    "sections": [
        {"h": "Start diving.", "p": ["If you're considering your first certification, ask about the course, prerequisites, study requirements and the days needed before you plan the rest of your stay."]},
        {"h": "Keep progressing.", "p": ["Already certified? Advanced and Rescue courses build confidence and skill, and specialties let you focus on what interests you, from deep diving and nitrox to wrecks and buoyancy."]},
        {"h": "Interested in wreck training?", "p": ["A wreck specialty teaches you to dive around wrecks safely; it is not general permission to go inside them. For advanced wreck and technical training, see our TDI Advanced Diver Course."]},
        {"h": "Get the whole course picture.", "p": ["Before confirming, ask for the agency, course name, eligibility, expected duration, training components, instructor availability and the total cost including any materials or certification fees."]},
    ],
    "inline_img": "surface-group",
    "catalog_h": "Current courses",
    "cta": "Ask About Scuba Courses",
    "interest": "courses",
    "related": [("tdi", None), ("first", None), ("faq", None)],
}

PAGES["tdi"] = {
    "inline_more": [[1, "c-irako-engine"]],
    "title": "TDI Advanced Diver Course in Coron | W Divers Coron",
    "meta": "Advanced and technical diver training in Coron with W Divers Coron's TDI instructors, including advanced wreck training for Coron's wrecks.",
    "eyebrow": "TDI advanced training",
    "h1": "Train for Coron's wrecks beyond recreational limits.",
    "intro": "Coron's wrecks draw divers who want to go further. W Divers Coron has TDI instructors, including a TDI Technical and Advanced Wreck Diver instructor, for divers ready to train beyond recreational diving.",
    "img": "wreck-mast",
    "summary": {
        "h": "Before you inquire",
        "for": "For experienced, certified divers.",
        "list": ["Your current certification and logged dives", "Nitrox or deep-diving experience", "The TDI course you're interested in", "How many days you have in Coron", "Whether you own technical or sidemount equipment"],
    },
    "sections": [
        {"h": "What TDI training is.", "p": ["TDI (Technical Diving International) teaches advanced and technical diving: longer, deeper and more complex dives that need extra training, equipment and planning. Coron's sheltered wrecks make it a popular place to learn."]},
        {"h": "Advanced wreck training.", "p": ["Entering a wreck safely is a skill of its own. Advanced wreck training covers dive planning, guideline use, gas management and moving through overhead environments: the training a guided dive cannot replace."]},
        {"h": "Find the right course.", "p": ["Prerequisites, durations and equipment differ between TDI programs. Tell the team about your experience and goals, and ask which TDI courses are available, what each qualifies you to do and the total cost."]},
    ],
    "inline_img": "w-engine-room",
    "cta": "Ask About TDI Training",
    "interest": "tdi",
    "related": [("courses", None), ("wreck", None), ("sites", None)],
}

PAGES["freediving"] = {
    "inline_more": [[1, "c-fd-lake"]],
    "title": "Free Diving in Coron | W Divers Coron",
    "meta": "Freediving in Coron with W Divers Coron: Barracuda Lake, Cathedral Cave and other clear, sheltered spots on a single breath.",
    "eyebrow": "Free diving",
    "h1": "Coron on a single breath.",
    "intro": "Clear lakes, limestone cliffs and calm, sheltered water make Coron a favourite with freedivers. W Divers Coron runs freediving tours to spots such as Barracuda Lake and Cathedral Cave.",
    "img": "c-fd-reef",
    "summary": {
        "h": "Before you inquire",
        "for": "For freedivers and confident snorkellers.",
        "list": ["Your freediving experience or certification", "The spots you'd like to visit", "Preferred dates", "Whether you need equipment"],
    },
    "sections": [
        {"h": "Why freedivers love Coron.", "p": ["Barracuda Lake, set between limestone walls, is known for its clear water and changing layers of temperature. Cathedral Cave and other sheltered spots offer calm water and dramatic light. Conditions and access can change, so ask what's possible for your dates."]},
        {"h": "Tours and training.", "p": ["Ask the team about freediving tours and whether a course is available for your level. Freediving should always be done with a trained buddy watching from the surface."]},
        {"h": "Plan your day.", "p": ["Tell the team about your experience, the spots you'd like to visit and how much time you have. Ask what's included, such as the boat, equipment and entrance fees."]},
    ],
    "inline_img": "c-fd-sand",
    "cta": "Ask About Free Diving",
    "interest": "freediving",
    "related": [("special", None), ("island", None), ("gallery", None)],
}

PAGES["special"] = {
    "title": "Special Trips from Coron | W Divers Coron",
    "meta": "Special trips with W Divers Coron: an Apo Reef yacht liveaboard, dugong watching, a deserted-island overnight and the Kyokuzan Maru wreck day trip.",
    "eyebrow": "Special trips",
    "h1": "Bigger days out from Coron.",
    "intro": "Some experiences need an early start, a longer boat ride or a night away. The W Divers team runs these special trips on selected dates; ask what's planned during your stay.",
    "img": "lagoon-boats",
    "note": "Dates, inclusions and prices vary by departure. Ask the team for upcoming trips.",
}

PAGES["trip"] = {
    "eyebrow": "Special trip",
    "glance_h": "At a glance",
    "ask_h": "Ask before you book",
    "others_h": "Other special trips",
    "cta": "Ask About {name}",
    "cta_note": "An inquiry does not reserve a place.",
}

PAGES["pros"] = {
    "title": "Pro's: Meet Team W Divers | W Divers Coron",
    "meta": "Meet Team W Divers Pro's in Coron, Palawan: head instructor Dean Kang, instructor Inhan Kang and divemaster Jex Lenver Tabat.",
    "eyebrow": "Team W Divers Pro's",
    "h1": "Meet the people you'll dive with.",
    "intro": "Shipwrecks, dugongs, hot springs and magnificent caves: an invitation to dive into the waters of Coron. Meet the instructors of Team W Divers.",
    "img": "dive-boat",
    "team_h": "Team W Divers",
    "team": [
        {"name": "Dean Kang", "role": "Head Instructor", "initials": "DK", "img": "dean", "zoom": 1.9,
         "intro": "Dean leads W Divers Coron and trains both divers and instructors, with instructor ratings across five agencies.",
         "creds_h": "Instructor ratings",
         "creds": ["SSI Instructor Trainer #112373", "PADI Master Scuba Diver Trainer (MSDT) #370544", "SDI Instructor #25307", "TDI Instructor #25307", "IDEA Instructor #K00419"],
         "spec_h": "Specialty instructor",
         "spec": ["Deep", "Enriched Air", "Sidemount", "Equipment Specialist", "Project AWARE", "Peak Performance Buoyancy", "Wreck", "AWARE Coral Reef Conservation", "EFR / Care for Children with AED", "Snorkel"]},
        {"name": "Inhan Kang", "role": "Rookie Instructor", "initials": "IK", "img": "inhan", "zoom": 1.35,
         "tag": "Teaches in native-level English, Tagalog and Korean",
         "intro": "Inhan qualified as a PADI Instructor at 18 and teaches recreational, technical and wreck courses.",
         "creds_h": "Instructor ratings",
         "creds": ["PADI Instructor", "SDI Instructor", "TDI Technical Instructor", "TDI Advanced Wreck Diver Instructor"]},
        {"name": "Jex Lenver Tabat", "nick": "GIGs", "role": "Divemaster", "initials": "JT", "img": "jex", "zoom": 1.35,
         "intro": "A Filipino divemaster on the W Divers team, guiding divers on the boat and underwater.",
         "creds_h": "Certification",
         "creds": ["SSI Divemaster"]},
        {"name": "Gunan Kang", "role": "Consultant & Interpreter", "initials": "GK", "img": "gunan", "zoom": 1.35,
         "tag": "Interprets in native-level English and Tagalog",
         "intro": "Gunan helps guests plan their time in Coron, interprets during briefings and trips, and designs W Divers' promotions and videos.",
         "creds_h": "Responsibilities",
         "creds": ["Interpreting: English and Tagalog", "Guest consulting", "Promotion design", "Video editing"]},
    ],
    "screen_h": "On screen in Coron.",
    "screen_t": "The W Divers team has supported Korean film and TV productions shooting in Coron.",
    "screen": [
        {"img": "jungle-crew", "cap": "Supporting SBS Law of the Jungle in Coron, including episodes searching for dugongs and a mystery wreck."},
        {"img": "film-crew", "cap": "With Korean actors while supporting the filming of the Korean film The Golden Holiday (국제수사) in Coron."},
    ],
    "cta_h": "Dive with Team W Divers.",
    "cta_t": "Send your dates, group size and diving experience, and the team will help plan your time in Coron.",
}

PAGES["sites"] = {
    "title": "Coron Dive Sites | Wreck Guides from W Divers Coron",
    "meta": "Introductions to Coron dive sites including Okikawa Maru, Akitsushima, Olympia Maru and Kogyo Maru, with questions to ask before planning a visit.",
    "eyebrow": "Coron dive-site guide",
    "h1": "Get to know Coron below the surface.",
    "intro": "Start exploring the region's wreck and reef environments. These guides introduce the destination; they are not a promise that every location is included in a W Divers itinerary.",
    "img": "stock-descent",
    "img_note": "Photos show general underwater scenes, not the specific sites.",
    "reef_note_h": "Looking for reefs?",
    "reef_note_t": "Reef guides will be added as sites are confirmed. In the meantime, ask W Divers about reef options for your dates.",
    "reef_note_link": "Reef Diving",
}

PAGES["site"] = {
    "eyebrow": "Coron dive-site guide",
    "distinct_h": "What makes this site distinctive.",
    "fit_h": "Is it right for your trip?",
    "fit_t": "Suitability depends on the planned depth, conditions, your certification, recent experience and the specific route. Ask W Divers whether this site is a suitable option for your dates.",
    "ask_h": "What to ask before you go.",
    "ask": ["Is a visit currently available?", "What experience is required?", "Which part of the site is planned?", "What equipment and fees apply?"],
    "cta": "Ask About {name}",
    "cta_note": "A site inquiry is not a confirmed itinerary.",
    "other_h": "Other site guides",
    "img_note": "Photo: general underwater scene, not this specific site.",
    "facts_h": "Site facts",
    "facts_l": {"kind": "Type", "length": "Length", "depth": "Depth", "vis": "Visibility", "lie": "Position"},
    "lie": {"upright": "Upright", "capsized": "On its side", "starboard": "Listing to starboard", "port": "Heeled to port", "forward": "Tilted forward"},
    "facts_src": "Figures from W Divers Coron's own site briefings.",
    "title_tpl": "{name} | Coron Dive Sites | W Divers Coron",
}

PAGES["island"] = {
    "inline_more": [[1, "boat-lunch"]],
    "title": "Island Hopping in Coron | W Divers Coron",
    "meta": "Ask W Divers Coron about island-hopping arrangements in Coron for your group, including divers and non-divers travelling together.",
    "eyebrow": "Island hopping",
    "h1": "See another side of Coron.",
    "intro": "Give your visit some time above the surface. Ask W Divers about island-hopping arrangements and the options available for your group.",
    "img": "island-aerial",
    "summary": {
        "h": "Ask for the arrangements",
        "for": "Confirm before you go:",
        "list": ["Route", "Boat arrangements", "Duration", "Inclusions", "Entrance fees", "Weather or access changes"],
    },
    "sections": [
        {"h": "Start with your kind of day.", "p": ["Tell us your dates, number of guests and what you'd like to experience. Mention whether anyone in the group prefers to stay out of the water."]},
        {"h": "Know the arrangements before you confirm.", "p": ["Ask for the route, boat arrangements, duration, inclusions, entrance fees and any changes that may depend on weather or local access."]},
        {"h": "Traveling with divers and non-divers?", "p": ["Mention everyone's interests when you inquire. The team can clarify whether a shared plan or separate activities make more sense."]},
    ],
    "inline_img": "flag-boat",
    "cta": "Ask About Island Hopping",
    "interest": "island",
    "related": [("article", "divers-and-non-divers-in-one-coron-trip"), ("plan", None), ("gallery", None)],
}

PAGES["plan"] = {
    "title": "Plan Your Coron Diving Trip | W Divers Coron",
    "meta": "Practical planning for a Coron diving trip: what to send before you arrive, what to pack, weather changes, flying after diving and caring for the marine environment.",
    "eyebrow": "Planning guide",
    "h1": "A little planning makes more room for the experience.",
    "intro": "Bring your dates and questions together before confirming your Coron diving trip.",
    "img": "stock-mask",
    "steps": [
        {"id": "before", "h": "Before you arrive.", "p": "Contact the team with your travel dates, group size and diving background. Keep your certification and recent dive information available if you're booking certified-diver activities."},
        {"id": "meeting", "h": "Know where your day starts.", "p": "Confirm the meeting point and time directly with W Divers. Ask whether transfers are part of your arrangement before relying on hotel pickup."},
        {"id": "packing", "h": "Pack for a day around the water.", "p": "Bring personal essentials such as swimwear, a towel, sun protection, drinking water and a dry bag. Confirm supplied items and any equipment you plan to bring or rent."},
        {"id": "conditions", "h": "Conditions can change the plan.", "p": "Sea conditions, weather and local access can affect the day's arrangements. Confirm how changes are handled before paying for your trip."},
        {"id": "flying", "h": "Leave space between diving and flying.", "p": "Tell the team about your onward travel before arranging dives. Flying after diving requires an appropriate surface interval; follow current guidance from your dive professional, your training and your dive computer. Read DAN's flying-after-diving guidance for general background.", "link": "DAN: Flying after diving"},
        {"id": "care", "h": "Keep Coron worth coming back to.", "p": "Follow your guide's instructions, maintain appropriate buoyancy, leave wrecks and marine life undisturbed, and take your waste back with you."},
    ],
    "cta": "Talk Through Your Trip",
    "interest": "unsure",
}

PAGES["about"] = {
    "title": "About W Divers Coron | Diving in Coron, Palawan",
    "meta": "W Divers Coron is based in Coron, Palawan. Explore wreck diving, reef diving and island-hopping options, then get in touch about the trip you want to arrange.",
    "eyebrow": "About W Divers Coron",
    "h1": "A Korean-run dive centre in Coron, since 2015.",
    "intro": "Wrecks, dugongs, hot springs and caves. W Divers Coron has guided divers through the waters of Coron, Palawan since March 2015, from first breaths to wreck penetration.",
    "img": "c-kwreck",
    "story_k": "Our story",
    "story_h": "From a shipyard in Korea to the wrecks of Coron.",
    "story_t": ["My name is Dean Kang (강덕환). For 20 years I built ships at Hyundai Samho Heavy Industries in Korea. By day I worked in the shipyard; whenever I could, I went diving. I became president of the company's scuba diving club, and somewhere along the way the sea became more than a hobby.", "When I left the shipyard, I already knew where my second chapter would begin: Coron, Palawan, home to some of the best wreck diving in the world. On 1 March 2015 I opened W Divers on the town's main street. The people close to me worried, because I hadn't first spent years in the local Korean community. It wasn't easy, but good people in Coron helped me settle in, and I'm still grateful to them today."],
    "facts_h": "What's ready when you arrive",
    "facts": [
        ("Shop", "An air-conditioned, glass-fronted dive shop on Coron's main street."),
        ("Boats", "Two of our own dive bancas, plus a clean, air-conditioned multicab for transfers."),
        ("Equipment", "Rental equipment bought new. Dive computers, scooters, nitrox and oxygen are available."),
        ("Stay", "Five air-conditioned rooms of our own, and help booking fan rooms, Korean resorts or hotel-style resorts with pools."),
        ("Hours", "Open every day, 7:00 am to 9:00 pm."),
        ("Languages", "Guidance in English and Korean."),
    ],
    "wreck_h": "Wreck diving, with a stamp to remember it.",
    "wreck_t": "Coron's wrecks are a training ground for technical divers learning penetration, yet many also let recreational divers safely look inside. Our guides have long wreck-diving experience, and each wreck has its own stamp for your logbook once you've dived it. Beyond the wrecks there's Barracuda Lake and Cathedral Cave, where warm water rises from hot springs, and reefs for easy fun dives.",
    "screen_k": "On screen",
    "screen_h": "Dugong and shipwreck guide for SBS Law of the Jungle.",
    "screen_t": "From 21 to 23 January 2020, W Divers supported the filming of SBS's Law of the Jungle in Coron. SSI Instructor Trainer Dean Kang worked as the show's dugong guide and shipwreck penetration guide.",
    "screen_link": "Meet our Pro's",
    "source": "Sources: the W Divers Coron profile on SSI and the W Divers Naver blog.",
    "s1_h": "A destination with more than one way to explore.",
    "s1_t": "Some visitors arrive with a wreck on their wish list. Others are considering their first scuba experience or planning a day on the water with friends. Start with your interests, then ask the team about the options for your visit.",
    "s2_h": "Get to know W Divers.",
    "s2_t": "Find recent updates through our social channels, browse our photographs, or message us directly with your plans.",
    "contact_link": "Contact W Divers",
    "gallery_link": "Browse the gallery",
    "lang_h": "Languages",
    "lang_t": "This website is available in English, Korean, Chinese, Japanese, Spanish, French, German, Italian, Russian, Vietnamese, Thai, Indonesian and Arabic. You can contact W Divers through WhatsApp, KakaoTalk, email or social media. Ask the team which language is available for your activity and briefing.",
}

PAGES["gallery"] = {
    "title": "Gallery | Underwater and Island Photos from Coron | W Divers Coron",
    "meta": "Underwater scenes, island views and moments from W Divers Coron. Browse photos and video, then start planning your own visit.",
    "eyebrow": "Gallery",
    "h1": "A closer look at life around the water.",
    "intro": "Explore underwater scenes and island views, then start imagining your time in Coron.",
    "img": "stock-clownfish",
    "insta": "See More on Instagram",
    "fb": "See More on Facebook",
    "nav_label": "Gallery sections",
    "sections": {
        "underwater": ("Underwater", "Reefs, wrecks and the life around them."),
        "video": ("On video", "A few quiet seconds with a dugong."),
        "islands": ("Above the surface", "Island views and days on the water."),
        "moments": ("W Divers moments", "Guests, the shop and time on the boat."),
    },
    "video_link": "Explore reef diving",
    "cta": "Plan Your Own Visit",
}

PAGES["faq"] = {
    "title": "FAQs | Diving in Coron with W Divers Coron",
    "meta": "Answers to common questions about diving in Coron with W Divers: first dives, certification, wreck penetration, equipment, pricing, weather and how to arrange a trip.",
    "eyebrow": "Frequently asked questions",
    "h1": "Questions before you get in the water?",
    "intro": "Start here, then contact W Divers for the details of your own trip.",
    "groups": [
        {"h": "Experience and suitability", "items": [
            ("first", "Can I inquire if I've never tried scuba diving?", "Yes. Let the team know you're a first-time diver and ask about introductory options, eligibility and the arrangements available for your dates."),
            ("certification", "Do I need a certification for a dive trip?", "Certified-diver trips and introductory experiences have different requirements. State your current level when you inquire so the team can discuss suitable options."),
            ("penetration", "Can every diver enter a shipwreck?", "No. Diving around a wreck and entering an overhead environment involve different requirements. Appropriate training, equipment, experience and conditions matter; a guide does not replace the required training."),
            ("recent", "What if I haven't dived recently?", "Tell the team when you last dived and describe your experience. Ask whether refresher training or another assessment is appropriate before joining a trip."),
        ]},
        {"h": "Prices and arrangements", "items": [
            ("equipment", "Is equipment included?", "Ask for an itemized quotation for your chosen arrangement, including any equipment rental and additional charges."),
            ("cost", "How much does diving cost?", "Contact W Divers with your dates, group size and interests for current pricing. Confirm the number of dives, equipment, fees and other inclusions before booking."),
            ("sites", "Are specific dive sites guaranteed?", "Request the sites you're interested in, but final plans depend on suitability, conditions, access and the arrangements confirmed with the team."),
            ("non-divers", "Can non-divers join?", "Mention non-divers in your inquiry and ask which options are available. Participation and boat arrangements should be confirmed for the specific activity."),
            ("weather", "What happens if the weather changes?", "Ask for the applicable weather, rescheduling and cancellation terms before confirming or paying for a trip."),
        ]},
        {"h": "Contact and language", "items": [
            ("language", "Can I read the website in another language?", "Use the language menu. Website translations help you browse; ask the team to confirm the language available for your activity and briefing."),
            ("arrange", "How do I arrange a trip?", "Send your preferred dates, group size, activity interests and diving background through WhatsApp, email or another listed contact channel. Your trip is confirmed only when W Divers explicitly confirms the arrangements."),
        ]},
    ],
    "cta_h": "Still have a question?",
    "cta": "Ask W Divers",
}

PAGES["journal"] = {
    "title": "Journal | Coron Diving Planning Articles | W Divers Coron",
    "meta": "Practical articles for planning a Coron diving trip: first trips, wreck-diving questions and travelling as a mixed group of divers and non-divers.",
    "eyebrow": "Journal",
    "h1": "Notes for planning time underwater.",
    "intro": "Practical reading for the decisions that come before a Coron diving trip.",
    "img": "stock-descent",
}

PAGES["contact"] = {
    "title": "Contact W Divers Coron | Plan Your Dive",
    "meta": "Contact W Divers Coron on WhatsApp, KakaoTalk, email or social media. Put your dates, group size and experience together and start planning your Coron dive.",
    "eyebrow": "Contact",
    "h1": "Let's plan your time in Coron.",
    "intro": "Tell us when you're visiting and what you'd like to do. If you're unsure where to start, share a little about your experience.",
    "form_h": "Put your trip details together.",
    "form_intro": "Fields marked required help the team reply. Everything else is optional.",
    "required": "required",
    "f_name": "Your name",
    "f_method": "Preferred contact method",
    "f_method_opts": [("whatsapp", "WhatsApp"), ("email", "Email"), ("kakao", "KakaoTalk"), ("instagram", "Instagram"), ("facebook", "Facebook Messenger")],
    "f_detail": "Your contact detail",
    "f_detail_hint": {
        "whatsapp": "Your WhatsApp number, including country code.",
        "email": "Your email address.",
        "kakao": "Your KakaoTalk ID.",
        "instagram": "Your Instagram username.",
        "facebook": "The name on your Facebook profile.",
    },
    "f_interest": "What are you interested in?",
    "f_interest_opts": [("wreck", "Wreck Diving"), ("reef", "Reef Diving"), ("first", "Discover Scuba Diving (DSD)"), ("courses", "Scuba Courses"), ("tdi", "TDI Advanced Training"), ("freediving", "Free Diving"), ("special", "Special Trips"), ("island", "Island Hopping"), ("unsure", "Not Sure Yet")],
    "f_choose": "Choose one",
    "f_message": "Your message",
    "f_message_hint": "What would you like to do, and is there anything the team should know?",
    "optional_h": "Helpful details",
    "f_dates": "Preferred date or date range",
    "f_dates_hint": "No confirmed dates yet? An approximate travel period is fine.",
    "f_guests": "Number of guests",
    "f_experience": "Certification or experience",
    "f_experience_hint": "For example: never dived, Open Water with 20 dives, Advanced.",
    "f_last": "Date of last dive",
    "f_last_hint": "Month and year is enough.",
    "f_lang": "Preferred communication language",
    "f_lang_opts": [("", "No preference"), ("English", "English"), ("Korean", "Korean (한국어)"), ("Other", "Other")],
    "privacy_micro": "We'll use the information you choose to send to respond to your inquiry.",
    "privacy_link": "Read our privacy information.",
    "no_sensitive": "Please don't include passport details, payment-card data, certification numbers or medical history.",
    "btn_whatsapp": "Continue in WhatsApp",
    "btn_whatsapp_help": "This prepares a message with your details. Review it in WhatsApp and send it when you're ready.",
    "btn_email": "Prepare an Email",
    "btn_copy": "Copy Inquiry",
    "copied": "Inquiry copied. Paste it into your preferred message app.",
    "copy_failed": "Copying isn't available in this browser. Select the text below and copy it.",
    "handoff_note": "Opening WhatsApp or your email app does not send anything until you press send there.",
    "error_summary": "Please check the following:",
    "err_name": "Enter your name.",
    "err_method": "Choose how you'd like to be contacted.",
    "err_detail": "Enter your contact detail.",
    "err_email": "Enter a valid email address.",
    "err_interest": "Choose what you're interested in.",
    "err_message": "Write a short message.",
    "kakao_tip": "Prefer KakaoTalk? Copy your inquiry, then send it to one of the IDs listed on this page.",
    "msg_intro": "Hello W Divers Coron, I'd like to ask about a trip.",
    "msg_labels": {"name": "Name", "method": "Contact via", "detail": "Contact", "interest": "Interest", "dates": "Dates", "guests": "Guests", "experience": "Experience", "last": "Last dive", "lang": "Language", "about": "About", "message": "Message"},
    "email_subject": "Dive inquiry",
    "direct_h": "Prefer to message directly?",
    "direct_t": "Use whichever channel suits you. An inquiry does not reserve a place; the team will confirm what's available.",
    "kakao_h": "KakaoTalk IDs",
    "directions_h": "Find W Divers in Coron.",
    "directions_t": "Open the location on Google Maps. Confirm your meeting point and time with the team before your activity.",
    "directions_btn": "Open in Google Maps",
    "noscript": "The inquiry builder needs JavaScript. You can still reach W Divers directly through WhatsApp, email or the other channels on this page.",
}

PAGES["booking"] = {
    "title": "Booking Information | W Divers Coron",
    "meta": "What to confirm with W Divers Coron before booking: trip details, your quotation, changes to plans and confirmation.",
    "eyebrow": "Booking information",
    "h1": "Know the arrangements before you confirm.",
    "intro": "Every trip starts with a discussion of your dates and interests. Request the details in writing before confirming or making a payment.",
    "steps": [
        {"h": "Your trip details.", "p": "Confirm the activity, date, meeting arrangements, guest count and any experience requirements."},
        {"h": "Your quotation.", "p": "Check the total price, inclusions, additional fees and payment instructions supplied by W Divers."},
        {"h": "Changes to plans.", "p": "Ask which cancellation, rescheduling and weather terms apply to your booking."},
        {"h": "Confirmation.", "p": "An inquiry does not reserve a place. Rely on the arrangements explicitly confirmed by W Divers."},
    ],
    "cta": "Ask a Booking Question",
    "interest": "unsure",
}

PAGES["privacy"] = {
    "title": "Privacy Information | W Divers Coron",
    "meta": "How the W Divers Coron website handles the information you choose to share, the external services it links to and how to ask about your personal information.",
    "eyebrow": "Privacy",
    "h1": "Privacy information",
    "intro": "This page explains, in plain language, how this website works with the information you choose to share.",
    "sections": [
        {"h": "Who we are", "p": ["This website is for W Divers Coron, based in Coron, Palawan, Philippines. You can contact us about privacy at {email}."]},
        {"h": "Information you choose to share", "p": ["The inquiry builder on the contact page helps you write a message that may include your name, contact detail, travel dates, group size, diving experience and language preference.", "This website does not store or transmit what you type into the inquiry builder. The text stays in your browser until you choose to continue in WhatsApp, prepare an email or copy it. You then review and send the message yourself in that app."]},
        {"h": "How we use your inquiry", "p": ["When you send us a message, we use the information you include to reply and to discuss the trip or activity you asked about."]},
        {"h": "External services", "p": ["If you choose WhatsApp, email, KakaoTalk, Facebook, Instagram, Naver Blog or Google Maps, the message or visit is handled by that service under its own privacy terms. This website links to those services; it does not embed them or load their content automatically.", "Like most websites, the hosting provider that delivers these pages may process technical request information, such as IP addresses, to serve and protect the site."]},
        {"h": "Storage in your browser", "p": ["If you choose a language from the language menu, this website remembers that choice in your browser's local storage so it can open the right language next time. You can clear it at any time through your browser settings.", "This website does not use analytics, advertising cookies or tracking pixels."]},
        {"h": "Questions about your information", "p": ["To ask about information you've sent us, or to request a correction or deletion, email {email}."]},
    ],
}

PAGES["sitemap"] = {
    "title": "Sitemap | W Divers Coron",
    "meta": "All pages on the W Divers Coron website.",
    "eyebrow": "Sitemap",
    "h1": "Every page in one place.",
    "intro": "Use this list to find any page on the website.",
    "groups": ["Diving", "Dive sites", "Plan your trip", "Journal", "About and contact", "Special trips"],
}

PAGES["404"] = {
    "title": "Page not found | W Divers Coron",
    "h1": "This page has drifted off.",
    "t": "The address may have changed, or the page may not exist. Try one of these instead.",
    "home": "Go to the homepage",
}

SITES = [
    {
        "slug": "okikawa-maru", "name": "Okikawa Maru", "type": "wreck", "img": "w-machinery", "kind": "Tanker", "length": "160.5 m", "depth": "12–26 m", "vis": "5–15 m", "lie": "upright",
        "card": "A large wreck with coral growth and abundant marine life around its structure.",
        "title": "Okikawa Maru Wreck Guide | Coron Dive Sites | W Divers Coron",
        "meta": "An introduction to the Okikawa Maru wreck in Coron, with the questions to ask W Divers Coron before planning a visit.",
        "p": [
            "Okikawa Maru was a Japanese tanker and is often described as one of the largest wrecks in the Coron area. She was sunk during the September 1944 air attacks on ships sheltering in and around Coron Bay.",
            "Decades underwater have turned the structure into a reef in its own right. Coral growth covers much of the hull and deck, and fish gather around the wreck. Because of its size, a single dive usually covers only part of the site, so it helps to ask which section a plan focuses on and what that section involves.",
        ],
    },
    {
        "slug": "akitsushima", "name": "Akitsushima", "type": "wreck", "img": "c-akitsushima", "kind": "Seaplane tender", "length": "118 m", "depth": "20–36 m", "vis": "5–15 m", "lie": "capsized", "photo_of_site": True,
        "card": "A seaplane tender known for its distinctive crane and machinery.",
        "title": "Akitsushima Wreck Guide | Coron Dive Sites | W Divers Coron",
        "meta": "An introduction to the Akitsushima, a Japanese seaplane tender wreck in Coron, with questions to ask before planning a visit.",
        "p": [
            "Akitsushima was an Imperial Japanese Navy seaplane tender, built to support flying boats. It is one of the warships among Coron's wrecks, which sets it apart from the cargo vessels and tankers found elsewhere in the area.",
            "The large crane once used to lift aircraft is the feature most visitors associate with this wreck, along with visible machinery and structural detail. Like the other Coron wrecks, it was sunk during the September 1944 air attacks. Ask the team how a dive here is planned and which parts of the wreck suit your experience.",
        ],
    },
    {
        "slug": "olympia-maru", "name": "Olympia Maru", "type": "wreck", "img": "c-olympia", "kind": "Auxiliary cargo and supply ship", "length": "128 m", "depth": "21–32 m", "vis": "10–20 m", "lie": "upright", "photo_of_site": True,
        "card": "A cargo wreck with an imposing underwater presence.",
        "title": "Olympia Maru Wreck Guide | Coron Dive Sites | W Divers Coron",
        "meta": "An introduction to the Olympia Maru cargo wreck in Coron, with questions to ask W Divers Coron before planning a visit.",
        "p": [
            "Olympia Maru was a Japanese cargo ship lost during the September 1944 air attacks on shipping around Coron Bay. Its long hull and large structure give the wreck an imposing presence underwater.",
            "Today the wreck supports coral growth and fish life along its surfaces, making it of interest to divers who enjoy both history and marine life. Different parts of the ship sit at different depths, so the right plan depends on your certification, recent diving and the conditions on the day.",
        ],
    },
    {
        "slug": "kogyo-maru", "name": "Kogyo Maru", "type": "wreck", "img": "c-kogyo", "kind": "Auxiliary cargo and supply ship", "length": "129 m", "depth": "18–34 m", "vis": "15 m", "lie": "capsized", "photo_of_site": True,
        "card": "A cargo wreck associated with wartime construction supplies.",
        "title": "Kogyo Maru Wreck Guide | Coron Dive Sites | W Divers Coron",
        "meta": "An introduction to the Kogyo Maru cargo wreck in Coron, associated with wartime construction supplies, with questions to ask before planning a visit.",
        "p": [
            "Kogyo Maru was a Japanese cargo ship sunk in the September 1944 air attacks on Coron Bay. The wreck is associated with wartime construction supplies, and its holds are reported to contain building materials from that period.",
            "That cargo gives the site a strong sense of history: rather than only seeing the outside of a ship, divers learn something about what it was carrying when it sank. Any interest in looking into holds should be raised with the team in advance, because entering an overhead environment requires appropriate training and planning.",
        ],
    },
    {"slug": "teru-kaze-maru", "name": "Teru Kaze Maru", "type": "wreck", "img": "w-three-divers", "card": "A small gunboat off East Tangat Island, shallow enough at the stern for new divers and a filming location for a Korean movie.", "kind": "Auxiliary submarine chaser (gunboat)", "length": "45 m", "depth": "3–22 m", "vis": "15 m", "lie": "starboard", "p": ["Also called the East Tangat Gunboat, this 45 m auxiliary submarine chaser lies on the edge of the reef, with its stern only 3 m deep and the wheelhouse at about 10 m. It suits Open Water divers, and the stern is shallow enough even for Discover Scuba Diving.", "Corals cover the deck and draw plenty of fish, and with luck mandarinfish are found near the hull. In September 2018 the wreck was a filming location for the Korean movie The Golden Holiday (국제수사). Visibility is usually best in the morning."]},
    {"slug": "irako", "name": "Irako", "type": "wreck", "img": "c-irako-wheel", "card": "Coron's deepest and best-preserved wreck, for advanced divers.", "kind": "Refrigeration ship", "photo_of_site": True, "length": "147 m", "depth": "28–42 m", "vis": "5–15 m", "lie": "port", "p": ["The Irako lies between Tangat and Lusong islands, its deck at 34 m and the rudder at 42 m. Apart from the captain's cabin it is largely intact, which makes it one of the finest wrecks in Coron and a dive for Advanced Open Water divers and above.", "There is usually current, so descents and ascents need care. Big groupers, tuna, lionfish and scorpionfish live on the wreck, and whale sharks are seen now and then."]},
    {"slug": "morazan-maru", "name": "Morazan Maru", "type": "wreck", "img": "c-morazan", "card": "A supply ship on its side, with big boilers, an air pocket and fire bricks in its holds.", "kind": "Auxiliary cargo and supply ship", "photo_of_site": True, "length": "91.5 m", "depth": "12–25 m", "vis": "15 m", "lie": "capsized", "p": ["The Morazan lies on its starboard side near Tangat Island, from 12 m on the hull to 25 m at the rudder. Its four cargo holds, two large boilers and the engine room can all be seen, and after more than 70 years there is still an air pocket inside.", "Bricks, tiles and broken toilets lie in the holds. Soft and hard corals cover the outside and draw jacks, lionfish, stonefish, turtles and lobsters, making it one of Coron's most popular wrecks."]},
    {"slug": "lusong-gunboat", "name": "Lusong Gunboat", "type": "wreck", "img": "c-fd-wreck", "card": "A small, coral-covered gunboat so shallow its stern almost breaks the surface at low tide.", "kind": "Submarine hunter (gunboat)", "length": "35 m", "depth": "0–18 m", "vis": "5–15 m", "lie": "forward", "p": ["This 35 m gunboat lies off the east side of Lusong Island, tilted forward from the surface to 18 m. At low tide the stern nearly reaches the surface, so snorkellers can enjoy it as well as divers.", "Hard corals cover the whole boat, and the reef around it is home to anemones, butterflyfish, angelfish and plenty of other reef fish. It is a favourite with new wreck divers and underwater photographers."]},
    {"slug": "nanshin-maru", "name": "Nanshin Maru", "type": "wreck", "img": "w-coral-wreck", "card": "A tanker off Black Island, often with the clearest water of any Coron wreck.", "kind": "Fuel oil tanker", "length": "70 m", "depth": "18–34 m", "vis": "up to 30 m", "lie": "forward", "p": ["Also known as the Black Island Wreck, this 70 m tanker lies about 50 m off the beach at Black Island in northwest Busuanga, sloping from 18 m at the poop deck to 34 m.", "Visibility often reaches 30 m. Corals cover the wreck down to about 20 m, with sand below, and lionfish, batfish, groupers, pufferfish and jacks are regular sightings."]},
    {"slug": "kyokuzan-maru", "name": "Kyokuzan Maru", "type": "wreck", "img": "w-valves", "card": "An intact freighter far from town, with Japanese cars and trucks still in its holds.", "kind": "Freighter", "length": "136 m", "depth": "24–40 m", "vis": "up to 30 m", "lie": "upright", "p": ["The Kyokuzan Maru lies northeast of Busuanga, far enough from Coron town that it is a full-day trip with an early start. The freighter sits upright with a slight list, its main deck at 24 m and the rudder at 40 m.", "It is almost undamaged, and Japanese cars and trucks can still be seen inside. Visibility is usually excellent. The wreck is dived twice in the day, bow and stern, and can be combined with a Dugong Point day trip."]},
    {"slug": "skeleton-wreck", "name": "Skeleton Wreck", "type": "wreck", "img": "hero-fish", "card": "The bare frame of a small boat near Coron Island, ideal for snorkelling and first dives.", "kind": "Submarine hunter (gunboat)", "length": "25 m", "depth": "5–22 m", "vis": "10 m", "p": ["About 15 minutes from Coron town, near Coron Island, only the frame of this small boat remains, which is how it got its name. The bow is at 5 m and the deepest point at about 22 m.", "Coral, good light and calm water make it a lovely spot for underwater photography, Discover Scuba Diving and snorkelling. Damselfish, lionfish, nudibranchs, parrotfish and stonefish live around the frame."]},
    {"slug": "barge-wreck", "name": "Philippine Barge Wreck", "type": "wreck", "img": "stock-descent", "card": "A 90 m barge with nine open cargo holds, from 18 m at the bow to 43 m.", "kind": "Barge", "length": "90 m", "depth": "18–43 m", "p": ["This large barge sank while it was being used for illegal fishing. It is about 90 m long, with the bow at 18 m and the bottom at 43 m.", "Nine open cargo holds run along the hull, and divers can look into them from above. Because of the depth it suits experienced divers; ask the team how a dive here is planned."]},
    {"slug": "barracuda-lake", "name": "Barracuda Lake", "type": "lake", "img": "c-fd-lake", "card": "A lake inside Coron Island where warm saltwater lies beneath fresh water, reaching up to 39 °C.", "kind": "Lake with a thermocline", "photo_of_site": True, "depth": "up to 40 m", "p": ["Barracuda Lake is 15 minutes by boat from Coron town, on the north of Coron Island. From the boat you climb about 38 wooden steps over the limestone and down again with your gear, then dive between sharp limestone walls up to 40 m deep.", "The top 4 m is fresh water at about 28 °C. From 4 to 14 m it turns warm and salty, and below 14 m the water can reach 39 °C, with the thermocline clearly visible between about 4 and 13 m. A cave at 21 m runs some 30 m into the rock, wide enough for one diver at a time. The lake is named after a single large barracuda that lives here, along with catfish and freshwater shrimp. The entry platform is small, so groups take turns."]},
    {"slug": "cathedral-cave", "name": "Cathedral Cave", "type": "lake", "img": "c-fd-beam", "card": "A cave at the southern tip of Coron Island where sunlight pours in from above.", "kind": "Cave", "p": ["Cathedral Cave is about two hours by banca from Coron town, under the cliffs at the southern tip of Coron Island. The entrance is a narrow 5 m passage taken one diver at a time, with loose sediment on the floor, so Open Water certification and good buoyancy are recommended. Beginners can join with close help from an experienced guide.", "After a safety stop you surface inside the cave, where sunlight falls through a large opening and makes the limestone glow green: a perfect place for a group photo. On the way back out there are reefs, rocks and plenty of fish to see."]}
]

ARTICLES = [
    {
        "slug": "planning-your-first-coron-dive-trip",
        "title": "Planning your first diving trip to Coron",
        "meta": "A practical starting point for choosing diving options in Coron, preparing your questions and arranging the details before you arrive.",
        "img": "crew-briefing",
        "body": [
            ("Start with the experience you already have.", [
                "Before choosing sites or comparing photographs, think about where you are in your diving journey. Are you considering your first scuba experience, returning after a break, or arriving with recent dives and a certification? That starting point shapes the questions worth asking.",
                "If you are new to scuba, ask about introductory experiences and how they differ from a certification course. If you are certified, have your certification level, approximate logged dives and date of your last dive ready. This information helps the operator discuss suitable options; it is not a substitute for their assessment.",
            ]),
            ("Separate the destination from the itinerary.", [
                "A photograph of a famous wreck can inspire a trip, but it does not tell you whether that location is appropriate for you or available on your dates. Ask which sites may suit your experience and what can affect the final plan. Avoid building your entire stay around a single unconfirmed location.",
            ]),
            ("Compare the whole arrangement.", [
                "Ask how many dives are planned, what equipment is included, where you will meet and whether additional fees apply. Clarify meals, transfers, equipment rental and any park or entrance fees. A clear quotation is more useful than a headline price without its inclusions.",
            ]),
            ("Leave room around your travel plans.", [
                "Tell the team about your arrival and onward travel. Diving and flying need to be planned together with an appropriate surface interval. Read current DAN guidance and follow advice appropriate to your diving rather than relying on a generic travel timetable.",
            ]),
            ("Start the conversation.", [
                "You do not need every detail decided before asking. Send your dates or approximate travel period, group size, experience and the type of diving you are interested in. W Divers can then clarify the options available for your visit.",
            ]),
        ],
        "cta": "Plan Your Dive", "interest": "unsure",
        "related": [("first", None), ("plan", None), ("faq", None)],
    },
    {
        "slug": "wreck-diving-questions-before-booking",
        "title": "Wreck diving in Coron: questions to ask before booking",
        "meta": "Know what to ask about experience requirements, dive plans, equipment and inclusions when considering a Coron wreck-diving trip.",
        "img": "wreck-mast",
        "body": [
            ("Ask about the planned dive, not just the wreck name.", [
                "A wreck can have different features at different depths. Ask which area the trip intends to explore and what conditions may change that plan. A familiar site name alone does not establish the suitability of a particular dive.",
            ]),
            ("Be specific about your background.", [
                "Share your certification level, recent diving experience and relevant training. If you have never dived around a wreck before, say so. Being clear about your experience gives the operator a better starting point for discussing options.",
            ]),
            ("Distinguish an exterior visit from penetration.", [
                "Swimming around the outside of a wreck and entering a space without direct access to the surface are different activities. Entering an overhead environment calls for appropriate training, equipment and experience, and a guide does not replace that training.",
                "If a plan mentions going inside any part of a wreck, ask what that involves, what training is expected and how the team decides whether it is appropriate for you. It is also completely reasonable to prefer an exterior-only dive.",
            ]),
            ("Ask how depth and conditions shape the plan.", [
                "Ask how the dive plan relates to the limits of your certification, and what happens if current, visibility or weather change on the day. Plans that can adapt to conditions are a normal part of diving, not a sign that something has gone wrong.",
            ]),
            ("Clarify equipment.", [
                "Ask which items are included and which can be rented, such as a dive computer or a torch. If you plan to bring your own equipment, mention it so the team knows what you will need on the day.",
            ]),
            ("Check the whole quotation.", [
                "Before confirming, ask how many dives are planned, what the boat arrangements are, whether meals and transfers are included, and whether park or entrance fees are extra. Ask for the total price and the payment, rescheduling and cancellation terms that apply.",
            ]),
            ("Bring your questions to the conversation.", [
                "Send your certification level, approximate logged dives, date of your last dive and preferred dates. If there is a particular wreck you hope to see, mention it, and ask whether it is a suitable option for you.",
            ]),
        ],
        "cta": "Plan a Wreck-Diving Trip", "interest": "wreck",
        "related": [("wreck", None), ("sites", None), ("booking", None)],
    },
    {
        "slug": "divers-and-non-divers-in-one-coron-trip",
        "title": "Divers and non-divers in one Coron trip",
        "meta": "Planning Coron with a mix of certified divers, first-timers and people who prefer to stay dry? Questions to ask so everyone's day makes sense.",
        "img": "boat-group",
        "body": [
            ("Start with everyone's interests.", [
                "Groups rarely arrive with identical plans. One person may be hoping for wrecks, another may be curious about trying scuba, and someone else may simply want a day on the water. Write down what each person would like to do before you ask about arrangements.",
            ]),
            ("Share each diver's experience.", [
                "Within one group, divers can have very different backgrounds. Share each person's certification level and recent diving, and mention anyone who has never dived. The team can then discuss which options make sense for each of them.",
            ]),
            ("Ask whether one boat suits everyone.", [
                "A dive day and an island-hopping day can have very different rhythms. Ask whether non-divers can join a diving trip, what they would do during the dives, and how long the day is likely to be. Participation and boat arrangements should be confirmed for the specific activity.",
            ]),
            ("Consider separate activities.", [
                "Sometimes the most enjoyable plan is different activities on the same day or a shared activity on another day. Mention your dates and let the team clarify whether a shared plan or separate activities make more sense.",
            ]),
            ("Plan around travel days.", [
                "If anyone in the group is diving, plan your final days with flying in mind. An appropriate surface interval before flying matters, so tell the team about everyone's onward travel when you inquire.",
            ]),
            ("Send one clear inquiry.", [
                "One message with your dates, the number of guests, each person's interests and the divers' experience is easier to answer than several separate conversations. You can always add details as your plans take shape.",
            ]),
        ],
        "cta": "Start a Group Inquiry", "interest": "unsure",
        "related": [("island", None), ("first", None), ("faq", None)],
    },
]

TRIPS = [
    {
     "slug": "apo-reef",
     "name": "Apo Reef Yacht Liveaboard",
     "short": "Apo Reef",
     "img": "c-yacht",
     "inline": [
      [
       0,
       "c-yacht-apo"
      ],
      [
       1,
       "c-yacht-cabin"
      ],
      [
       4,
       "c-yacht-deck"
      ]
     ],
     "card": "A 4-night yacht liveaboard to the Philippines' largest coral reef, for up to 10 divers.",
     "title": "Apo Reef Yacht Liveaboard | Special Trips | W Divers Coron",
     "meta": "A W Divers Coron yacht liveaboard to Apo Reef Natural Park, the largest coral reef in the Philippines: 4 nights, up to 10 divers, nitrox and meals included.",
     "intro": "Apo Reef Natural Park, about 30 km off the west coast of Occidental Mindoro, is the largest coral reef in the Philippines and on UNESCO's tentative World Heritage list. W Divers Coron charters the Caribbean Tigress yacht for small, divers-only groups.",
     "facts": [
      [
       "Format",
       "Yacht liveaboard, full charter"
      ],
      [
       "Yacht",
       "Caribbean Tigress"
      ],
      [
       "Group size",
       "Up to 10 divers"
      ],
      [
       "Length",
       "4 nights, 5 days (2027 departure)"
      ],
      [
       "Dives",
       "10 included, more if you have the energy"
      ],
      [
       "Depth and visibility",
       "5–40 m, often 15–50 m"
      ],
      [
       "Boarding",
       "Batangas, with Manila airport pick-up"
      ]
     ],
     "sections": [
      {
       "h": "A reef worth the journey.",
       "p": [
        "Apo Reef covers about 34 km² and is divided into a north and a south lagoon. Depths run from 5 to 40 m, visibility is often 15 to 50 m, and gentle currents make most dives easy drift dives. Mantas, sharks, schooling barracuda and big napoleon wrasse are all part of the reef's appeal."
       ]
      },
      {
       "h": "Life on board.",
       "p": [
        "The Caribbean Tigress has an air-conditioned master cabin with a double bed, plus twin and triple cabins with single beds. Meals, drinking water, coffee and tea are served throughout the trip, and there is wifi on board."
       ]
      },
      {
       "h": "What's included.",
       "list": [
        "Water taxi to the yacht from the Batangas harbour",
        "10 dives, with extra dives free if you have the energy",
        "Nitrox on every dive",
        "Free night dive",
        "Manila airport pick-up and drop-off",
        "All meals: breakfast, lunch and dinner",
        "Drinking water, coffee and tea",
        "Wifi on board"
       ]
      },
      {
       "h": "Not included.",
       "list": [
        "Apo Reef Natural Park entrance fee (USD 100)",
        "International flights",
        "Dive insurance",
        "Equipment rental",
        "Alcohol and other drinks (tell us your preferred brands before departure)",
        "Tips: dive guide USD 60, yacht crew USD 40",
        "Personal expenses"
       ]
      },
      {
       "h": "Booking and cancellation.",
       "p": [
        "Your place is confirmed once the full trip price is paid. Because this is a liveaboard, cancellations are not refunded, except that cancelling at least three months before departure returns 50% of the price. If weather stops the trip, it is rescheduled rather than refunded, and if the yacht has an engine problem a yacht of the same standard is used."
       ]
      }
     ],
     "prices": {
      "at": 1,
      "h": "2027 prices per person",
      "note": "Indicative prices for the 2027 departure. Dates are still being confirmed, so ask the team for the current price before you book.",
      "rows": [
       [
        "Master cabin, double bed (2 people)",
        "USD 2,500"
       ],
       [
        "Twin cabin, single beds (2 people)",
        "USD 2,200"
       ],
       [
        "Triple cabin, single beds (3 people)",
        "USD 2,000–2,100"
       ]
      ]
     },
     "ask": [
      "2027 departure dates and places left",
      "Price for your cabin type",
      "Park entrance fee and tips",
      "Certification and experience required",
      "Flights to Manila and transfer times",
      "Dive insurance"
     ]
    },
    {
     "slug": "dugong-watching",
     "name": "Dugong Watching",
     "short": "Dugong Watching",
     "img": "c-dugong",
     "video": "dugong",
     "inline": [[0, "dugong-diver"], [1, "c-dugong-divers"], [2, "c-dugong-graze"], [3, "c-dugong-freediver"]],
     "animals": {"h": "Other animals you may meet.", "p": "Dugong Point is not the only wildlife on this trip. Sea turtles and reef fish are common on the beach dives at Dimipac Island, and Calauit Safari Park is home to giraffes and zebras, descended from animals brought from Kenya in 1977, alongside the endemic Calamian deer.", "items": [["c-fd-turtle", "Sea turtles often appear on the beach dives near Dugong Point."], ["calauit-giraffes", "Giraffes roam freely at Calauit Safari Park."], ["calauit-feeding", "At the feeding area you can get close enough to feed the giraffes."], ["calauit-zebras", "Zebras graze in the open at Calauit Safari Park."]]},
     "card": "An early start to meet dugongs at Dugong Point, off Calauit in northern Busuanga.",
     "title": "Dugong Watching Day Trip | Special Trips | W Divers Coron",
     "meta": "A W Divers Coron day trip to Dugong Point in northern Busuanga: 4 am pick-up, small groups of four, the official watching rules and an optional visit to Calauit Safari Park.",
     "intro": "Dugongs, gentle sea mammals that graze on seagrass, live off Calauit Island in northern Busuanga. On this day trip you leave before dawn, travel by van and boat to Dugong Point, and watch the dugongs in small groups with a trained dugong guide.",
     "facts": [
      [
       "Format",
       "Day trip by van and boat"
      ],
      [
       "Pick-up",
       "04:00–04:30 from your hotel"
      ],
      [
       "Where",
       "Dugong Point, off Calauit Island, northern Busuanga"
      ],
      [
       "Getting there",
       "1 h 40 min by van, then 25 min by boat"
      ],
      [
       "With the dugong",
       "About 15 minutes per group of 4"
      ],
      [
       "Back in Coron",
       "Around 3–4 pm, sometimes 6–7 pm"
      ],
      [
       "Add-on",
       "Calauit Safari Park visit"
      ]
     ],
     "sections": [
      {
       "h": "Why the early start.",
       "p": [
        "Dugong Point gets busy in peak season, and groups take turns in the order they arrive. Pick-up is between 4:00 and 4:30 am so you are among the first. If your hotel can't prepare breakfast, the shop provides a simple one to eat in the van or at the pier."
       ]
      },
      {
       "h": "How the day runs.",
       "list": [
        "1 hour 40 minutes by van to Quezon pier in northern Busuanga",
        "Load the equipment onto the boat, then register and pay the admission fee at the Dugong Office, 5 minutes from the pier",
        "About 25 minutes by boat to Dugong Point",
        "If many groups are waiting, you may beach-dive first at Dimipac Island, 15 minutes away",
        "A dugong guide briefs your group, then searches for the dugong",
        "When it is found, your group of four enters and spends about 15 minutes with it",
        "Lunch is eaten on the boat, and you return in reverse order"
       ]
      },
      {
       "h": "Dugong watching rules.",
       "list": [
        "No more than four guests in the water with a dugong at a time",
        "Stay at least 5 m away",
        "Enter quietly by the ladder and put your equipment on at the surface: no jumping in",
        "Stay quiet on the boats and don't shout when a dugong is spotted",
        "Never touch, chase or swim in front of a dugong",
        "No strobes or flash photography",
        "Let the dugong choose to come close, and never separate a mother and calf"
       ],
       "after": [
        "Breaking the rules can bring a heavy penalty, and the whole group may lose its turn. Sightings are never guaranteed: dugongs are wild."
       ]
      },
      {
       "h": "Tips for the day.",
       "list": [
        "Don't race off at full speed when the guide signals; save your energy for the dive",
        "Wear about 1 kg more weight than usual so you can get down quickly",
        "Bring sun protection and a light jacket for the early drive"
       ]
      },
      {
       "h": "Make a day of it.",
       "p": [
        "The trip can be combined with a visit to Calauit Safari Park on Busuanga, home to giraffes and zebras. Ask the team how the day is planned and what's included."
       ]
      }
     ],
     "ask": [
      "Pick-up time from your hotel",
      "Snorkelling or diving, and equipment",
      "Admission and environmental fees",
      "Calauit Safari Park option",
      "Total price and what's included"
     ]
    },
    {
        "slug": "deserted-island-overnight", "name": "Deserted Island 2 Days 1 Night", "short": "Deserted Island 2D1N", "img": "c-island-beach", "inline": [[0, "c-island-tents"], [1, "boat-lunch"], [2, "c-island-sunset"]],
        "card": "Five dives and a night camping on an uninhabited island, two days away from town.",
        "title": "Deserted Island 2 Days 1 Night Tour | Special Trips | W Divers Coron",
        "meta": "A W Divers Coron 2-day, 1-night diving package: 5 dives and a night camping on an uninhabited island away from Coron town.",
        "intro": "Trade Coron town for a quiet island for a night. This 2-day, 1-night diving package includes 5 dives and an overnight camp on an uninhabited island, arranged by the W Divers team.",
        "facts": [("Format", "Diving package with island camping"), ("Length", "2 days, 1 night"), ("Dives", "5 dives"), ("Stay", "Camping on an uninhabited island"), ("Non-divers", "Ask about snorkelling and beach time")],
        "sections": [
            {"h": "Five dives and a night on the island.", "p": ["The package includes five dives over the two days. Between dives you head to a quiet, uninhabited island, set up camp for the evening, and wake up on the beach before the next day on the water."]},
            {"h": "Know the arrangements.", "p": ["Overnight trips need clear plans. Ask about sleeping arrangements, meals, drinking water, toilets and shade, what to bring, and what happens if the weather changes."]},
            {"h": "Who it suits.", "p": ["Groups of friends, families, and divers travelling with non-divers. Mention everyone's interests when you inquire so the team can shape the two days."]},
        ],
        "ask": ["Which dive sites the 5 dives visit", "Tents, bedding and what to bring", "Meals and drinking water", "Facilities on the island", "Options for non-divers", "Weather and cancellation terms", "Total price"],
    },
    {
        "slug": "kyokuzan-maru", "name": "Kyokuzan Maru Day Trip", "short": "Kyokuzan Maru", "img": "w-coral-wreck", "inline": [[0, "w-valves"], [2, "crew-briefing"]],
        "card": "A full day out to one of the region's more remote Japanese wrecks.",
        "title": "Kyokuzan Maru Wreck Day Trip | Special Trips | W Divers Coron",
        "meta": "A full-day W Divers Coron trip to dive the Kyokuzan Maru, a Japanese cargo wreck away from the main cluster of Coron wrecks.",
        "intro": "The Kyokuzan Maru lies away from the main cluster of Coron wrecks, so reaching it takes a full day. For wreck enthusiasts, it is a chance to dive a site fewer divers visit.",
        "facts": [("Format", "Full-day wreck trip"), ("For", "Certified divers"), ("Site", "Kyokuzan Maru, a Japanese cargo wreck"), ("Also", "Ask which other sites can be dived on the way")],
        "sections": [
            {"h": "A wreck off the usual route.", "p": ["Like other wrecks in the area, the Kyokuzan Maru was a Japanese cargo ship lost during the Second World War. Its distance from Coron town means fewer visitors, and the longer boat ride is part of the day."]},
            {"h": "Is it right for you?", "p": ["The planned depth and conditions decide who can join. Share your certification level, logged dives and the date of your last dive, and ask the team what experience the trip requires."]},
            {"h": "Plan the day.", "p": ["Ask about the departure time, number of dives, equipment, meals and fees, and what happens if conditions change on the day."]},
        ],
        "ask": ["Required certification and experience", "Planned depth and number of dives", "Departure time and length of the day", "Equipment, meals and fees", "Total price"],
    },
]
