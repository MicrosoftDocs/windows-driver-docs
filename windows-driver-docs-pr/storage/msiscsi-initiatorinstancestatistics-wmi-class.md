---
title: MSiSCSI\_InitiatorInstanceStatistics WMI Class
description: MSiSCSI\_InitiatorInstanceStatistics WMI Class
ms.assetid: 5cb20302-e3f9-40fe-b501-7c23d284c120
---

# MSiSCSI\_InitiatorInstanceStatistics WMI Class


## <span id="ddk_msiscsi_initiatorinstancestatistics_wmi_class_kr"></span><span id="DDK_MSISCSI_INITIATORINSTANCESTATISTICS_WMI_CLASS_KR"></span>


The MSiSCSI\_InitiatorInstanceStatistics WMI class exposes initiator statistics.

Because this class is associated with a particular instance of a storage miniport driver, the miniport driver must register the class using the name of the particular physical device object (PDO) that the miniport driver manages.

The MSiSCSI\_InitiatorInstanceStatistics class is defined in *Iscsiprf.mof*.

```
class MSiSCSI_InitiatorInstanceStatistics : Win32_PerfRawData {
  [read,key] String InstanceName;
  [read] boolean Active;
  [WmiDataId(1),
    DisplayName("Adapter Id") : amended, DisplayInHex,
    description("Id that is globally unique to each instance 
    of each adapter. Using the address of the Adapter 
    Extension is a good idea.") : amended]
    uint64  UniqueAdapterId;
  [WmiDataId(2), DisplayName("Session Digest Errors"): 
    amended, PerfDefault, CounterType(0x00010000),
    // PERF_COUNTER_RAWCOUNT
    DefaultScale(0), PerfDetail(100), read,
    Description("Count of Session digest errors"): amended]
    uint32  SessionDigestErrorCount;
  [WmiDataId(3), DisplayName("Session Cxn Timeout Errors"): 
    amended, PerfDefault, CounterType(0x00010000),
    // PERF_COUNTER_RAWCOUNT
    DefaultScale(0), PerfDetail(100), read,
    Description("Count of Session connection timeout
    error"): amended] 
    uint32  SessionConnectionTimeoutErrorCount;
  [WmiDataId(4), DisplayName("Session Format Errors"): 
    amended, PerfDefault, CounterType(0x00010000),
    // PERF_COUNTER_RAWCOUNT
    DefaultScale(0), PerfDetail(100), read,
    Description("Count of Session format error"): amended]
    uint32  SessionFormatErrorCount;
  [WmiDataId(5),
    DisplayName("Sessions Failed"): amended, PerfDefault,
    CounterType(0x00010000),
    // PERF_COUNTER_RAWCOUNT
    DefaultScale(0), PerfDetail(100), read,
    Description("Number of Sessions failed belonging to this 
    instance"): amended] 
    uint32  SessionFailureCount;
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**MSiSCSI\_InitiatorInstanceStatistics**](https://msdn.microsoft.com/library/windows/hardware/ff563035) data structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSiSCSI_InitiatorInstanceStatistics%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




