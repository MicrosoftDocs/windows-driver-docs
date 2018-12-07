---
title: Bluetooth Universal Windows driver model for Windows 10
description: In Windows 10, the Bluetooth transport driver interface for all devices is converged and uses the Universal Windows driver model.
ms.assetid: E65A71D3-C0D2-4E13-9E19-1E6C6C1A172E
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





