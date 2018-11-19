---
title: MSFC\_TM WMI Class
description: MSFC\_TM WMI Class
ms.assetid: c81b9b2a-6381-4ff9-a579-bee53ac8678d
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSFC\_TM WMI Class


## <span id="ddk_msfc_tm_wmi_class_kr"></span><span id="DDK_MSFC_TM_WMI_CLASS_KR"></span>


A WMI provider uses the MSFC\_TM WMI class to time stamp events.

The MSFC\_TM class is defined as follows in *Hbaapi.mof*:

```cpp
class MSFC_TM {
  [WmiDataId(1)] uint32  tm_sec;
  [WmiDataId(2)] uint32  tm_min;
  [WmiDataId(3)] uint32  tm_hour;
  [WmiDataId(4)] uint32  tm_mday;
  [WmiDataId(5)] uint32  tm_mon;
  [WmiDataId(6)] uint32  tm_year;
  [WmiDataId(7)] uint32  tm_wday;
  [WmiDataId(8)] uint32  tm_yday;
  [WmiDataId(9)] uint32  tm_isdst;
};
```

When compiled by the WMI tool suite this class definition produces the following data structure:

[**MSFC\_TM**](https://msdn.microsoft.com/library/windows/hardware/ff562520)

 

 





