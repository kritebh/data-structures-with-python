data = [23,76,3,6,1,5,4,8]

for i in range(len(data)):
    temp=data[i]
    j=i-1
    while j>=0 and temp<data[j]:
        data[j+1]=data[j]
        j=j-1
    data[j+1]=temp    
    
print(data)