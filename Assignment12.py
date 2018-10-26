import time
import datetime


print("Current date and time: " , datetime.datetime.now())

import webbrowser

webbrowser.open('https://www.youtube.com/watch?v=RGq39k6XMsk&list=RDRGq39k6XMsk&start_radio=1')

import os
path = 'C:/Users/ASIM/Documents/DBMS LAb'
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.jpg'))
    i = i+1