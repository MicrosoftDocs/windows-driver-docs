---
title: DSM\_VERSION WMI Class
description: DSM\_VERSION WMI Class
ms.assetid: 79239921-169d-496d-a52b-f4b6b0cb0c80
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

When this class definition is compiled by the WMI tool suite, it produces the [**DSM\_VERSION**](https://msdn.microsoft.com/library/windows/hardware/ff552750) data structure. There are no methods associated with this WMI class.

 

 





