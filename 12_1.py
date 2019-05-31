def solution(N, M):
    if M==1: return(N)
    if N==1 or N==M: return(1)
    if M>N: M = M % N
    c = pos = 0
    current = N
    while (current%M!=0) or (c==0):
        current=N-pos
        c += 1+(current//M)
        pos = M-(current%M)
    return(c-1)