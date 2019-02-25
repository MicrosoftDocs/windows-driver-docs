---
title: MSFC\_EventBuffer WMI Class
description: MSFC\_EventBuffer WMI Class
ms.assetid: ce16e42c-5d0b-47e9-9baa-53dcec482940
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSFC\_EventBuffer WMI Class


## <span id="ddk_msfc_eventbuffer_wmi_class_kr"></span><span id="DDK_MSFC_EVENTBUFFER_WMI_CLASS_KR"></span>


An HBA miniport driver that supports the T11 committee's *Fibre Channel HBA API* specification uses the MSFC\_EventBuffer class to report adapter event data to WMI clients that have registered to be notified of these events.

The MSFC\_EventBuffer class is defined as follows in *Hbaapi.mof*:

```cpp
class MSFC_EventBuffer { 
  [WmiDataId(1)] uint32  EventType;
  [WmiDataId(2)] uint32  EventInfo[4];
};
```

When compiled by the WMI tool suite this class definition produces the following data structure:

[**MSFC\_EventBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff562480)

There are no methods associated with this WMI class.

 

 





