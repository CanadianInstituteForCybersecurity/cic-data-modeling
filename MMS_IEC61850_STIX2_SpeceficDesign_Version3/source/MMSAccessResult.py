#!/usr/bin/env python3
# This object type is used in the MMSResponsePdu class. The structure for this design is based on the observations of
# packets in wireshark.
# Copyright 2021 CIC

from stix2 import properties
from stix2 import CustomObject

@CustomObject('mms-access-result', [
    ('status', properties.BooleanProperty(required=True)),
    ('number_of_items', properties.IntegerProperty()),
    ('data_list', properties.ListProperty(properties.Property))
])

class MMSAccessResult(object):
    def __init__(self, **kwargs):
        pass



