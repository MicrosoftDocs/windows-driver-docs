---
title: Enumerating Serenum Devices
author: windows-driver-content
description: Enumerating Serenum Devices
ms.assetid: c850c52b-82d7-48c2-a6c4-bfd071756632
keywords: ["Serenum driver WDK , device enumeration", "enumerating Serenum devices WDK serial devices"]
---

# Enumerating Serenum Devices


## <a href="" id="ddk-enumerating-serenum-devices-kg"></a>


In Microsoft Windows 2000, boot time can be significantly delayed by the time it takes to automatically enumerate high-capacity multiport adapters (containing 16 or more ports). To address this issue, Windows XP and later supports the following enhancements:

-   Compared to Windows 2000, the time Serenum requires to automatically enumerate high-capacity multiport adapters is substantially reduced.

-   In Windows XP and later, Serenum supports an optional **SkipEnumerations** registry entry value for each serial port installed on a system. A vendor can use this entry value to control whether Serenum enumerates a port (whether initiated by a system boot or by a user through Device Manager or Add Hardware Wizard).

For details about how to set a serial port's **SkipEnumerations** entry value in Windows XP, see [Registry Settings for Serenum](registry-settings-for-serenum.md).

Windows does not support a single registry setting that globally controls the enumeration of all serial ports.

Serenum must open a serial port to enumerate it. Devices that keep a port open indefinitely should not use Serenum.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Enumerating%20Serenum%20Devices%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


