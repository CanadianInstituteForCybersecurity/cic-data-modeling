#!/usr/bin/env python3
# This file includes an instance of our design for MMS (confirmed-RequestPDU - Read).
# Copyright 2021 CIC

import MMSDomainSpecific as DS
import MMSRequestPdu as RPDU

ds1 = DS.MMSDomainSpecific(domain_id=10,
        item_id=20)
ds2 = DS.MMSDomainSpecific(domain_id=30,
        item_id=70)
rpdu1 = RPDU.MMSRequestPdu(packet_type="Confirmed-RequestPDU",
                       invoke_id=20,
                       service_type="Read",
                       variable_access_specification="VariableListName",
                       domain_specific_list=[ds1],
                       specification_with_result=True)
rpdu2 = RPDU.MMSRequestPdu(packet_type="Confirmed-RequestPDU",
                       invoke_id=21,
                       service_type="Read",
                       variable_access_specification="ListOfVariable",
                       domain_specific_list=[ds1, ds2],
                       number_of_items=2)
print(rpdu1)
print("*****************************************************************************************")
print(rpdu2)