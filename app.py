from flask import Flask
import time
import sys
sys.path.append('ledService')
##import blink
import blink

app = Flask(__name__)


@app.route('/led/on/all')
def onAll():
    blink.allOn()
    return 'Todos encendidos'

@app.route('/led/on/<color>')
def on(color):
    blink.pinOn(color)
    return 'Encendido el led'

@app.route('/led/off/all')
def offAll():
    blink.allOff()
    return 'Todos apagados'

@app.route('/led/off/<color>')

def off(color):
    blink.pinOff(color)
    return 'Apagado el led'

@app.route('/')
def index():
    return 'Esperando llamada'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


##blinkLed()
