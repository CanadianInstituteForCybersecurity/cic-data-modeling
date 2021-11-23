#!/usr/bin/env python3
# This file includes instances of our design for OPC A&E.
# Copyright 2021 CIC
import OPCEvent as OE


opc_event1 = OE.OPCEvent(source="192.168.100.27",
                      time="2017-01-28T21:33:10.772474Z",
                      type="simple",
                      actor_ID="",
                      event_category="Process Events",
                      severity=900,
                      message="This is a message related to the OPC A&E specification - simple",
                      )
print (opc_event1)
print ("********************************************************************************************")
opc_event2 = OE.OPCEvent(source="192.168.100.27",
                      time="2017-01-28T21:33:10.772474Z",
                      type="tracking-related",
                      event_category="System Events",
                      severity=900,
                      actor_ID="Actor1",
                      message="This is a message related to the OPC A&E specification - tracking-related"
                      )
print(opc_event2)
print ("********************************************************************************************")
opc_event3 = OE.OPCEvent(source="192.168.100.27",
                      time="2017-01-28T21:33:10.772474Z",
                      type="condition-related",
                      event_category="System Events",
                      severity=900,
                      message="This is a message related to the OPC A&E specification - tracking-related",
                      actor_ID="Actor2",
                      condition_name="condition",
                      sub_condition_name="sub_condition",
                      change_mask=["change_mask1", "change_mask2"],
                      new_state="new_state",
                      condition_quality=100,
                      ack_required=True,
                      active_time="2017-01-28T21:33:10.772474Z",
                      cookie="cookie"
                      )
print(opc_event3)