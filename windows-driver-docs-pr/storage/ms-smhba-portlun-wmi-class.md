---
title: MS\_SMHBA\_PORTLUN WMI Class
description: MS\_SMHBA\_PORTLUN WMI Class
ms.assetid: 28473b3b-2b88-4abc-81b5-9a6a7f8166e3
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MS\_SMHBA\_PORTLUN WMI Class


An HBA miniport driver that supports the Storage Management API uses the MS\_SMHBA\_PORTLUN class to expose the mapping between the target LUN and SAS adapter.

The MS\_SMHBA\_PORTLUN class is defined as follows in *Hbaapi.mof*:

```cpp
class MS_SMHBA_PORTLUN 
{
    [HBAType("HBA_WWN"), WmiDataId(1)]
    uint8   PortWWN[8];

    [HBAType("HBA_WWN"), WmiDataId(2)]
    uint8   domainPortWWN[8];

    [HBAType("HBA_SCSILUN"), WmiDataId(3)]
    uint64  TargetLun;
};
```

When this class definition is compiled by the WMI tool suite, it produces the following data structure:

[**MS\_SMHBA\_PORTLUN**](https://msdn.microsoft.com/library/windows/hardware/ff563169)

There are no methods associated with this WMI class.

 

 





