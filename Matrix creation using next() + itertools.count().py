import itertools

N = 4

print("The dimension : " + str(N))

temp = itertools.count(1)
res = [[next(temp) for i in range(N)] for i in range(N)]

print("The created matrix of N * N: " + str(res))