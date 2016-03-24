---
title: Request Ownership
description: Request Ownership
ms.assetid: 60494e97-0483-454f-aafc-7a69019c95f2
keywords: ["request objects WDK KMDF , ownership", "ownership WDK KMDF , I/O requests"]
---

# Request Ownership


When the I/O manager sends an I/O request to a framework-based driver, the framework intercepts the request and creates a framework request object. The framework "owns" the request object, because only the framework can access the request and perform operations on the object.

After the framework creates a request object, it places the object in one of the driver's I/O queues. The framework continues to own the request object until it removes the request from the queue and delivers it to the driver.

After the driver [receives](receiving-i-o-requests.md) the request object, it owns the request. The driver can access the request object through a handle and perform operations on the object. While the driver owns the request object it can [requeue](requeuing-i-o-requests.md), [complete](completing-i-o-requests.md), [cancel](canceling-i-o-requests.md), or [forward](forwarding-i-o-requests.md) the request, after which it no longer owns the request object and cannot access it.

As ownership of a request object passes between a driver and the framework, the object handle's value does not change. For example, if a driver receives a request from an I/O queue, requeues it to a different queue, and then receives the request again, the handle's value will not change. Likewise, if a driver forwards a request to an I/O target and later receives notification that the I/O target completed the request, the driver's notification callback function receives the same handle value that the driver supplied to the I/O target.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Request%20Ownership%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




