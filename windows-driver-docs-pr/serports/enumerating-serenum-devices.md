---
title: Enumerating Serenum Devices
description: Enumerating Serenum Devices
ms.assetid: c850c52b-82d7-48c2-a6c4-bfd071756632
keywords:
- Serenum driver WDK , device enumeration
- enumerating Serenum devices WDK serial devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enumerating Serenum Devices





In Microsoft Windows 2000, boot time can be significantly delayed by the time it takes to automatically enumerate high-capacity multiport adapters (containing 16 or more ports). To address this issue, Windows XP and later supports the following enhancements:

-   Compared to Windows 2000, the time Serenum requires to automatically enumerate high-capacity multiport adapters is substantially reduced.

-   In Windows XP and later, Serenum supports an optional **SkipEnumerations** registry entry value for each serial port installed on a system. A vendor can use this entry value to control whether Serenum enumerates a port (whether initiated by a system boot or by a user through Device Manager or Add Hardware Wizard).

For details about how to set a serial port's **SkipEnumerations** entry value in Windows XP, see [Registry Settings for Serenum](registry-settings-for-serenum.md).

Windows does not support a single registry setting that globally controls the enumeration of all serial ports.

Serenum must open a serial port to enumerate it. Devices that keep a port open indefinitely should not use Serenum.

 

 




