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



'''
output

Enter password 1 : asda@#SF1213
Enter password 2 : 123SDF4dfsdf
Enter password 3 : 23234234234
Enter password 4 : 234SDFwf$%#$%53#%@#$
Enter password 5 : sdf435dgdfg##
Valid Passwords are : 
 ['asda@#SF1213', '123SDF4dfsdf']
Invalid Passwords are: 
 ['23234234234', '234SDFwf$%#$%53#%@#$', 'sdf435dgdfg##']

'''