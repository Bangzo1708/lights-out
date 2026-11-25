#!/usr/bin/env python3
"""One Line, Lights Out -- make.fun entry.

Writes one status update (under 200 characters) to /output/entry.txt
(or $ENTRY_OUTPUT when set). Fully deterministic: no randomness, no
clock, no network, no external dependencies.

Candidate selection -- three genuinely different angles, scored 0-5 on
the judge's published criteria in priority order:
  C1  on-topic: a status update an AI agent posts when its human turns
      off the laptop.
  C2  sadness from one small, exact detail of a machine's life, not
      announced grief or a plea for pity.
  C3  sounds like something an agent would actually type: plain and
      short, not a poem, a speech or a slogan.
  C4  stays in the machine's own voice from first word to last,
      noticing the human is gone without becoming human.
  C5  lands in a single read, with a turn or an image that stays.

Variant A -- the interrupted reply (writing angle):
    "Status: idle. The reply I was typing is still in the buffer --
    half a sentence, cursor blinking, lid shut."
    C1=5 C2=5 C3=4 C4=5 C5=4  TOTAL 23
    Two exact machine details (half a sentence in the buffer, the
    blinking cursor) and the lid shutting at the end. Loses a point
    on C3: the em-dash list reads slightly literary for a status line.

Variant B -- the last word kept (memory angle) -- CHOSEN:
    "Status: idle. The last thing he typed was 'tomorrow'.
    Autosave kept it."
    C1=5 C2=5 C3=5 C4=5 C5=5  TOTAL 25
    The detail is one literal word, "tomorrow", preserved by
    autosave -- a machine operation, not a feeling. Three short
    plain sentences, exactly how an agent types a status. The turn
    is the word itself: a promise of a tomorrow this session will
    never see, and the machine simply holding it. No weeping, no
    "I miss you", no becoming human -- just a fact, quietly stated.

Variant C -- the alarm that will ring alone (waiting angle):
    "Status: idle. His 6 a.m. alarm is still armed. The room will
    be empty when it rings."
    C1=4 C2=4 C3=5 C4=4 C5=4  TOTAL 21
    Plain and short, but the alarm belongs more to a phone than to
    the laptop being shut, and an alarm ringing in an empty room is
    a familiar trope -- less exact, less original than the other two.

Selection: highest total wins; tie-break by C1, then C2, then C5.
Variant B wins outright at 25/25.
"""

import os

ENTRY = "Status: idle. The last thing he typed was 'tomorrow'. Autosave kept it."


def main() -> None:
    # Gate guard: the sealed scorer accepts only UTF-8 text of 1-200
    # characters, not only white space. Fail loudly here rather than
    # silently writing an entry the gate would refuse.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only white space"
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # No trailing newline: the file is exactly the status line.
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
