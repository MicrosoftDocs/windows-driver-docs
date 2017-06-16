---
title: Introduction to WDM
author: windows-driver-content
description: To allow driver developers to write device drivers that are source-code compatible across all Microsoft Windows operating systems, the Windows Driver Model (WDM) was introduced. Kernel-mode drivers that follow WDM rules are called WDM drivers.
ms.assetid: 00225ec6-fe56-4cbc-b94d-2ba5f28c0bb9
keywords: ["WDM WDK kernel", "Windows Driver Model WDK kernel", "WDM drivers WDK kernel", "Wdm.h", "Ntddk.h", "WDM drivers WDK kernel , about WDM drivers"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to WDM


To allow driver developers to write device drivers that are source-code compatible across all Microsoft Windows operating systems, the *Windows Driver Model* (WDM) was introduced. Kernel-mode drivers that follow WDM rules are called *WDM drivers*.

## <a href="" id="ddk-introduction-to-wdm-kg"></a>


All WDM drivers must do the following:

-   Include Wdm.h, not Ntddk.h. (Note that Wdm.h is a subset of Ntddk.h.)

-   Be designed as a bus driver, a function driver, or a filter driver, as described in [Types of WDM Drivers](types-of-wdm-drivers.md).

-   Create device objects as described in [WDM Device Objects and Device Stacks](wdm-device-objects-and-device-stacks.md).

-   Support [Plug and Play (PnP)](implementing-plug-and-play.md).

-   Support [power management](implementing-power-management.md).

-   Support [Windows Management Instrumentation](implementing-wmi.md) (WMI).

### Does the WDK Cover Non-WDM Drivers?

The Windows Driver Kit (WDK) emphasizes the development of WDM drivers for kernel mode, but the WDK also includes information that is pertinent to kernel-mode drivers that do not follow WDM rules. This information allows you to maintain existing non-WDM drivers and to write new drivers that interface with these existing drivers.

### Should You Always Write a WDM Driver?

If you are writing new kernel-mode drivers, they should be WDM drivers, *unless* you are writing a driver that will be inserted into a stack of non-WDM drivers. Please read the documentation for device type-specific Microsoft-supplied drivers to determine how new drivers must interface with Microsoft-supplied drivers. For more device type-specific information, see [Device and Driver Technologies](https://msdn.microsoft.com/library/windows/hardware/ff557557).)

**Note**  All new driver stacks should consist of WDM drivers.

 

There are cross-platform issues to consider, whether you are developing WDM or non-WDM drivers. For more information, see [Writing Drivers for Different Versions of Windows](https://msdn.microsoft.com/library/windows/hardware/ff554887).

If you are writing a new WDM driver, you should also consider using the [Kernel-Mode Driver Framework](https://msdn.microsoft.com/library/windows/hardware/dn265580) (KMDF). KMDF provides interfaces that are simpler to use than WDM interfaces.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Introduction%20to%20WDM%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


