import re

di1 = dict()
data = '''Jay,+919999999999,jay@xyz.com,11:22:33:44:55:66
Jatin,+898888888888,jatin@xyz.com,22:33:44:55:66:77
Keval,+917777777777,keval@xyz.com,33:44:55:66:77:88
Harshil,+911111111111,harshil@xyz.com,44:55:66:77:88:99
Priyanka,+912222222222,priyanka@xyz.com,55:66:77:88:99:00
Bhumika,+913333333333,bhumika@xyz.com,66:77:88:99:00:11
'''
sp_data = data.split()

size1 = len(sp_data)

for i in range(0, size1):
    name = re.findall(r"[A-Za-z]\w+", sp_data[i])
    other = re.findall(r"(\+.+)", sp_data[i])
    print(dict(zip(name, other)))
