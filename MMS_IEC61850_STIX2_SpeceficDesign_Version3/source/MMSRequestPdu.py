#!/usr/bin/env python3
# This object type is to represent the confirmed-RequestPDU - Read type in MMS. It further includes a list
# from the MMSDomainSpecific type. The structure for this design is based on the observations of
# packets in wireshark.
# Copyright 2021 CIC

from stix2 import properties
from stix2 import CustomObject
import MMSDomainSpecific as DS

@CustomObject('mms-request-pdu', [
    ('packet_type', properties.StringProperty(required=True)),
    ('invoke_id', properties.IntegerProperty(required=True)),
    ('service_type', properties.StringProperty(required=True)),
    ('variable_access_specification', properties.EnumProperty(["ListOfVariable", "VariableListName"], required=True)),
    ('domain_specific_list', properties.ListProperty(DS.MMSDomainSpecific)),
    ('number_of_items', properties.IntegerProperty()),
    ('specification_with_result', properties.BooleanProperty())
])

class MMSRequestPdu(object):
    def __init__(self, packet_type=None, service_type=None, variable_access_specification=None, **kwargs):
        if packet_type and packet_type != "Confirmed-RequestPDU":
            raise ValueError("the value for packet_type is invalid")
        if service_type and service_type != "Read":
            raise ValueError("the value for service_type is invalid")



