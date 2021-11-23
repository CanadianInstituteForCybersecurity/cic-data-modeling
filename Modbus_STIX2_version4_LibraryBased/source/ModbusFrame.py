#!/usr/bin/env python3
# This object type is to represent the library-based Modbus. It further includes an object of the
# ModbusPDU class (as one of its properties). The command_type property defines whether it is
# Modbus TCP or Modbus RTU.
# Copyright 2021 CIC

import ModbusPdu
from stix2 import properties
from stix2 import CustomObject
import ModbusPdu as a
import random


@CustomObject('modbus-frame', [
    ('host', properties.StringProperty(required=True)),
    ('unit_id', properties.IntegerProperty(min=0, max=255)),
    ('command_type', properties.StringProperty(required=True)),
    ('pdu', properties.STIXObjectProperty(ModbusPdu.ModbusPdu))
])

class ModbusFrame(object):
        def __init__(self, host, command_type, **kwargs):
            if host and (host == "" or not host):
                raise ValueError("the value for host is invalid")
            if command_type and command_type not in ["TCP", "RTU"]:
                raise ValueError ("the value for command type is invalid")

