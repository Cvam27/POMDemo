import re

str = open("../RegEX/test_data.txt", "r").read()

pattern = re.compile(r"am")
search = pattern.finditer(str)
for i in search:
    print(search)
