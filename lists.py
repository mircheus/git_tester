a = [int(i) for i in input().split()]
b = []
i = 0
k = len(a)
for i in range(k):
    if i != k-1:
        if i != 0:
            sum = a[i - 1] + a[i + 1]
            b.append(sum)
        else:
            sum = a[i+1] + a[k-1]
            b.append(sum)
    else:
        sum = a[i-1] + a[0]
        b.append(sum)

for i in b:
    print(i, end=' ')
