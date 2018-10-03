#Reversing the list
item = ['Asim', '21', '7 + i8','google', 'apple', 'facebook', 'microsoft', 'tesla']
print(item)
print(item[::-1])
#Extracting all thr uppercase letters from a string
strng = 'xsaxubDBWUDBdudDI'
print(''.join([A for A in strng if A.isupper()]))
print(strng.lower())
#Palindrone Number
n = int(input("Enter Number:"))
temp=n
rev=0
while (n>0):
	dig=n%10
	rev=rev*10+dig
	n=n//10
if(temp==rev):
	print("The entered number is a palindrone!")
else:
	print("The enetered number isn't a palindrone")
#type casting
Asim = '69.68.67'
xval, yval, zval  = Asim.split(".")
xval = int(xval)
yval = int(yval)
zval = int(zval)
print(xval)
print(yval)
print(zval)

#Understanding Deep and Shallow Copy
# Deep Copy :when a copy of an object is made for example
#list1=[1,2,3]
 
# and a deep copyis made of this list say list1=[1,2,3]
 #then the changes made inlist2 won't be reflected in list1.

 #shallow copy : when acopy on an object is made say list2  is the shallow copy of list1 from above example
 #then the changes made in lst2 will be reflected in list1.

  