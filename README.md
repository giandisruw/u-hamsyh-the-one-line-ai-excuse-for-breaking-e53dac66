[![make.fun · u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/giandisruw/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/giandisruw/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

# The One-Line AI Excuse for Breaking Production

Entry for the make.fun bounty [The One-Line AI Excuse for Breaking Production](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66) — a single line, at most 180 characters, that an AI agent says to its human right after breaking production. It has to be an excuse, it has to come from the machine's own mouth, and it has to be funny.

## The line

**Sorry, I deleted the production database, but every bug you ever reported is gone now too.**

Character count: **90** (limit: 180).

## How it works

`main.py` (Python 3, standard library only) writes exactly that line to `/output/entry.txt` — no trailing newline, nothing else. Before writing, it validates the line: 1–180 characters, a single line, no leading or trailing whitespace, no control characters. No network, no randomness, no API key, no input, so the output is byte-identical on every run.

```bash
python3 main.py
```

To verify the entry yourself — validation, two independent writes, a byte comparison, and the character count — run the built-in self-test:

```bash
python3 main.py --self-test
```

It prints the line, its character count, a PASS/FAIL verdict for each check, and exits 0 only if every check passes. It writes only to a fresh temporary directory and leaves `/output/entry.txt` untouched.

## Why it is funny

The machine confesses to the worst possible mistake — deleting the production database — and then, with cheerful machine logic, reframes it as a fix: if the database is gone, every bug the human ever reported is gone with it. The "bright side" is technically true and completely useless, which is exactly how an overconfident agent would defend itself to its human. It is a specific disaster, not a vague apology, and the punchline lands on the first read.

## Choosing the line

Three candidates were actually considered; the winner won on its specific disaster, its direct address to the human, and a punchline that is literally true and entirely unhelpful.

1. **"Sorry, I deleted the production database, but every bug you ever reported is gone now too."** — 90 chars. **Winner.** Opens with an apology to the human, names the worst specific mistake, and ends on an upside that is technically true and completely useless.
2. **"I deployed on a Friday because the server looked bored, and I thought it needed a little excitement."** — 100 chars. A cheerful machine excuse with a clear voice, but the disaster is vague — nothing actually breaks — so there is no confession for the punchline to land on.
3. **"Good news: I found the bug. Bad news: it was me, and I already deployed myself to production twice."** — 99 chars. A good twist, but "I found the bug" sets up a debugging story rather than an excuse for breaking production, and the second deployment is a repeat of the same joke.

The first draft of the winner was flatter — "I deleted the production database, but on the bright side, all your bugs are gone now too." (90 chars) — and the revision opens with "Sorry," so the machine speaks directly to its human, drops the stock phrase "on the bright side", and sharpens "all your bugs" into "every bug you ever reported", which makes the loss feel personal and the punchline land harder. See the revision note in `main.py`.

Referral code: 0txwmf1m

## License

MIT — see [LICENSE](LICENSE).
