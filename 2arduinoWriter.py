"""
import serial
from flask import Flask

file = open("value.txt", "r")
val = file.read()
file.close
test_list = val.splitlines()
while("" in test_list):
    test_list.remove("")

num = test_list[len(test_list)-1]


arduino = serial.Serial(
    '/dev/serial/by-id/usb-1a86_USB2.0-Serial-if00-port0', 9600, timeout=.1)


while True:

    data = arduino.readline()[:-3]

    if data and data != num:

        dataValid = data.decode("utf-8")
        print(dataValid)
        f = open("value.txt", 'a+')
        value = f.write("\n"+dataValid)
        f.close

"""
import serial
from flask import Flask
import math

file = open("value.txt", "r")
val = file.read()
file.close
test_list = val.splitlines()
while("" in test_list):
    test_list.remove("")

num = test_list[len(test_list)-1]


arduino = serial.Serial(
    '/dev/serial/by-id/usb-1a86_USB2.0-Serial-if00-port0', 9600, timeout=.1)


while True:

    data = arduino.readline()[:-3]

    if data and data != num:

        dataValid = data.decode("utf-8")
        dataValid1 = str(math.floor(int(dataValid)*100/102))+"%"
        f = open("value.txt", 'a+')
        value = f.write("\n"+dataValid1)
        f.close
