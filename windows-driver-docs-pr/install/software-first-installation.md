---
title: Software-First Installation
description: Software-First Installation
ms.assetid: 2199316d-17d5-463a-8c97-f89c87473f20
keywords: ["installation applications WDK , software-first installations", "device installation applications WDK , software-first installations", "distribution medium WDK device installations , software-first installations", "software-first installations WDK device installations", "AutoRun-enabled installation applications WDK", "device installations WDK , types"]
---

# Software-First Installation


A software-first installation involves the staging and preinstallation of your [driver package](driver-packages.md) on the system before the hardware device is plugged in. After the device is plugged in, the driver from the driver package is installed.

If the user inserts your distribution medium before plugging in the device, an AutoRun-enabled installation application can:

-   [Check for in-progress installations](checking-for-in-progress-installations.md), and stop executing if other installation activities are in progress.

-   [Determine whether a device is plugged in](determining-whether-a-device-is-plugged-in.md).

-   [Preinstall driver packages](preinstalling-driver-packages.md)

-   Use Microsoft Installer to [install device-specific applications](installing-device-specific-applications.md).

-   If the device is "hot-pluggable," tell the user to plug it in.

    If the bus does not provide hot-plug notification, initiate reenumeration by calling [**CM\_Reenumerate\_DevNode**](https://msdn.microsoft.com/library/windows/hardware/ff539763).

-   If the device is not hot-pluggable, tell the user to turn the system off, plug in the device, and turn the system back on.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Software-First%20Installation%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




