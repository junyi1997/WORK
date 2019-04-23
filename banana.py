import speech_recognition as sr
import RPi.GPIO as GPIO
import time
a="" #存文字
c=0  #存按鈕觸發
d=0 #存上一個按鈕觸發
Lamp=0 #燈狀態
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
LEDon = GPIO.output(37,GPIO.HIGH)

def Button(Lamp,d,c):
    print("進入按鈕模式")
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37, GPIO.OUT)
    LEDon = GPIO.output(37,GPIO.LOW)
    time.sleep(5)
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)     # set up BCM GPIO numbering  
    GPIO.setup(23, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)    # set GPIO25 as input (button)  
    GPIO.setup(11, GPIO.OUT) 
    # this will carry on until you hit CTRL+C
    print("D=",d)
    print("C=",c)
    c=GPIO.input(23)
    
    if c!=d: # if port 25 == 1
        print("狀態改變")
        d=c
        print("C=",c)
        print("D=",d)
        Lamp=~Lamp
        GPIO.output(11, Lamp)         # set port/pin value to 1/HIGH/True
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)
        #LEDon = GPIO.output(11,d)
               
        my_main(Lamp,d,c)
def Hello():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    LEDon = GPIO.output(11,GPIO.HIGH)
            

def Close():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    LEDon = GPIO.output(11,GPIO.LOW)
    print("燈已經關閉")

def my_main(Lamp,d,c):
    
    while(True):
        print("Lamp=",Lamp)
        
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(37, GPIO.OUT)
        LEDon = GPIO.output(37,GPIO.HIGH)
            
    #obtain audio from the microphone
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Please wait. Calibrating microphone...") 
            #listen for 5 seconds and create the ambient noise energy level 
            r.adjust_for_ambient_noise(source, duration=5)
            print("Say something!")
            audio=r.listen(source)
            

        # recognize speech using Google Speech Recognition 
        try:
            print("Google Speech Recognition thinks you said:")
            a=r.recognize_google(audio, language="zh-TW")
            print(a)
        except sr.UnknownValueError:
            a=""
            Button(Lamp,d,c)
        except sr.RequestError as e:
            a=""
            return
            #Button(Lamp,d,c)
            
                        
        if Lamp==-1:
            if "開" in a:
                pass
            elif "關" in a:
                Lamp=0
                print("C_Lamp=",Lamp)
                Close()
            
        elif Lamp==0:
            if "開" in a:
                Lamp=-1
                Hello()
                print("D_Lamp=",Lamp)
            elif "關" in a:
                pass
        else:
            Button(Lamp,d,c)
        '''
        if a=="開燈":
            Hello()
           
        elif a=="關燈":
            Close()
        '''       
if __name__=='__main__':
    print("程式開始")
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(11, GPIO.OUT)
    GPIO.output(11,GPIO.LOW)
    d=GPIO.input(23)
    c=d
    my_main(Lamp,d,c)
#上面程式是利用 SpeechRecognition 模組中的 recognixe_google() 函數透過 Google 語音辨識 API 來將麥克風收到的語音物件 audio 辨識成指定語系的文字 :



