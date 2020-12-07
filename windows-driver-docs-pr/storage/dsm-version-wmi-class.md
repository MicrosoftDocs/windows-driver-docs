---
title: DSM\_VERSION WMI Class
description: DSM\_VERSION WMI Class
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DSM\_VERSION WMI Class


An MPIO driver uses the DSM\_VERSION WMI class to identify the version of a configured DSM.

```cpp
class DSM_VERSION
{
    //
    // Version: Major, Minor, Product, Qfe
    //
    [WmiDataId(1)] uint32 MajorVersion;
    [WmiDataId(2)] uint32 MinorVersion;
    [WmiDataId(3)] uint32 ProductBuild;
    [WmiDataId(4)] uint32 QfeNumber;

};
```

When this class definition is compiled by the WMI tool suite, it produces the [**DSM\_VERSION**](/windows-hardware/drivers/ddi/mpiowmi/ns-mpiowmi-_dsm_version) data structure. There are no methods associated with this WMI class.

 

