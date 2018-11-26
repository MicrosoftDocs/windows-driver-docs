---
title: Receiving I/O Requests
description: Receiving I/O Requests
ms.assetid: 0bd41b7b-d64e-4d02-ab5c-0188e926c8e1
keywords:
- I/O requests WDK KMDF , receiving
- receiving I/O requests WDK KMDF
- request processing WDK KMDF , receiving requests
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Receiving I/O Requests


If a framework-based driver is using the [sequential](dispatching-methods-for-i-o-requests.md#sequential-dispatching) or [parallel](dispatching-methods-for-i-o-requests.md#parallel-dispatching) dispatching method for an I/O queue, it receives I/O requests from the queue as input arguments to its [request handlers](request-handlers.md).

If a framework-based driver is using the [manual](dispatching-methods-for-i-o-requests.md#manual-dispatching) dispatching method for an I/O queue, it obtains I/O requests from the queue by polling the queue.

After the driver receives a request, it [owns](request-ownership.md) the request until it [requeues](requeuing-i-o-requests.md), [completes](completing-i-o-requests.md), [cancels](canceling-i-o-requests.md), or [forwards](forwarding-i-o-requests.md) the request.

 

 





