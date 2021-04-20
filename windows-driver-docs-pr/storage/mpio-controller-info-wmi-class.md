---
title: MPIO\_CONTROLLER\_INFO WMI Class
description: MPIO\_CONTROLLER\_INFO WMI Class
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MPIO\_CONTROLLER\_INFO WMI Class


An MPIO driver uses the MPIO\_CONTROLLER\_INFO WMI class to identify a storage controller and its associated DSM.

```cpp
class MPIO_CONTROLLER_INFO
{

    //
    // Devices behind this controller will have a matching
    // ControllerId in the PDO_INFORMATION class.
    //
    [WmiDataId(1)] uint32 IdentifierType;
    [WmiDataId(2)] uint32 IdentifierLength;
    [WmiDataId(3)] uint8 Identifier[32];
    [WmiDataId(4)] uint32 ControllerState;
    [WmiDataId(5)] uint32 Pad;
    [WmiDataId(6), MaxLen(63)] string AssociatedDsm;
};
```

When this class definition is compiled by the WMI tool suite, it produces the [**MPIO\_CONTROLLER\_INFO**](/windows-hardware/drivers/ddi/mpiowmi/ns-mpiowmi-_mpio_controller_info) data structure. There are no methods associated with this WMI class.

 

