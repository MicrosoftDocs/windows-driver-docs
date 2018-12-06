---
title: MPIO\_PATH\_INFORMATION WMI Class
description: MPIO\_PATH\_INFORMATION WMI Class
ms.assetid: fd6311c5-2d98-4a3a-beb9-54f3a84be8eb
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MPIO\_PATH\_INFORMATION WMI Class


A WMI client uses the MPIO\_PATH\_INFORMATION WMI class to query the MPIO driver for information regarding all paths that are associated with an MPIO disk.

```cpp
class MPIO_PATH_INFORMATION
{

    [key, read]
     string InstanceName;
    [read] boolean Active;

    //
    // Number of paths to the device.
    //
    [WmiDataId(1),
     read,
     Description("Number of Paths in use") : amended
    ] uint32 NumberPaths;

    //
    // Pad for data alignment.
    //
    [WmiDataId(2),
     read,
     Description("Pad for ULONGLONG Alignment.") : amended
    ] uint32 Pad;

    //
    // Array containing each path&#39;s information.
    // Note that each of these are ULONGLONG aligned.
    //
    [WmiDataId(3),
     read,
     Description("Array of Adapter/Path Information.") : amended,
     WmiSizeIs("NumberPaths")
    ] MPIO_ADAPTER_INFORMATION PathList[];

};
```

When this class definition is compiled by the WMI tool suite, it produces the [**MPIO\_PATH\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff562441) data structure. There are no methods associated with this WMI class.

 

 





