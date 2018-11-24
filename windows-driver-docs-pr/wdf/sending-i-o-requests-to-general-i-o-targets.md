---
title: Sending I/O Requests to General I/O Targets
description: Sending I/O Requests to General I/O Targets
ms.assetid: 3fa897f5-2de8-484b-becb-c2de23fb5e8c
keywords:
- general I/O targets WDK KMDF , sending I/O requests to
- sending I/O requests WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sending I/O Requests to General I/O Targets





Your driver can send I/O requests to general I/O targets either synchronously or asynchronously.

If a driver sends I/O requests synchronously, a driver thread sends the requests one at a time. The thread waits for each request to complete before it sends the next one. This process is simpler than sending the I/O requests asynchronously. Your driver can send I/O requests synchronously if it does not send many requests and if system or device performance is not reduced while your driver waits for each I/O request.

If a driver sends I/O requests asynchronously, a driver thread sends each request as soon as the request is ready to be sent, without waiting for previously sent requests to finish. If your driver must handle many I/O requests in short periods of time, you probably cannot allow your driver to wait for each request to complete before sending the next request. Otherwise, you might lose data or reduce the performance of your driver's devices and, possibly, of the entire system.

The framework's I/O target object provides two sets of methods that your driver can call: one set to [send I/O requests synchronously](sending-i-o-requests-synchronously.md) and the other set to [send I/O requests asynchronously](sending-i-o-requests-asynchronously.md).

For each of these methods, you must supply a request object and some buffer space. You can use these methods to forward a request that your driver received in one of its I/O queues or to create and send a new request.

 

 





