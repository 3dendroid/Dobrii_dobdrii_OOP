try:
    x, y = map(int, input().split())
    res = x / y

except ValueError:
    print("ValueError")
except:
    print("ZeroDivisionError")

print("Done")
