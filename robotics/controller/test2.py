import serial

bluetoothSerial = serial.Serial( "/dev/ttyUSB0", baudrate=9600 )
print bluetoothSerial.readline()
bluetoothSerial.write("255")
