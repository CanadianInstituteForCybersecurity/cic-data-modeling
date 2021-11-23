This is the library-based design for Modbus protocol in which it is assumed that some parts are handled by the library. The structure of this design is as follows:
* In ModbusFrame (ModbusFrame.py file) which corresponds to "modbus-frame" STIX object type, there is a property called "pdu" whose type is ModbusPdu.
* ModbusPdu (ModbusPdu.py file) which corresponds to "modbus-pdu" STIX object type represents the PDU section of Modbus messages.