
#this is decorator function
def deco(name_decorator):
    return name_decorator.upper()

def main_func(func):
    name_modifier = func("Testing")
    print(name_modifier)

main_func(deco)

def input_type(func):
    def timeit_wrapper(numtype):
        result = func(numtype)
        print(f'Value is {numtype}, Type of the value {result}')
        return result

    return timeit_wrapper


@input_type
def validate_datatype(num):
    value_type = type(num)
    return value_type


validate_datatype(1000.10)
validate_datatype(10)
validate_datatype('ABC')
validate_datatype(True)

'''Output
Value is 1000.1, Type of the value <class 'float'>
Value is 10, Type of the value <class 'int'>
Value is ABC, Type of the value <class 'str'>
Value is True, Type of the value <class 'bool'>
'''