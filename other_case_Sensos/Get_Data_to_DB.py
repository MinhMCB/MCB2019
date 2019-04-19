import pymysql
import json
from datetime import datetime

def Sensor(jsonData):

	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['SensorID']
	if (SensorID ==1):
		SensorID = "Sensor1"
	elif (SensorID ==2):
		SensorID = "Sensor2"
	elif (SensorID ==3):
		SensorID = "Sensor3"
	elif (SensorID ==4):
		SensorID = "Sensor4"
	else :
		SensorID = "Sensor5"
	Data_and_Time = (datetime.today()).strftime("%d-%b-%y %H:%M:%S")
	Temperature = json_Dict['Temperature']
	Humidity = json_Dict['Humidity']
	db= pymysql.connect('localhost','thanhminh','minh6464','wsn')
	cursor= db.cursor()

	sql= """insert into Sensors(SensorID, Data_and_Time, Temperature, Humidity)
				values(%s,%s, %s, %s)
		"""
	val = (SensorID, Data_and_Time, Temperature, Humidity)
	cursor.execute(sql, val)
	db.commit()

	print("		=>******tao gia tri cam bien moi thanh cong*******")
	print("")
	db.close()
	
