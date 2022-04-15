import re

pass_list = []
for i in range(1, 6):
    passwrd = input(f"Enter password {i} : ")
    pass_list.append(passwrd)

valid_pass = []
invalid_pass = []

for j in pass_list:
    if re.findall(r"[A-Z]", j) and re.findall(r"[a-z]", j) and re.findall(r"[\w]"r"[\d]", j) and (8 <= len(j) <= 12):
        valid_pass.append(j)
    else:
        invalid_pass.append(j)

print("Valid Passwords are : \n", valid_pass)
print("Invalid Passwords are: \n", invalid_pass)
