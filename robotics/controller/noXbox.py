import serial

bluetoothSerial = serial.Serial('/dev/ttyUSB1', baudrate=9600)

val += str(100)
val += "\r\n"
bluetoothSerial.write(val)

while True:
    steer = raw_input('Set steering offset (-100-100)');
    val += str(2000 + steer)
    val += "\r\n"
    bluetoothSerial.write(val)
