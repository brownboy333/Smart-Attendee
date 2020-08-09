
import RPi.GPIO as GPIO
import time

control = [5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]

servo = 4

GPIO.setmode(GPIO.BCM)

GPIO.setup(servo,GPIO.OUT)


p=GPIO.PWM(servo,50)# 50hz frequency

p.start(0)



from Adafruit_CharLCD import Adafruit_CharLCD
lcd = Adafruit_CharLCD(rs=7, en=8, d4=25, d5=24, d6=23, d7=18, cols=16, lines=2)

Emp_list = ['gautam uppal', 'harshit baurai', 'anupama koley', 'kriti gautam', 'bhavna mishra', 'dhruv gothwal']
OTP_list =[]
for i in range(1000):
    if i<10:
        OTP_list.append('0'+'0'+str(i))
    elif i<100:
        OTP_list.append('0'+str(i))
    else :
        OTP_list.append(str(i))
vars = ["Name","Code"]
Recieved = {}
index = 1
import sys

for i in vars:
      temp = sys.argv[index]
      index = index + 1
      Recieved[i] = temp
      print(temp)
name = Recieved["Name"]
if (Recieved["Code"] in OTP_list and Recieved["Name"].lower() in Emp_list):
       print("Attendence  Marked")  #kadcb
       lcd.set_cursor(1, 0)
       lcd.message('Attendence Marked')
       lcd.set_cursor(1, 1)
       lcd.message('Go Inside')
       p.ChangeDutyCycle(20)
       time.sleep(5)
       p.ChangeDutyCycle(5)
       from firebase import firebase

       url = "https://attendence-3d75d.firebaseio.com/" #add your URL here
       firebase = firebase.FirebaseApplication(url)
       result = firebase.put("/Test Val","Value",name)
       print(result)

