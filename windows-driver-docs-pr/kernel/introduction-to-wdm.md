---
title: Introduction to WDM
description: To allow driver developers to write device drivers that are source-code compatible across all Microsoft Windows operating systems, the Windows Driver Model (WDM) was introduced. Kernel-mode drivers that follow WDM rules are called WDM drivers.
ms.assetid: 00225ec6-fe56-4cbc-b94d-2ba5f28c0bb9
keywords: ["WDM WDK kernel", "Windows Driver Model WDK kernel", "WDM drivers WDK kernel", "Wdm.h", "Ntddk.h", "WDM drivers WDK kernel , about WDM drivers"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Introduction to WDM


To allow driver developers to write device drivers that are source-code compatible across all Microsoft Windows operating systems, the *Windows Driver Model* (WDM) was introduced. Kernel-mode drivers that follow WDM rules are called *WDM drivers*.




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

 

 




