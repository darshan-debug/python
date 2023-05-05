from math import gcd
t=int(input())
for i in range(0,t):
    a,b=map(int,input().split())
    if(a==b):
        print(0,0)
        continue
    maxgcd=abs(a-b)
    if((a)%maxgcd==0 or (b)%maxgcd==0 ):
        print(maxgcd,0)
    else:
        for i in range(1,maxgcd+1):
            if((a+i)%maxgcd==0 or (b+i)%maxgcd==0 ):
                c1=i
        for i in range(1,maxgcd+1):
            if((a-i)%maxgcd==0 or (b-i)%maxgcd==0 ):
                c2=i
        print(maxgcd,min(c1,c2))
    

    
    