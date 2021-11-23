#!/usr/bin/env python3
# This file includes an instance of our design for GOOSE.
# Copyright 2021 CIC

from GOOSE import GOOSE
from GOOSEPdu import GOOSEPdu as GP
from GOOSEDatagram import GOOSEDatagram

goose_pdu = GP (gocbRef = "LIED11PROT/LLN0$Alarm",
                timeAllowedtoLive = 2000,
                datSet = "LIED11PROT/LLN0$Alarm",
                goID = "LIED11PROT/LLN0$Alarm",
                t = "2017-01-28T21:33:10.772474Z",
                stNum = 1,
                sqNum = 19,
                simulation = False,
                confRev = 1,
                ndsCom = False,
                numDatSetEntries = 5,
                allData = [False, True, True, True, True])
goose = GOOSE (aPPID = 1000,
               length = 128,
               reserved1 = 0,
               reserved2 = 0,
               goosePdu = goose_pdu)

goose_datagram = GOOSEDatagram(preamble = 100,
                               start_frame = 171,
                               destination_MAC = "01-0C-CD-01-09-01",
                               source_MAC = "01-0C-CD-01-09-02",
                               tag = 2164295784,
                               ethertype = 35000,
                               goose_frame = goose)
print(goose_datagram)