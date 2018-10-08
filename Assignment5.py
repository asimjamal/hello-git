year = int(input('Enter Year:'))
if (year % 4 == 0):
	print("Leap Year")
else :
	print('Not a Leap Year')
lenght1 = int(input('Enter 1st Dimension:'))

lenght2 = int(input('Enter 2nd Dimension:'))
if (lenght2==lenght1):
	print('It is a Square')
else:
	print("It is a rectangle")	
age1 = int(input('Enter 1person age:'))
age2 = int(input('Enter 2person age:'))
age3 = int(input('Enter 3person age:'))

if (age1 > age2 and age1 > age3):
		print('Person 1 is the oldest')
		if (age2 > age3):
			print('Person3 is youngest')
		else:
			print('Person2 is youngest')
elif( age2 > age3 and age2 > age1):
	print('Person2 is oldest')
	if(age1 > age3):
	   print('Person3 is youngest')
	else:
		print('Person1 is youngest')
else:
    print('Person3 is oldest')

    if (age1 > age2):
        print('Person2 is youngest')
    else:
        print('Person 1 is youngest')

    
age = int(input('Enter Age:'))
sex = str(input('Enter Sex(M/F):'))
mrrg = str(input('Enter Maritial Status(Y/N):'))
if (sex == 'F'):
	print('Work in Urban Areas only')
elif (sex == 'M' and 20<age<40):
	print('He is allowed to work anywhere')
elif (sex == 'M' and 40<age<60):
	print('He is allowed to work in Urban areas')
else:
	print('ERROR')

quantity = int(input('Enter Quantity:'))
cbd = quantity*100
print('Cost before discount is :',cbd)
cb = cbd*0.10
fc = cbd-cb
if(cbd > 1000):
     print('Final Cost:',fc)
else:
	print('Final Cost:',cbd)

for i in range(0, 10):
    i = int(input('Enter Number:'))

#while(1==1):
	#print('star')
out_list1 = []
out_list2=[]
first=int(input("enter 1st num:"))
second=int(input("enter 2nd num:"))
third=int(input("enter 3ed num:"))
out_list1.append(first)
out_list1.append(second)
out_list1.append(third)

for i in out_list1:
	out_list2.append(i*i)

print(out_list2)	
our_list = [23, 'tring',1.23,20,'nazia']
str_1=[]
int_1=[]
flt_1=[]
for i in our_list:
     if type(i) == int:
        int_1.append(i)
     elif type(i) == str:
        str_1.append(i)
     elif type(i) == float:
        flt_1.append(i)

print(int_1)
print(str_1)
print(flt_1)

primes = [j for j in range(1,101) if 0 not in [j%i for i in range(2, int(j/2)+ 1) ]]
print(primes)

for i in range(0, 5):
    for j in range(0, i+1):
        print("* ", end="")
        print()
    

list_1=[]
for i in range(0,5):
 	ele= int( input("enter numbers:") )
 	list_1.append(ele)
print(list_1)
new_num=int(input("enter num to be deleted:"))

for i in list_1:
	if i==new_num:
		list_1.remove(i)

print(list_1)

