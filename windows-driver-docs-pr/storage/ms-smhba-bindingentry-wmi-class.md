---
title: MS\_SMHBA\_BINDINGENTRY WMI Class
description: MS\_SMHBA\_BINDINGENTRY WMI Class
ms.assetid: b7b2315f-21db-41a4-8390-3c413cb39f5b
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MS\_SMHBA\_BINDINGENTRY WMI Class


An HBA miniport driver that supports the Storage Management API uses the MS\_SMHBA\_BINDINGENTRY class to expose binding information between data that the operating system uses to identify a SCSI device and the SSP protocol identifier for the device.

The MS\_SMHBA\_BINDINGENTRY class is defined as follows in Hbaapi.mof:

```cpp
class MS_SMHBA_BINDINGENTRY
{
    [SMHBA_BIND_TYPE_QUALIFIERS, WmiDataId(1)]
    uint32 type;

    [HBAType("MS_SMHBA_PORTLUN"), WmiDataId(2)]
    MS_SMHBA_PORTLUN  PortLun;

    [HBAType("HBA_LUID"), WmiDataId(3)]
    uint8  LUID[256];

    [HBA_STATUS_QUALIFIERS, WmiDataId(4)]
    HBA_STATUS Status;

    [HBAType("HBA_SCSIID"), WmiDataId(5)]
    HBAScsiID ScsiId;
};
```

When this class definition is compiled by the WMI tool suite, it produces the following data structure:

MS\_SMHBA\_BINDINGENTRY found in hbapiwmi.h.

There are no methods associated with this WMI class.

 

 





