---
title: MPIO\_PATH\_INFORMATION WMI Class
description: MPIO\_PATH\_INFORMATION WMI Class
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
    // Array containing each path's information.
    // Note that each of these are ULONGLONG aligned.
    //
    [WmiDataId(3),
     read,
     Description("Array of Adapter/Path Information.") : amended,
     WmiSizeIs("NumberPaths")
    ] MPIO_ADAPTER_INFORMATION PathList[];

};
```

When this class definition is compiled by the WMI tool suite, it produces the [**MPIO\_PATH\_INFORMATION**](/windows-hardware/drivers/ddi/mpiowmi/ns-mpiowmi-_mpio_path_information) data structure. There are no methods associated with this WMI class.

 

