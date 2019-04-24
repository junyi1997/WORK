import RPi.GPIO as GPIO
import time
ou1_pin=31#馬達IN1
ou2_pin=33#馬達IN2
ou3_pin=35#馬達IN3
ou4_pin=37#馬達IN4
in1_pin=36#一般桶
in2_pin=38#紙類桶
in3_pin=40#塑膠桶
a=0
b=0
c=0
w=0
def motor_1():
    while True:
        a=GPIO.input(in1_pin)
        if a ==1:
            print("1啟動")
            GPIO.output(ou1_pin,GPIO.HIGH)
            GPIO.output(ou2_pin,GPIO.HIGH)
            GPIO.output(ou3_pin,GPIO.LOW)
            GPIO.output(ou4_pin,GPIO.LOW)
            my_main()
        elif a==0:
            GPIO.output(ou1_pin,GPIO.HIGH)
            GPIO.output(ou2_pin,GPIO.LOW)
            GPIO.output(ou3_pin,GPIO.LOW)
            GPIO.output(ou4_pin,GPIO.HIGH)

def motor_2():
    while True:
        b=GPIO.input(in2_pin)
        if b ==1:
            print("2啟動")
            GPIO.output(ou1_pin,GPIO.HIGH)
            GPIO.output(ou2_pin,GPIO.HIGH)
            GPIO.output(ou3_pin,GPIO.LOW)
            GPIO.output(ou4_pin,GPIO.LOW)
            my_main()
        elif b==0:
            GPIO.output(ou1_pin,GPIO.HIGH)
            GPIO.output(ou2_pin,GPIO.LOW)
            GPIO.output(ou3_pin,GPIO.LOW)
            GPIO.output(ou4_pin,GPIO.HIGH)
    
def motor_3():
    while True:
        c=GPIO.input(in3_pin)
        if c ==1:
            print("3啟動")
            GPIO.output(ou1_pin,GPIO.HIGH)
            GPIO.output(ou2_pin,GPIO.HIGH)
            GPIO.output(ou3_pin,GPIO.LOW)
            GPIO.output(ou4_pin,GPIO.LOW)
            my_main()
        elif c==0:
            GPIO.output(ou1_pin,GPIO.HIGH)
            GPIO.output(ou2_pin,GPIO.LOW)
            GPIO.output(ou3_pin,GPIO.LOW)
            GPIO.output(ou4_pin,GPIO.HIGH)
    
def my_main():
    w=input("第幾個分類桶")
    if w==1:
        motor_1()
    elif w==2:
        motor_2()
    elif w==3:
        motor_3()
def test():
    while True:
        a=GPIO.input(in1_pin)
        print("a=",a)
        time.sleep(1)

if __name__=='__main__':
    print("程式開始")
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(in1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(in2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(in3_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    GPIO.setup(ou1_pin, GPIO.OUT)
    GPIO.setup(ou2_pin, GPIO.OUT)
    GPIO.setup(ou3_pin, GPIO.OUT)
    GPIO.setup(ou4_pin, GPIO.OUT)
    
    #my_main()
    test()
    
   
#上面程式是利用 SpeechRecognition 模組中的 recognixe_google() 函數透過 Google 語音辨識 API 來將麥克風收到的語音物件 audio 辨識成指定語系的文字 :



