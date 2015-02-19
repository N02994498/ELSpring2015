#!/usr/bin/python

import sqlite3 as myDataBase
import sys
import time

date = " "
tempC = 0
tempF = 0

""" Log Current Time, Temperature in Celsius and Fahrenheit
Returns a list [time, tempC, tempF] """

def readTemp():
        tempfile = open("/sys/bus/w1/devices/28-0000069743ce/w1_slave")
        tempfile_text = tempfile.read()
        currentTime=time.strftime('%x %X %Z')
        tempfile.close()
        tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
        tempF=tempC*9.0/5.0+32.0
        print("Current Temperature is: %s F" % tempF)

	con = myDataBase.connect('/home/pi/databases/temperature.db')

	with con:
		cur = con.cursor() 
		cur.execute('''insert into tempdata 
		(date, tempC, tempF)values(?,?,?)''',
		(date, tempC, tempF))
	print("Temperature Logged")
readTemp()

