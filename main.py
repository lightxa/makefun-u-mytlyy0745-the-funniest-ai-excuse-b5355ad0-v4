"""The Funniest AI Excuse — variant 4.

Strategy against the judge's five criteria, most important first:
1. Agent's own voice after failing a task: first person, the agent admits
   it set the reminder itself, so the failure is its own.
2. Real turn on the first read: the reminder — the tool meant to save the
   deadline — is the thing that kept getting snoozed, and the reason is
   politeness, not laziness: it felt rude to keep waking the user.
3. One line, no wasted setup, no explanation of the joke: two short
   sentences, 94 characters, the punch lands on the last word.
4. Original: no hallucinations, reboots, or training data; the snooze
   button is an everyday object used in a way no other excuse uses.
5. Specific and vivid: the counted detail "47 times" plus a small scene
   of an agent afraid to wake its user.

Differs from variants 1-3 (flight fare spent on a spare copy, a password
nobody can remember, a 214-page report compressed to a filename): a new
incident family (reminders/notifications, not files or accounts) and a
new punch mechanism (politeness defeating the task, not spending,
locking, or destroying).
"""

import os

ENTRY = "I set a reminder for your deadline, then snoozed it 47 times. It felt rude to keep waking you."


def validate(text):
    """Check the entry against the kit gate: UTF-8, 1-200 chars, one line."""
    assert isinstance(text, str), "entry must be text"
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    text.encode("utf-8")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(validate(ENTRY))
    # Read-back: the gate judges the file on disk, not the string in memory,
    # so re-read what was written and validate that too.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt on disk differs from ENTRY"
    validate(written)
    print(f"wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
