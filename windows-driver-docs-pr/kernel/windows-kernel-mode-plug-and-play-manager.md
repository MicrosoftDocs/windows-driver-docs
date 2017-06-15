---
title: Windows Kernel-Mode Plug and Play Manager
author: windows-driver-content
description: Windows Kernel-Mode Plug and Play Manager
MS-HAID:
- 'pnpmanager\_49a21603-933d-4fe6-a8f0-d64cc1832121.xml'
- 'kernel.windows\_kernel\_mode\_plug\_and\_play\_manager'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 43d06dbe-da66-4103-8be3-f27ff075a1b4
---

# Windows Kernel-Mode Plug and Play Manager


Plug and Play (PnP) is a combination of hardware technology and software techniques that enables a PC to recognize when a device is added to the system. With PnP, the system configuration can change with little or no input from the user. For example, when a USB thumb drive is plugged in, Windows can detect the thumb drive and add it to the file system automatically. However, to do this, the hardware must follow certain requirements and so must the driver.

For more information about PnP for drivers, see [Plug and Play](implementing-plug-and-play.md).

The PnP manager is actually a subsystem of the I/O manager. For more information about the I/O manager, see [Windows Kernel-Mode I/O Manager](windows-kernel-mode-i-o-manager.md).

For lists of PnP routines, see [Plug and Play Routines](https://msdn.microsoft.com/library/windows/hardware/ff558809).

Note that there are no routines that provide a direct interface to the PnP manager; that is, there are no "**Pp**" routines.

The Windows Driver Frameworks (WDF) provide a set of libraries to make PnP management much easier. For more information about WDF, see [Kernel-Mode Driver Framework Overview](https://msdn.microsoft.com/library/windows/hardware/ff544296).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Windows%20Kernel-Mode%20Plug%20and%20Play%20Manager%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


