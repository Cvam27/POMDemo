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
