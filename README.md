# DanfossRead
Software for communication with the Modbus interface of the Danfoss EKC202 refrigerator controllers.

The interface is intended to be used in cojunction with the properietary ADAP-KOOL® system from Danfoss. No documentation regarding the communication protocol is provided, and thus the protocol must be reverse enigneered.

A menu entry on the controller allows for setting the bus address. Menu entry o03 network address, allowed range is between 0 and 240.

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


By sending a read coil status, or read input status command, the response is a modbus exception code 01 ILLEGAL FUNCTION. This indicates that these functions are unsupported. Please see the modbus spesification for more details.

### Examples
Read coil status for controller address 02
Command: [02][01][00][02][00][64][9c][12]
Response: [02][81][01][71][90]

Similarily for a read input status request

Command: [02][02][00][02][00][64][d8][12]
Response: [02][81][01][71][90]

### Register examples
By attemting to read a input register the response is modbus exception 02 ILLEGAL DATA ADDRESS.
[02][84][02][32][C1]
