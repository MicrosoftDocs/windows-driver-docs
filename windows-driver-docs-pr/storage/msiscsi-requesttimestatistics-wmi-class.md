---
title: MSiSCSI\_RequestTimeStatistics WMI Class
description: MSiSCSI\_RequestTimeStatistics WMI Class
ms.assetid: 3e9f3214-3120-41f6-bb06-7ace4f243c5f
---

# MSiSCSI\_RequestTimeStatistics WMI Class


The MSiSCSI\_RequestTimeStatistics WMI class provides statistics about iSCSI requests. This class is defined as follows in *Mgmt.mof.*

```
class MSiSCSI_RequestTimeStatistics : Win32_PerfRawData
{
    [read,key] String InstanceName;
    [read] boolean Active;


    [read,
     WmiDataId(1),
     WmiVersion(1),
     description("Name of the iSCSI Target"),
     MaxLen(MAX_ISCSI_NAME_LEN)] string iSCSIName;

    [read,
     WmiDataId(2),
     WmiVersion(1),
     Description("The iSCSI connection ID for this connection instance."): amended
    ] uint16 CID; //session wide namespace

    [read,
     WmiDataId(3),
     Description("A uniquely generated session ID used only internally.  This is the value returned by the LoginToTarget method."): amended,
     WmiVersion(1)] uint64 USID;

    [WmiDataId(4),
     DisplayName("Adapter Id") : amended,
     DisplayInHex,
     description("Id that is globally unique to each instance of each adapter. This is the value reported by the MSiSCSI_HBAInformation class.") : amended
    ]
    uint64 UniqueAdapterId;

    [WmiDataId(5),
    DisplayName("Max Request Processing Time"): amended,
    PerfDefault,
    CounterType(PERF_COUNTER_BULK_COUNT),
    DefaultScale(0),
    PerfDetail(100),
    read,
    Description("Maximum time taken to process a request over this connection"): amended
    ] uint32 MaximumProcessingTime;

    [WmiDataId(6),
    DisplayName("Average Request Processing Time"): amended,
    PerfDefault,
    CounterType(PERF_COUNTER_BULK_COUNT),
    DefaultScale(0),
    PerfDetail(100),
    read,
    Description("Average time taken to process a request over this connection"): amended
    ] uint32 AverageProcessingTime;
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**MSiSCSI\_RequestTimeStatistics**](https://msdn.microsoft.com/library/windows/hardware/ff563123) data structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSiSCSI_RequestTimeStatistics%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




