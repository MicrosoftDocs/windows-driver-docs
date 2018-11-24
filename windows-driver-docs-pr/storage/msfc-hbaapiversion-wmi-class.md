---
title: MSFC\_HbaApiVersion WMI Class
description: MSFC\_HbaApiVersion WMI Class
ms.assetid: 642b8313-d1ca-4c07-9c39-b49ef65b4438
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSFC\_HbaApiVersion WMI Class


An HBA miniport driver that supports the T11 committee's *Fibre Channel HBA API* specification uses the MSFC\_HbaApiVersion class to report the HBA API version that is currently supported.

The MSFC\_HbaApiVersion class is defined as follows in *Hbaapi.mof*:

```cpp
class MSFC_HbaApiVersion
{
    uint32 WmiHbaApiVersion;
    uint32 HbaApiVersion;
    string Description;
};
```

When this class definition is compiled by the WMI tool suite, it produces the following data structure:

[**MSFC\_HbaApiVersion**](https://msdn.microsoft.com/library/windows/hardware/ff562507)

There are no methods associated with this WMI class.

 

 





