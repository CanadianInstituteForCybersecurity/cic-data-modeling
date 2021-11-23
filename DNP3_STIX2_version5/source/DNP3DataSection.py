# !/usr/bin/env python3
# This object type (a part of the standard DNP3 Frame) includes the fields of
# Transport header in addition to a property which is from the DNP3ApplicationData
# type. The source for design is "DNP3 SPECIFICATION Volume 1: DNP3 INTRODUCTION"
# (https://cdn.chipkin.com/assets/uploads/imports/resources/DNP3Introduction-Draft_G.pdf)
# Copyright 2021 CIC

from stix2 import properties
from stix2 import CustomObject
import DNP3ApplicationData as ap


@CustomObject('dnp3-data-section', [
    ('header_fin', properties.IntegerProperty(required=True, min=0, max=1)),
    ('header_fir', properties.IntegerProperty(required=True, min=0, max=1)),
    ('header_sequence', properties.IntegerProperty(required=True, min=0, max=63)),
    ('application_data', properties.STIXObjectProperty(ap.DNP3ApplicationData, required=True))
])

class DNP3DataSection(object):
    def __init__(self, **kwargs):
        pass



