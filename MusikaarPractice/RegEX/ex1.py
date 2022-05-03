import re

word = 0
digit = 0
special = 0
data_file = open("../RegEX/test_data.txt", "r").read()
# pattern_for_digit = r"[\d]"
# pattern_for_string = r"[a-zA-Z]"
main_pattern = r"[^\n]"

search_string = re.findall(main_pattern, data_file)
print(search_string)

for i in search_string:
    if re.search(r"[a-zA-Z]", i):
        word += 1
    elif re.search(r"\d", i):
        digit += 1
    elif re.search(r"\W", i):
        special += 1

#
print("words are : ", word)
print("digits are : ", digit)
print("special chars are : ", special)
