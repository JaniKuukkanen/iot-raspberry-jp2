import mysql.connector as mariadb
import RPi.GPIO as GPIO
import time

mariadb_connection = mariadb.connect(user='pi', password='Qwerty789',host='10.207.5.78',port='3306',database='raspberry')
cursor = mariadb_connection.cursor()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
Timenow = time.strftime("%Y-%m-%d %H:%M:%S")

while True:
	i=GPIO.input(7)
	if i==0:
	
		time.sleep(0.1)
	elif i==1:
		print("PANIC!!!" + time.strftime("%Y-%m-%d %H:%M:%S"))
		time.sleep(0.1)

while True:
	y=GPIO.input(7)
	sql = ("""INSERT INTO motion (datetime,detected) VALUES (%s,%s)""",(time.strftime("%Y-%m-%d %H:%M:%S"),y))
	try:
		print("Writing to database")
		cur.execute(*sql)
		db.commit()
		print("Done'd")
	
	except:
		db.rollback()
		print("Fatal error!!")

	cur.close()
	db.close()
	break


