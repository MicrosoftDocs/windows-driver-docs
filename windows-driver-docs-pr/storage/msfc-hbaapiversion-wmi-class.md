---
title: MSFC\_HbaApiVersion WMI Class
description: MSFC\_HbaApiVersion WMI Class
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

[**MSFC\_HbaApiVersion**](/previous-versions/windows/hardware/drivers/ff562507(v=vs.85))

There are no methods associated with this WMI class.

 

