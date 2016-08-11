# DanfossRead
Software for communication with the Modbus interface of the Danfoss EKC202 refrigerator controllers.

The interface is intended to be used in cojunction with the properietary ADAP-KOOL® system from Danfoss. No documentation regarding the communication protocol is provided, and thus the prodocol must be reverse enigneered.


## Interface board
In order for the controller to support Modbus, the EKA178A extention module must be connected. The module consists of a Atmel Atmega32 microcontroller, a 6LB184 differential transciever, and a CM0403CG common mode choke connected between the transciever and the RS485 terminals.

The board connects to a 8-pin socket in the controller.

There are no labels on the screw terminals for the RS485 bus, the correct connection has been determined by inspecting the circuit board.


![alt tag](https://raw.githubusercontent.com/gbThreepwood/DanfossRead/master/eka178a.jpg)

![alt tag](https://raw.githubusercontent.com/gbThreepwood/DanfossRead/master/ekc202_front.jpg)

![alt tag](https://raw.githubusercontent.com/gbThreepwood/DanfossRead/master/ekc202_top.jpg)
