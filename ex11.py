def factorial():
    result = 1 
    num = 5

    while num>0:
        result *= num
        num -= 1

    return result
result = factorial()
print result
