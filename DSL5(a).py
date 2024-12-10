n=int(input("Enter no of students attended training program:"))
print("Enter roll no in random order")
l=[]
for i in range (n):
	e=int(input())
	l.append(e)

def linear(l,n):
	key=int(input("Enter roll no to be search"))
	
	for i in range(0,n):
		if(l[i]==key):
			return i
	return -1

def sentinel(l,n):

	key=int(input("Enter the roll no to be search"))
	last=l[n-1]
	l[n-1]=key
	for i in range(0,n):
		if(l[i]==key):
			return i
	return -1

while(True):
	print("\n")
	print("Linear/sentinel search")
	print("1.Linear search\n2.sentinel search")
	choice=int(input("Enter choice:"))
	if choice==1:
		a=linear(l,n)
		if(a==-1):
			print("Element not found")
		else:
			print("Element found at location",a)
	elif choice==2:
		a=sentinel(l,n)
		if(a==-1):
			print("Element not found")
		else:
			print("Element found at location ",a)
	else:
		print("wrong choice")
		break
