---
title: Enumerating the Devices on a Bus
description: Enumerating the Devices on a Bus
ms.assetid: 5731db82-2bc8-4a8d-98f1-3977845f572c
keywords:
- PnP WDK KMDF , bus enumeration
- Plug and Play WDK KMDF , bus enumeration
- bus enumeration WDK KMDF
- enumeration WDK KMDF
- child devices WDK KMDF
- listing child devices WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enumerating the Devices on a Bus


*Bus enumeration* is the act of determining which child devices are connected to a parent device. A parent device is typically a bus adapter, but it can also be a device that supports multiple functions, such as a sound card, for which each function requires a separate set of drivers.

Kernel-Mode Driver Framework (KMDF) supports two types of bus enumeration:

-   [Static enumeration](static-enumeration.md), which is easy to implement and is ideal if the number and type of child devices is not system-specific and does not change after the hardware has been plugged in.

-   [Dynamic enumeration](dynamic-enumeration.md), which should be used if the number or type of child devices changes from one computer to another.

A bus driver can use either or both types of bus enumeration.

For more information about writing a KMDF bus driver, see [Bus Driver Development Based on KMDF](https://msdn.microsoft.com/windows/hardware/gg463281).

 

 





