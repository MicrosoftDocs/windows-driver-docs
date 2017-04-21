---
title: Bluetooth Universal Windows driver model for Windows 10
description: In Windows 10, the Bluetooth transport driver interface for all devices is converged and uses the Universal Windows driver model.
ms.assetid: E65A71D3-C0D2-4E13-9E19-1E6C6C1A172E
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Bluetooth Universal Windows driver model for Windows 10


In Windows 10, the Bluetooth transport driver interface for all devices is converged and uses the Universal Windows driver model. You can write a single driver that runs on all Windows device platforms.

The Bluetooth audio driver surface area is diverged for Windows 10 and allows the following two options:

-   You can write a new audio Universal Windows driver that works for both desktop and mobile devices.
-   An existing Windows Phone 8.1 Bluetooth audio driver will run on Windows 10 Mobile.

## <span id="How_to_write_a_Bluetooth_Universal_Windows_driver"></span><span id="how_to_write_a_bluetooth_universal_windows_driver"></span><span id="HOW_TO_WRITE_A_BLUETOOTH_UNIVERSAL_WINDOWS_DRIVER"></span>How to write a Bluetooth Universal Windows driver


To write a Bluetooth Universal Windows driver, see [Getting Started with Universal Windows drivers](https://msdn.microsoft.com/windows-drivers/develop/getting_started_with_universal_drivers), and follow the steps in the section titled *Building a Universal Windows driver* to build a Universal Windows driver using the Kernel Mode Driver (KMDF) template.

Then, see the Bluetooth design and reference sections for implementation guidance.

-   [Bluetooth profile drivers](bluetooth-profile-drivers-overview.md)
-   [Bluetooth device reference](https://msdn.microsoft.com/library/windows/hardware/ff536585)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[bltooth\bltooth]:%20Bluetooth%20Universal%20Windows%20driver%20model%20for%20Windows%2010%20%20RELEASE:%20%283/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




