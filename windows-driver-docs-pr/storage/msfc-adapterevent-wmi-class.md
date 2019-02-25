---
title: MSFC\_AdapterEvent WMI Class
description: MSFC\_AdapterEvent WMI Class
ms.assetid: 83077288-e3f6-4b21-80ed-677aad7d2979
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSFC\_AdapterEvent WMI Class


## <span id="ddk_msfc_adapterevent_wmi_class_kr"></span><span id="DDK_MSFC_ADAPTEREVENT_WMI_CLASS_KR"></span>


An HBA miniport driver that supports the T11 committee's *Fibre Channel HBA API* specification uses the MSFC\_AdapterEvent class to report the characteristics of adapter events to WMI clients that have registered to be notified of these events.

The MSFC\_AdapterEvent class is defined as follows in *Hbaapi.mof*:

```cpp
class MSFC_AdapterEvent : WMIEvent  {
  [key] string InstanceName; boolean  Active;
  [WmiDataId(1), Description("Event Type") : amended, 
    _TYPE_QUALIFIERS] uint32  EventType;
  [WmiDataId(2), Description("Adapter WWN") : amended, 
    ("HBA_WWN")] uint8  PortWWN[8];
};
```

When compiled by the WMI tool suite this class definition produces the following data structure:

[**MSFC\_AdapterEvent**](https://msdn.microsoft.com/library/windows/hardware/ff562475)

There are no methods associated with this WMI class.

 

 





