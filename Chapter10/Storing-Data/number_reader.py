from pathlib import Path
import json

path = Path('Chapter10/Storing-Data/numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)
