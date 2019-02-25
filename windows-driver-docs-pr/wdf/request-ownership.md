---
title: Request Ownership
description: Request Ownership
ms.assetid: 60494e97-0483-454f-aafc-7a69019c95f2
keywords:
- request objects WDK KMDF , ownership
- ownership WDK KMDF , I/O requests
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Request Ownership


When the I/O manager sends an I/O request to a framework-based driver, the framework intercepts the request and creates a framework request object. The framework "owns" the request object, because only the framework can access the request and perform operations on the object.

After the framework creates a request object, it places the object in one of the driver's I/O queues. The framework continues to own the request object until it removes the request from the queue and delivers it to the driver.

After the driver [receives](receiving-i-o-requests.md) the request object, it owns the request. The driver can access the request object through a handle and perform operations on the object. While the driver owns the request object it can [requeue](requeuing-i-o-requests.md), [complete](completing-i-o-requests.md), [cancel](canceling-i-o-requests.md), or [forward](forwarding-i-o-requests.md) the request, after which it no longer owns the request object and cannot access it.

As ownership of a request object passes between a driver and the framework, the object handle's value does not change. For example, if a driver receives a request from an I/O queue, requeues it to a different queue, and then receives the request again, the handle's value will not change. Likewise, if a driver forwards a request to an I/O target and later receives notification that the I/O target completed the request, the driver's notification callback function receives the same handle value that the driver supplied to the I/O target.

 

 





