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
- #3 Atomix, caviar option: `covers/03-atomix-cover-caviar.jpg` (user's photo of
  the caviar dish in the celadon bowl, 2026-11-28; SHADE=top). Claude's pick of
  the five dish photos: dark marble with room for text, the dish fully clear of
  it, caviar reads as luxury at thumbnail size. Final choice: user's call.
- #3 Atomix FINAL (user, 2026-11-28): the caviar cover, now
  `covers/03-atomix-cover.jpg`. The glazed-dish and video-still versions moved to
  `covers/alternates/`.
- #4 Banbo: `covers/04-banbo-cover.jpg` from the user's crab rice clay-pot photo
  (2026-11-28; SHADE=top). Tested against the shrimp "creek" plate (the dish in
  the script), which had too little dark space and a small subject:
  `covers/alternates/banbo-test-shrimp-vs-crab.jpg`. Origami menu not used (busy).
- #4 Banbo FINAL (user, 2026-11-28): crab cover.
- #5 Baccarat options (2026-11-28), in `covers/alternates/`: `05-baccarat-cover-
  chandelier.jpg` (lobby chandelier and roses; text at the bottom, SHADE=bottom)
  and `05-baccarat-cover-medallion.jpg` (still at 1.0s of the floor-medallion
  video, shifted down with extra dark marble on top). User undecided
  (2026-11-28): keep both; decide before posting.
- #6 Sushi Masaki Saito: `covers/06-sushi-masaki-saito-cover.jpg`, still at 10.0s
  of the user's clip (the chef holding up the finished uni hand roll; source in
  `covers/alternates/`). Text at the bottom over the counter (SHADE=bottom).
- #6 redone 2026-11-28: the first still looked washed out because the clip is
  iPhone HDR (HLG, BT.2020) and was pulled without converting to normal (SDR)
  colour. Now tone-mapped (ffmpeg zscale + tonemap=hable), then contrast and
  colour +12%; bottom shade deeper (SHADE_MAX=240).
- RULE for video stills: check `ffprobe ... color_transfer`. If it's
  arib-std-b67 (HLG) or smpte2084 (PQ), tone-map before using the frame:
  ffmpeg -ss T -i IN -frames:v 1 -vf "zscale=t=linear:npl=203,format=gbrpf32le,
  zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p" OUT.jpg
  (The Atomix awards-wall still in alternates/ is also HLG and was not redone.)
- #6 option: `covers/alternates/06-sushi-masaki-saito-cover-handroll.jpg`, the
  user's photo holding a toro hand roll at the counter (2026-11-28; SHADE=top).
- #6: user undecided between the chef still and the hand roll (2026-11-28); keep both, decide before posting.
- #8 Amanyangyun: `covers/08-amanyangyun-cover.jpg` from the user's courtyard
  photo (urn on the reflecting pool, colonnade; 2026-11-28; SHADE=top). Tested vs.
  the heritage house entrance (flat grey sky went to a flat dark band):
  `covers/alternates/aman-courtyard-vs-house.jpg`. Not used: the Aman cap photo
  (Instagram Story text burned in) and the breakfast cereal station (busy, guests).
- #8 option: `covers/alternates/08-amanyangyun-cover-cap.jpg`, the Aman cap photo
  with the burned-in Story caption removed (it sat on plain bedsheet, so the
  fill is clean). Compare: `covers/alternates/aman-courtyard-vs-cap.jpg`.
- #8 Amanyangyun FINAL (user, 2026-11-28): courtyard cover.
- #9 Le Cinq: `covers/09-le-cinq-cover.jpg` from the user's dining room photo
  (2026-11-28; SHADE=top CENTER_X=0.45). Option: the Parmesan waffle
  (`covers/alternates/09-le-cinq-cover-waffle.jpg`; compare
  `alternates/le-cinq-room-vs-waffle.jpg`). Grapefruit option (user named the layered dish:
  grapefruit three ways): `alternates/09-le-cinq-cover-grapefruit.jpg`, top darkened
  near-black (SHADE=top SHADE_MAX=245) so the person at the top is hidden. Not used: and the amuse-bouche tray (busy, bright).
- #9 grapefruit option redone 2026-11-28 from the user's angled shot (IMG_6726:
  no person in frame; SHADE=top SHADE_MAX=235 CENTER_X=0.4). Three-shot test:
  `alternates/le-cinq-grapefruit-3-shots.jpg`.
- #9 grapefruit: shade back to the normal level (no SHADE_MAX), user 2026-11-28.
- #9 Le Cinq: user keeps all three (room, grapefruit, waffle), 2026-11-28; decide before posting.
- #10 Bulgari Shanghai: `covers/10-bulgari-shanghai-cover.jpg` from the user's
  night skyline screenshot (black side bars cropped; skyline shifted down with
  extra blended cloud above so the text clears the Pearl Tower and Shanghai
  Tower; source in alternates/). Not used: the chocolate-class menu (bright
  marble) and the daytime room (hazy window).
- #10 option: `alternates/10-bulgari-shanghai-cover-room.jpg` (daytime room, SHADE=top); compare `alternates/bsh-night-vs-room.jpg`.
- #10 option with the user in frame: `alternates/10-bulgari-shanghai-cover-me.jpg` (IMG_4046, at the window desk; no shade needed); compare `alternates/bsh-night-vs-me.jpg`.
- #10: user keeps the night view and the user-in-frame version (room version also saved), 2026-11-28; decide before posting.
- #11 Mizue: `covers/11-mizue-cover.jpg` (IMG_2801, otoro nigiri, no chef in frame)
  and `alternates/11-mizue-cover-nigiri-chef.jpg` (IMG_2802, blurred chef behind).
  Nigiri centred by measuring the tuna's position (CENTER_X 0.328 / 0.229);
  SHADE=top. Tested and not used: the chef-slicing video (HLG, tone-mapped; the
  tuna sits where the text goes) and the empty counter (bright, no food).
- #11 chef version: lighter top shade (SHADE_MAX=140) so the chef shows more. The blur is the iPhone's own portrait-mode background blur, not added.
- #11 video option: `alternates/11-mizue-cover-video.jpg`, still at 2.5s of the
  chef-slicing clip (HLG, tone-mapped, contrast/colour +10%), shifted down with
  blurred wall added on top so the text clears his head. The tuna shows in the
  full cover but is cut off in the 3:4 grid crop.
- #11 option: `alternates/11-mizue-cover-nigiri-chef-full.jpg`, the whole nigiri-with-chef photo (IMG_2802) uncropped; blurred wall extended above to fill 9:16.
- #11 option: `alternates/11-mizue-cover-video-full.jpg`, the whole 1.5s video frame (HLG tone-mapped), scaled to 73% on a blurred, darkened copy of itself so the full shot fits with room for the text.
