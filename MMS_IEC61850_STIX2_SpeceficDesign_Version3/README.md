This design is specific to two types of MMS messages including confirmed-RequestPDU (Read) and confirmed-ResponsePDU (Read).
The structure for confirmed-RequestPDU (Read) is as follows:
* In MMSRequestPdu (MMSRequestPdu.py file) which corresponds to "mms-request-pdu" STIX object type, there is a list property called "domain_specific_list" whose type is MMSDomainSpecific.
* MMSDomainSpecific (MMSDomainSpecific.py file) which corresponds to "mms-domain-specific" STIX object type represents a section required in MMSRequestPdu.
The structure for confirmed-ResponsePDU (Read) is as follows:
* In MMSResponsePdu (MMSResponsePdu.py file) which corresponds to "mms-response-pdu" STIX object type, there is a list property called "access_result_list" whose type is MMSAccessResult.
* MMSAccessResult (MMSAccessResult.py file) which corresponds to "mms-access-result" STIX object type represents a section required in MMSResponsePdu.
