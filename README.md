# Introduction
We present custom OT-based STIX models that can be used in the OT environment. The five OT protocols that we have modelled using the [stix2](https://github.com/oasis-open/cti-python-stix2) library are:
* DNP3
* Modbus (there are two versions for Modbus, one is library-based and the other one is standard Modbus)
* IEC61850-MMS (there are two versions for MMS, one is "general" and the other one includes the details for "confirmed-RequestPDU - Read" and "confirmed-ResponsePDU - Read")
* IEC61850-GOOSE
* OPC-A&E 

There are two groups of STIX models that we created. The first is used for remediation; it contains connection parameters about the device and the command to run on that device.
The second can be used for data collection which can be passed on to threat intelligence; they are mapped directly to frame of each OT protocol such that a packet that is sniffed on the network can be directly mapped to the model.
Most of the designed models follow a nested structure which means each object type related to a protocol (corresponded to a frame or part of a frame) may include another object type as one of its property's type.

# Protocol Directory
Each directory related to a specific protocol consists of two subfolders:
* Source: contains class files (including STIX objects for that protocol)
* Example: contains an example of how the STIX model is used

A README.md file is available for each protocol design as well.

**Note:** In our design (in different protocols), we have defined fields as required or optional. However, it (being required or optional) can be changed based on the requirements for some fields (by adding or removing "required=True" in the definitions).

`**Note:** Examples provided (as instances in example directory for each protocol or protocol variation) are not based on real scenarios or values and are just to provide a general understanding of how the models work and also to check the models.

# Support
For support and other details, please contact [Kwasi Boakye-Boateng](mailto:kwasi.boakye-boateng@unb.ca).

# Contributors
[Ida Sri Rejeki Siahaan](mailto:ida.siahaan@unb.ca)
[Mahdi Abrishami](mailto:mahdi.abrishami@unb.ca)
[Kwasi Boakye-Boateng](mailto:kwasi.boakye-boateng@unb.ca)
