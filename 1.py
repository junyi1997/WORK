
import RPi.GPIO as GPIO
import time

c=0
def Button():
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)     # set up BCM GPIO numbering  
    GPIO.setup(37, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)    # set GPIO25 as input (button)  
    c=GPIO.input(37)
    print("c=",c)

if __name__=='__main__':
    print("程式開始")
    Button()
    



