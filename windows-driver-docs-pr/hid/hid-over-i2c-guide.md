---
title: HID over I2C
author: windows-driver-content
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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20HID%20over%20I2C%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


