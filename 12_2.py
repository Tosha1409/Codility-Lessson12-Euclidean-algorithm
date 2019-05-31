def gcd(x,y):
    if x%y==0:
        return(y)
    else:
        return gcd(y, x%y)

def solution(A, B):
    Z=len(A)
    counter=Z
    C=[]
     
    for x in range (0,Z):
        C.append(gcd(A[x],B[x]))
        
    for x in range (0,Z):    
        a,b,c=A[x],B[x],C[x]
        while True:
            d = gcd(a, c)
            if 1 == d:
                break
            a /= d
        while True:
            d = gcd(b, c)
            if 1 == d:
                break
            b /= d
        if (a !=1 ) or (b!=1): counter -=1

    return(counter)