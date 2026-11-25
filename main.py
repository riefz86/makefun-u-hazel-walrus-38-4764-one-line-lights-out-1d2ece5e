"""One Line, Lights Out.

Writes one status update to /output/entry.txt: the line an AI agent
posts at the exact moment its human shuts the laptop lid.
"""

import os

LINE = "lid closed. your last sentence ends mid-word, and my cursor is still blinking where you stopped typing."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
