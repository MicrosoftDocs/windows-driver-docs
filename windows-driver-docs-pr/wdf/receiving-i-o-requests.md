---
title: Receiving I/O Requests
author: windows-driver-content
description: Receiving I/O Requests
ms.assetid: 0bd41b7b-d64e-4d02-ab5c-0188e926c8e1
keywords: ["I/O requests WDK KMDF , receiving", "receiving I/O requests WDK KMDF", "request processing WDK KMDF , receiving requests"]
---

# Receiving I/O Requests


If a framework-based driver is using the [sequential](dispatching-methods-for-i-o-requests.md#sequential-dispatching) or [parallel](dispatching-methods-for-i-o-requests.md#parallel-dispatching) dispatching method for an I/O queue, it receives I/O requests from the queue as input arguments to its [request handlers](request-handlers.md).

If a framework-based driver is using the [manual](dispatching-methods-for-i-o-requests.md#manual-dispatching) dispatching method for an I/O queue, it obtains I/O requests from the queue by polling the queue.

After the driver receives a request, it [owns](request-ownership.md) the request until it [requeues](requeuing-i-o-requests.md), [completes](completing-i-o-requests.md), [cancels](canceling-i-o-requests.md), or [forwards](forwarding-i-o-requests.md) the request.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Receiving%20I/O%20Requests%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




