num = []
for i in range(1,100000):
    num.append(i)
# print(num)
k = 999999
low = 0
high = len(num)-1
step =0

while low <=high:
    mid = (low+high)//2
    if num[mid]==k:
        print("Found")
        break
    elif num[mid]>k:
        high = mid-1
    elif num[mid]<k:
        low = mid+1
    step=step+1
print(step)
