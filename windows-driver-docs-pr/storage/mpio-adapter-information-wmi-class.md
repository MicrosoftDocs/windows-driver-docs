---
title: MPIO\_ADAPTER\_INFORMATION WMI Class
description: MPIO\_ADAPTER\_INFORMATION WMI Class
ms.assetid: 748205a5-d37b-4080-b6ce-9176139cef4a
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MPIO\_ADAPTER\_INFORMATION WMI Class


An MPIO driver uses the MPIO\_ADAPTER\_INFORMATION WMI class to identify a path that is associated with an MPIO disk.

```cpp
class MPIO_ADAPTER_INFORMATION
{
    //
    // Path ID. The PDO_INFORMATION class includes
    // it&#39;s pathId. These values can be used to find
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

When this class definition is compiled by the WMI tool suite, it produces the [**MPIO\_ADAPTER\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff562313) data structure. There are no methods associated with this WMI class.

 

 





