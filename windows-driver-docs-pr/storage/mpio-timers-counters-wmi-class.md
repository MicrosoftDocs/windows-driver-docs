---
title: MPIO\_TIMERS\_COUNTERS WMI Class
description: MPIO\_TIMERS\_COUNTERS WMI Class
ms.assetid: 386110f8-504c-4617-b8ae-557ea504d41d
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MPIO\_TIMERS\_COUNTERS WMI Class


A WMI client uses the MPIO\_TIMERS\_COUNTERS WMI class to query MPIO for all global timer values.

```cpp
class MPIO_TIMERS_COUNTERS
{

    [key, read]
     string InstanceName;
    [read] boolean Active;

    //
    // Flag indicating if automatic path verification must be performed every
    // N seconds (where N depends on the value set in PathVerificationPeriod).
    // Type is boolean and must be filled with either 0 (disbale) or 1 (enable).
    //
    [WmiDataId(1),
     read, write,
     Description("Enable/Disable Auto Path-Verification.") : amended
    ] uint32 PathVerifyEnabled;

    //
    // This timer is specified in seconds. The default is 30 seconds
    // and its max allowed is MAXULONG. It controls the periodicity
    // for path verification.
    //
    [WmiDataId(2),
     read, write,
     Description("Path Verification Timer.") : amended
    ] uint32 PathVerificationPeriod;

    //
    // This timer is specified in seconds. The default is 20 seconds
    // and its max allowed is MAXULONG. It controls the amount of time
    // that the pseudo-LUN will continue to be in memory, even after
    // loosing all its paths.
    //
    [WmiDataId(3),
     read, write,
     Description("PDO Remove Timer.") : amended
    ] uint32 PDORemovePeriod;

    //
    // The number of times a failed I/O will be retried if DsmInterpretError
    // requests a retry. The default is set to 3.
    //
    [WmiDataId(4),
     read, write,
     Description("Request Retry Count (Max 500)") : amended
    ] uint32 RetryCount;

    //
    // This value is specified in seconds. The default is 1 second. It
    // controls the interval of time after which a failed request is
    // retried (after the DSM has decided so).
    //
    [WmiDataId(5),
     read, write,
     Description("Retry Interval (seconds) (Max MAXULONG)") : amended
    ] uint32 RetryInterval;

};
```

When this class definition is compiled by the WMI tool suite, it produces the [**MPIO\_TIMERS\_COUNTERS**](https://msdn.microsoft.com/library/windows/hardware/ff562461) data structure. There are no methods associated with this WMI class.

 

 





