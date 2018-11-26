---
title: HID Transports Supported in Windows
description: Windows supports the following transports.
ms.assetid: 03B66788-A930-4C18-A019-CA906634DC4C
ms.date: 04/20/2017
ms.localizationpriority: medium
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
-   Gameenum.sys – The gameport bus driver. The game port bus driver creates a PDO for each game port device that is daisy-chained to a game port.

They are now considered legacy as the hardware is not found on modern machines (replaced by USB and other modern transports).

## Recommended transports for keyboards, mice, and touchpads


The following table shows the recommended transports for keyboards, mice, and touchpad devices on portable (such as laptops and slates) and non-portable systems (such as all-in-one and desktops).

| System Type                  | Portable                                 | Non-portable                                |
|------------------------------|------------------------------------------|---------------------------------------------|
| Legacy systems               | Internal: PS/2, External: USB, Bluetooth | Internal: N/A, External: USB, Bluetooth     |
| System on Chip (SoC) systems | Internal: I2C, External: USB, Bluetooth  | Internal: I2C, USB External: USB, Bluetooth |

 

[**USB Generic HID Test**](https://msdn.microsoft.com/library/windows/hardware/dn942240) in the Windows Hardware Lab Kit (HLK) covers HidUsb and HidClass drivers. There is no HLK test for third-party HID mini drivers. 
 




