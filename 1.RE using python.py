import re
text = "The rain in Spain falls mainly in the plain."
# Regular expression pattern
pattern = r'\b\w*ain\b'
# Match at the start of the string
match = re.match(pattern, text)
print("Match at start:", match)
# Search for the first occurrence
search = re.search(pattern, text)
print("First occurrence:", search.group() if search else None)
# Find all occurrences
all_matches = re.findall(pattern, text)
print("All occurrences:", all_matches)
