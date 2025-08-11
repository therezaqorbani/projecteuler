def multiples(n):
    j = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            j += i
    return j


print(multiples(1000))
