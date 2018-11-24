---
title: MPIO\_DISK\_INFO WMI Class
description: MPIO\_DISK\_INFO WMI Class
ms.assetid: 75c66c84-d815-43a5-a70d-1952bf0e8d44
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MPIO\_DISK\_INFO WMI Class


A WMI client uses the MPIO\_DISK\_INFO WMI class to query MPIO so that it gathers information regarding every MPIO disk that is configured in the system.

```cpp
class MPIO_DISK_INFO
{
    [key, read]
     string InstanceName;
    [read] boolean Active;

    //
    // The Number of multi-path disk pdos that have been
    // created.
    //
    [WmiDataId(1),
     read,
     Description("Number of Multi-Path Drives.") : amended
    ] uint32 NumberDrives;

    //
    // Variable-length array of DRIVE_INFO structures.
    // NOTE: Each entry will be ULONG aligned. App. writers
    // take note when iterating through the array.
    //
    [WmiDataId(2),
     read,
     Description("Multi-Path Drive Info Array.") : amended,
     WmiSizeIs("NumberDrives")
    ] MPIO_DRIVE_INFO DriveInfo[];
};
```

When compiled by the WMI tool suite, this class definition produces the [**MPIO\_DISK\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff562367) data structure. There are no methods associated with this WMI class.

 

 





