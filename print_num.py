def printnum(n):
    if(n==1):
        print(1,end=' ')
        return 1
    printnum(n-1)
    print(n,end=" ")

n=int(input())
printnum(n)    
