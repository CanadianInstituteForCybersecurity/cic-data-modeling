#!/usr/bin/env python3
# This object type is to represent the PDU section of library-based Modbus.
# Copyright 2021 CIC

from stix2 import properties
from stix2 import CustomObject


@CustomObject('modbus-pdu', [
    ('function_code', properties.IntegerProperty(required=True, min=0, max=255)),
    ('address', properties.IntegerProperty(min=0, max=65535)),
    ('quantity', properties.IntegerProperty(min=0, max=65280)),
    ('value', properties.IntegerProperty(min=0, max=65535)),
])
class ModbusPdu(object):
    def __init__(self, **kwargs):
        pass


