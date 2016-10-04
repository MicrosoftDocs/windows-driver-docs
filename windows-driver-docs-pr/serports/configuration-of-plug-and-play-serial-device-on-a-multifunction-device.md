---
title: Configuration of Plug and Play Serial Device on a Multifunction Device that Requires a 16550 UART-Compatible Interface
author: windows-driver-content
description: Configuration of Plug and Play Serial Device on a Multifunction Device that Requires a 16550 UART-Compatible Interface
MS-HAID:
- 'sseovr\_016ede5f-97a2-4196-a8dc-b3b56fa88a78.xml'
- 'serports.configuration\_of\_plug\_and\_play\_serial\_device\_on\_a\_multifunction\_device'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 63588ac9-4c87-421d-8da3-3e950cbd466c
keywords: ["Plug and Play serial devices WDK", "serial devices WDK , Plug and Play", "universal asynchronous receiver-transmitters WDK serial devices", "UART WDK serial devices", "16550 UART-compatible interfaces WDK serial devices", "multifunction devices", "multifunction devices WDK serial devices"]
---

# Configuration of Plug and Play Serial Device on a Multifunction Device that Requires a 16550 UART-Compatible Interface


## <a href="" id="ddk-configuration-of-plug-and-play-serial-device-on-a-multifunction-de"></a>


This section describes the configuration of hardware, drivers, and device stacks for multifunction serial devices that:

-   Support Plug and Play.

-   Require a 16550 UART-compatible interface.

-   Are not connected to an RS-232 port.

A specific example is a PCMCIA card that has a modem and a LAN adapter.

The following diagram shows the typical configuration for a sample toaster device and a sample blender device that require a 16550 UART-compatible interface

![diagram illustrating hardware and drivers-and-device-stacks configurations for a toaster on a multifunction pcmcia card, and for a toaster and blender](images/ser4.png)

In these configurations, the Toaster device is a child device on the multifunction device, and the multifunction device is a child device on a PCMCIA bus.

The INF file and installers for the Toaster device install the Serial driver as lower-level device filter driver to provide a 16550 UART-compatible interface for the Toaster device. The Toaster driver creates and attaches an FDO to the Serial driver filter DO.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Configuration%20of%20Plug%20and%20Play%20Serial%20Device%20on%20a%20Multifunction%20Device%20that%20Requires%20a%2016550%20UART-Compatible%20Interface%20%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


