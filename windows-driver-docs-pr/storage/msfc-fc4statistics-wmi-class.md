---
title: MSFC\_FC4STATISTICS WMI Class
description: MSFC\_FC4STATISTICS WMI Class
ms.assetid: 49cd4104-1fe8-46ec-9216-c5c078666c02
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSFC\_FC4STATISTICS WMI Class


## <span id="ddk_msfc_fc4statistics_wmi_class_kr"></span><span id="DDK_MSFC_FC4STATISTICS_WMI_CLASS_KR"></span>


An HBA miniport driver that supports the T11 committee's *Fibre Channel HBA API* specification uses the MSFC\_FC4STATISTICS WMI class to report traffic statistics on a port of type Nx\_Port for the indicated FC-4 protocol in response to a call to the [**GetFC4Statistics**](getfc4statistics.md) WMI method.

The MSFC\_FC4STATISTICS class is defined as follows in *Hbaapi.mof*:

```cpp
class MSFC_FC4STATISTICS {
  [WmiDataId(1)] uint64  InputRequests;
  [WmiDataId(2)] uint64  OutputRequests;
  [WmiDataId(3)] uint64  ControlRequests;
  [WmiDataId(4)] uint64  InputMegabytes;
  [WmiDataId(5)] uint64  OutputMegabytes;
};
```

When compiled by the WMI tool suite this class definition produces the following data structure:

[**MSFC\_FC4STATISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff562492)

There are no methods associated with this WMI class.

 

 





