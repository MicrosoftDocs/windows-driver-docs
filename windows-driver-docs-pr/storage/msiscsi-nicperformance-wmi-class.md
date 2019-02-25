---
title: MSiSCSI\_NICPerformance WMI Class
description: MSiSCSI\_NICPerformance WMI Class
ms.assetid: e5894b20-8ea7-46ec-9960-3d9891b06ac4
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSiSCSI\_NICPerformance WMI Class


## <span id="ddk_msiscsi_nicperformance_wmi_class_kr"></span><span id="DDK_MSISCSI_NICPERFORMANCE_WMI_CLASS_KR"></span>


The MSiSCSI\_NICPerformance WMI class exposes performance statistics for a network interface card (NIC) port. The miniport driver that registers this class should create one instance of the class for each port on the adapter.

The initiator should implement one instance of the MSiSCSI\_NICPerformance class for each Ethernet port on the adapter and register each instance of the class the name of the particular physical device object (PDO) for the port.

The MSiSCSI\_NICPerformance class is defined in *Iscsiprf.mof*.

```cpp
class MSiSCSI_NICPerformance : Win32_PerfRawData {
  [key] string  InstanceName;
  boolean  Active;
  [read, WmiDataId(1), PerfDefault, 
    CounterType(PERF_COUNTER_COUNTER),
    //    32bit per sec display
    DefaultScale(0), PerfDetail(100), description("Number of 
    bytes per second transmitted via Ethernet port") : 
    amended] 
    uint32  BytesTransmitted;
  [read, WmiDataId(2), PerfDefault, 
    CounterType(PERF_COUNTER_COUNTER),
    //    32bit per sec display
    DefaultScale(0), PerfDetail(100), description("Number of 
    bytes per second received via Ethernet port") : amended] 
    uint32  BytesReceived;
  [read, WmiDataId(3), PerfDefault, 
    CounterType(PERF_COUNTER_COUNTER),
    //    32bit per sec display
    DefaultScale(0), PerfDetail(100), description("Number of 
    bytes per second transmitted via Ethernet port") :
    amended] 
    uint32  PDUTransmitted;
  [read, WmiDataId(4), PerfDefault, 
    CounterType(PERF_COUNTER_COUNTER),
    //    32bit per sec display
    DefaultScale(0), PerfDetail(100), description("Number of 
    bytes per second received via Ethernet port") : amended]
    uint32  PDUReceived;
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**MSiSCSI\_NICPerformance**](https://msdn.microsoft.com/library/windows/hardware/ff563087) data structure.

 

 





