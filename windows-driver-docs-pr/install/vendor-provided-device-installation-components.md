---
title: Vendor-Provided Device Installation Components
description: Vendor-Provided Device Installation Components
ms.assetid: d86bdf75-9726-4b44-8753-7e9c19e88a61
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Vendor-Provided Device Installation Components


This topic describes device installation components that are provided by an IHV or OEM.

<a href="" id="driver-package"></a>Driver Package  
A [driver package](driver-packages.md) consists of all the software components that you must supply for your device to be supported under Windows. These components include the following:

-   An [INF file](inf-files.md), which provides information about the devices and drivers to be installed. For more information, see [Creating an INF File](https://msdn.microsoft.com/library/windows/hardware/ff538378).

-   A [catalog file](catalog-files.md), which contains the digital signature of the [driver package](driver-packages.md). For more information, see [Digital Signatures](digital-signatures.md).

-   The driver for the device.

<a href="" id="drivers"></a>Drivers  
A driver allows the system to interact with the hardware device. Windows copies the driver's binary file (.sys) to the %SystemRoot%\\system32\\drivers directory when the device is installed. Drivers are required for most devices.

For more information, see [Choosing a Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff554652).

For more information about drivers for Windows, see [Getting Started with Windows Drivers](https://msdn.microsoft.com/library/windows/hardware/ff554690).

 

 





