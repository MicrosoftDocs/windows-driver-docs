---
title: PDO\_INFORMATION WMI Class
description: PDO\_INFORMATION WMI Class
ms.assetid: 1a972905-42ea-4cb2-b937-5ed0f287d80a
---

# PDO\_INFORMATION WMI Class


An MPIO driver uses the PDO\_INFORMATION WMI class to identify the device-to-path mapping of a physical device.

```
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

When this class definition is compiled by the WMI tool suite, it produces the [**PDO\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff563828) data structure. There are no methods associated with this WMI class.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20PDO_INFORMATION%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




