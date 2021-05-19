import os
from time import strftime
import time
print(strftime("Current Date & Time : %d-%m-%Y ,%a %H:%M:%S %p"))
# starting time
starttime = time.time()
fname=input("Enter File Name : ")
if os.path.isfile(fname):
    print('File Exists : ',fname)
    f=open(fname,'r')
    print('The contents of the file is : ')
    print(f.read())
else:
    print('File does not Exists :',fname)
endtime = time.time()
# total time taken
print("Runtime of the total program is : ", endtime - starttime)
