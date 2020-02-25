from random import uniform


def getRandomArray(n):
    randSet = set()
    for i in range(n):
        randSet.add(uniform(-n, n))
    return list(randSet)


print(getRandomArray(5))
