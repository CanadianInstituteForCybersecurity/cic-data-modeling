#!/usr/bin/env python3
# This file includes an instance of our design for Modbus (the library-based design).
# Copyright 2021 CIC

import ModbusPdu as MP
import ModbusFrame as MF
print("Modbus RTU")
pdu_obj = MP.ModbusPdu(function_code=51,
          address=52,
          quantity=53,
          value=54)

rtu_obj = MF.ModbusFrame(host="192,168.1.2",
                    unit_id=61,
                    command_type = "RTU",
                    pdu=pdu_obj)
print(rtu_obj)
print ("*******************************************************************************************")
pdu_obj = MP.ModbusPdu(function_code=71,
          address=72,
          quantity=73,
          value=74)

tcp_obj = MF.ModbusFrame(host="192,168.1.2",
                    unit_id=81,
                    command_type = "TCP",
                    pdu=pdu_obj)
print(tcp_obj)