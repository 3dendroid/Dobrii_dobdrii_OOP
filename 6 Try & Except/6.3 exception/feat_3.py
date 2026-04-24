def input_int_numbers():
    digits = input().split()
    try:
        res = []
        for x in digits:
            if not (x.isdigit() or (x.startswith('-') and x[1:].isdigit())):
                raise TypeError('все числа должны быть целыми')
            res.append(int(x))
        return tuple(res)
    except ValueError:
        raise TypeError('все числа должны быть целыми')

try:
    result = input_int_numbers()
except TypeError:
    result = ()




