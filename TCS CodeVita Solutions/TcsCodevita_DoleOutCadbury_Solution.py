T = int(input())

def count_for(a,b):
    min_side = min(a,b)
    max_side = max(a,b)

    if(min_side == 0):
        return 0 
    if(min_side == 1):
        return a*b

    total = max_side // min_side 
    new_side = max_side % min_side
    total = total + count_for(new_side,min_side)
    return total


for case in range(T):
    P,Q,R,S = list(map(int, input().split()))
    ans = 0
    for i in range(P , Q+1):
        for j in range (R, S+1):
            ans = ans + count_for(i,j)

    print(ans)

