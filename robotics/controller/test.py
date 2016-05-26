
import serial
import XboxController


xboxCont = XboxController.XboxController(
    controllerCallBack=None,
    joystickNo=0,
    deadzone=0.1,
    scale=1,
    invertYAxis=False)

bluetoothSerial = serial.Serial( "/dev/rfcomm9", baudrate=9600 )
bluetoothSerial.write( "255" )
print bluetoothSerial.readline()


lastinput = 0

def LeftThumb(value):
    global bluetoothSerial
    global lastinput
    lastinput+=1

    if lastinput> 20:
        lastinput = 0
        val = str(int(abs(value)) * 255)
        print val
        bluetoothSerial.write(val)
        print bluetoothSerial.readline()

def RightThumb(value):
    global bluetoothSerial
    global lastinput
    lastinput+=1

    if lastinput> 20:
        lastinput = 0
        val = str(int(abs(value)) * 255)
        bluetoothSerial.write(val+'\r\n')
        print bluetoothSerial.readline()

xboxCont.setupControlCallback(xboxCont.XboxControls.LTHUMBY, LeftThumb)

xboxCont.setupControlCallback(xboxCont.XboxControls.RTHUMBY,RightThumb)

xboxCont.start()
