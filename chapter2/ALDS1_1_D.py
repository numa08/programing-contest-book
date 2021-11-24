n = int(input())

minv = int(input())
maxv = -2000000000

for i in range(n - 1):
    num = int(input())
    maxv = max(maxv, num - minv)
    minv = min(minv, num)
print(maxv)
