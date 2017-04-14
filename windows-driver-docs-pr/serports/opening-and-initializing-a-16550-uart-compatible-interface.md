---
title: Opening and Initializing a 16550 UART-Compatible Interface
author: windows-driver-content
description: Opening and Initializing a 16550 UART-Compatible Interface
ms.assetid: 341cc1cb-bbcf-4514-8f5d-8970e49923c2
keywords: ["Serial driver WDK , 16550 UART-compatible interfaces", "universal asynchronous receiver-transmitters WDK serial devices", "UART WDK serial devices", "16550 UART-compatible interfaces WDK serial devices", "initializing 16550 UART-compatible interfaces"]
---

# Opening and Initializing a 16550 UART-Compatible Interface


## <a href="" id="ddk-opening-and-initializing-a-16550-uart-compatible-interface-kg"></a>


When Serial is used as a lower-level device filter driver, the following considerations apply to opening and initializing the filter device:

-   Serial supports only one open at a time on the filter device.

-   The filter device is in an undefined state when it is open.

    A client should initialize the filter device to a known state before using it. A user-mode client can use the [IOCTL\_SERIAL\_SET\_Xxx](https://msdn.microsoft.com/library/windows/hardware/ff547466) requests. Note, however, that a Win32-compliant application must use the communication functions that are supported by the Windows Base Services in the Microsoft Windows SDK. A kernel-mode client can use the IOCTL\_SERIAL\_Xxx and the [IOCTL\_SERIAL\_INTERNAL\_Xxx](https://msdn.microsoft.com/library/windows/hardware/ff547480) requests.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Opening%20and%20Initializing%20a%2016550%20UART-Compatible%20Interface%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


