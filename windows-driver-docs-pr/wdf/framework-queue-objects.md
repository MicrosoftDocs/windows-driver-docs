---
title: Framework Queue Objects
description: Framework Queue Objects
ms.assetid: 42736e2d-2482-46b4-bf52-4efe369db40b
keywords:
- I/O requests WDK KMDF , queue objects
- I/O queues WDK KMDF
- queue objects WDK KMDF
- I/O queue objects WDK KMDF
- request processing WDK KMDF , queue objects
- queues WDK KMDF
- queues WDK KMDF , framework objects
- I/O queues WDK KMDF , about I/O queues
- callback functions WDK KMDF
- event callback functions WDK KMDF
- framework objects WDK KMDF , I/O queue objects
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Framework Queue Objects





Framework queue objects represent *I/O queues*, which are containers for the I/O requests that a driver receives. Each driver can create one or more I/O queues for each device. The framework queue object defines a set of [event callback functions](https://msdn.microsoft.com/library/windows/hardware/dn265647) that the driver can provide and a set of object methods that the driver can call.

When the framework receives an I/O request that is directed to one of the driver's devices, the framework places the request in the appropriate I/O queue. If your driver registers one or more [request handlers](request-handlers.md), the framework can notify your driver each time an I/O request is available. Alternatively, your driver can poll the I/O queue for requests.

This section includes:

[Creating I/O Queues](creating-i-o-queues.md)

[Deleting I/O Queues](deleting-i-o-queues.md)

[Managing I/O Queues](managing-i-o-queues.md)

[Using Power-Managed I/O Queues](using-power-managed-i-o-queues.md)

[Guaranteeing Forward Progress of I/O Operations](guaranteeing-forward-progress-of-i-o-operations.md)

[I/O Queue States](i-o-queue-states.md)

[Example Uses of I/O Queues](example-uses-of-i-o-queues.md)

 

 





