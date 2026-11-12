# Striver A2Z sheet parser

A utility script to extract and clean sections from a Next.js raw data payload and parse them into a clean, structured JSON file format.

## Features
- Extracts JSON array payloads nested inside markdown files.
- Automatically handles unescaping of double quotes (`\"`) and backslashes (`\\`).
- Outputs a clean JSON file structure representing DSA sheet sections.

## Usage
1. Open `parse_striver.py` and modify the input `path` to point to your raw data markdown file.
2. Update the output path to point to your target JSON file location.
3. Run the script using Python:
   ```bash
   python parse_striver.py
   ```

.....
