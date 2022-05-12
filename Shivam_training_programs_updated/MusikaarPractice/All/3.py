'''3.	Write a program that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order with first character of each word in capital. For example :
	Input:  your name is xyz,
        	Output:  Xyz Is Name Your
'''

name = str(input("Enter string: "))
split_name = name.split()
cap_name = []
for i in split_name:
    cap_name.append(i.capitalize())
print(" ".join(cap_name[::-1]))



'''
output
Enter string: testing
Testing

'''