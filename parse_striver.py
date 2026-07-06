import re
import json

path = r"C:\Users\traya\.gemini\antigravity\brain\f30557f1-256e-4b6d-91cb-b5e844c38fc1\.system_generated\steps\1970\content.md"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# We look for the "sections":[...] pattern in the file
# Since next.js payload escapes quotes like \", we need to parse it carefully
# Let's find "sections":
start_idx = content.find('"sections":')
if start_idx == -1:
    # Try with escaped quotes
    start_idx = content.find('\\"sections\\":')

if start_idx != -1:
    print("Found sections start at:", start_idx)
    # Let's find the matching bracket [ ]
    # First, let's extract from the bracket
    bracket_start = content.find('[', start_idx)
    if bracket_start != -1:
        # We need to count brackets while ignoring escaped characters
        bracket_count = 0
        in_string = False
        escape = False
        parsed_chars = []
        for i in range(bracket_start, len(content)):
            char = content[i]
            parsed_chars.append(char)
            if escape:
                escape = False
                continue
            if char == '\\':
                escape = True
                continue
            if char == '"':
                in_string = not in_string
                continue
            if not in_string:
                if char == '[':
                    bracket_count += 1
                elif char == ']':
                    bracket_count -= 1
                    if bracket_count == 0:
                        break
        
        json_str = "".join(parsed_chars)
        print("Extracted string length:", len(json_str))
        
        # Let's clean the string because it has escaped quotes like \"
        # We can unescape it
        try:
            # Let's wrap it in a dummy dict to let json.loads handle unescaping if we load it as a raw string,
            # or just replace '\\"' with '"' etc.
            # Actually, the entire next.js chunk is a JSON string itself inside a JS call.
            # Let's write a simple replacement:
            clean_str = json_str.replace('\\"', '"').replace('\\\\', '\\')
            data = json.loads(clean_str)
            print("Successfully parsed JSON array with", len(data), "sections!")
            
            # Let's write the parsed sections to a clean JSON file
            output_path = r"e:\java interview projwct\src\main\resources\frontend\striver_a2z.json"
            with open(output_path, "w", encoding="utf-8") as out_f:
                json.dump(data, out_f, indent=4)
            print("Saved clean JSON to:", output_path)
            
        except Exception as e:
            print("Error parsing clean string:", e)
            # Let's try another way: parse the whole next.js push lines as a json stream
            # We can find line with "sections"
            print("Sample clean_str around error:")
            print(clean_str[:200])
            print("...")
            print(clean_str[-200:])
else:
    print("Could not find sections in the content file.")
