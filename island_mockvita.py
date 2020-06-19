#get input of number of cases
case=int(input())


#for each case, find the coins required
for i in range(1,case+1):
    #get input of value
    value=int(input())
    
    #count the number of coins 
    #logic number of coins required will be one more than the earlier rupee value that was a power of 2
    
    #set coin counter at 0
    count = 0
    while value>=1:
        value=value//2
        count=count+1
        
        #print the answer    
    print (count)