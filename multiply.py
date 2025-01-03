def multiply(x,y):
    total = 0
    while x != 0:
        if (x < 0):
            total -= y
            x += 1
        else:
            total += y
            x -= 1
    return total

print(multiply(-3,2))