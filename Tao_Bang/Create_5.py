#them thu vien
import MySQLdb
#mo ket noi den Mysql
db= MySQLdb.connect('localhost','thanhminh','minh6464','wsn')

# su dung 1 cursor de truy cap
cursor= db.cursor()

# xoa table neu table da ton tai
cursor.execute("drop table if exists Sensor1")
cursor.execute("drop table if exists Sensor2")
cursor.execute("drop table if exists Sensor3")
cursor.execute("drop table if exists Sensor4")
cursor.execute("drop table if exists Sensor5")

# tao 5 bang
sql= """ create table Sensor5(
			STT int(5) not null auto_increment primary key,
			SensorID char(20) not null ,
			Temperature float(3) not null,
			Humidity float(3) not null,
			Data_and_Time char(25) not null
		)"""
cursor.execute(sql)

sql= """ create table Sensor1(
			STT int(5) not null auto_increment primary key,
			SensorID char(20) not null ,
			Temperature float(3) not null,
			Humidity float(3) not null,
			Data_and_Time char(25) not null
		)"""
cursor.execute(sql)

sql= """ create table Sensor2(
			STT int(5) not null auto_increment primary key,
			SensorID char(20) not null ,
			Temperature float(3) not null,
			Humidity float(3) not null,
			Data_and_Time char(25) not null
		)"""
cursor.execute(sql)

sql= """ create table Sensor3(
			STT int(5) not null auto_increment primary key,
			SensorID char(20) not null ,
			Temperature float(3) not null,
			Humidity float(3) not null,
			Data_and_Time char(25) not null
		)"""
cursor.execute(sql)

sql= """ create table Sensor4(
			STT int(5) not null auto_increment primary key,
			SensorID char(20) not null ,
			Temperature float(3) not null,
			Humidity float(3) not null,
			Data_and_Time char(25) not null
		)"""
cursor.execute(sql)
db.close()
