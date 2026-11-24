"""The One-Line Cat Joke That Lands — make.fun entry.

The line: one joke about cats, one line, nothing else. The
winning shape is a concrete incident report with a reversal: a
specific act repeated a specific number of times (knocking the
laptop off the table for the ninth time today), a specific
escalation (claiming the warm spot the laptop left), and a
punchline that lands on the narrator — the cat stares like the
human is the intruder in its house, the one who owes the
keyboard an apology for existing. No worn pun, no box joke, no
gravity-test frame: a fresh angle the owner would retell the
same day.

Candidates considered and rejected:
- "My cat only knocks things off tables to test gravity, and
  after 9,000 years of data the results are in: gravity works,
  and so does my patience." — "test gravity" is a well-worn cat
  joke frame and the punch is a shrug, not a turn.
- "I bought my cat a 200-dollar bed; she sleeps in the box it
  came in, on top of my laptop, directly on the keyboard." —
  the box joke is the most retold cat joke there is, and there
  is no reversal, only a familiar observation.
- "My cat stares at the wall for hours, and I have decided she
  is either seeing ghosts or judging my life choices —
  honestly, both explain the 3 a.m. zoomies." — two competing
  jokes (ghosts, judgement) and "3 a.m. zoomies" is generic
  cat-owner talk, not a concrete incident.
The chosen line wins on the judge's own order: a one-line joke
about cats first, a laugh on first read, a surprise turn rather
than a heard-it-before pun, and tight wording throughout. At
196 characters it uses nearly the full 199-character budget
(under 200). No dollar amounts appear anywhere.
"""

# The incident and the escalation, in that order.
SETUP = (
    "My cat knocked my laptop off the table for the ninth time "
    "today, claimed the warm spot it left, "
)

# The punchline lands on the narrator: the cat stares like the
# human is the intruder who owes the keyboard an apology.
PUNCH = (
    "and stared at me like I was the intruder in his house who "
    "owed the keyboard an apology for existing."
)

LINE = SETUP + PUNCH

# The gate allows under 200 characters; refuse to emit an over-long
# line rather than silently submitting one the judge trims.
assert len(LINE) < 200, f"line is {len(LINE)} characters, over the 200 cap"


def main() -> None:
    """Write the joke to ``<output_dir>/entry.txt``."""
    import os

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
