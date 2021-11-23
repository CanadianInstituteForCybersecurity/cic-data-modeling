#!/usr/bin/env python3
# This object type (a part of the standard GOOSE) is to represent the GOOSE pdu. The main source for design is
# "IEC 61850 network cybersecurity: Mitigating GOOSE message vulnerabilities" by
# da Silveira, Mauricio Gadelha and Franco, Paulo Henrique.
# Copyright 2021 CIC

from stix2 import properties
from stix2 import CustomObject

@CustomObject('goose-pdu', [
    ('gocbRef', properties.StringProperty(required=True)),
    ('timeAllowedtoLive', properties.IntegerProperty(required=True)),
    ('datSet', properties.StringProperty(required=True)),
    ('goID', properties.StringProperty(required=True)),
    ('t', properties.TimestampProperty(required=True)),
    ('stNum', properties.IntegerProperty(required=True)),
    ('sqNum', properties.IntegerProperty(required=True)),
    ('simulation', properties.BooleanProperty(required=True)),
    ('confRev', properties.IntegerProperty(required=True)),
    ('ndsCom', properties.BooleanProperty(required=True)),
    ('numDatSetEntries', properties.IntegerProperty(required=True)),
    ('allData', properties.ListProperty(properties.Property))
])

class GOOSEPdu(object):
    def __init__(self, **kwargs):
        pass