---
title: MPIO\_PATH\_HEALTH\_CLASS WMI Class
description: MPIO\_PATH\_HEALTH\_CLASS WMI Class
ms.assetid: fcbc86a4-9035-489e-a406-9901c5af0a32
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MPIO\_PATH\_HEALTH\_CLASS WMI Class


A WMI client uses the MPIO\_PATH\_HEALTH\_CLASS WMI class to query the MPIO subsystem so that it gathers health statistics for a particular path that is associated with an MPIO disk.

```cpp
class MPIO_PATH_HEALTH_CLASS
{
    //
    // Identifier representing the path.
    //
    [WmiDataId(1),     read,     Description("Path identifier.") : amended    ] uint64 PathId;

    //
    // Number of read requests serviced by this path.
    //
    [WmiDataId(2),     read,     Description("Number of read requests serviced by this path.") : amended
    ] uint64 NumberReads;

    //
    // Number of writes serviced by this path.
    //
    [WmiDataId(3),
     read,
     Description("Number of writes serviced by this path.") : amended
    ] uint64 NumberWrites;

    //
    // Cumulative number of bytes read by requests serviced by this path.
    //
    [WmiDataId(4),
     read,
     Description("Cumulative number of bytes read by requests serviced by this path.") : amended
    ] uint64 NumberBytesRead;

    //
    // Cumulative number of bytes written by requests serviced by this path.
    //
    [WmiDataId(5),
     read,
     Description("Cumulative number of bytes written by requests serviced by this path.") : amended
    ] uint64 NumberBytesWritten;

    //
    // Number of requests retried using this path.
    //
    [WmiDataId(6),
     read,
     Description("Number of requests retried using this path.") : amended
    ] uint64 NumberRetries;

    //
    // Number of requests serviced by this path that failed.
    //
    [WmiDataId(7),
     read,
     Description("Number of requests serviced by this path that failed.") : amended
    ] uint64 NumberIoErrors;

    //
    // System time at which this health packet was created for this path.
    //
    [WmiDataId(8),
     read,
     Description("System time at which this health packet was created for this path.") : amended
    ] uint64 CreateTime;

    //
    // System time at which this path went offline/failed.
    //
    [WmiDataId(9),
     read,
     Description("System time at which this path went offline/failed.") : amended
    ] uint64 FailTime;

    //
    // Flag that indicates if the path is offline/failed.
    //
    [WmiDataId(10),
     read,
     Description("Flag that indicates if the path is offline/failed") : amended
    ] boolean PathOffline;

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
    // Number of requests sent down this path that are in flight.
    //
    [WmiDataId(15),
     read,
     Description("Number of requests sent down this path that are currently in flight.") : amended
    ] uint8 OutstandingRequests;

    //
    // Pad for data alignment.
    //
    [WmiDataId(16),
     read
    ] uint8 Pad[2];
};
```

When compiled by the WMI tool suite, this class definition produces the [**MPIO\_PATH\_HEALTH\_CLASS**](https://msdn.microsoft.com/library/windows/hardware/ff562424) data structure. There are no methods associated with this WMI class.

 

 





