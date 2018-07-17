---
title: Tools for Changing Boot Options for Driver Testing and Debugging
description: Tools for Changing Boot Options for Driver Testing and Debugging
ms.assetid: 4fd58868-7a43-42e3-adf9-5a82593c1675
keywords:
- tools WDK , boot options
- driver development tools WDK , boot options
- boot options WDK
- driver testing WDK boot options
- testing drivers WDK boot options
- debugging drivers WDK boot options
- driver debugging WDK boot options
- operating system boot options WDK
- load configurations WDK boot options
ms.author: windowsdriverdev
ms.date: 07/09/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Tools for Changing Boot Options for Driver Testing and Debugging

To test and debug drivers on a Microsoft Windows operating system, you must enable and configure features that are established when the operating system loads. The settings for these features are included in the *boot options*--values that determine how the boot loader loads and configures the operating system and other bootable programs and devices.

> [!TIP] 
> If you are using the Windows Driver Kit (WDK) 8, you can configure computers for testing and debugging from Visual Studio. When you configure the test computers, the WDK driver test framework automatically enables the test computer for remote debugging and transfers the necessary test binaries and support files. 
> For more information, see [Provision a computer for driver deployment and testing (WDK 8.1)](https://docs.microsoft.com/windows-hardware/drivers/gettingstarted/provision-a-target-computer-wdk-8-1), or [Provision a computer for driver deployment and testing (WDK 8)](https://msdn.microsoft.com/library/windows/hardware/hh698272), and [How to test a driver at runtime using Visual Studio](https://docs.microsoft.com/windows-hardware/drivers/develop/testing-a-driver-at-runtime).

This section explains how to add, delete, and change boot options to create new load configurations for an operating system and how to use the boot entry parameters to customize a load configuration for driver testing and debugging.

By editing boot options, you can:

- Enable and configure debugging

- Load a particular kernel or hardware abstraction layer (HAL) file

- Limit the physical memory available to Windows

- Enable, disable, and configure Physical Address Extension (PAE) on 32-bit versions of Windows

- Reapportion virtual address space between user-mode and kernel-mode components (3GB) to test a driver in a very small kernel-mode address space

- Enable and configure Data Execution Prevention (/noexecute)

- Designate ports for Emergency Management Services (EMS) console redirection on headless servers

- Display the names of drivers as they load

This section includes:

- [Introduction to Boot Options](introduction-to-boot-options.md)
- [Editing Boot Options](editing-boot-options.md)
- [Boot.ini Boot Parameter Reference](https://msdn.microsoft.com/library/windows/hardware/ff542248)
- [BCD Boot Options Reference](https://msdn.microsoft.com/library/windows/hardware/ff542205)
- [Using Boot Parameters](using-boot-parameters.md)
- [Bypassing Boot Options](bypassing-boot-options.md)

Beginning in Windows Vista, Windows includes a new boot loader architecture, new boot options, and a new boot options editor. For information, see [Boot Options in Windows Vista](boot-options-in-windows-vista-and-later.md).
