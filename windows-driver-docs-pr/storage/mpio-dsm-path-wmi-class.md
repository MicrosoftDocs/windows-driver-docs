---
title: MPIO\_DSM\_Path WMI Class
description: MPIO\_DSM\_Path WMI Class
ms.assetid: 4f8d7fb0-2b9a-44dc-bb87-f70285f1b47c
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MPIO\_DSM\_Path WMI Class


MPIO publishes the MPIO\_DSM\_Path\_V2 WMI class but expects the DSM to register the GUID and handle its implementation. An MPIO driver uses the MPIO\_DSM\_Path\_V2 WMI class to identify a path ID as reported by a DSM.

```cpp
class MPIO_DSM_Path
{

    //
    // Unique identifier to distinguish paths known to the DSM.
    // This is what is returned to MPIO during DsmSetDeviceInfo.
    //
    [WmiDataId(1),
     Description("DSM Path Id") : amended
    ]
    uint64 DsmPathId;

    //
    // Reserved.
    //
    [WmiDataId(2),
     Description("Reserved field") : amended
    ]
    uint64 Reserved;

    //
    // Value that determines which path the DSM picks if the load balance is
    // Weighted Paths.
    //
    [WmiDataId(3),
     Description("Weight assigned to the path") : amended
    ]
    uint32 PathWeight;

    //
    // Flag to indicate if this is a primary path.
    //
    [WmiDataId(4),
     Description("Flag set to TRUE if the path is a primary path. Else FALSE.") : amended
    ]
    uint32 PrimaryPath;
};
```

When this class definition is compiled by the WMI tool suite, it produces the [**MPIO\_DSM\_Path**](https://msdn.microsoft.com/library/windows/hardware/ff562382) data structure. There are no methods associated with this WMI class.

 

 





