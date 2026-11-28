# Reel covers

Saved 2026-11-27. Format from profile.md: `[PRICE] [THING]. WORTH IT?`, same
font and position every time, prices in USD (match the hook).

Specs (secondary sources, checked 2026-11-27: Buffer, Hopper HQ, Linearity,
Influencer Marketing Hub; Meta's own docs not checked):
- Make the cover 1080 x 1920 (9:16).
- The profile grid shows a 3:4 centre crop (~1080 x 1440), cutting ~240 px off
  the top and bottom. Keep the text and the subject inside that middle band.
- Check the "Profile grid" preview in Instagram's cover editor before posting.

| # | Reel | Cover text | Shot (from the script and footage notes) |
|---|---|---|---|
| 1 | Providence | $2,400 3-STAR DINNER. WORTH IT? | The custom three-star Dom bottle in the cellar, or the kitchen view from the private room |
| 2 | Bulgari Tokyo | $1,400 A NIGHT. WORTH IT? | Skyline from the room (Mount Fuji if it's clear in a frame) |
| 3 | Atomix | $1,600 KOREAN TASTING. WORTH IT? | A plated dish or the banchan spread |
| 4 | Banbo | $850 TASTING MENU. WORTH IT? | The shrimp "river" plate |
| 5 | Baccarat | $12,000 HOTEL STAY. WORTH IT? | The crystal: chandelier or lobby |
| 6 | Sushi Masaki Saito | $1,800 SUSHI DINNER. WORTH IT? | A piece of nigiri being placed, or the counter |
| 8 | Amanyangyun | $1,400 AMAN STAY. WORTH IT? | The room or the grounds |
| 9 | Le Cinq | $2,700 PARIS DINNER. WORTH IT? | The dining room, or the Parmesan waffle |
| 10 | Bulgari Shanghai | $7,000 FOR 5 NIGHTS. WORTH IT? | The night view: city lights over the river |
| 11 | Mizue | $600 2-STAR SUSHI. WORTH IT? | A thick-cut nigiri at the counter |

## Made
- `covers/make_cover.py` builds each cover: photo fitted to 1080x1920, white
  line + red "WORTH IT?" (Inter Display Bold), soft shadow, and a
  `-grid-preview.jpg` (the 3:4 centre crop) for checking.
- #2 Bulgari Tokyo: `covers/02-bulgari-tokyo-cover.jpg` (user's night skyline
  photo, 2026-11-27); text centred at y=620, in the dark sky above the skyline.
  Gold letter-spaced line "3 MICHELIN KEYS" above (user, 2026-11-27). Use the
  rating line on every cover (e.g. "3 MICHELIN STARS", "1 MICHELIN KEY"); text
  only, no Michelin logo or Key symbol (their trademarks).
- Michelin Key logo (user, 2026-11-27): the user supplied the 3-Key image and
  chose to use it after being told Michelin's rules (as quoted in a hotel's
  2025 PDF) prohibit use of its brand assets without authorization. Pass a
  file from `assets/michelin/` as the KICKER argument.

## Michelin icon assets (user-supplied, 2026-11-27)
`instagram/assets/michelin/`, transparent PNGs cropped to the artwork:
- Keys: `key-1-`, `keys-2-`, `keys-3-` in `outline` (red line, see-through
  middle) and `filled` (red line, white middle).
- Stars: `star-1-`, `stars-2-`, `stars-3-`, same two styles.
- `star-1-outline.png` had stray specks in its see-through areas; cleaned.
- Covers scale every icon set to the same height (165 px), so 1, 2 and 3
  icons look consistent across the grid.
- STYLE: FILLED on every cover (user, 2026-11-27): filled keys for hotels,
  filled stars for restaurants. Bulgari Tokyo uses
  `keys-3-filled`.
- #1 Providence: `covers/01-providence-cover.jpg` from the user's photo of the
  engraved "Congratulations / three stars / Providence" Dom Perignon 2012
  magnum. Remade 2026-11-28 from a second photo with no cable or tape measure
  (CENTER_X=0.62 SHADE=top). SHADE=top darkens behind the text; CENTER_X moves
  the 9:16 crop sideways.
- #3 Atomix: `covers/03-atomix-cover.jpg` from the user's plated dish photo
  (2026-11-28; SHADE=top). Also tested: the 50 Best trophy and the chef's menu
  card (text and logos clashed; mockup in `covers/atomix-test-trophy-vs-card.jpg`),
  the entrance sign and a landscape awards-wall video (not used).
- #3 Atomix, alternative: `covers/03-atomix-cover-video.jpg`, a still from the
  awards-wall video at 4.3s (`covers/src-atomix-video-4.3s.jpg`), zoomed ~1.27x
  on the MICHELIN 2025 plaque; SHADE=band behind the text.
