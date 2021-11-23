#!/usr/bin/env python3
# This object type (a part of the standard DNP3 Frame) includes the fields
# of Application header in addition to a list property which is from the DNP3Segment
# type. The source for design is "DNP3 SPECIFICATION Volume 1: DNP3 INTRODUCTION"
# (https://cdn.chipkin.com/assets/uploads/imports/resources/DNP3Introduction-Draft_G.pdf)
# Copyright 2021 CIC

from stix2 import CustomObject
from stix2 import properties
from DNP3Segment import DNP3Segment


@CustomObject('dnp3-application-data', [
    ('header_application_control', properties.IntegerProperty(required=True, min=0, max=255)),
    ('header_function_code', properties.IntegerProperty(required=True, min=0, max=255)),
    ('header_lsb', properties.IntegerProperty(required=True, min=0, max=255)),
    ('header_msb', properties.IntegerProperty(required=True, min=0, max=255)),
    ('segment_objects', properties.ListProperty(DNP3Segment, required=True))
])
class DNP3ApplicationData(object):
    def __init__(self, **kwargs):
        pass





