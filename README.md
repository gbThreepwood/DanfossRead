# DanfossRead
Software for communication with the Modbus interface of the Danfoss EKC202 refrigerator controllers.

The interface is intended to be used in cojunction with the properietary ADAP-KOOL® system from Danfoss. No documentation regarding the communication protocol is provided, and thus the protocol must be reverse enigneered.

A menu entry on the controller allows for setting the bus address.

## Interface board
In order for the controller to support Modbus, the EKA178A extention module must be connected. The module consists of a Atmel Atmega32 microcontroller, a 6LB184 differential transciever, and a CM0403CG common mode choke connected between the transciever and the RS485 terminals.

The board connects to a 8-pin socket in the controller.

There are no labels on the screw terminals for the RS485 bus, the correct connection has been determined by inspecting the circuit board.

![alt tag](https://raw.githubusercontent.com/gbThreepwood/DanfossRead/master/images/eka178a.jpg)


## Danfoss EKC202
The microcontroller is located on the small circuit board in front, behind the seven segment display. The socket for the extention module is located to the left of the display.

![alt tag](https://raw.githubusercontent.com/gbThreepwood/DanfossRead/master/images/ekc202_front.jpg)

![alt tag](https://raw.githubusercontent.com/gbThreepwood/DanfossRead/master/images/ekc202_top.jpg)

## Modbus test software
As the registry map is undocumented, all possible registry addresses should be polled, until something interesting appears. This is achieved using Python with the Pymodbus extention module. 
