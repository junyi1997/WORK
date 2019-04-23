
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
LEDon = GPIO.output(37,GPIO.HIGH)
c=0
def Button():
    print("進入按鈕模式")
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)     # set up BCM GPIO numbering  
    GPIO.setup(23, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)    # set GPIO25 as input (button)  
    c=GPIO.input(23)
    print("c=",c)

    if c!=d: # if port 25 == 1
        print("狀態改變")
   
if __name__=='__main__':
    print("程式開始")
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    Button()
    



