---
title: Processing I/O Requests
description: Learn about processing I/O requests. For example, when a driver receives an I/O request it can requeue, complete, or cancel a request.
keywords:
- I/O requests WDK KMDF , processing
- request objects WDK KMDF , processing I/O requests
- request processing WDK KMDF , options
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Processing I/O Requests





When a driver [receives](receiving-i-o-requests.md) an I/O request, it can:

-   [Requeue](requeuing-i-o-requests.md) the request to a different queue.

-   [Complete](completing-i-o-requests.md) the request.

-   [Cancel](canceling-i-o-requests.md) the request.

-   [Forward](forwarding-i-o-requests.md) the request to an I/O target.

The driver cannot ignore or delete the request.

 

 





