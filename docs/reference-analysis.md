# Reference analysis

Reference: **Website Ocean Design Concept** by Lina Design (Behance, published 1 December 2023)
https://www.behance.net/gallery/185796499/Website-Ocean-Design-Concept

Scope: the reference is a single static desktop hero composition. It is a visual anchor for the W Divers homepage opening and the shared design language, not a specification for a full website. No pixel-perfect match, exact font or exact colour values are claimed.

## Observed (from the brief's inspection of the artwork)

- Blurred blue underwater backdrop surrounding a wide panel with a thin pale rounded border.
- Swimmer and rocks on the left; darkened, softly blurred right area carrying light rounded geometric lettering.
- Short teal rule, small supporting copy and an outlined rounded button.
- Fine central divider.
- Sparse top navigation with a hamburger at upper right.
- Vertical dots at left, a rotated scroll cue near the middle bottom and small social icons at lower right.

## Adapted for W Divers Coron

| Reference element | W Divers implementation |
|---|---|
| Blurred surround | `hero-backdrop.webp`, a blurred and darkened derivative of the hero photo, generated in `src/media.py` |
| Framed panel | HTML/CSS frame, 1px pale border, radius 20-28px, about 88% of viewport width up to 1440px, min-height targeting ~1.7:1. Grows with content. |
| Swimmer photo | Replaced with W Divers' own photo of two scuba divers beside a fish school (`512086947_...jpg`). The reference photo is not used. |
| Soft dark right side | `.hero-soft`: `backdrop-filter: blur()` on the image layer only, masked from the left, with a dark gradient fallback when backdrop-filter is unsupported |
| Central divider | Gradient hairline at 50%, desktop only |
| Typography | Outfit (light 300) for Latin display; Inter for body. Korean falls back to Apple SD Gothic Neo / Malgun Gothic / Noto Sans KR. Fonts are self-hosted (OFL). "In the style of" the reference, not its actual font. |
| Teal rule | 56 x 2px `--accent #4EAAA6`; draws in on load (skipped with reduced motion) |
| Outlined button | `.btn-outline`, radius 14px, fills on hover/focus, 50px tall |
| Top nav + hamburger | Short visible menu on desktop (Diving / Dive Sites / Plan Your Trip / About / Contact) with keyboard-operable dropdowns; full navigation in one accessible panel behind "Menu" on smaller screens and in the sticky bar. No duplicate competing menus. |
| Left dots | Real anchor links to six homepage sections, with accessible names and an active-section state |
| Scroll cue | Rotated "Scroll" link to the next section; hidden on small screens |
| Social icons | Verified W Divers Facebook, Instagram and WhatsApp only |

### Extension to the rest of the site (proposed, not observed)

- Inner pages reuse the framed opening at a shorter height with a left-aligned title, breadcrumb and the same accent rule.
- Long reading moves onto muted light "paper" panels (`--paper #E8EEEC`). This is a usability adaptation.
- Fine 1px lines separate lists (route chooser, dive-site index, steps, FAQ) instead of glossy card grids.
- Motion: 600-700ms opacity/translate reveals, a slow settle on the hero image, a drawn accent rule. All disabled under `prefers-reduced-motion`. No parallax, scroll hijacking or loading screen.
- Mobile: near-full-width frame with 16px gutters; the photo sits at the top of the frame and the copy moves into a dark lower region inside the same frame. Divider, rail and scroll cue are removed.

## Not shown in the reference

Inner pages, footer, mobile layout, exact typeface, exact colour values, animation and working interactions are not demonstrated. Everything above beyond the hero is a W Divers design decision.

## Visual check performed

The homepage hero was rendered in headless Chromium at 1280, 1440, 1600 and 390px wide and compared against the observed hierarchy. Checks: frame, subject on the left, soft dark text region on the right, light display type, accent rule, outlined CTA and negative space. Inner pages were rendered at 360, 768, 1024, 1366, 1440 and 1920px.
