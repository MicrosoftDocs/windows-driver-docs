---
title: HID over I2C
description: For Windows 8, Microsoft created a new HID miniport driver that allows devices to communicate over an Inter-Integrated Circuit (I²C) bus.
ms.assetid: E8A056C0-B10F-48E2-B8E3-67B00AAC87D8
keywords:
- HID miniport driver
- Inter-Integrated Circuit
- I2C bus
- HIDI2C.sys
- Simple Peripheral Bus
- SPB
- GPIO
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# HID over I2C


For Windows 8, Microsoft created a new HID miniport driver that allows devices to communicate over an Inter-Integrated Circuit (I²C) bus.

The new HID miniport solution extends the HID protocol, beyond USB and Bluetooth, to support I²C devices. I²C is a simple but efficient protocol and has been used for over a decade in phone and embedded platforms. This protocol is supported in Windows 8 by an in-box KMDF driver named HIDI2C.sys.

This combined support for I²C over HID in the inbox driver, allows hardware manufactures to get their devices running quickly on windows without imposing the need to create a driver.

In order to ensure correct behavior on a system with multiple ACPI resources, the following two resources must appear first:

-   HID I²C connection
-   Device interrupt

After these resources are defined, additional ACPI resources, of other types, may follow.

*Important notes:*

-   Today, the HID I²C driver targets SoC systems that support Simple Peripheral Bus (SPB) and GPIO. In the future, Microsoft may support this driver on non-SoC systems.
-   The HID I²C driver is optimized to support all HID Clients.
-   The HID I²C driver enables devices and system manufacturers to reduce the total number of drivers they have to develop to support common device types like keyboards, touchpads, touch screens, sensors, and so on.
-   The HID I²C driver is available on all client SKUs of Windows and is included in WinPE.

 

 




