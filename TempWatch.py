'''NOW ON GITHUB LOL'''
import os
import sys
import time
from termcolor import colored

def getTemp():
        temp = os.popen("sensors | grep 'CPU Temperature' | cut -d ' ' -f 6").readline().replace("\n"," ")
        return temp

print(colored("CPU Temp Watch by morpheus", "blue"))

while True:
        temperature = getTemp()
        tempfloat = float(temperature[1:][:-4])
        if tempfloat < 45.0:
            sys.stdout.write("\r"+colored(temperature, 'green'))
        if tempfloat > 45.0:
            sys.stdout.write("\r"+colored(temperature, 'yellow'))
        if tempfloat > 87.0:
            sys.stdout.write("\r"+colored(temperature, 'red'))
        '''print(tempfloat)'''
        if tempfloat > 90.0:
            print("OVERHEAT")
        time.sleep(1)
