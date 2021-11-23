#!/usr/bin/env python3
# This object type (a part of the standard DNP3 Frame) includes values to be transmitted as DNP3 objects.
#  The source for design is "DNP3 SPECIFICATION Volume 1: DNP3 INTRODUCTION"
#  (https://cdn.chipkin.com/assets/uploads/imports/resources/DNP3Introduction-Draft_G.pdf)
# Copyright 2021 CIC
from stix2 import properties
from stix2 import CustomObject
@CustomObject('dnp3-object', [
    ('dnp3_object', properties.Property())
])
class DNP3Object(object):
    def __init__(self, **kwargs):
        pass


