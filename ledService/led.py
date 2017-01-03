
import RPi.GPIO as GPIO
import sys
sys.path.append('ledModel')
import config

GPIO.setmode(GPIO.BCM)

for name in config.pinLeds:
        GPIO.setup(config.pinLeds[name], GPIO.OUT)
        
def pinOn(name):        
        GPIO.output(config.pinLeds[name], True)
        print "Encenido led "       
        
def pinOff(name):
        print "Apagado led "
        GPIO.output(config.pinLeds[name], False)
        
def allOn():
        for name in config.pinLeds:
                GPIO.output(config.pinLeds[name], True)
                
def allOff():
        for name in config.pinLeds:
                GPIO.output(config.pinLeds[name], False)
def checkAll():
       for name in config.pinLeds:
                GPIO.output(config.pinLeds[name])
  
##        GPIO.cleanup()
        
