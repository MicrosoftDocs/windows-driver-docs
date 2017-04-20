---
title: Installing Serial Ports and COM Ports
author: windows-driver-content
description: Installing Serial Ports and COM Ports
ms.assetid: 9c755dfa-65e5-4ecb-8544-dd63c6b69c8e
keywords:
- serial ports WDK
- COM ports WDK serial devices
- Serial driver WDK , COM ports
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installing Serial Ports and COM Ports


## <a href="" id="ddk-installing-serial-ports-and-com-ports-kg"></a>


For most devices, the Ports [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509) and the Serial function driver provide the functionality required to operate serial ports and COM ports. To install serial ports and COM ports using these system-supplied components, do the following:

-   Provide an INF file that specifies the Ports device setup class and the Serial function driver as the service for the port.

-   To configure a serial port as COM port, comply with the requirements that are defined in [Configuration of COM Ports](configuration-of-com-ports.md).

For more information about installing serial ports and COM ports using the Ports device setup class and the Serial function driver, see the following topics:

[Installing Plug and Play Serial Ports and COM Ports](installing-plug-and-play-serial-ports-and-com-ports.md)

[Installing Legacy COM Ports](installing-legacy-com-ports.md)

If you do a custom installation of a COM port, you must comply with the COM port requirements that are defined in [Configuration of COM Ports](configuration-of-com-ports.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Installing%20Serial%20Ports%20and%20COM%20Ports%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


