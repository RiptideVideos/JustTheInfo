import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.json")

with open(file_path, 'r') as f:
    data = json.load(f)

old_story = data["story1"]['text']