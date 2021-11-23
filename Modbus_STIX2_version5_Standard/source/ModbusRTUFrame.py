#!/usr/bin/env python3
# This object type is to represent the standard Modbus (RTU). It further includes an object of the
# PDU class (as one of its properties - This property exists in Modbus TCP as well).
# The main sources for design are https://www.simplymodbus.ca/TCP.htm and
# "MODBUS APPLICATION PROTOCOL SPECIFICATION V1. 1b3"
# Copyright 2021 CIC

from stix2 import properties
from stix2 import CustomObject
import PDU as pdu


@CustomObject('modbus-rtu-frame', [
    ('address', properties.IntegerProperty(required = True, min=0, max=255)),
    ('pdu', properties.STIXObjectProperty(pdu.PDU))
])

class ModbusRTUFrame(object):
        def __init__(self, **kwargs):
            pass


