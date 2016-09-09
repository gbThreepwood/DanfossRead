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
ser.writeTimeout = 0.1 #timeout for write
ser.readTimeout = 0.1

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
    command = chr(dev) + '\x04' + struct.pack('>H',reg) + '\x00\x01'
    crc =  crc16.calcString(command, 0xFFFF)
    command = command + struct.pack('<H',crc) 

    print 'Register: ' +  str(reg)
    print ":".join("{:02x}".format(ord(c)) for c in command)
    
    ser.rts = True
    ser.write(command)
    time.sleep(0.008)
    ser.rts = False

    time.sleep(1)        
    
    return ser.readline()
  
def main():
#    for reg in range(0,9999):
#        #print 'Polling register: ' +  str(reg)
#
#        response = read_input_register(1, reg)
#
#        if response[1:2] == '\x83':
#            a = 1
#            #print '.',
#        else:
#            print 'Register: ' +  str(reg)
#            print ":".join("{:02x}".format(ord(c)) for c in response)
#
    #reg = [2010, 2002, 1999, 1504, 1020, 1010, 1006, 1000, 101, 100, 99]

    reg = [2588, 2575, 2103, 2102, 2002, 1010, 102, 101, 100, 99]
    dev = [1, 2]

    for j in range(len(dev)):
        print '==========================='
        print 'Using device: ' + str(dev[j]) 
        for i in range(len(reg)):
            #print 'Polling register: ' +  str(reg)

            response = read_input_register(dev[j], reg[i])

            if response[1:2] == '\x83':
                a = 1
                #print '.',
            else:
                #print 'Register: ' +  str(reg[i])
                print ":".join("{:02x}".format(ord(c)) for c in response)
                print '-'


if __name__ == '__main__':
    main()
