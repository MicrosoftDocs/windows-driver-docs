---
title: MPIO\_PATH\_HEALTH\_INFO WMI Class
description: MPIO\_PATH\_HEALTH\_INFO WMI Class
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

When the class definition is compiled by the WMI tool suiteit produces the [**MPIO\_PATH\_HEALTH\_INFO**](/windows-hardware/drivers/ddi/mpiowmi/ns-mpiowmi-_mpio_path_health_info) data structure. There are no methods associated with this WMI class.

 

