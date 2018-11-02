---
title: DSM\_PARAMETERS WMI Class
description: DSM\_PARAMETERS WMI Class
ms.assetid: c946f8cb-327c-4d5a-a133-0051a405fcad
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DSM\_PARAMETERS WMI Class


An MPIO driver users the DSM\_PARAMETERS WMI class to identify a DSM and all its associated timer values.

```cpp
class DSM_PARAMETERS
{
    //
    // Friendly name of the registered DSM.
    //
    [WmiDataId(1), MaxLen(63)] string DsmName;

    //
    // DSM-unique handle.
    //
    [WmiDataId(2)] uint64 DsmContext;

    //
    // Version Info
    //
    [WmiDataId(3)] DSM_VERSION DsmVersion;

    //
    // Counters Info
    //
    [WmiDataId(4)] DSM_COUNTERS DsmCounters;
};
```

When this class definition is compiled by the WMI tool suite, it produces the [**DSM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff552713) data structure. There are no methods associated with this WMI class.

 

 





