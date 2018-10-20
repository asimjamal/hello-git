class circle():
	def __init__(self,rad):
		self.rad = rad
	def getArea(self):
		return 3.14*self.rad*self.rad
	def getCircumference(self):
		return 2*3.14*self.rad


calc = circle(10)
print(calc.getArea())
print(calc.getCircumference())

class student():
	def __init__(self, fname, roll):
		self.firstname = fname
		self.roll = roll
	
		
	def display(self):
		print(self.firstname +" " + self.roll)
	def setAge(self, age):
		self.age = age
		print(self.age)
	def setMarks(self, marks):
		self.marks = marks
		print(self.marks)

	
Mohit = student("Mohit", "12345", )
print(Mohit.display())
print(Mohit.setAge(21))
print(Mohit.setMarks(200))




class Temprature():
	def __init__(self):
		pass 

	def convertF(self,ctemp):

		 self.ctemp = ctemp
		 t=self.ctemp * 1.8 +32
		 return t

	def convertC(self,ftemp):
		self.ftemp = ftemp
		t=(self.ftemp - 32) /1.8
		return t

new = Temprature()
print(new.convertF(20))
print(new.convertC(30))

class MovieDetails():
	def __init__(self,aname,yor,rat,details):
		self.aname= aname
		self.yor=yor
		self.rat= rat
		self.details=details

	def display(self):
		print(self.aname + " "+ str(self.yor) + " "+ str(self.rat))
	
	def add(self):
		print(self.details)

new= MovieDetails('hello',2015,7.5,'good')
new1= MovieDetails('hell',2014,4.5,'nice')
print(MovieDetails.display(new))
print(MovieDetails.add(new))


class animal():
	
	def __init__(self):
			pass
	def display(self):
			return("I'm an animal")
		 


class tiger(animal):
	def __init__(self):
		pass	

def dis(self):

    	print("I'm tiger")

     

x=tiger()


print(x.display())



OUTPUT = A B
A, B



class shape:
	def __init__(self,side1,side2):
		self.side1=side1
		self.side2=side2


	def area(self):
		return self.side1 * self.side2


class sqaure(shape):
	def __init__(self,side1):
 		super(sqaure, self).__init__(side1,side1)

	

class rectangle(shape):
	def __init__(self,side1,side2):
		super(rectangle, self).__init__(side1,side2)
		


sqr=sqaure(4)
rec=rectangle(2,4)
print(rec.area())
print(sqr.area())


