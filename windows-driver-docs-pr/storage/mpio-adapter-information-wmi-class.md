---
title: MPIO_ADAPTER_INFORMATION WMI Class
description: MPIO\_ADAPTER\_INFORMATION WMI Class
ms.date: 10/17/2018
---

# MPIO\_ADAPTER\_INFORMATION WMI Class


An MPIO driver uses the MPIO\_ADAPTER\_INFORMATION WMI class to identify a path that is associated with an MPIO disk.

```cpp
class MPIO_ADAPTER_INFORMATION
{
    //
    // Path ID. The PDO_INFORMATION class includes
    // it's pathId. These values can be used to find
    // which devices are on which path.
    //
    [WmiDataId(1)] uint64 PathId;

    //
    // Adapter Location.
    //
    [WmiDataId(2)] uint8 BusNumber;
    [WmiDataId(3)] uint8 DeviceNumber;
    [WmiDataId(4)] uint8 FunctionNumber;
    [WmiDataId(5)] uint8 Pad;

    //
    // Adapter Name.
    //
    [WmiDataId(6), MaxLen(63)] string AdapterName;
};
```

When this class definition is compiled by the WMI tool suite, it produces the [**MPIO\_ADAPTER\_INFORMATION**](/windows-hardware/drivers/ddi/mpiowmi/ns-mpiowmi-_mpio_adapter_information) data structure. There are no methods associated with this WMI class.

 

