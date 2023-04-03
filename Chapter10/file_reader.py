from pathlib import Path

path = Path('Chapter10/pi_digits.txt')
contents = path.read_text()
print(contents)
