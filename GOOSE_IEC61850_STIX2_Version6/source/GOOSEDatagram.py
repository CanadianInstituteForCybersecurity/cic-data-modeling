#!/usr/bin/env python3
# This object type (a part of the standard GOOSE) includes some of the fields of the GOOSE frame
# in addition to a property from the GOOSE object type. The main source for design is
# "IEC 61850 network cybersecurity: Mitigating GOOSE message vulnerabilities" by
# da Silveira, Mauricio Gadelha and Franco, Paulo Henrique.
# Copyright 2021 CIC

from stix2 import properties
from stix2 import CustomObject
from GOOSE import GOOSE as g

@CustomObject('goose-datagram', [
    ('preamble', properties.IntegerProperty(required=True, min=0, max=72057594037927935)),
    ('start_frame', properties.IntegerProperty(required= True)),
    ('destination_MAC', properties.StringProperty(required=True)),
    ('source_MAC', properties.StringProperty(required=True)),
    ('tag', properties.IntegerProperty(required=True)),
    ('ethertype', properties.IntegerProperty(required=True)),
    ('goose_frame', properties.STIXObjectProperty(g))
])
class GOOSEDatagram(object):
    def __init__(self, tag= None, preamble=None, start_frame=None, destination_MAC=None, source_MAC=None, ethertype=None, **kwargs):
        if preamble and preamble not in range (0, 72057594037927936):
            raise ValueError ("the value for preamble is invalid")
        if start_frame and start_frame != 171:
            raise ValueError ("the value for start_frame is invalid")
        if tag and tag != 2164295784:
            raise ValueError("the value for tag is invalid")
        if destination_MAC and destination_MAC.startswith("01-0C-CD-01")!= True:
            raise ValueError ("the value for destination_MAC is invalid")
        if source_MAC and source_MAC.startswith("01-0C-CD-01")!= True:
            raise ValueError ("the value for source_MAC is invalid")
        if ethertype and ethertype != 35000:
            raise ValueError ("the value for ethertype is invalid")


