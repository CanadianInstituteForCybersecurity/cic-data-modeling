#!/usr/bin/env python3
# This object type is used in the MMSRequestPDU class. The structure for this design is based on the observations of
# packets in wireshark.
# Copyright 2021 CIC

from stix2 import properties
from stix2 import CustomObject


@CustomObject('mms-domain-specific', [
    ('domain_id', properties.StringProperty(required=True)),
    ('item_id', properties.StringProperty(required=True)),
])

class MMSDomainSpecific(object):
    def __init__(self, **kwargs):
        pass


