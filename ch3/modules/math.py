PI = 3.14159

def add(val1, val2):
    return val1 + val2

def sub(val1 , val2):
    return val1 - val2


print(__name__)

if(__name__ == "__main__"):
    var1 = 10
    var2 = 20

    sum = add(var1, var2)

    print(f'Sum of {var1} and {var2} is \"{sum}\"')