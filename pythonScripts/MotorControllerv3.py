import RPi.GPIO as GPIO #importing library for gpio control
import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient
#os.system("sudo killall pigpiod")
#os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
#import pigpio #importing GPIO library
from pyPS4Controller.controller import Controller


class MyController(Controller):
    
    #connect the ESC for each motor to gpio pins
    rESC = 11  #Actual pin number
    lESC = 13
    
    #set up gpio
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(lESC, GPIO.OUT)
    GPIO.setup(rESC, GPIO.OUT)
    pi_pwml = GPIO.PWM(lESC, 1000)
    pi_pwmr = GPIO.PWM(rESC, 1000)
    pi_pwml.start(0)
    pi_pwmr.start(0)
    
    #set up some speed constants
    max_esc_val = 100 #vesc max val
    min_esc_val = 0  #vesc min val
    esc_step = (max_esc_val - min_esc_val) / 10
    max_controller_val = 32767
    min_controller_val = 0
    controller_step = max_controller_val / 35
    
    
    def Controllmotor(self, direc, value):
        if direc == "release":                 #if release stop
            MyController.pi_pwml.ChangeDutyCycle(0)
        elif direc == "up":
            if value <= MyController.controller_step:
                MyController.pi_pwml.ChangeDutyCycle(2)
            elif value <= (MyController.controller_step*2):
                MyController.pi_pwml.ChangeDutyCycle(4)
            elif value <= (MyController.controller_step*3):
                MyController.pi_pwml.ChangeDutyCycle(6)
            elif value <= (MyController.controller_step*4):
                MyController.pi_pwml.ChangeDutyCycle(8)
            elif value <= (MyController.controller_step*5):
                MyController.pi_pwml.ChangeDutyCycle(10)
            elif value <= (MyController.controller_step*6):
                MyController.pi_pwml.ChangeDutyCycle(12)
            elif value <= (MyController.controller_step*7):
                MyController.pi_pwml.ChangeDutyCycle(14)
            elif value <= (MyController.controller_step*8):
                MyController.pi_pwml.ChangeDutyCycle(16)
            elif value <= (MyController.controller_step*9):
                MyController.pi_pwml.ChangeDutyCycle(18)
            elif value <= (MyController.controller_step*10):
                MyController.pi_pwml.ChangeDutyCycle(20)
            elif value <= (MyController.controller_step*11):
                MyController.pi_pwml.ChangeDutyCycle(22)
            elif value <= (MyController.controller_step*12):
                MyController.pi_pwml.ChangeDutyCycle(24)
            elif value <= (MyController.controller_step*13):
                MyController.pi_pwml.ChangeDutyCycle(26)
            elif value <= (MyController.controller_step*14):
                MyController.pi_pwml.ChangeDutyCycle(28)
            elif value <= (MyController.controller_step*15):
                MyController.pi_pwml.ChangeDutyCycle(30)
            elif value <= (MyController.controller_step*16):
                MyController.pi_pwml.ChangeDutyCycle(32)
            elif value <= (MyController.controller_step*17):
                MyController.pi_pwml.ChangeDutyCycle(34)
            elif value <= (MyController.controller_step*18):
                MyController.pi_pwml.ChangeDutyCycle(36)
            elif value <= (MyController.controller_step*19):
                MyController.pi_pwml.ChangeDutyCycle(38)
            elif value <= (MyController.controller_step*20):
                MyController.pi_pwml.ChangeDutyCycle(40)
            elif value <= (MyController.controller_step*21):
                MyController.pi_pwml.ChangeDutyCycle(42)
            elif value <= (MyController.controller_step*22):
                MyController.pi_pwml.ChangeDutyCycle(44)
            elif value <= (MyController.controller_step*23):
                MyController.pi_pwml.ChangeDutyCycle(46)
            elif value <= (MyController.controller_step*24):
                MyController.pi_pwml.ChangeDutyCycle(48)
            elif value <= (MyController.controller_step*25):
                MyController.pi_pwml.ChangeDutyCycle(50)
            elif value <= (MyController.controller_step*26):
                MyController.pi_pwml.ChangeDutyCycle(52)
            elif value <= (MyController.controller_step*27):
                MyController.pi_pwml.ChangeDutyCycle(54)
            elif value <= (MyController.controller_step*28):
                MyController.pi_pwml.ChangeDutyCycle(56)
            elif value <= (MyController.controller_step*29):
                MyController.pi_pwml.ChangeDutyCycle(58)
            elif value <= (MyController.controller_step*30):
                MyController.pi_pwml.ChangeDutyCycle(60)
            elif value <= (MyController.controller_step*31):
                MyController.pi_pwml.ChangeDutyCycle(62)
            elif value <= (MyController.controller_step*32):
                MyController.pi_pwml.ChangeDutyCycle(64)
            elif value <= (MyController.controller_step*33):
                MyController.pi_pwml.ChangeDutyCycle(66)
            elif value <= (MyController.controller_step*34):
                MyController.pi_pwml.ChangeDutyCycle(68)
            elif value <= (MyController.controller_step*35):
                MyController.pi_pwml.ChangeDutyCycle(70)

                
    def Controlrmotor(self, direc, value):
       if direc == "release":                 #if release stop
            MyController.pi_pwmr.ChangeDutyCycle(0)
       elif direc == "up":
            if value <= MyController.controller_step:
                MyController.pi_pwmr.ChangeDutyCycle(2)
            elif value <= (MyController.controller_step*2):
                MyController.pi_pwmr.ChangeDutyCycle(4)
            elif value <= (MyController.controller_step*3):
                MyController.pi_pwmr.ChangeDutyCycle(6)
            elif value <= (MyController.controller_step*4):
                MyController.pi_pwmr.ChangeDutyCycle(8)
            elif value <= (MyController.controller_step*5):
                MyController.pi_pwmr.ChangeDutyCycle(10)
            elif value <= (MyController.controller_step*6):
                MyController.pi_pwmr.ChangeDutyCycle(12)
            elif value <= (MyController.controller_step*7):
                MyController.pi_pwmr.ChangeDutyCycle(14)
            elif value <= (MyController.controller_step*8):
                MyController.pi_pwmr.ChangeDutyCycle(16)
            elif value <= (MyController.controller_step*9):
                MyController.pi_pwmr.ChangeDutyCycle(18)
            elif value <= (MyController.controller_step*10):
                MyController.pi_pwmr.ChangeDutyCycle(20)
            elif value <= (MyController.controller_step*11):
                MyController.pi_pwmr.ChangeDutyCycle(22)
            elif value <= (MyController.controller_step*12):
                MyController.pi_pwmr.ChangeDutyCycle(24)
            elif value <= (MyController.controller_step*13):
                MyController.pi_pwmr.ChangeDutyCycle(26)
            elif value <= (MyController.controller_step*14):
                MyController.pi_pwmr.ChangeDutyCycle(28)
            elif value <= (MyController.controller_step*15):
                MyController.pi_pwmr.ChangeDutyCycle(30)
            elif value <= (MyController.controller_step*16):
                MyController.pi_pwmr.ChangeDutyCycle(32)
            elif value <= (MyController.controller_step*17):
                MyController.pi_pwmr.ChangeDutyCycle(34)
            elif value <= (MyController.controller_step*18):
                MyController.pi_pwmr.ChangeDutyCycle(36)
            elif value <= (MyController.controller_step*19):
                MyController.pi_pwmr.ChangeDutyCycle(38)
            elif value <= (MyController.controller_step*20):
                MyController.pi_pwmr.ChangeDutyCycle(40)
            elif value <= (MyController.controller_step*21):
                MyController.pi_pwmr.ChangeDutyCycle(42)
            elif value <= (MyController.controller_step*22):
                MyController.pi_pwmr.ChangeDutyCycle(44)
            elif value <= (MyController.controller_step*23):
                MyController.pi_pwmr.ChangeDutyCycle(46)
            elif value <= (MyController.controller_step*24):
                MyController.pi_pwmr.ChangeDutyCycle(48)
            elif value <= (MyController.controller_step*25):
                MyController.pi_pwmr.ChangeDutyCycle(50)
            elif value <= (MyController.controller_step*26):
                MyController.pi_pwmr.ChangeDutyCycle(52)
            elif value <= (MyController.controller_step*27):
                MyController.pi_pwmr.ChangeDutyCycle(54)
            elif value <= (MyController.controller_step*28):
                MyController.pi_pwmr.ChangeDutyCycle(56)
            elif value <= (MyController.controller_step*29):
                MyController.pi_pwmr.ChangeDutyCycle(58)
            elif value <= (MyController.controller_step*30):
                MyController.pi_pwmr.ChangeDutyCycle(60)
            elif value <= (MyController.controller_step*31):
                MyController.pi_pwmr.ChangeDutyCycle(62)
            elif value <= (MyController.controller_step*32):
                MyController.pi_pwmr.ChangeDutyCycle(64)
            elif value <= (MyController.controller_step*33):
                MyController.pi_pwmr.ChangeDutyCycle(66)
            elif value <= (MyController.controller_step*34):
                MyController.pi_pwmr.ChangeDutyCycle(68)
            elif value <= (MyController.controller_step*35):
                MyController.pi_pwmr.ChangeDutyCycle(70)







       
        #controller input events
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
                
    def on_L3_up(self, value):
        self.Controllmotor("up", -1 * value)
                
    def on_L3_down(self, value):
        self.Controllmotor("down", value)

    def on_L3_y_at_rest(self):
        self.Controllmotor("release", 0)

    def on_R3_up(self, value):
        self.Controlrmotor("up", -1 * value)
              
    def on_R3_down(self, value):
        self.Controlrmotor("down", value)

    def on_R3_y_at_rest(self):
        self.Controlrmotor("release",  0)
 
 
 
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()

  