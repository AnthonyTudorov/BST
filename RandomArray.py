from random import uniform


def getRandomArray(n):
    randSet = set()
    i = 0
    while i < n:
        num = uniform(-n, n)
        if num not in randSet:
            randSet.add(num)
            i += 1
    return list(randSet)


# print(getRandomArray(5))
