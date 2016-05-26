import serial
import time
import XboxController

xboxCont = XboxController.XboxController(
    controllerCallBack=None,
    joystickNo=0,
    deadzone=0.1,
    scale=1,
    invertYAxis=False)

bluetoothSerial = serial.Serial('/dev/ttyUSB1', baudrate=9600)

print('Starting Up Serial Monitor')

print(bluetoothSerial.read())
bluetoothSerial.write("255")
def LeftThumb(value):
    global bluetoothSerial
    val = '1'
    val += str(abs(value) * 255)
    val += "\r\n"
    bluetoothSerial.write(val)

def RightThumb(value):
    global sebluetoothSerial
    val = '2'
    val += str(abs(value) * 255)
    val += "\r\n"
    bluetoothSerial.write(val)

xboxCont.setupControlCallback(xboxCont.XboxControls.LTHUMBY, LeftThumb)

xboxCont.setupControlCallback(xboxCont.XboxControls.RTHUMBY,RightThumb)

xboxCont.start()
