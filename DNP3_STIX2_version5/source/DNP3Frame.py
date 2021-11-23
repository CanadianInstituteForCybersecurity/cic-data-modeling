# !/usr/bin/env python3
# This object type (a part of the standard DNP3 Frame) includes the fields of
# Data link header in addition to a property which is from the DNP3DataSection
# type. The source for design is "DNP3 SPECIFICATION Volume 1: DNP3 INTRODUCTION"
# (https://cdn.chipkin.com/assets/uploads/imports/resources/DNP3Introduction-Draft_G.pdf)
# Copyright 2021 CIC

from stix2 import properties
from stix2 import CustomObject
import DNP3DataSection as ds


@CustomObject('dnp3-frame', [
    ('start', properties.IntegerProperty(required=True)),
    ('header_length', properties.IntegerProperty(required=True, min=5, max=255)),
    ('header_link_control', properties.IntegerProperty(required=True, min=0, max=255)),
    ('header_source_address', properties.IntegerProperty(required=True, min=0, max=65519)),
    ('header_destination_address', properties.IntegerProperty(required=True, min=0, max=65535)),
    ('data_section', properties.STIXObjectProperty(ds.DNP3DataSection, required=True)),
])
class DNP3Frame(object):
        def __init__(self, start=None, **kwargs):
            if start and start != 1380:
                raise ValueError("the value for start is invalid")


