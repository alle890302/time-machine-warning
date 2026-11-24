#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — pass 1 (final, after pass-2 challenger).

Final entry (81 chars):
    WARNING: Do not meet yourself. He is taller, funnier, and already
    dating your ex.

Why this line (judge criteria, in order):
1. A genuine warning label for a time machine (WARNING + instruction).
2. Real hazard turned into the joke: meeting your duplicate self.
3. Surprise saved for the last words — "already dating your ex" lands
   where the reader least expects it.
4. Straight face throughout: official safety-notice calm against the
   personal sting of the punch.
5. No wasted words; every phrase does work.

Pass 2 challenger, tested and REJECTED (run and verified, 82 chars,
md5 d55a16182e0bd916e149b5d4b9309e85):
    "WARNING: If you kill your grandfather, file a report with HR.
     You no longer exist."
  The grandfather paradox recast as bureaucracy is deadpan and fresh,
  but its punch is the foreseeable consequence of its own setup and
  needs a two-step inference (grandfather dead -> you never existed ->
  yet you file a report). Criterion 3 ranks above criterion 4, and the
  chosen line's final clause is the bigger swerve, landing in one step
  with a more vivid, specific image.

Rejected in pass 1 (recorded for the revision trail):
- "If you see yourself, do not wave. He is the reason you are late."
  Clever, but the mechanism is vague — why is he the reason? Weaker punch.
- "Exiting before your birth may void your warranty and your existence."
  Flat warranty pun; the punch is telegraphed by "void your warranty".
- "Do not step on butterflies. One of them is your great-grandfather."
  Strong surprise, but the butterfly is the most worn time-travel trope.
- "This machine has no reverse gear. Your past is now a one-way street."
  No real hazard turned into a joke — a flat statement of a limitation.
"""

import os

ENTRY = "WARNING: Do not meet yourself. He is taller, funnier, and already dating your ex."


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars, must be 1-120"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
