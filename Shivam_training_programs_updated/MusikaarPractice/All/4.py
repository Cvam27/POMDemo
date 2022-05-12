'''4.	Write a one line program which outputs the summation of cube of all the odd numbers from 0 to 300 using lambda, map, reduce and filter concept.  '''

total = sum(map(lambda x: x ** 3, filter(lambda y: y % 2 != 0, range(0, 300))))

print(total)


'''
output

1012477500
'''