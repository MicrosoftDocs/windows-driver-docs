---
title: MPIO\_DEVINSTANCE\_HEALTH\_INFO WMI Class
description: MPIO\_DEVINSTANCE\_HEALTH\_INFO WMI Class
ms.date: 10/17/2018
---

# MPIO\_DEVINSTANCE\_HEALTH\_INFO WMI Class


An MPIO driver uses the MPIO\_DEVINSTANCE\_HEALTH\_INFO WMI class to report health statistics of an MPIO disk by using underlying different paths.

```cpp
class MPIO_DEVINSTANCE_HEALTH_INFO
{
    [key, read]
     string InstanceName;
    [read] boolean Active;

    [WmiDataId(1),
     read,
     Description("Number of Health Packets.") : amended
    ] uint32 NumberDevInstancePackets;

    [WmiDataId(2),
     read,
     Description("Reserved for future use.") : amended
    ] uint32 Reserved;

    [WmiDataId(3),
     read,
     Description("Multi-Path Health Info Array.") : amended,
     WmiSizeIs("NumberDevInstancePackets")
    ] MPIO_DEVINSTANCE_HEALTH_CLASS DevInstanceHealthPackets[];
};
```

When this class definition is compiled by the WMI tool suite, it produces the [**MPIO\_DEVINSTANCE\_HEALTH\_INFO**](/windows-hardware/drivers/ddi/mpiodisk/ns-mpiodisk-_mpio_devinstance_health_info) data structure. There are no methods associated with this WMI class.

 

