---
title: Sending I/O Requests to Lower Drivers
description: Sending I/O Requests to Lower Drivers
ms.assetid: 89868b4d-e2c1-4f38-b81e-a96b8cff3e4f
keywords: ["I/O requests WDK UMDF , lower drivers", "request processing WDK UMDF , lower drivers"]
---

# Sending I/O Requests to Lower Drivers


\[This topic applies to UMDF 1.*x*.\]

When a driver receives an I/O request that it cannot fully process, the driver typically forwards the received request to the next lower driver in the stack. The driver calls the [**IWDFIoRequest::Send**](https://msdn.microsoft.com/library/windows/hardware/ff559149) method to forward the request. To forward synchronously, the driver passes the WDF\_REQUEST\_SEND\_OPTION\_SYNCHRONOUS flag in the *Flags* parameter. Otherwise, the driver forwards the request asynchronously. Before the driver forwards the request, it should register a completion routine. For more information, see [Completing I/O Requests](completing-i-o-requests.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Sending%20I/O%20Requests%20to%20Lower%20Drivers%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




