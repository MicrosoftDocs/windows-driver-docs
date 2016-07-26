---
title: Plug and Play Manager
description: Plug and Play Manager
ms.assetid: b1890b3c-fc7b-4a2e-b48a-8266f237c9b6
---

# Plug and Play Manager


The Plug and Play (PnP) manager provides the support for PnP functionality in Windows and is responsible for the following PnP-related tasks:

-   Device detection and enumeration while the system is booting

-   Adding or removing devices while the system is running

The kernel-mode PnP manager notifies the user-mode PnP manager that a new device is present on the system and must be installed.

The kernel-mode PnP manager also calls the [*DriverEntry*](https://msdn.microsoft.com/library/windows/hardware/ff544113) and [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routines of a device's driver and sends the [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request to start the device.

The PnP manager maintains the [Device Tree](https://msdn.microsoft.com/library/windows/hardware/ff543194) that keeps track of the devices in the system. The device tree contains information about the devices present on the system. When the computer starts, the PnP manager builds this tree by using information from drivers and other components, and updates the tree as devices are added or removed.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Plug%20and%20Play%20Manager%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




