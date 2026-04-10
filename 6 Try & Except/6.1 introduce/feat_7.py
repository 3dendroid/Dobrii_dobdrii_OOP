lst_in = input().split()

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

print(sum(map(int, filter(is_int, lst_in))))