---
title: MPIO\_DISK\_HEALTH\_INFO WMI Class
description: MPIO\_DISK\_HEALTH\_INFO WMI Class
ms.assetid: 5a3ca8be-8940-4ba4-9206-75d0c7c90d53
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MPIO\_DISK\_HEALTH\_INFO WMI Class


An MPIO driver uses the MPIO\_DISK\_HEALTH\_INFO WMI class to report health statistics of all the MPIO disks that it manages.

```cpp
class MPIO_DISK_HEALTH_INFO
{
    [key, read]
     string InstanceName;
    [read] boolean Active;

    [WmiDataId(1),
     read,
     Description("Number of Pseudo-LUN Health Packets.") : amended
    ] uint32 NumberDiskPackets;

    [WmiDataId(2),
     read,
     Description("Reserved for future use.") : amended
    ] uint32 Reserved;

    [WmiDataId(3),
     read,
     Description("MPIO Pseudo-LUN Health Info Array.") : amended,
     WmiSizeIs("NumberDiskPackets")
    ] MPIO_DISK_HEALTH_CLASS DiskHealthPackets[];
};
```

When this class definition is compiled by the WMI tool suite, it produces the [**MPIO\_DISK\_HEALTH\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff562359) data structure. There are no methods associated with this WMI class.

 

 





