#!/usr/bin/env python3
# This object type (a part of the standard GOOSE) includes four fields of the GOOSE frame
# in addition to a property from the GOOSEPDU type (which includes the GOOSE pdu). The main source for design is
# "IEC 61850 network cybersecurity: Mitigating GOOSE message vulnerabilities" by
# da Silveira, Mauricio Gadelha and Franco, Paulo Henrique.
# Copyright 2021 CIC

from stix2 import properties
from stix2 import CustomObject
from GOOSEPdu import GOOSEPdu as GP


@CustomObject('goose', [
    ('aPPID', properties.IntegerProperty(required=True, min=0 , max=65535)),
    ('length', properties.IntegerProperty(required=True, min=0, max=65535)),
    ('reserved1', properties.IntegerProperty(required=True, min=0, max=65535)),
    ('reserved2', properties.IntegerProperty(required=True, min=0, max=65535)),
    ('goosePdu', properties.STIXObjectProperty(GP))
])
class GOOSE(object):
    def __init__(self, Reserved1=None, Reserved2=None, **kwargs):
        if Reserved1 and Reserved1 != 0:
            raise ValueError ("the value for Reserved1 is invalid")
        if Reserved2 and Reserved2 != 0:
            raise ValueError ("the value for Reserved2 is invalid")


