# using a library pySerial
import serial

ser = serial.Serial()
ser.port = "/dev/tty.usbmodem14401"
ser.baudrate = 115200
ser.setDTR(False)
ser.open()

times = 0
while True:
    line = ser.readline()
    print(line)
    times += 1
    if times >= 10:
        break

ser.close()