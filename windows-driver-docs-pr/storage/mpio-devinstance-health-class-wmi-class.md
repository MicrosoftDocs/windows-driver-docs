---
title: MPIO\_DEVINSTANCE\_HEALTH\_CLASS WMI Class
description: MPIO\_DEVINSTANCE\_HEALTH\_CLASS WMI Class
ms.assetid: d2c77461-d89c-4c1b-86dc-3373de0f11e4
---

# MPIO\_DEVINSTANCE\_HEALTH\_CLASS WMI Class


An MPIO driver uses the MPIO\_DEVINSTANCE\_HEALTH\_CLASS WMI class to report health statistics of a device through a specific path.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MPIO_DEVINSTANCE_HEALTH_CLASS%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




