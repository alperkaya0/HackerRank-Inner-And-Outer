import numpy

a = input().split(" ")

for x in range(len(a)):
    a[x] = int(a[x])

b = input().split(" ")

for x in range(len(b)):
    b[x] = int(b[x])


print(numpy.inner(a,b))
print(numpy.outer(a,b))
