
b = [3, 1, 0, 2, 4] 

def bubble_sortYO(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp


bubble_sortYO(b)
print(f"g{b}")