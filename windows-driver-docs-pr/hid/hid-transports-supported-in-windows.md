---
title: HID Transports Supported in Windows
author: windows-driver-content
description: Windows supports the following transports.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 03B66788-A930-4C18-A019-CA906634DC4C
---

# HID Transports Supported in Windows


Windows supports the following transports.

| Transport    | Windows 7 | Windows 8 | Notes                                                                                                 |
|--------------|-----------|-----------|-------------------------------------------------------------------------------------------------------|
| USB          | Yes       | Yes       | Support for USB HID 1.11+ is provided on Windows operating systems dating back to Windows 2000.       |
| Bluetooth    | Yes       | Yes       | Support for Bluetooth HID 1.1+ is provided on Windows operating systems dating back to Windows Vista. |
| Bluetooth LE | No        | Yes       | Windows 8 introduces support for HID over Bluetooth LE.                                               |
| I2C          | No        | Yes       | Windows 8 introduces support for HID over I2C                                                         |

 

Previous versions of Windows (prior to Windows 7) also included support for the following.

-   HidGame.sys - HID minidriver for game port (I/O port 201) devices. The HID class driver creates a functional device object (FDO) for a game port device, and creates a physical device object (PDO) for each HID collection that the game port device supports.
-   • Gameenum.sys – The gameport bus driver. The game port bus driver creates a PDO for each game port device that is daisy-chained to a game port.

They are now considered legacy as the hardware is not found on modern machines (replaced by USB and other modern transports).

## Recommended transports for keyboards, mice, and touchpads


The following table shows the recommended transports for keyboards, mice, and touchpad devices on portable (such as laptops and slates) and non-portable systems (such as all-in-one and desktops).

| System Type                  | Portable                                 | Non-portable                                |
|------------------------------|------------------------------------------|---------------------------------------------|
| Legacy systems               | Internal: PS/2, External: USB, Bluetooth | Internal: N/A, External: USB, Bluetooth     |
| System on Chip (SoC) systems | Internal: I2C, External: USB, Bluetooth  | Internal: I2C, USB External: USB, Bluetooth |

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20HID%20Transports%20Supported%20in%20Windows%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


