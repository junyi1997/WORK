import RPi.GPIO as gpio
import time

#蓋子馬達
in1_pin = 31
in2_pin = 33
#平台馬達
in3_pin = 35
in4_pin = 37

gpio.setmode(gpio.BOARD)
gpio.setup(in1_pin, gpio.OUT)
gpio.setup(in2_pin, gpio.OUT)
gpio.setup(in3_pin, gpio.OUT)
gpio.setup(in4_pin, gpio.OUT)

while True:
    a=eval(input("1是蓋子正轉\n，2是蓋子反轉\n，3是平台正轉\n，4是平台反轉\n"))
    if(a==1):
        print("蓋子正轉")
        gpio.output(in1_pin,True)
        gpio.output(in2_pin,False)
        time.sleep(1.5)
        gpio.output(in1_pin,False)
        gpio.output(in2_pin,False)
    if(a==2):
        print("蓋子反轉")
        gpio.output(in1_pin,False)
        gpio.output(in2_pin,True)
        time.sleep(1.5)
        gpio.output(in1_pin,False)
        gpio.output(in2_pin,False)
    
    if(a==3):
        print("平台正轉")
        gpio.output(in3_pin,True)
        gpio.output(in4_pin,False)
        time.sleep(1.5)
        gpio.output(in3_pin,False)
        gpio.output(in4_pin,False)
    if(a==4):
        print("平台反轉")
        gpio.output(in3_pin,False)
        gpio.output(in4_pin,True)
        time.sleep(1.5)
        gpio.output(in3_pin,False)
        gpio.output(in4_pin,False)
        