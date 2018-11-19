---
title: MPIO\_PATH\_HEALTH\_INFO WMI Class
description: MPIO\_PATH\_HEALTH\_INFO WMI Class
ms.assetid: 26c329d0-0d9c-4d24-bbe4-ebb7d7b36a89
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MPIO\_PATH\_HEALTH\_INFO WMI Class


A WMI client uses the MPIO\_PATH\_HEALTH\_INFO WMI class to query MPIO so that it gathers statistics for all paths that are managed by MPIO.

```cpp
class MPIO_PATH_HEALTH_INFO
{
    [key, read]
     string InstanceName;
    [read] boolean Active;

    [WmiDataId(1),
     read,
     Description("Number of Path Health Packets.") : amended
    ] uint32 NumberPathPackets;

    [WmiDataId(2),
     read,
     Description("Reserved for future use.") : amended
    ] uint32 Reserved;

    [WmiDataId(3),
     read,
     Description("MPIO Path Health Info Array.") : amended,
     WmiSizeIs("NumberPathPackets")
    ] MPIO_PATH_HEALTH_CLASS PathHealthPackets[];
};
```

When the class definition is compiled by the WMI tool suiteit produces the [**MPIO\_PATH\_HEALTH\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff562431) data structure. There are no methods associated with this WMI class.

 

 





