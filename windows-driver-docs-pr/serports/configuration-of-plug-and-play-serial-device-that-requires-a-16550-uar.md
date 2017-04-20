---
title: Configure PnP Serial Devices for 16550 UART Interface
author: windows-driver-content
description: Configuration of Plug and Play Serial Device that Requires a 16550 UART-Compatible Interface
ms.assetid: b99259bd-7573-4f71-9ab5-b263eed41288
keywords:
- Plug and Play serial devices WDK
- serial devices WDK , Plug and Play
- universal asynchronous receiver-transmitters WDK serial devices
- UART WDK serial devices
- 16550 UART-compatible interfaces WDK serial devices
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Configuration of Plug and Play Serial Device that Requires a 16550 UART-Compatible Interface


## <a href="" id="ddk-configuration-of-plug-and-play-serial-device-that-requires-a-16550"></a>


This section describes the typical configuration of hardware, drivers, and device stacks that is used for serial devices that:

-   Support Plug and Play.

-   Require a 16550 UART-compatible interface.

-   Are not connected to an RS-232 port.

An example is a PCMCIA card with a modem.

The following diagram shows the typical configuration for a sample toaster device and a sample blender device that require a 16550 UART-compatible interface.

![left figure: hardware configuration for a plug and play toaster device on a pcmcia card. right figure: configuration of drivers and device stacks for a plug and play toaster device on a pcmcia card](images/ser3.png)

In these configurations, the Toaster device is a child device on a PCMCIA bus. The PCMCIA bus driver creates a PDO for the Toaster device when it enumerates the PCMCIA card. The INF file for the Toaster device specifies Serial as a lower-level device filter driver. Serial provides a 16550 UART-compatible interface to the hardware device. The Toaster driver creates and attaches an FDO to the Toaster device stack.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Configuration%20of%20Plug%20and%20Play%20Serial%20Device%20that%20Requires%20a%2016550%20UART-Compatible%20Interface%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


