n = int(input())
max = n
while n != 0:
    if n > max:
        max == n
    n = int(input())
print(max)


n = int(input())
max = n
k = 1
ind = 1
while n != 0:
    if n > max:
        max = n
        ind = k
    n = int(input())
    k += 1
print(ind)