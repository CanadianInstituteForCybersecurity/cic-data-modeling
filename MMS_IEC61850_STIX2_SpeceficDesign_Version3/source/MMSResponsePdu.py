#!/usr/bin/env python3
# This object type is to represent the confirmed-ResponsePDU -Read type in MMS. It further includes a list
# from the MMSAccessResult type. The structure for this design is based on the observations of
# packets in wireshark.
# Copyright 2021 CIC

from stix2 import properties
from stix2 import CustomObject
import MMSAccessResult as AR


@CustomObject('mms-response-pdu', [
    ('packet_type', properties.StringProperty(required=True)),
    ('invoke_id', properties.IntegerProperty(required=True)),
    ('service_type', properties.StringProperty(required=True)),
    ('number_of_access_results', properties.IntegerProperty()),
    ('access_result_list', properties.ListProperty(AR.MMSAccessResult))
])

class MMSResponsePdu(object):
    def __init__(self, packet_type=None, service_type=None, **kwargs):
        if packet_type and packet_type != "Confirmed-ResponsePDU":
            raise ValueError("the value for packet_type is invalid")
        if service_type and service_type != "Read":
            raise ValueError("the value for service_type is invalid")


