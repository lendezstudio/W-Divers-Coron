# Owner confirmation checklist

Private project notes. Nothing on this list is shown on the public website. Items marked **open** are omitted from public pages until confirmed.

## Contact and identity

| Item | Status | Notes |
|---|---|---|
| Facebook, Instagram, WhatsApp (+82 10 8621 8096), email, Google Maps, Naver Blog | Confirmed by Lyneth, 25 Oct 2026 | Used site-wide |
| KakaoTalk | Published as IDs | `redscandle3384` (Korean phone) and `wdiverscoron` (PH phone), from the business's own contact cards (`assets/images/513276370_...jpg`, `808897143_...jpg`). No channel URL or QR found. Confirm both are current. |
| Korean instructor number +82 10 2654 8096 ("Dean Kang") on the contact cards | **open** | Differs from the supplied WhatsApp number. Not published. Do not publish the name without approval. |
| Philippine number +63 956 159 8095 on the contact cards | **open** | Not published. Supplied contacts take priority. |
| Exact address / meeting point | **open** | Site shows "Barangay Poblacion 5, National Highway, Coron Town Proper, Coron, Palawan 5316". The cards add "R2R BayView Inn building 1F". Confirm before adding it. Pages tell visitors to confirm the meeting point. |
| Legal display name | **open** | Cards say "W DIVERS CORON Inc."; SSI directory lists "WDIVERS CORON INC." |
| Agency affiliation (SSI / PADI / TDI) | **open** | Shop photos show SSI and PADI signage and a TDI banner. No affiliation is claimed on the site. |
| Domain | **open** | Set `SITE_URL` in `src/config.py` to enable canonical URLs, hreflang, og:url and `sitemap.xml`. |
| Hours and primary inquiry manager | **open** | |

## Services (needed before adding details)

- Current fun-diving, introductory-diving and training catalogue: exact program names, agency, prerequisites, minimum ages, durations, dives, instructor languages, inclusions and PHP prices. Add verified courses to `COURSES` in `src/data.py`.
- Rates, dive count, equipment and computers, torches, gas options, meals, transfers and park fees.
- Sites regularly visited, suitability assessment, group sizes, boat capacity and emergency arrangements.
- Island-hopping routes, shared/private options and non-diver participation.
- Booking confirmation steps, deposit/payment, cancellation and weather policies. Replace the guidance on `/booking-information/` with approved terms.
- Languages spoken by staff for briefings.

## Media and promotions found but not used

| File(s) | Reason |
|---|---|
| `808763897_...jpg`, `809039960_...jpg`, `809876729_...jpg` | Apo Reef "Caribbean Tigress" yacht liveaboard, 30 Oct to 3 Nov 2026. Time-limited, outside Coron, prices and inclusions unconfirmed. Ask if it should be promoted. |
| `599959646_...jpg` | TDI technical diving banner. Would imply a credential. |
| `594074064_...jpg` | Group with certificates. Would imply certification courses. |
| `512677394_...jpg` | Night shot of tanks and a dive watch. Low clarity. |
| `Apo-Reef.jpg`, `3D2N-explore-Apo-Reef-Tour-Package-A.jpg`, `images (1).jpg` | Apo Reef / unknown locations, not Coron |
| `gallery-*.jpg`, `group-shop-lounge.jpg`, `team-shop-interior.jpg`, `island-hopping-boat.jpg`, `hero-reef-diver.jpg`, `reef-diving-coral.jpg`, `wreck-diving-splitshot.jpg` | From the earlier demo. Some show a different shop interior and signage, possibly the similarly named listing. Not used, to avoid blending businesses. |
| `assets/logo-full.png`, `logo-mark.png`, `logo-source.png`, `favicon.png` | Teal "W" logo from the earlier demo. Does not match the shop signage. The site uses the supplied black mark (`Restored divers coron logo...png`) and a white reversed version generated from it. |
| Dugong video | Used in the gallery's Video tab with a neutral caption. Confirm it is W Divers footage and whether a location can be named. |

Pool training photos are used on the First-Time Divers and Courses pages without saying where they were taken. Confirm the location if a caption is wanted.

## Content decisions to review

- The brief was cut off at 50,000 characters, during Journal Article 2. Article 2's later sections and all of Article 3 ("Divers and non-divers in one Coron trip") were written to match the brief's rules. Please review both. The truncated part may also have listed more locales. The site ships with English and Korean, and more can be added via `src/content/<code>.py` and `LOCALES` in `src/config.py`.
- Olympia Maru: the brief's card said "upright". The site leaves out orientation until it is verified.
- Kogyo Maru: building materials are described as "reported".
- Site guides are reviewed October 2026; sources are listed in `src/data.py`.
- No author names or publication dates on journal articles. Public authorship needs owner approval.
- No reviews, ratings or guide names are shown. Old ratings from the earlier brief are not current.

## Before launch

- [ ] Owner reviews all English and Korean copy (the Korean was written for this project, not professionally translated)
- [ ] Confirm KakaoTalk IDs, address wording and photo permissions
- [ ] Set `SITE_URL` and rebuild
- [ ] Configure the host to serve `/404.html` for missing pages
- [ ] Review the privacy page against the actual hosting provider
