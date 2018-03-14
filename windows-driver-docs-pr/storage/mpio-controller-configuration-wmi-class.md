---
title: MPIO\_CONTROLLER\_CONFIGURATION WMI Class
description: MPIO\_CONTROLLER\_CONFIGURATION WMI Class
ms.assetid: c11429d6-b016-464e-a7b4-03b6cdc8ddb7
---

# MPIO\_CONTROLLER\_CONFIGURATION WMI Class


A WMI client uses the MPIO\_CONTROLLER\_CONFIGURATION WMI class to query MPIO for information regarding the storage controllers that are attached to a system.

```
class MPIO_CONTROLLER_CONFIGURATION
{

    [key, read]
     string InstanceName;
    [read] boolean Active;

    //
    // Number of controllers in the array.
    //
    [WmiDataId(1),
     read,
     Description("Number of Controllers.") : amended
    ] uint32 NumberControllers;

    //
    // Array of each controller&#39;s information.
    // Note that these are ULONGLONG aligned.
    //
    [WmiDataId(2),
     read,
     Description("Array of Controller Information Structures.") : amended,
     WmiSizeIs("NumberControllers")
    ] MPIO_CONTROLLER_INFO ControllerInfo[];

};
```

When this class definition is compiled by the WMI tool suite, it produces the [**MPIO\_CONTROLLER\_CONFIGURATION**](https://msdn.microsoft.com/library/windows/hardware/ff562321) data structure. There are no methods associated with this WMI class.

 

 





