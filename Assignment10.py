
pipe = open("temp.txt","r")

var= pipe.read()
print(var)

pipe.close()


test_string = input("Enter string:")
l = []
l = test_string.split()
wordfreq = [l.count(p) for p in l]
print(dict(zip(l,wordfreq)))


pipe1= open("temp.txt", "r+")
var1 = pipe1.read()
pipe2 = open("temp1.txt", "w+")
pipe2.write(var1)

pipe1.close()
pipe2.close()


pip2 = open("temp3.txt","r+")
var=pip2.read().split("/n")

pip1 = open("temp2.txt","a+")
for row in pip1:
  pip1.append(var)



pip1.close()
pip2.close()

import csv

file_obj = open("temp2.csv", "a+")
myfile2= csv.writer(file_obj)
file_obj1 = open("temp3.csv", "w+")
myfile3 = csv.writer(file_obj1)
myfile2.writerow(myfile3)

file_obj.close()
file_obj1.close()