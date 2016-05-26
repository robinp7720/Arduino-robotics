import serial
import XboxController
import time

xbox = XboxController.XboxController(
    controllerCallBack = None,
    joystickNo = 0,
    deadzone = 0.01,
    scale = 1,
    invertYAxis = False
)

ser = serial.Serial( "/dev/ttyUSB1", 9600 )
ser.write("0")

LeftSpeed = 0
RightSpeed = 0


def setRightSpeed(number):
    ser.write('1'+str(int(abs(number)*250))+'\r\n')


def setLeftSpeed(number):
    ser.write('2'+str(int(abs(number)*250))+'\r\n')


def LeftThumb(val):
    global ser
    global LeftSpeed
    LeftSpeed = val

def RightThumb(val):
    global ser
    global RightSpeed
    RightSpeed = val


xbox.setupControlCallback(xbox.XboxControls.LTHUMBY, LeftThumb)
xbox.setupControlCallback(xbox.XboxControls.RTHUMBY, RightThumb)

xbox.start()

while True:
    setRightSpeed(RightSpeed)
    time.sleep(0.5)
    setLeftSpeed(LeftSpeed)
    time.sleep(0.5)
    print(RightSpeed,LeftSpeed)

