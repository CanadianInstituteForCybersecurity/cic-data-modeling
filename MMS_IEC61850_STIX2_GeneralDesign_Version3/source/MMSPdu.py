#!/usr/bin/env python3
# This file includes a general design (encompassing different pdu types) of the standard MMS protocol.
# The main source for design is https://www.sisconet.com/wp-content/uploads/2016/03/mms_abstract_syntax.txt
# Copyright 2021 CIC

from stix2 import properties
from stix2 import CustomObject


allowed_pdu_types = ["confirmed-RequestPDU", "confirmed-ResponsePDU", "confirmed-ErrorPDU",
                     "unconfirmed-PDU", "reject-PDU", "cancel-RequestPDU", "cancel-ResponsePDU",
                     "initiate-RequestPDU", "initiate-ResponsePDU", "initiate-ErrorPDU",
                     "conclude-RequestPDU", "conclude-ResponsePDU", "conclude-ErrorPDU"]
@CustomObject('mms-pdu', [
    ('mms_pdu_type', properties.EnumProperty(allowed_pdu_types, required=True)),
    ('invoke_id', properties.IntegerProperty()),
    ('service_type', properties.EnumProperty(["Read", "Write"])),
    ('content_list', properties.ListProperty(properties.Property))
])
class MMSPdu(object):
    def __init__(self, **kwargs):
        pass




