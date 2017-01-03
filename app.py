from flask import Flask
import sys
sys.path.append('ledService')
import led 

app = Flask(__name__)


@app.route('/led/on/all')
def onAll():
    led.allOn()
    return 'Todos encendidos'

@app.route('/led/on/<color>')
def on(color):
    led.pinOn(color)
    return 'Encendido el led'

@app.route('/led/off/all')
def offAll():
    led.allOff()
    return 'Todos apagados'

@app.route('/led/off/<color>')

def off(color):
    led.pinOff(color)
    return 'Apagado el led'

@app.route('/')
def index():
    return 'Esperando llamada'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


##ledLed()
