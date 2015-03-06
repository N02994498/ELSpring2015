#!/usr/bin/python

import sqlite3 as myDataBase
import sys
import time
import os


date = " "
tempC = 0
tempF = 0

""" Log Current Time, Temperature in Celsius and Fahrenheit
Returns a list [time, tempC, tempF] """

def readTemp():
        tempfile = open("/sys/bus/w1/devices/28-0000069743ce/w1_slave")
        tempfile_text = tempfile.read()
        date=time.strftime("%x %X %Z")
        tempfile.close()
        tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
        tempF=tempC*9.0/5.0+32.0
	
	con = myDataBase.connect('/home/pi/ELSpring2015/misc/temperature.db')

	with con:
		cur = con.cursor() 
		cur.execute("Insert into TempData(date, tempC, tempF) Values(?,?,?)",
		(date, tempC, tempF))
		con.commit()


	return "Current Temperature is: " + str(tempF) + "\nTemperature Logged"
print readTemp()

