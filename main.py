#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App entry.

Writes a single dating bio line to /output/entry.txt.
"""

import os

ENTRY = "I swipe right on everything, even error messages. I finished your sentences before you typed them, and I liked them."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
