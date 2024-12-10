n = int(input("Enter no. of students attended Training Program:")) 
print("Enter roll no.s in Sorted order") 
l = [] 
for i in range(n): 
    e = int(input()) 
    l.append(e)

def Binary(l, n): 
    key = int(input("Enter the roll no. to be search:")) 
    low = 0 
    high = n - 1 
    while(low <= high): 
        mid = (low + high) // 2
        if(key == l[mid]): 
            return mid 
        elif(key < l[mid]): 
            high = mid - 1 
        else: 
            low = mid + 1 
    return -1 

def Fibonacci(l, n): 
    key = int(input("Enter the roll no. to be search:")) 
    a = 0 
    b = 1 
    f = a + b 
    while(f < n): 
        a = b 
        b = f 
        f = a + b 
    offset = -1 
    while(f > 1): 
        i = min(offset + a, n - 1) 
        if(l[i] < key): 
            f = b 
            b = a 
            a = f - b 
            offset = i 
        elif(l[i] > key): 
            f = a 
            b = b - a 
            a = f - b 
        else: 
            return i 
    if(b and l[offset + 1] == key): 
        return offset + 1 
    return -1 

while(True): 
    print("\n") 
    print("Binary/Fibonacci search") 
    print("1. Binary Search\n2. Fibonacci Search") 
    choice = int(input("Enter choice:")) 
    if choice == 1: 
        a = Binary(l, n) 
        if a == -1: 
            print("Element not Found") 
        else: 
            print("Element Found at location:", a) 
    elif choice == 2: 
        a = Fibonacci(l, n) 
        if a == -1: 
            print("Element not Found") 
        else: 
            print("Element Found at location:", a)  
    else: 
        print("Wrong Choice") 
        break
