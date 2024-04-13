---
title: MPIO_REGISTERED_DSM WMI Class
description: MPIO\_REGISTERED\_DSM WMI Class
ms.date: 10/17/2018
---

# MPIO\_REGISTERED\_DSM WMI Class


A WMI client uses the MPIO\_REGISTERED\_DSM WMI class to query all the DSMs that are configured in a system.

```cpp
class MPIO_REGISTERED_DSM
{
    [key, read]
     string InstanceName;
    [read] boolean Active;

    //
    // The Number of DSMs that have registered with MPIO.
    //
    [WmiDataId(1),
     read,
     Description("Number of registered DSMs.") : amended
    ] uint32 NumberDSMs;

    //
    // Variable-length array of DSM_PARAMETERS structures.
    // NOTE: Each entry will be ULONG aligned. App. writers
    // take note when iterating through the array.
    //
    [WmiDataId(2),
     read,
     Description("Counters information of registered DSMs.") : amended,
     WmiSizeIs("NumberDSMs")
    ] DSM_PARAMETERS DsmParameters[];
};
```

When this class definition is compiled by the WMI tool suite, it produces the [**MPIO\_REGISTERED\_DSM**](/windows-hardware/drivers/ddi/mpiowmi/ns-mpiowmi-_mpio_registered_dsm) data structure. There are no methods associated with this WMI class.

 

