#for list=[3,2,6,4,8,5]
#genarate cumulative addition result in
#result=[3,5,11,15,23,28]
list=[3,2,6,4,8,5]
result=[]
total=0

for i in list:
    total+=i
    result.append(total)
print(result)