---
title: Vendor-Provided Device Installation Components
description: Vendor-Provided Device Installation Components
ms.assetid: d86bdf75-9726-4b44-8753-7e9c19e88a61
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Vendor-Provided%20Device%20Installation%20Components%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




