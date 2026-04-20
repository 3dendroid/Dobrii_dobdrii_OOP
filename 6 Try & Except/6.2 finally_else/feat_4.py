result = None

try:
    a, b = input().split()
    try:
        result = int(a) + int(b)
    except ValueError:
        try:
            result = float(a) + float(b)
        except ValueError:
            result = a + b

except Exception as e:
    print(e)

finally:
    print(result)

