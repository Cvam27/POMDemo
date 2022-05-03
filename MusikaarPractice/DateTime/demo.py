import re

test = "this is )("
print(re.findall(r"\b.+\w", test))
