# Upload kit for regular Claude (claude.ai)

Made 2026-11-28 from this repo.

## 1. Skills (one ZIP each)
`skills/ig-*.zip`. On claude.ai (web): Customize -> Skills (older pages: Settings ->
Capabilities) -> "+" -> Create skill -> Upload a skill. Upload each ZIP. Turn on code
execution: ig-reel, ig-human, ig-caption and others run small Python scripts.

Changes from the repo copies: ig-viral, ig-plan, ig-audit and ig-repurpose each carry
their own copy of `hooks.json` (on claude.ai a skill may not be able to read another
skill's files); ig-viral's swipe.py looks for it next to itself first.

## 2. Project for your rules
Create a Project (e.g. "Stars n Suites"). Upload everything in `project-files/`.
Paste `project-instructions.txt` into the Project's instructions.

## 3. Keeping it current
These are copies. When rules or scripts change in the repo, re-upload the changed files.
