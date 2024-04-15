'''import os

shutdown = input("Do you wish to shutdown your computer ? (yes / no): ")

if shutdown == 'no':
	exit()
else:
	os.system("shutdown /s /t 1")
'''

import time
import sys
x=int(input("seconds: "))
print("The timer has started. Time remaining for shut down: ")
def custom_print(string, how = "normal", dur = 0, inline = True):
    if how == "typing": # if how is equal to typing then run this block of code
        letter = 1
        while letter <= len(string):
            new_string = string[0:letter]
            if inline: sys.stdout.write("\r")
            sys.stdout.write("{0}".format(new_string))
            if inline == False: sys.stdout.write("\n")
            if inline: sys.stdout.flush()
            letter += 1
            time.sleep(float(dur))
            if new_string=="0":
                print("\nShut down has started")
            else:
                pass
for k in range(1,x+1):
    k=x-k
    custom_print(str(k), "typing", 1)