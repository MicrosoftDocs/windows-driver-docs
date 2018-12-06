---
title: DSM\_QueryUniqueId WMI Class
description: DSM\_QueryUniqueId WMI Class
ms.assetid: 576e208d-972c-47ba-ab30-a05bf3d0943d
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DSM\_QueryUniqueId WMI Class


MPIO publishes the DSM\_QueryUniqueId WMI class but expects the DSM to register the GUID and handle its implementation. A WMI client uses the DSM\_QueryUniqueId WMI class to query the unique identifier for a path.

```cpp
class DSM_QueryUniqueId
{

    [key, read]
    string InstanceName;

    [read]
    boolean Active;

    //
    // This Identifier needs to be set by DSMs that want management applications
    // like VDS to be able to manage the devices controlled by the particular DSM.
    // This DsmUniqueId will be used in conjuction with the DsmPathId to construct
    // a path identitifer that is unique not just among all paths known to this DSM,
    // but also among all the DSMs present on the system.
    //
    [WmiDataId(1),
     DisplayName("DSM Unique Identifier") : amended,
     Description("DSM Unique Identifier to be used by a management application") : amended
    ]
    uint64 DsmUniqueId;
};
```

When this class definition is compiled by the WMI tool suite, it produces the [**DSM\_QueryUniqueId**](https://msdn.microsoft.com/library/windows/hardware/ff552742) data structure. There are no methods associated with this WMI class.

 

 





