import pymysql
import json
from datetime import datetime

def Sensor(jsonData):

	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['SensorID']
	if SensorID == 1:
		Data_and_Time = (datetime.today()).strftime("%d-%b-%y %H:%M:%S")
		SensorID = "Sensor1"
		Temperature = json_Dict['Temperature']
		Humidity = json_Dict['Humidity']
		db= pymysql.connect('localhost','thanhminh','minh6464','wsn')
		cursor= db.cursor()

		sql= """insert into Sensor1(SensorID, Data_and_Time, Temperature, Humidity)
				values(%s,%s, %s, %s)
			"""
		val = (SensorID, Data_and_Time, Temperature, Humidity)
		cursor.execute(sql, val)
		db.commit()

		print("		=>******tao gia tri cam bien moi thanh cong*******")
		print("")
		db.close()
	elif SensorID == 2:
		Data_and_Time = (datetime.today()).strftime("%d-%b-%y %H:%M:%S")
		SensorID = "Sensor2"
		Temperature = json_Dict['Temperature']
		Humidity = json_Dict['Humidity']
		db= pymysql.connect('localhost','thanhminh','minh6464','wsn')
		cursor= db.cursor()

		sql= """insert into Sensor2(SensorID, Data_and_Time, Temperature, Humidity)
				values(%s,%s, %s, %s)
			"""
		val = (SensorID, Data_and_Time, Temperature, Humidity)
		cursor.execute(sql, val)
		db.commit()

		print("		=>******tao gia tri cam bien moi thanh cong*******")
		print("")
		db.close()
	elif SensorID == 3:
		Data_and_Time = (datetime.today()).strftime("%d-%b-%y %H:%M:%S")
		SensorID = "Sensor3"
		Temperature = json_Dict['Temperature']
		Humidity = json_Dict['Humidity']
		db= pymysql.connect('localhost','thanhminh','minh6464','wsn')
		cursor= db.cursor()

		sql= """insert into Sensor3(SensorID, Data_and_Time, Temperature, Humidity)
				values(%s,%s, %s, %s)
			"""
		val = (SensorID, Data_and_Time, Temperature, Humidity)
		cursor.execute(sql, val)
		db.commit()

		print("		=>******tao gia tri cam bien moi thanh cong*******")
		print("")
		db.close()
	elif SensorID == 4:
		Data_and_Time = (datetime.today()).strftime("%d-%b-%y %H:%M:%S")
		SensorID = "Sensor4"
		Temperature = json_Dict['Temperature']
		Humidity = json_Dict['Humidity']
		db= pymysql.connect('localhost','thanhminh','minh6464','wsn')
		cursor= db.cursor()

		sql= """insert into Sensor4(SensorID, Data_and_Time, Temperature, Humidity)
				values(%s,%s, %s, %s)
			"""
		val = (SensorID, Data_and_Time, Temperature, Humidity)
		cursor.execute(sql, val)
		db.commit()

		print("		=>******tao gia tri cam bien moi thanh cong*******")
		print("")
		db.close()
	else:
		Data_and_Time = (datetime.today()).strftime("%d-%b-%y %H:%M:%S")
		SensorID = "Sensor5"
		Temperature = json_Dict['Temperature']
		Humidity = json_Dict['Humidity']
		db= pymysql.connect('localhost','thanhminh','minh6464','wsn')
		cursor= db.cursor()

		sql= """insert into Sensor5(SensorID, Data_and_Time, Temperature, Humidity)
				values(%s,%s, %s, %s)
			"""
		val = (SensorID, Data_and_Time, Temperature, Humidity)
		cursor.execute(sql, val)
		db.commit()

		print("		=>******tao gia tri cam bien moi thanh cong*******")
		print("")
		db.close()
		
