#!/usr/bin/env python3
# This object type is to represent the PDU section of the standard Modbus. It is used in the Modbus RTU and
# Modbus TCP frames. The main sources for design are https://www.simplymodbus.ca/TCP.htm and
# # "MODBUS APPLICATION PROTOCOL SPECIFICATION V1. 1b3"
# Copyright 2021 CIC

from stix2 import properties
from stix2 import CustomObject


@CustomObject('pdu', [
    ('function_code', properties.IntegerProperty(required=True, min=0, max=255)),
    ('data', properties.ListProperty(properties.Property()))
])
class PDU(object):
    def __init__(self, **kwargs):
        pass


