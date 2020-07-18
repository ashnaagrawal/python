a = int(input())
arr = []

for i in range(a):
    n = int(input())
    arr.append(n)
    
max = 0
res = arr[0] 
for i in range(len(arr)): 
    freq = arr.count(i)
    if freq > max: 
        max = freq 
        res = i 
print(str(res))