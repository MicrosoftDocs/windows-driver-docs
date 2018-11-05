---
title: MSFC\_LinkEvent WMI Class
description: MSFC\_LinkEvent WMI Class
ms.assetid: 9507fb1a-ce2a-4ce9-8272-77c8c9d0a92c
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSFC\_LinkEvent WMI Class


## <span id="ddk_msfc_linkevent_wmi_class_kr"></span><span id="DDK_MSFC_LINKEVENT_WMI_CLASS_KR"></span>


A WMI provider uses the MSFC\_LinkEvent WMI class to report link events.

The MSFC\_LinkEvent class is defined as follows in *Hbaapi.mof*:

```cpp
class MSFC_LinkEvent : WMIEvent {
  [key] 
  string InstanceName;
  boolean Active;
  [WmiDataId(1), Description("Type of event") : amended,
    EVENT_TYPES_QUALIFIERS] uint32  EventType;
  [WmiDataId(2), Description("Discovered Port WWN") : amended,    HBAType("HBA_WWN")]uint8  AdapterWWN[8];
  [WmiDataId(3), Description("Size of RLIR buffer") : amended]
    uint32 RLIRBufferSize;
  [WmiDataId(4), Description("Size of RLIR buffer") : amended,
     WmiSizeIs("RLIRBufferSize")]uint8 RLIRBuffer[];
};
```

When compiled by the WMI tool suite this class definition produces the following data structure:

[**MSFC\_LinkEvent**](https://msdn.microsoft.com/library/windows/hardware/ff562514)

There are no methods associated with this WMI class.

 

 





