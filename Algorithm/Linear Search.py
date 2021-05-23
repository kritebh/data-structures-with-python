num = []
for i in range(1,100000):
    num.append(i)
print(num)
k = 99999
step = 0
for i in range(len(num)):
    if num[i]==k:
        print(f"{k} found at {i}")
    step = step +1
print(step)
