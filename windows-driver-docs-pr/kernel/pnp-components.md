---
title: PnP Components
author: windows-driver-content
description: PnP Components
MS-HAID:
- 'PlugPlay\_d0d066ff-b462-49b1-9aa3-45194b444ed1.xml'
- 'kernel.pnp\_components'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 33612da4-1ddb-40cf-a8a2-838f85b52cd6
keywords: ["PnP WDK kernel , components", "Plug and Play WDK kernel , components", "software components WDK PnP", "PnP drivers WDK kernel", "user-mode PnP manager WDK", "kernel-mode PnP manager WDK", "PnP managers WDK", "PnP components WDK user-mode"]
---

# PnP Components


## <a href="" id="ddk-pnp-components-kg"></a>


The following figure shows the components that work together to support PnP.

![diagram illustrating plug and play software components](images/pnpcomp.png)

The PnP manager has two parts: the kernel-mode PnP manager and the user-mode PnP manager. The kernel-mode PnP manager interacts with operating system components and drivers to configure, manage, and maintain devices. The user-mode PnP manager interacts with user-mode setup components, such as Class Installers, to configure and install devices. The user-mode PnP manager also interacts with applications to, for example, register an application for notification of device changes and notify the application when a device event occurs.

PnP drivers support the physical, logical, and virtual devices on a machine. The term "PnP driver" refers to any Windows driver that supports the interfaces described in this section. While most PnP drivers are also WDM drivers and thus source-compatible across Windows platforms, a few drivers support PnP without fully implementing WDM.

All drivers should support PnP and power management. If a single driver does not support PnP and power management, it constrains the PnP and power management support of the system as a whole.

See [Device Installation Overview](https://msdn.microsoft.com/library/windows/hardware/ff549455) for information about device and driver setup, including (INF) files, CAT files, and the registry.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20PnP%20Components%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


