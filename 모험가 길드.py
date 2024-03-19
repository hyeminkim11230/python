# N = int(input())
# M = map(int,input().split())

# result = sorted(M)
# print(result)
# while True:
#     if result[0]<=1 :
#         N -= 1
#     elif result[N-1]<N :
#         N -= result[N-1] 
#     else :
#         pass


n = int(input())
data = list(map(int,input().split()))
data.sort()

result=0
count=0

for i in data:
    count +=1
    if count >=i:
        result +=1
        count = 0

print(result)




