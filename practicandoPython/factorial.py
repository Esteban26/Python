def factorial(n):
    """
    calcula el factorial de n 

    n int > 0
    return n!
    """
    if n == 1:
        return 1

    else:
        return n * factorial(n -1)

print(factorial(4))

# 4