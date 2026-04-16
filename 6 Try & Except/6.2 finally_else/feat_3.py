try:
    val = float(input())
except ValueError as e:
    print(e)
else:
    val *= 10
    print(val)
finally:
    print("finally")