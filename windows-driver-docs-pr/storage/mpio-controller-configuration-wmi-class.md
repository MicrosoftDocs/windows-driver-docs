---
title: MPIO\_CONTROLLER\_CONFIGURATION WMI Class
description: MPIO\_CONTROLLER\_CONFIGURATION WMI Class
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MPIO\_CONTROLLER\_CONFIGURATION WMI Class


A WMI client uses the MPIO\_CONTROLLER\_CONFIGURATION WMI class to query MPIO for information regarding the storage controllers that are attached to a system.

```cpp
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
    // Array of each controller's information.
    // Note that these are ULONGLONG aligned.
    //
    [WmiDataId(2),
     read,
     Description("Array of Controller Information Structures.") : amended,
     WmiSizeIs("NumberControllers")
    ] MPIO_CONTROLLER_INFO ControllerInfo[];

};
```

When this class definition is compiled by the WMI tool suite, it produces the [**MPIO\_CONTROLLER\_CONFIGURATION**](/windows-hardware/drivers/ddi/mpiowmi/ns-mpiowmi-_mpio_controller_configuration) data structure. There are no methods associated with this WMI class.

 

