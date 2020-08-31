---
title: Introduction to WDM
description: To allow driver developers to write device drivers that are source-code compatible across all Microsoft Windows operating systems, the Windows Driver Model (WDM) was introduced. Kernel-mode drivers that follow WDM rules are called WDM drivers.
ms.assetid: 00225ec6-fe56-4cbc-b94d-2ba5f28c0bb9
keywords: ["WDM WDK kernel", "Windows Driver Model WDK kernel", "WDM drivers WDK kernel", "Wdm.h", "Ntddk.h", "WDM drivers WDK kernel , about WDM drivers"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Introduction to WDM

> [!NOTE]
> This section contains guidance on WDM drivers, which is no longer the recommended driver model. For guidance on choosing a driver model, see [Choosing a driver model](../gettingstarted/choosing-a-driver-model.md).

To allow driver developers to write device drivers that are source-code compatible across all Microsoft Windows operating systems, the *Windows Driver Model* (WDM) was introduced. Kernel-mode drivers that follow WDM rules are called *WDM drivers*.

All WDM drivers must do the following:

-   Include Wdm.h, not Ntddk.h. (Note that Wdm.h is a subset of Ntddk.h.)

-   Be designed as a bus driver, a function driver, or a filter driver, as described in [Types of WDM Drivers](types-of-wdm-drivers.md).

-   Create device objects as described in [WDM Device Objects and Device Stacks](wdm-device-objects-and-device-stacks.md).

-   Support [Plug and Play (PnP)](implementing-plug-and-play.md).

-   Support [power management](./introduction-to-power-management.md).

-   Support [Windows Management Instrumentation](implementing-wmi.md) (WMI).

### Should You Write a WDM Driver?

If you are writing a new driver, consider using the [Kernel-Mode Driver Framework](../wdf/index.md) (KMDF). KMDF provides interfaces that are simpler to use than WDM interfaces.

Do not write a WDM driver if the driver will be inserted into a stack of non-WDM drivers. Please read the documentation for device type-specific Microsoft-supplied drivers to determine how new drivers must interface with Microsoft-supplied drivers. For more device type-specific information, see [Device and Driver Technologies](../index.yml).)