---
title: PDO\_INFORMATION WMI Class
description: PDO\_INFORMATION WMI Class
ms.date: 10/17/2018
---

# PDO\_INFORMATION WMI Class


An MPIO driver uses the PDO\_INFORMATION WMI class to identify the device-to-path mapping of a physical device.

```cpp
class PDO_INFORMATION
{

    [WmiDataId(1)] PDOSCSI_ADDR ScsiAddress;

    //
    // Indicates whether this device-path is usable,
    // i.e. whether DsmIsPathActive returned TRUE for this device-path.
    //
    [WmiDataId(2)] uint32 DeviceState;

    //
    // The PathId matches the identifier returned by DsmSetDeviceInfo.
    //
    [WmiDataId(3)] uint64 PathIdentifier;

    //
    // Matches the MPIO_CONTROLLER_INFO ControllerId of the controller
    // fronting this device.
    //
    [WmiDataId(4)] uint32 IdentifierType;
    [WmiDataId(5)] uint32 IdentifierLength;
    [WmiDataId(6)] uint8 Identifier[32];
    [WmiDataId(7)] uint8 Pad[4];
};
```

When this class definition is compiled by the WMI tool suite, it produces the [**PDO\_INFORMATION**](/windows-hardware/drivers/ddi/mpiodisk/ns-mpiodisk-_pdo_information) data structure. There are no methods associated with this WMI class.

 

