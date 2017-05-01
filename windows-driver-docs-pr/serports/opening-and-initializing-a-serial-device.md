---
title: Opening and Initializing a Serial Device
author: windows-driver-content
description: Opening and Initializing a Serial Device
ms.assetid: 08266561-4738-4313-b53b-d60081e875c7
keywords:
- Serial driver WDK , device opening
- Serial driver WDK , device initializing
- serial devices WDK , opening
- serial devices WDK , initializing
- initializing serial devices
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Opening and Initializing a Serial Device


## <a href="" id="ddk-opening-and-initializing-a-serial-device-kg"></a>


When Serial is used as a function driver, the following considerations apply to opening and initializing a serial device:

-   Serial supports only one open at a time on a serial device.

-   A device is in an undefined state when it is opened. A client should initialize a device to a known state before using the device. A user-mode client must use the communications functions that are supported by the Windows Base Services in the Microsoft Windows SDK. A kernel-mode client can use the [IOCTL\_SERIAL\_SET\_Xxx](https://msdn.microsoft.com/library/windows/hardware/ff547466) and the [IOCTL\_SERIAL\_INTERNAL\_Xxx](https://msdn.microsoft.com/library/windows/hardware/ff547480) requests.

-   All clients must open a serial device when needed, and close the device immediately after they are through with the port.

-   Serenum must open an RS-232 port to enumerate the port. Clients that hold an RS-232 port open indefinitely should not use Serenum.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Opening%20and%20Initializing%20a%20Serial%20Device%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


