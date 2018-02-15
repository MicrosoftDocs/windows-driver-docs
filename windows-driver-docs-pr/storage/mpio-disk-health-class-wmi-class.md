---
title: MPIO\_DISK\_HEALTH\_CLASS WMI Class
description: MPIO\_DISK\_HEALTH\_CLASS WMI Class
ms.assetid: 4595f74e-586d-4411-acfd-e93e00778b67
---

# MPIO\_DISK\_HEALTH\_CLASS WMI Class


An MPIO driver uses the MPIO\_DISK\_HEALTH\_CLASS WMI class to report health statistics of an MPIO disk.

```
class MPIO_DISK_HEALTH_CLASS
{
    //
    // The MPIODisk(N).
    //
    [WmiDataId(1), MaxLen(63)] string Name;

    //
    // Number of read requests sent to this device.
    //
    [WmiDataId(2),
     read,
     Description("Number of read requests sent to this device.") : amended
    ] uint64 NumberReads;

    //
    // Number of write requests sent to this device.
    //
    [WmiDataId(3),
     read,
     Description("Number of write requests sent to this device.") : amended
    ] uint64 NumberWrites;

    //
    // Cumulative number of bytes read by requests sent to this device.
    //
    [WmiDataId(4),
     read,
     Description("Cumulative number of bytes read by requests sent to this device.") : amended
    ] uint64 NumberBytesRead;

    //
    // Cumulative number of bytes written by requests sent to this device.
    //
    [WmiDataId(5),
     read,
     Description("Cumulative number of bytes written by requests sent to this device.") : amended
    ] uint64 NumberBytesWritten;

    //
    // Number of requests sent to this device that were retried.
    //
    [WmiDataId(6),
     read,
     Description("Number of requests sent to this device that were retried.") : amended
    ] uint64 NumberRetries;

    //
    // Number of requests sent to this device that failed.
    //
    [WmiDataId(7),
     read,
     Description("Number of requests sent to this device that failed.") : amended
    ] uint64 NumberIoErrors;

    //
    // System time at which this health packet was created for this device.
    //
    [WmiDataId(8),
     read,
     Description("System time at which this health packet was created for this device.") : amended
    ] uint64 CreateTime;

    //
    // Number of path failures experienced by this device.
    //
    [WmiDataId(9),
     read,
     Description("Number of path failures experienced by this device.") : amended
    ] uint64 PathFailures;

    //
    // System time at which this device went offline/failed.
    //
    [WmiDataId(10),
     read,
     Description("System time at which this device went offline/failed.") : amended
    ] uint64 FailTime;

    //
    // Flag that indicates if the device is offline/failed.
    //
    [WmiDataId(11),
     read,
     Description("Flag that indicates if the device is offline/failed.") : amended
    ] boolean DeviceOffline;

    //
    // Count of the number of times that the NumberReads field wrapped.
    //
    [WmiDataId(12),
     read,
     Description("Count of the number of times that the NumberReads field wrapped.") : amended
    ] uint8 NumberReadsWrap;

    //
    // Count of the number of times that the NumberWrites field wrapped.
    //
    [WmiDataId(13),
     read,
     Description("Count of the number of times that the NumberWrites field wrapped.") : amended
    ] uint8 NumberWritesWrap;

    //
    // Count of the number of times that the NumberBytesRead field wrapped.
    //
    [WmiDataId(14),
     read,
     Description("Count of the number of times that the NumberBytesRead field wrapped.") : amended
    ] uint8 NumberBytesReadWrap;

    //
    // Count of the number of times that the NumberBytesWritten field wrapped.
    //
    [WmiDataId(15),
     read,
     Description("Count of the number of times that the NumberBytesWritten field wrapped.") : amended
    ] uint8 NumberBytesWrittenWrap;

    //
    // Pad for data alignment.
    //
    [WmiDataId(16),
     read
    ] uint8 Pad[3];
};
```

When the class definition is compiled by the WMI tool suite, it produces the [**MPIO\_DISK\_HEALTH\_CLASS**](https://msdn.microsoft.com/library/windows/hardware/ff562350) data structure. There are no methods associated with this WMI class.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MPIO_DISK_HEALTH_CLASS%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




