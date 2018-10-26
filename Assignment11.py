import re
def validmail(email):
	if len(email) > 7:
		if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
			return True
			return False
if validmail("jamalasim081@gmail.com") == True :
	print("this is a Valid Mail Id")
else:
	print("Not a valid mail id")

import re

def validnumber(n):

	pattern = re.compile("(0/91)?[6-9][0-9]{9}")
	return pattern.match(n)

n = "9873823374"

if (validnumber(n)):
	print("valid Number it is")
else:
	print("invalid number")



