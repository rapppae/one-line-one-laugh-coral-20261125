"""One Line, One Laugh — make.fun entry.

Entry text: 126 characters (limit 200).
"""

import os

ENTRY = "I told my AI assistant to act more human, so now it sighs, says 'per my last email,' and blames the Wi-Fi like the rest of us."


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
