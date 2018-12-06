---
title: MSiSCSI\_InitiatorInstanceStatistics WMI Class
description: MSiSCSI\_InitiatorInstanceStatistics WMI Class
ms.assetid: 5cb20302-e3f9-40fe-b501-7c23d284c120
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSiSCSI\_InitiatorInstanceStatistics WMI Class


## <span id="ddk_msiscsi_initiatorinstancestatistics_wmi_class_kr"></span><span id="DDK_MSISCSI_INITIATORINSTANCESTATISTICS_WMI_CLASS_KR"></span>


The MSiSCSI\_InitiatorInstanceStatistics WMI class exposes initiator statistics.

Because this class is associated with a particular instance of a storage miniport driver, the miniport driver must register the class using the name of the particular physical device object (PDO) that the miniport driver manages.

The MSiSCSI\_InitiatorInstanceStatistics class is defined in *Iscsiprf.mof*.

```cpp
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

 

 





