---
title: MPIO_GET_DESCRIPTOR WMI Class
description: MPIO\_GET\_DESCRIPTOR WMI Class
ms.date: 10/17/2018
---

# MPIO\_GET\_DESCRIPTOR WMI Class


A WMI client uses the MPIO\_GET\_DESCRIPTOR WMI class to query MPIO for the device-path pairing of an MPIO disk.

```cpp
class MPIO_GET_DESCRIPTOR
{
    [key, read]
     string InstanceName;
    [read] boolean Active;

    //
    // Number of instances of this device via different paths.
    //
    [WmiDataId(1),
     read,
     Description("Number of Port Objects backing the device.") : amended
    ] uint32 NumberPdos;

    //
    // Device Name (i.e. MPIODiskN)
    //
    [WmiDataId(2),
     read,
     MaxLen(63),
     Description("Name of Device.") : amended
    ] string DeviceName;

    //
    // Array of device-path pair that form the instances of this device.
    //
    [WmiDataId(3),
     read,
     Description("Array of Information classes describing the real device.") : amended,
     WmiSizeIs("NumberPdos")
    ] PDO_INFORMATION PdoInformation[];
};
```

When this class definition is compiled by the WMI tool suite, it produces the [**MPIO\_GET\_DESCRIPTOR**](/windows-hardware/drivers/ddi/mpiodisk/ns-mpiodisk-_mpio_get_descriptor) data structure. There are no methods associated with this WMI class.

 

