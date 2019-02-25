---
title: PDOSCSI\_ADDR WMI Class
description: PDOSCSI\_ADDR WMI Class
ms.assetid: 8fdcfc5a-308a-457f-a015-e082e96f9df7
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# PDOSCSI\_ADDR WMI Class


An MPIO driver uses the PDOSCSI\_ADDR WMI class to identify the SCSI address of a physical device.

```cpp
class PDOSCSI_ADDR
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

When this class definition iscompiled by the WMI tool suite, it produces the [**PDOSCSI\_ADDR**](https://msdn.microsoft.com/library/windows/hardware/ff563809) data structure. There are no methods associated with this WMI class.

 

 





