This is the standard design for Modbus protocol in which frames of Modbus RTU and Modbus TCP differ. The structure of this design is as follows:
* In ModbusRTUFrame (ModbusRTUFrame.py file) which corresponds to "modbus-rtu-frame" STIX object type, there is a property called "pdu" whose type is PDU.
* In ModbusTCPFrame (ModbusTCPFrame.py file) which corresponds to "modbus-tcp-frame" STIX object type, there is a property called "pdu" whose type is PDU.
* PDU (PDU.py file) which corresponds to "pdu" STIX object type represents the PDU section of Modbus (both RTU and TCP) messages.