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
bubble(l)
def interpolation_search(l,k):
    high = len(l)-1
    low = 0
    while low<=high and k>=l[low] and k<=l[high]:
            pos = low+int(((high-low)/(l[high]-l[low])*(k-l[low])))
            if l[pos]==k:
                return pos
            if l[pos]<k:
                low=pos+1
            if l[pos]>k:
                high=pos-1
            
print(interpolation_search(l,119))