# Workflow for every reel

Saved 2026-11-22. Built from what came up on Providence, Atomix, Banbo and
Bulgari Tokyo. "Claude" steps happen in a session on this repo; "You" steps
happen on your phone or computer.

## 1. Prep (Claude, ~5 min)
- [ ] Pull the place's notes from `backlog.md`.
- [ ] Verify stars / Keys and any award the script will mention, with sources.
- [ ] Check the three talking points are covered (restaurants: Food, Service,
      Experience; hotels: Room, Service, Amenities). Ask you for any gap.
- [ ] Pick the hook technique (list in `voice.md`; suggestions in `backlog.md`).

## 2. Script (you write it, or Claude drafts it)
- [ ] Hook: score it (`hookscore.py`), aim for STRONG and 8-10 words.
- [ ] Time it (`beats.py`), aim for 30-45s.
- [ ] Humanizer (`/ig-human`), aim for PASS.
- [ ] Facts in the script match the notes and the verified sources.
- [ ] Open sign-off is fine ("...the next one just might be").
- [ ] Saved to `reels/NN-place.md` and committed.

### What makes a script better (learned 2026-11-22)
- Lead with the payoff number and a promise ("$2,400 for dinner for two.
  Here's what you actually get.") rather than the same "I paid $X... worth
  it?" every time. Rotate the hook techniques.
- Contractions and "I / you / we" (the humanizer's biggest factor).
- Each talking point gets a reaction, not a label ("and you can feel it",
  "not one miss").
- End on a line that repeats a word from the hook, so the reel loops.
- Cut lines that repeat the verdict ("the entire experience was amazing").
- Keep each line under ~4s, or plan a shot change inside it.

## 3. Shot list (Claude)
- [ ] One shot per line from the footage you have; a new shot every 1-2s.
- [ ] Whatever is ON SCREEN matches what is SAID (Atomix lesson: don't say
      "World's 50 Best" over the North America's 50 Best trophy).
- [ ] Flag any line with no footage.

## 4. Record the voiceover (you)

## 5. Edit in CapCut (you)
- [ ] Canvas 1080x1920 (9:16).
- [ ] Hook text on screen from frame 1, with movement in the first shot.
- [ ] Captions word by word, key word in red, sitting at about 65-70% of the
      frame height. Keep text between y=230 and y=1440 of 1920 and clear of
      the right 230px (Instagram's buttons and caption cover the rest).
- [ ] On-screen cards: 6 words or fewer.
- [ ] Photos: slow keyframe zoom, no more than ~130%.
- [ ] Verdict card in red at the end ("Worth it? NO" style).
- [ ] Delete the CapCut end card.
- [ ] Export for posting: 1080x1920, H.264, 30fps, ~5,000-8,000 kbps
      (third-party guides; not confirmed by Instagram).
- [ ] Export a review copy: 720p, lowest bitrate, under 30 MB.

## 6. Review (Claude)
- [ ] You upload the 720p review copy.
- [ ] Claude pulls frames and the captions, then checks: on-screen facts,
      shot/words match, caption position, end card, length.
- [ ] The as-made script is saved to the reel's file.
- Claude can't hear audio; captions are the transcript.

## 7. Caption and cover (Claude, then you)
- [ ] `/ig-caption`: first line survives the "...more" cut, one ask, hashtags
      below the fold, then humanizer.
- [ ] Cover: `[PRICE] [THING]. WORTH IT?`, text in the centre for the 3:4 grid crop.

## 8. Before posting (you)
- [ ] Re-check stars / Keys on guide.michelin.com that week.
- [ ] Tag the restaurant or hotel; set the location.
- [ ] Turn on Instagram's highest-quality upload setting.
- [ ] Post or schedule (Meta Business Suite); about 2 a week.

## 9. After posting
- [ ] Tell Claude it's posted: log it in `log.md` (date, hook technique, first line).
- [ ] Reply to comments (`/ig-reply`).
- [ ] After 4-5 reels: paste Insights (watch time, sends per reach) into
      `/ig-audit` and adjust the order and hooks.
