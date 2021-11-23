#!/usr/bin/env python3
# This file includes instances of our design for Modbus RTU and TCP (the standard design).
# Copyright 2021 CIC

import PDU
import ModbusRTUFrame
import ModbusTCPFrame
print("Modbus RTU")
pdu_obj = PDU.PDU(function_code=200,
          data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

rtu_obj = ModbusRTUFrame.ModbusRTUFrame(address = 200,
                                        pdu = pdu_obj)
print(rtu_obj)
print ("*******************************************************************************************")
pdu_obj = PDU.PDU(function_code=250,
                  data=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])

tcp_obj = ModbusTCPFrame.ModbusTCPFrame(transaction_id = 60000,
                                        protocol_id = 0,
                                        length = 5000,
                                        unit_id = 200,
                                        pdu = pdu_obj)
print(tcp_obj)