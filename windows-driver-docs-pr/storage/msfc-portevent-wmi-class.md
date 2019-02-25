---
title: MSFC\_PortEvent WMI Class
description: MSFC\_PortEvent WMI Class
ms.assetid: 38b8e358-b118-4a0c-ac47-2f257d0ed1bf
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSFC\_PortEvent WMI Class


## <span id="ddk_msfc_portevent_wmi_class_kr"></span><span id="DDK_MSFC_PORTEVENT_WMI_CLASS_KR"></span>


A WMI provider uses the MSFC\_PortEvent WMI class to report port events.

The MSFC\_PortEvent class is defined as follows in *Hbaapi.mof*:

```cpp
class MSFC_PortEvent : WMIEvent {
  [key] 
  string InstanceName;
  boolean Active;
  [WmiDataId(1), Description("Type of event") : amended,
    EVENT_TYPES_QUALIFIERS] uint32  EventType;
  [WmiDataId(2), Description("Fabric port id") : amended]
    uint32 FabricPortId;
  [WmiDataId(3), Description("Port WWN") : amended,
    HBAType("HBA_WWN")] uint8  PortWWN[8];
};
```

When compiled by the WMI tool suite this class definition produces the following data structure:

[**MSFC\_PortEvent**](https://msdn.microsoft.com/library/windows/hardware/ff562516)

 

 





