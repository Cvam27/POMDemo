'''6.	Write a program read a text file and count number of words and new line characters from the file.'''

import re

with open("f1.txt", "a+") as f:
    f.write("Test1, test2, testtttt" + "\n")

with open("f1.txt", "r") as f:
    spl = f.read()
    perword = spl.split()
    print("Words are : ", len(perword))
    print("New line are : ", len(re.findall(r"\n", spl)))


'''
output
Words are :  19
New line are :  5

'''