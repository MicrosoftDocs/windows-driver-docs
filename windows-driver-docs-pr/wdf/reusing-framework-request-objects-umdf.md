---
title: Reusing Framework Request Objects
author: windows-driver-content
description: Reusing Framework Request Objects
ms.assetid: 804efc94-a7df-4ebd-a42e-82d1c5376e19
keywords: ["I/O requests WDK UMDF , reusing objects", "request processing WDK UMDF , reusing I/O request objects", "User-Mode Driver Framework WDK , reusing I/O request objects", "UMDF WDK , reusing I/O request objects", "user-mode drivers WDK UMDF , reusing I/O request objects", "reusing I/O request objects WDK UMDF"]
---

# Reusing Framework Request Objects


\[This topic applies to UMDF 1.*x*.\]

To improve driver performance, framework-based drivers that create and send many nearly identical asynchronous requests to an I/O target can reuse request objects instead of creating a new request object for each request. A driver can reuse a request object after the request has been completed.

If a driver has created a request object by calling [**IWDFDevice::CreateRequest**](https://msdn.microsoft.com/library/windows/hardware/ff557021), it can reuse the request by calling [**IWDFIoRequest2::Reuse**](https://msdn.microsoft.com/library/windows/hardware/ff559048). A driver can also reuse request objects that it has received from the framework in its I/O queues.

If your driver provides an [**IRequestCallbackRequestCompletion::OnCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff556905) callback function for a request object that it reuses, the driver must call [**IWDFIoRequest::SetCompletionCallback**](https://msdn.microsoft.com/library/windows/hardware/ff559153) after it calls [**Reuse**](https://msdn.microsoft.com/library/windows/hardware/ff559048).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Reusing%20Framework%20Request%20Objects%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




