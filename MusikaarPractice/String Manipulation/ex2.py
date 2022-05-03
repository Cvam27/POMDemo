import re
words = "This is test, test belongs to automation. This is new automation"
new_words = re.findall(r"\w+", words)


li2 = []

print(new_words)

for i in new_words:
    if i not in li2:
        li2.append(i)

print(li2)



























a = words.split(",")
b = a[0].split() + a[1].split()

for i in b:
    if i not in li2:
            li2.append(i)