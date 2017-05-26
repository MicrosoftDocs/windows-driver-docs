---
title: Serial Device Control Requests
author: windows-driver-content
description: Serial Device Control Requests
ms.assetid: 12dab038-e4da-47b5-ada8-e1c7ee980cde
keywords:
- serial devices WDK , device control requests
- device control requests WDK serial devices
- Serial driver WDK , device control requests
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Serial Device Control Requests


## <a href="" id="ddk-serial-device-control-requests-kg"></a>


Serial provides device control requests to control the operation of serial devices that support a 16550 UART-compatible interface.

Serial supports [IOCTL\_SERIAL\_Xxx](https://msdn.microsoft.com/library/windows/hardware/ff547466) requests that a client can use to perform the following tasks:

-   Get and set control registers and control signals.

-   Get and set line control and modem control.

-   Set FIFO control.

-   Get and set handshake and flow control operation and parameters.

-   Get and set wait events.

-   Purge internal buffers, set the receive buffer size, and reset the device.

-   Get and set timeouts that are used for read and write requests.

-   Get and clear performance statistics.

-   Get status information.

-   Get properties of the device.

Serial supports [IOCTL\_SERIAL\_INTERNAL\_Xxx](https://msdn.microsoft.com/library/windows/hardware/ff547480) requests that a trusted kernel-mode client can use to perform the following tasks:

-   Set basic settings on a device and restore previous settings.

-   Disable and enable the wait/wake operation of a device.

For more information about the high-level operation of [COM ports](configuration-of-com-ports.md), see the information about the communication resources that are supported by the Windows Base Services in the Microsoft Windows SDK.

For more information about Serial I/O requests, see [Serial Driver Reference](https://msdn.microsoft.com/library/windows/hardware/ff547476).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Serial%20Device%20Control%20Requests%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


