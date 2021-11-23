#!/usr/bin/env python3
# This object type is to represent the standard Modbus (TCP). It further includes an object of the
# PDU class (as one of its properties - This property exists in Modbus RTU as well).
# The main sources for design are https://www.simplymodbus.ca/TCP.htm and
# "MODBUS APPLICATION PROTOCOL SPECIFICATION V1. 1b3"
# Copyright 2021 CIC

from stix2 import properties
from stix2 import CustomObject
import PDU as pdu


@CustomObject('modbus-tcp-frame', [
    ('transaction_id', properties.IntegerProperty(required=True, min=0, max=65535)),
    ('protocol_id', properties.IntegerProperty(required=True, min=0, max=65535)),
    ('length', properties.IntegerProperty(required=True, min=0, max=65535)),
    ('unit_id', properties.IntegerProperty(required=True, min=0, max=255)),
    ('pdu', properties.STIXObjectProperty(pdu.PDU))
])

class ModbusTCPFrame(object):
        def __init__(self, protocol_id, **kwargs):
            if protocol_id and protocol_id != 0:
                raise ValueError ("Invalid value for protocol_identifier")

