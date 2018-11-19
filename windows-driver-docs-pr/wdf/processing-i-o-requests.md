---
title: Processing I/O Requests
description: Processing I/O Requests
ms.assetid: 90b1cc51-da40-45c1-9d6c-57f637f474d9
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

 

 





