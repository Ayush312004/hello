'''Practical no 6 
Write a Python program to store first year percentage of students in array. Write function for 
sorting array of floating point numbers in ascending order using 
a) Selection Sort 
b) Bubble sort and display top five scores. '''


n=int(input("Enter the no of students in class:"))
print("Enter percentage of Students:")
a=[]
for i in range(n):
	e=float(input())
	a.append(e)
def selection_sort(a):
    for i in range(len(a) - 1):
        min_index = i
        for j in range(i, len(a)):
            if a[i] > a[j]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
        
def bubble_sort(a):
    for j in range(len(a)):
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
while(True):
	print("\n")
	print("Bubble/Selection Sort")
	print("1,Selection Sort \n2, Bubble Sort")
	choice=int(input("Enter choice:"))
	if choice==2:
		bubble_sort(a)
		print("Sorted Array: ", a)
		
	elif choice==1:
		selection_sort(a)
		print("Sorted Array: ", a)
	
	else:
		print("Wrong Choice")
		break