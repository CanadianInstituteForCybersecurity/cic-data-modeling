#!/usr/bin/env python3
# This object type (a part of the standard DNP3 Frame) includes a list of
# DNP3 objects (a list which includes objects of DNP3Object type).
#  The sources for design are "DNP3 SPECIFICATION Volume 1: DNP3 INTRODUCTION"
#  (https://cdn.chipkin.com/assets/uploads/imports/resources/DNP3Introduction-Draft_G.pdf)
# and "DNP3, Distributed Network Protocol v3 an INTRODUCTION"
# (https://na.eventscloud.com/file_uploads/b68188f3ce5b22895a67b1afe5e51b6a_DNP3IntroductionHORS.PDF)
# Copyright 2021 CIC

from stix2 import properties
from stix2 import CustomObject
import DNP3Object as do


@CustomObject('dnp3-segment', [
    ('header_group', properties.IntegerProperty(required=True)),
    ('header_variation', properties.IntegerProperty(required=True)),
    ('header_qualifier_field', properties.IntegerProperty(required=True, min=0, max=255)),
    ('header_range_field', properties.IntegerProperty(min=0, max=4294967294)),
    ('dnp3_objects', properties.ListProperty(do.DNP3Object)),
])
class DNP3Segment(object):
    def __init__(self, header_group=None, header_variation=None,  **kwargs):
        if header_group and header_group not in [10, 12, 40, 41, 1, 2, 20, 21, 22, 23, 30, 32]:
            raise ValueError("the value for header_group in invalid")
        if header_variation:
            if (header_group == 10 and header_variation not in [1, 2]):
                raise ValueError("the value for header_variation in invalid")
            if (header_group == 12 and header_variation not in [1, 2, 3]):
                raise ValueError("the value for header_variation in invalid")
            if (header_group in [40, 41] and header_variation not in [1, 2, 3, 4]):
                raise ValueError("the value for header_variation in invalid")
            if (header_group == 1 and header_variation not in [1, 2]):
                raise ValueError("the value for header_variation in invalid")
            if (header_group == 2 and header_variation not in [1, 2, 3]):
                raise ValueError("the value for header_variation in invalid")
            if (header_group == 30 and header_variation not in [1, 2, 3, 4, 5, 6]):
                raise ValueError("the value for header_variation in invalid")
            if (header_group == 32 and header_variation not in [1, 2, 3, 4, 5, 6, 7, 8]):
                raise ValueError("the value for header_variation in invalid")
            if (header_group in [20, 22] and header_variation not in [1, 2, 5, 6]):
                raise ValueError("the value for header_variation in invalid")



