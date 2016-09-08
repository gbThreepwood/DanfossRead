#!/usr/bin/python
import serial
import time

import crc16

import struct

#def compute_crc(data):
#    crc = '10'
#    return crc
#


ser = serial.Serial('/dev/danfoss', 9600, timeout=1, rtscts=False)


ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_EVEN #set parity check: no parity
ser.stopbits = serial.STOPBITS_ONE #number of stop bits
ser.xonxoff = False    #disable software flow control
ser.rtscts = False    #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
ser.writeTimeout = 1 #timeout for write


print ser

#address = '\x09'
#command = '\x11'
#
#data = address + command
#data = data + compute_crc(data)
#
#print('Transmitting: ' + str(data))
#ser.rts = True
#
#ser.dtr = True
#time.sleep(0.1)
#ser.write(data)
#
#ser.write(':010310010001EA\r\n')
#print repr(ser.read(1000)) # Read 1000 bytes, or wait for timeout


def read_input_register(dev, reg):
    command = chr(dev) + '\x04\x00' + chr(reg) + '\x00\x01'
    crc =  crc16.calcString(command, 0xFFFF)
    command = command + struct.pack('<H',crc) 

    print ":".join("{:02x}".format(ord(c)) for c in command)
    
    ser.rts = True
    ser.write(command)
    time.sleep(0.008)
    ser.rts = False

    return ser.readline()
  
def main():
    for reg in range(0,99):
        print 'Polling register: ' +  str(reg)

        response = read_input_register(3, reg)
        
        print ":".join("{:02x}".format(ord(c)) for c in response)



if __name__ == '__main__':
    main()
