#!/usr/bin/env python3
# This file includes an instance of our design for MMS (confirmed-ResponsePDU - Read).
# Copyright 2021 CIC

import MMSAccessResult as AR
import MMSResponsePdu as RPDU

ar1 = AR.MMSAccessResult(status=True,
                      number_of_items=8,
                      data_list=[22,23,24,25,23,234,54,34])
ar2 = AR.MMSAccessResult(status=False)
rpdu = RPDU.MMSResponsePdu(packet_type="Confirmed-ResponsePDU",
                       invoke_id=24,
                       service_type="Read",
                       number_of_access_results=2,
                       access_result_list=[ar1, ar2])

print(rpdu)

