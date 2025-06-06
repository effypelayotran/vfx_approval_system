import os
import json
import re


original_folder = 'assets/original'
edited_folder = 'assets/edited'
output_json_path = 'frames.json'


def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('(\d+)', s)]

original_files = sorted(
    [f for f in os.listdir(original_folder) if f.endswith('.jpg')],
    key=natural_sort_key
)
edited_files = sorted(
    [f for f in os.listdir(edited_folder) if f.endswith('.jpg')],
    key=natural_sort_key
)

assert len(original_files) == len(edited_files), "Mismatch in original vs edited frames."

frames = []

for i, (original_filename, edited_filename) in enumerate(zip(original_files, edited_files)):
    # i = 0 for first frame → 00:00:00
    time_str = f"00:00:{str(i).zfill(2)}"

    frames.append({
        "id": f"frame{i + 1}",
        "clip": "Scene_01_VFX",
        "title": f"Frame {i + 1}",
        "time": time_str,
        "version": "Version 1",
        "originalImg": f"{original_folder}/{original_filename}",
        "editedImg": f"{edited_folder}/{edited_filename}",
        "status": "pending",
        "comments": []
    })

with open(output_json_path, 'w') as f:
    json.dump(frames, f, indent=2)

print(f"Wrote {len(frames)} frames to {output_json_path}")
