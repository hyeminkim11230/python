import sys

# data=sys.stdin.readline().rstrip()

# n = int(input)
# N,K = map(int,input().split())1

       
# if N % K != 0 :
#     N -= 1
#     j += 1

# for i in range(1,50):
#     N = N // K
#     j += 1
#     if N == 1 : 
#         print(j)
#         break

result = 0
n,k=map(int,input().split())
while True:
    
    target =(n//k) * k
    result +=(n-target)
    n = target

    if n<k:
        break
    result += 1
    n //= k

result += (n-1)
print(result)




