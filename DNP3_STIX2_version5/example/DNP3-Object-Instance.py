#!/usr/bin/env python3
# This file includes an instance of our design for DNP3.
# Copyright 2021 CIC

import DNP3DataSection as ds
import DNP3Object as do
import DNP3Segment as dns
import DNP3ApplicationData as ap
import DNP3Frame as df
DO_object =  do.DNP3Object(dnp3_object=1000)
DS_object = dns.DNP3Segment(header_group=10,
                         header_variation=2,
                         header_qualifier_field=12,
                         header_range_field=13,
                         dnp3_objects=[DO_object])
AP_object = ap.DNP3ApplicationData(header_application_control=21,
                             header_function_code=22,
                             header_lsb=23,
                             header_msb=24,
                             segment_objects=[DS_object])
DS_object = ds.DNP3DataSection(header_fin=1,
                         header_fir=1,
                         header_sequence=31,
                         application_data=AP_object)
DF_object = df.DNP3Frame(start = 1380,
                  header_length=42,
                  header_link_control=43,
                  header_source_address=44,
                  header_destination_address=45,
                  data_section=DS_object)
print(DF_object)