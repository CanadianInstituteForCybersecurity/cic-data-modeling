#!/usr/bin/env python3
# This file includes an instance of our design for MMS (the general design).
# Copyright 2021 CIC

from MMSPdu import MMSPdu as MP

mp_1 = MP(mms_pdu_type="confirmed-RequestPDU",
          invoke_id=20,
          service_type="Read",
          content_list= ["listOfvariable", [10, 20], [30, 70]])
mp_2 = MP(mms_pdu_type="confirmed-RequestPDU",
          invoke_id=21,
          service_type="Read",
          content_list= ["variableListName", [10, 20]])
mp_3 = MP(mms_pdu_type="confirmed-ResponsePDU",
          invoke_id=22,
          service_type="Read",
          content_list=[[True, [22, 23, 24, 225, 26, 27, 28, 29, 30]], [False]])


print(mp_1)
print("*****************************************************************************************")
print(mp_2)
print("*****************************************************************************************")
print(mp_3)



