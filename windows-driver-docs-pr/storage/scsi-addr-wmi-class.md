---
title: SCSI\_ADDR WMI Class
description: SCSI\_ADDR WMI Class
ms.assetid: 720cf803-b004-4c63-8884-66b0e07d82c0
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SCSI\_ADDR WMI Class


An MPIO driver uses the SCSI\_ADDR WMI class to identify the SCSI address of an MPIO disk.

```cpp
class SCSI_ADDR
{
    //
    // ScsiAddress: Port, Bus, Target, Lun
    //
    [WmiDataId(1)] uint8 PortNumber;
    [WmiDataId(2)] uint8 ScsiPathId;
    [WmiDataId(3)] uint8 TargetId;
    [WmiDataId(4)] uint8 Lun;
};
```

When this class definition is compiled by the WMI tool suite, it produces the [**SCSI\_ADDR**](https://msdn.microsoft.com/library/windows/hardware/ff564952) data structure. There are no methods associated with this WMI class.

 

 





