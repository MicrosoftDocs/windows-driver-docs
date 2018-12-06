---
title: MPIO\_DEVINSTANCE\_HEALTH\_CLASS WMI Class
description: MPIO\_DEVINSTANCE\_HEALTH\_CLASS WMI Class
ms.assetid: d2c77461-d89c-4c1b-86dc-3373de0f11e4
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MPIO\_DEVINSTANCE\_HEALTH\_CLASS WMI Class


An MPIO driver uses the MPIO\_DEVINSTANCE\_HEALTH\_CLASS WMI class to report health statistics of a device through a specific path.

```cpp
class MPIO_DEVINSTANCE_HEALTH_CLASS
{
    //
    // Path identifier through which this instance is exposed.
    //
    [WmiDataId(1),
     read,
     Description("Path identifier through which this device instance is exposed.") : amended
    ] uint64 PathId;

    //
    // Number of read requests serviced by this device through this instance.
    //
    [WmiDataId(2),
     read,
     Description("Number of read requests serviced by this device through this instance.") : amended
    ] uint64 NumberReads;

    //
    // Number of write requests serviced by this device through this instance.
    //
    [WmiDataId(3),
     read,
     Description("Number of write requests serviced by this device through this instance.") : amended
    ] uint64 NumberWrites;

    //
    // Cumulative number of bytes read on this device through this instance.
    //
    [WmiDataId(4),
     read,
     Description("Cumulative number of bytes read on this device through this instance.") : amended
    ] uint64 NumberBytesRead;

    //
    // Cumulative number of bytes written to this device through this instance.
    //
    [WmiDataId(5),
     read,
     Description("Cumulative number of bytes written to this device through this instance.") : amended
    ] uint64 NumberBytesWritten;

    //
    // Number of failed requests retried on this device using this instance.
    //
    [WmiDataId(6),
     read,
     Description("Number of failed requests retried on this device using this instance.") : amended
    ] uint64 NumberRetries;

    //
    // Number of requests to this device serviced by this instance that were failed back to the application.
    //
    [WmiDataId(7),
     read,
     Description("Number of requests to this device serviced by this instance that were failed back to the application.") : amended
    ] uint64 NumberIoErrors;

    //
    // System time when this device instance was exposed to the system.
    //
    [WmiDataId(8),
     read,
     Description("System time when this device instance was exposed to the system.") : amended
    ] uint64 CreateTime;

    //
    // System time when this device instance got removed from the system.
    //
    [WmiDataId(9),
     read,
     Description("System time when this device instance got removed from the system.") : amended
    ] uint64 FailTime;

    //
    // Flag that indicates if this device instance is removed from the system.
    //
    [WmiDataId(10),
     read,
     Description("Flag that indicates if this device instance is removed from the system.") : amended
    ] boolean DeviceOffline;

    //
    // Count of the number of times that the NumberReads field wrapped.
    //
    [WmiDataId(11),
     read,
     Description("Count of the number of times that the NumberReads field wrapped.") : amended
    ] uint8 NumberReadsWrap;

    //
    // Count of the number of times that the NumberWrites field wrapped.
    //
    [WmiDataId(12),
     read,
     Description("Count of the number of times that the NumberWrites field wrapped.") : amended
    ] uint8 NumberWritesWrap;

    //
    // Count of the number of times that the NumberBytesRead field wrapped.
    //
    [WmiDataId(13),
     read,
     Description("Count of the number of times that the NumberBytesRead field wrapped.") : amended
    ] uint8 NumberBytesReadWrap;

    //
    // Count of the number of times that the NumberBytesWritten field wrapped.
    //
    [WmiDataId(14),
     read,
     Description("Count of the number of times that the NumberBytesWritten field wrapped.") : amended
    ] uint8 NumberBytesWrittenWrap;

    //
    // Pad for data alignment.
    //
    [WmiDataId(15),
     read
    ] uint8 Pad[3];
};
```

When this class definition is compiled by the WMI tool suite, it produces the [**MPIO\_DEVINSTANCE\_HEALTH\_CLASS**](https://msdn.microsoft.com/library/windows/hardware/ff562337) data structure. There are no methods associated with this WMI class.

 

 





