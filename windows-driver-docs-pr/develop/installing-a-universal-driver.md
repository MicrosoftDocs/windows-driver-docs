---
ms.assetid: 1D47B648-C652-4188-A406-AA5EB537138F
title: Installing a Universal Windows driver
description: A driver for any OneCore-based edition of Windows 10 other than Windows 10 for desktop editions must be a Universal Windows driver, and it must be installed using a universal INF file.
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installing a Universal Windows driver

A driver for any OneCoreUAP-based edition of Windows 10 other than Windows 10 for desktop editions (Home, Pro, and Enterprise) must be a [Universal Windows driver](getting-started-with-universal-drivers.md), and it must be installed using a *universal INF file*.

To install a Universal Windows driver on Windows 10 for desktop editions, we recommend using a universal INF file due to improved performance, but you can use a legacy (non-universal) INF file.

**Note**  The SetupAPI component is not part of UWP, so a Universal Windows driver cannot call functions in this API set.

An INF for a Universal Windows driver cannot include any of the following:

-   Coinstallers
-   Class installers
-   RegisterDLL, DelFile, or DelReg directives
-   Non-HKR AddReg directives

For more information, see:

* [Using a Universal INF File](../install/using-a-universal-inf-file.md)
* [InfVerif](../devtest/infverif.md)
