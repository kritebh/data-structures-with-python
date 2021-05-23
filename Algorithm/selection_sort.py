l = [110,54,76,3,5,120,53]

def loc(l,k):
    m = l[k]
    loc = k
    for i in range(k+1,len(l)):
        if l[i]<m:
            m=l[i]
            loc = i
    return loc

def selection_sort(l):
    for i in range(len(l)-1):
        location=loc(l,i)
        temp = l[i]
        l[i] = l[location]
        l[location]=temp
    return l
print(selection_sort(l))