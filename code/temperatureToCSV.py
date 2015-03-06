
import csv
import sqlite3 as myDataBase


con = myDataBase.connect('/home/pi/ELSpring2015/misc/temperature.db')
cursor = con.cursor()
cursor.execute("select * from TempData;")

with open("temperature.csv", "wb") as csv_file:

	csvWriter = csv.writer(csv_file)
	csvWriter.writerows(cursor)
