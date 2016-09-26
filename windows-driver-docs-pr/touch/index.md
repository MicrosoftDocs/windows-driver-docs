---
title: Windows Touch Drivers
description: Starting in Windows 8, Touch has been expanded to include any pointer device and is now referred to as Windows Pointer Device. Windows Pointer Device refers to devices that support pen (stylus input), touch, or multi-touch functionality.
ms.assetid: CFFB0353-3F8B-45AF-BD10-EE759074B08B
---

# Windows Touch Drivers


Starting in Windows 8, Touch has been expanded to include any pointer device and is now referred to as *Windows Pointer Device*. Windows Pointer Device refers to devices that support pen (stylus input), touch, or multi-touch functionality.

Windows pointer devices use the Human Interface Device (HID) protocol to communicate with Windows. Because Windows 8 includes an HID driver, you do not need to implement one. You only need to report Windows Pointer Device usages in the firmware for your pointer device. Windows will use your firmware and its own HID driver to enable touch and pointer capabilities for your device and furnish the Windows touch and pointer APIs with access to your device.

For details on the usages to report in the firmware for your device, see [Windows Pointer Device Data Delivery](windows-pointer-device-data-delivery.md).

If you are searching for information on touch drivers for Windows 7 or earlier, see [Legacy Windows Touch Drivers (Windows 7)](legacy-windows-touch-drivers.md).

If you are looking for information on precision touchpad drivers, see [Windows Precision Touchpad Implementation Guide](windows-precision-touchpad-implementation-guide.md)

 

 




