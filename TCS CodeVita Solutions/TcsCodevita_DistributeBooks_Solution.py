

def swap(m):
    if(m==1):
        return 0
    if (m==2):
        return 1
    if (m==0):
        return 1
    return (m-1)*(swap(m-1)+swap(m-2))

n = int(input())
if(n>0 and n<1000000):
    print(swap(n))




