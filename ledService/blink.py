
import RPi.GPIO as GPIO
import time
import sys
sys.path.append('ledModel')
import config

GPIO.setmode(GPIO.BCM)

for name in config.pinLeds:
        GPIO.setup(config.pinLeds[name], GPIO.OUT)

def blinkLed():
        
        print "Ejecucion iniciada..."
        iteracion = 0
        while iteracion < 5: ## Segundos que durara la funcion

                GPIO.output(17, True) ## Enciendo el 17
                GPIO.output(22, True) ## Apago el 22
                GPIO.output(27, True) ## Apago el 27

                time.sleep(0.1) ## Esperamos 1 segundo

                GPIO.output(17, False) ## Apago el 17
                GPIO.output(27, True) ## Enciendo el 22
                GPIO.output(22, False) ## Apago el 27

                time.sleep(0.1) ## Esperamos 1 segundo

                GPIO.output(17, False) ## Apago el 17
                GPIO.output(27, False) ## Apago el 22
                GPIO.output(22, True) ## Enciendo el 27
                

                time.sleep(0.1) ## Esperamos 1 segundo
                
                GPIO.output(17, False) ## Apago el 17
                GPIO.output(27, True) ## Enciendo el 22
                GPIO.output(22, False) ## Apago el 27

                time.sleep(0.1) ## Esperamos 1 segundo



                iteracion = iteracion + 0.4 ## Sumo 2 porque he hecho dos parpadeos

        print "Ejecucion finalizada"

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
##        GPIO.cleanup()
        
