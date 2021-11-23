#!/usr/bin/env python3
# This object type is to represent the standard OPC A&E. The main source for design is
# https://www.emerson.com/documents/automation/white-paper-opc-alarms-events-overview-deltav-en-56294.pdf
# Copyright 2021 CIC

from stix2 import properties
from stix2 import CustomObject

@CustomObject('opc-event', [
    ('source', properties.StringProperty(required=True)),
    ('time', properties.TimestampProperty(required=True)),
    ('type', properties.EnumProperty(["condition-related", "tracking-related", "simple"])),
    ('event_category', properties.EnumProperty(["Process Events", "System Events", "Batch Events"], required=True)),
    ('severity', properties.IntegerProperty(required=True, min=1, max=1000)),
    ('message', properties.StringProperty()),
    ('actor_ID', properties.StringProperty(required=True)),
    ('condition_name', properties.StringProperty()),
    ('sub_condition_name', properties.StringProperty()),
    ('change_mask', properties.ListProperty(properties.StringProperty)),
    ('new_state', properties.StringProperty()),
    ('condition_quality', properties.IntegerProperty(min=0, max=255)),
    ('ack_required', properties.BooleanProperty()),
    ('active_time', properties.TimestampProperty()),
    ('cookie', properties.StringProperty())

])
class OPCEvent(object):
    def __init__(self, type, actor_ID, **kwargs):
        if (type=="tracking-related" and bool(actor_ID)==False):
            raise ValueError ("actor_ID should not be null in the tracking-related")




