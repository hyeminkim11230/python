
# S = map(int,input())

# a = list[S.Split()]
# i=0
# for i in range(0,20):
#     result = a[i]
#     if a[i]==0 or 1 :
#         result +=  a[i+1]
#     else :
#         result *=  a[i+1]


data = input()

result = int(data[0])

for i in range(1,len(data)) :
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
