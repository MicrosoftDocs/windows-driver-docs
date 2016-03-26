---
title: Sending I/O Requests to General I/O Targets
description: Sending I/O Requests to General I/O Targets
ms.assetid: 3fa897f5-2de8-484b-becb-c2de23fb5e8c
keywords: ["general I/O targets WDK KMDF , sending I/O requests to", "sending I/O requests WDK KMDF"]
---

# Sending I/O Requests to General I/O Targets


## <a href="" id="ddk-sending-i-o-requests-to-general-i-o-targets-df"></a>


Your driver can send I/O requests to general I/O targets either synchronously or asynchronously.

If a driver sends I/O requests synchronously, a driver thread sends the requests one at a time. The thread waits for each request to complete before it sends the next one. This process is simpler than sending the I/O requests asynchronously. Your driver can send I/O requests synchronously if it does not send many requests and if system or device performance is not reduced while your driver waits for each I/O request.

If a driver sends I/O requests asynchronously, a driver thread sends each request as soon as the request is ready to be sent, without waiting for previously sent requests to finish. If your driver must handle many I/O requests in short periods of time, you probably cannot allow your driver to wait for each request to complete before sending the next request. Otherwise, you might lose data or reduce the performance of your driver's devices and, possibly, of the entire system.

The framework's I/O target object provides two sets of methods that your driver can call: one set to [send I/O requests synchronously](sending-i-o-requests-synchronously.md) and the other set to [send I/O requests asynchronously](sending-i-o-requests-asynchronously.md).

For each of these methods, you must supply a request object and some buffer space. You can use these methods to forward a request that your driver received in one of its I/O queues or to create and send a new request.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Sending%20I/O%20Requests%20to%20General%20I/O%20Targets%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




