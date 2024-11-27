import re

text = "The quick brown fox jumps over the lazy dog. The cat is also agile."
pattern = r'\b\w{3}\b'
matches = re.findall(pattern, text)
print(f"Words with exactly 3 letters in the text: {matches}")
