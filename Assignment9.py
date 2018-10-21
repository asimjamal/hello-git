# a=3
# try:

#     if a<4:
#     	 a=a/(a-3)
#     	 print(a)

  
   

# except:
#  	print("a should not be 3")
# Zero Division error
# try:
# 	l = [1,2,3]
# 	print(l[3]) 

# except IndexError:
# 	print("index shoud range between 0 to 2")

 

# Index error
# try:
# 	raise NameError("Hi there")  # Raise Error
# except NameError:
# 	print("An exception")
# 	raise  # To determine whether the exception was raised or not

# OUTPUT:
# An exception
# Traceback (most recent call last):
#   File "C:\Users\ASIM\Desktop\Assignment9.py", line 25, in <module>
#     raise NameError("Hi there")  # Raise Error
# NameError: Hi there     
#         

     # Function which returns a/b
# def AbyB(a , b):

# try:
# 	c = ((a+b) / (a-b))

		
# except ZeroDivisionError:
# 	print("a/b result in 0")

        
# else:
# 	 print(c)

       
    

# AbyB(2.0, 3.0)
# AbyB(3.0, 3.0)
# OUTPUT
#  -5
#  a/b result in 0

    
    
#Import Error
# try:
# import heyy

# except ImportError:
# 	print ("doesn't exist")

#Value Error

# try:
# 	x=int(input("enter your age:")
# except ValueError:
# 	print("enter an integer")
# else:
# 	print(x)


#Index Error
#try:
# 	list = [66,89,69,61,"asim"]
# 	print(list[6]) 

# except IndexError:
# 	print("index shoud range between 0 to 4")



    
