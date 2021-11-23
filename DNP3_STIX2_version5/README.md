The structure of the DNP3 protocol's design is as follows:
* In DNP3Frame (DNP3Frame.py file) which corresponds to "dnp3-frame" STIX object type, there is a property called "data_section" whose type is DNP3DataSection.
* In DNP3DataSection (DNP3DataSection.py file) which corresponds to "dnp3-data-section" STIX object type, there is a property called "application_data" whose type is DNP3ApplicationData.
* In DNP3ApplicationData (DNP3ApplicationData.py file) which corresponds to "dnp3-application-data" STIX object type, there is a list property called "segment_objects" whose type is DNP3Segment.
* In DNP3Segment (DNP3Segment.py file) which corresponds to "dnp3-segment" STIX object type, there is a list property called "dnp3_objects" whose type is DNP3Object.
* DNP3Object (DNP3Object.py file) which corresponds to "dnp3-object" STIX object type represents the data to be conveyed.

