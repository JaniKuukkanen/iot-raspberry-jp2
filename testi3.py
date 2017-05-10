import mysql.connector as mariadb
import RPi.GPIO as GPIO
import time
import os

mariadb_connection=mariadb.connect(host="10.207.5.78",port=3306,database="raspberry",user="pi3",password="Qwerty789")
cursor=mariadb_connection.cursor()
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
		time.sleep(5)
		os.system("fswebcam -r 1280x720 /home/pi/pictures/test"+ time.strftime("%Y-%m-%d_%H:%M:%S") + ".jpg" )
		os.system("scp /home/pi/pictures/*.jpg projekti@10.207.5.78:/home/projekti/pictures/")
		time.sleep(5)
		os.system("sudo rm /home/pi/pictures/*.jpg")	

		while i==1:		

			sql = ("""INSERT INTO motion (datetime,detected) VALUES (%s,%s)""",(time.strftime("%Y-%m-%d %H:%M:%S"),i))


			try:
				print("Writing to database")
				cursor.execute(*sql)
				mariadb_connection.commit()
				print("Done'd")
	
			except:
				mariadb_connection.rollback()
				print("Fatal error!!")

		#	cursor.close()
		#	mariadb_connection.close()
			break				


