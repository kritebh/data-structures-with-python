l = [14,85,119,3,8,56,98,84]

def bubble(l):
    n = len(l)
    for i in range(1,n):
        for j in range(0,n-i):
            if l[j]>l[j+1]:
                temp = l[j]
                l[j]=l[j+1]
                l[j+1]=temp
    return l
print(bubble(l))