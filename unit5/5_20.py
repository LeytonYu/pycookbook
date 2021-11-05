# 与串行端口的数据通信, 好的选择是使用 pySerial包

import serial

ser = serial.Serial('/dev/tty.usbmodem641',  # Device name varies
                    baudrate=9600,
                    bytesize=8,
                    parity='N',
                    stopbits=1)


ser.write(b'G1 X50 Y50\r\n')
resp = ser.readline()