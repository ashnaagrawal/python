from itertools import permutations

n = input()
d = int(input())

def multiple(a,b):
    p = str(n)
    p = ''.join(sorted(p))

    permlist = permutations(p)
    for i in list(permlist):
        str1 = ''.join(i)
        
        number = int(str1)
        if(number % d == 0):
            result = number
            break
        else:
            result = -1
    return result

print(multiple(n,d))
            

