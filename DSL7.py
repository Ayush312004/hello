def q(l, low, high): 
    if low < high: 
        p = partition(l, low, high) 
        q(l, low, p - 1) 
        q(l, p + 1, high) 

def partition(l, low, high): 
    pivot = l[low] 
    
    i = low 
    j = high 
    while i < j:  
        while l[i] < pivot: 
            i += 1 
        while l[j] > pivot: 
            j -= 1 
        if i < j: 
            l[i], l[j] = l[j], l[i]
    l[low], l[j] = l[j], l[low] 
    return j

n = int(input("Enter number of elements: ")) 
A = [int(input()) for i in range(n)] 
print("Before sort:", A) 
q(A, 0, n - 1) 
print("After sort:", A)

