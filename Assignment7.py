# 1 Question
dicti = {'Ford' : 1997, 'Chevy' : 1998, 'English' : 2009}
i = int(input("Enter the Year:"))
for name,year in dicti.items():
	if year == i:
		print(name)
        

# 2 Question     
school = { 'nazia' : {'eng':92,'hin':93, 'math': 99, 'sci':96},
'asim' : {'eng':2,'hin':3, 'math': 9, 'sci':6},
'raheem' : {'eng':2,'hin':3, 'math': 9, 'sci':6}
}

stu = input("Enter name of Student:")
for name,sub in school.items():
	if name== stu:
		print(school[name])