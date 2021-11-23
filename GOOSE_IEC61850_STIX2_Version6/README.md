The structure of the GOOSE protocol's design is as follows:
* In GOOSEDatagram (GOOSEDatagram.py file) which corresponds to "goose-datagram" STIX object type, there is a property called "goose_frame" whose type is GOOSE.
* In GOOSE (GOOSE.py file) which corresponds to "goose" STIX object type, there is a property called "goosePdu" whose type is GOOSEPdu.
* GOOSEPdu (GOOSEPdu.py file) which corresponds to "goose-pdu" represents the PDU section of GOOSE messages.