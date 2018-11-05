---
title: MSFC\_TargetEvent WMI Class
description: MSFC\_TargetEvent WMI Class
ms.assetid: 251f7526-98e6-495d-a987-83257e968bb8
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSFC\_TargetEvent WMI Class


## <span id="ddk_msfc_targetevent_wmi_class_kr"></span><span id="DDK_MSFC_TARGETEVENT_WMI_CLASS_KR"></span>


A WMI provider uses the MSFC\_TargetEvent WMI class to report target events.

The MSFC\_TargetEvent class is defined as follows in *Hbaapi.mof*:

```cpp
class MSFC_TargetEvent : WmiEvent {
  [key] 
  string InstanceName;
  boolean Active;
  [WmiDataId(1), Description("Type of event") : amended,
    EVENT_TYPES_QUALIFIERS] uint32  EventType;
  [WmiDataId(2), Description("Port WWN") : amended,
     HBAType("HBA_WWN")]uint8  PortWWN[8];
  [WmiDataId(3), Description("Discovered Port WWN") : amended,
    HBAType("HBA_WWN")]uint8  DiscoveredPortWWN[8];
};
```

When compiled by the WMI tool suite this class definition produces the following data structure:

[**MSFC\_TargetEvent**](https://msdn.microsoft.com/library/windows/hardware/ff562518)

 

 





