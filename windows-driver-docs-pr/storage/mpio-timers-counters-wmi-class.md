---
title: MPIO\_TIMERS\_COUNTERS WMI Class
description: MPIO\_TIMERS\_COUNTERS WMI Class
ms.assetid: 386110f8-504c-4617-b8ae-557ea504d41d
---

# MPIO\_TIMERS\_COUNTERS WMI Class


A WMI client uses the MPIO\_TIMERS\_COUNTERS WMI class to query MPIO for all global timer values.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MPIO_TIMERS_COUNTERS%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




