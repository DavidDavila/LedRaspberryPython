



import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT) ## GPIO 17 como salida

GPIO.setup(22, GPIO.OUT) ## GPIO 17 como salida

GPIO.setup(27, GPIO.OUT) ## GPIO 27 como salida



def blink():

        print "Ejecucion iniciada..."

        iteracion = 0

        while iteracion < 30: ## Segundos que durara la funcion

                GPIO.output(17, True) ## Enciendo el 17
                GPIO.output(22, False) ## Apago el 22
                GPIO.output(27, False) ## Apago el 27

                time.sleep(0.5) ## Esperamos 1 segundo

                GPIO.output(17, False) ## Apago el 17
                GPIO.output(27, True) ## Enciendo el 22
                GPIO.output(22, False) ## Apago el 27

                time.sleep(0.5) ## Esperamos 1 segundo

                GPIO.output(17, False) ## Apago el 17
                GPIO.output(27, False) ## Apago el 22
                GPIO.output(22, True) ## Enciendo el 27
                

                time.sleep(0.5) ## Esperamos 1 segundo

                iteracion = iteracion + 1.5 ## Sumo 2 porque he hecho dos parpadeos

        print "Ejecucion finalizada"

        GPIO.cleanup() ## Hago una limpieza de los GPIO



blink() ## Hago la llamada a la funcion blink


