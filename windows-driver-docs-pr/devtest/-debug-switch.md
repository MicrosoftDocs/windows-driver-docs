---
title: /Debug Switch
description: The /Debug switch of the Enhanced Storage Certificate Management tool reports on the capabilities and information about the authentication silo certificate (ASC) store in an IEEE 1667-compliant USB storage device.
ms.assetid: 9a7c8fd0-34a8-4f60-a8cb-d5777645f672
keywords:
- /Debug Switch Driver Development Tools
topic_type:
- apiref
api_name:
- /Debug
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# /Debug Switch


The /**Debug** switch of the Enhanced Storage Certificate Management tool reports on the capabilities and information about the authentication silo certificate (ASC) store in an IEEE 1667-compliant USB storage device. This report includes the following parts:

-   The algorithms that are used for hashing and signing.

-   The total number of certificate slots.

-   The number of occupied and empty certificate slots.

**Note**  In this topic, the specified IEEE 1667-compliant USB storage device is referred to as the *target device*.



```
    EhStorCertMgrCmd /Debug -Volume:
    VolumeName
```

## <span id="Subparameters"></span><span id="subparameters"></span><span id="SUBPARAMETERS"></span>Subparameters


<span id="_______-Volume_______"></span><span id="_______-volume_______"></span><span id="_______-VOLUME_______"></span> **-Volume:**   
The volume name of the target device. For more information about the format of this parameter, see [Overview of the Enhanced Storage Certificate Management Tool](overview-of-the-enhanced-storage-certificate-management-tool.md).

**Note**  To produce a list of the volume names of the IEEE 1667-compliant USB storage devices that are currently connected to a computer, enter **EhStorCertMgrCmd /List** from the command-line.



### <span id="example"></span><span id="EXAMPLE"></span>Example

The following example shows an excerpt from the output that is produced by the **/Debug** switch:

```
Execute Debug operation for specified volume name...

Certificate silo device Capabilities...

Certificate Extension Parsing :- 1
Render User Data Unusable :- 1

Hash Algorithm :-
1.3.14.3.2.26
2.16.840.1.101.3.4.2.1
2.16.840.1.101.3.4.2.2
2.16.840.1.101.3.4.2.3

Asymmetric Key Cryptography :-
1.2.840.113549.1.1.1,1024
1.2.840.113549.1.1.1,2048
1.2.840.113549.1.1.1,3072

Signing Algorithm :-
1.2.840.113549.1.1.10,1.3.14.3.2.26
1.2.840.113549.1.1.10,2.16.840.1.101.3.4.2.1
1.2.840.113549.1.1.10,2.16.840.1.101.3.4.2.2
1.2.840.113549.1.1.10,2.16.840.1.101.3.4.2.3
1.3.14.3.2.29
1.2.840.113549.1.1.5
1.2.840.113549.1.1.11
1.2.840.113549.1.1.12
1.2.840.113549.1.1.13

Firmware version :- 1.1

Specification version :- 1.1

Total available slots   :- 16
Occupied slots          :- 3
Free slots              :- 13
```





