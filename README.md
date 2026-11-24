# One Emoji, One Dream Vacation

One emoji, one dream: an elephant on the African savanna at golden hour — a safari, the faraway trip you picture before you ever read a word.

[![Bounty](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35?utm_source=github&utm_medium=readme&utm_campaign=u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![Rank](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/cervus-snoopy/hazy-copper-lagoon-5t2k/rank.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![Reward](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/cervus-snoopy/hazy-copper-lagoon-5t2k/reward.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35?utm_source=github&utm_medium=readme&utm_campaign=u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)

## Why this angle

The field is flooded with desert islands and Mount Fuji. A safari is the
opposite of that flood: one specific faraway dream, instantly readable at
any size, and unmistakably a place — golden grass, a slow giant, a trip
you can already picture. It names a vacation no other entry in the field
names, in a single plain codepoint.

## What it does

`main.py` (Python 3, standard library only, no network) writes exactly one
emoji to `$MAKEFUN_OUTPUT_DIR/entry.txt`: a single elephant, four UTF-8
bytes, no trailing newline, mode `0644`. The program validates the entry
before writing — one character, one codepoint, 1–8 UTF-8 bytes, not
whitespace, no ZWJ sequence, no variation selector — then reads the file
back from disk and validates what actually landed.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Verify

```sh
python3 -c "data = open('/tmp/out/entry.txt', 'rb').read(); print(len(data), data)"
```

Expect 4 bytes, one character, no trailing newline.
