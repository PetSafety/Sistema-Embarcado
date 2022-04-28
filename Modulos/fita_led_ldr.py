from Modulos.imports import *

adc = Adafruit_ADS1x15.ADS1015()

pwm = GPIO.PWM(12,100)
pwm.start(0)
value_max = 1910

def led_control():
    ldr = adc.read_adc(3, gain=1)
    
    dark =  (ldr / value_max)*100
    
    if (dark>100):
        dark = 100
    elif (dark < 15):
        dark = 0
        
    pwm.ChangeDutyCycle(dark)

