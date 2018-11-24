---
title: Porting I/O Queues
description: Porting I/O Queues
ms.assetid: 90319342-5FAB-451B-BCA1-B273B81418DB
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting I/O Queues


WDF drivers create queues and register I/O event callbacks in the [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback. By default, each I/O queue object is the child of a device object. The WDF driver can configure the following tasks for each queue:

-   Which I/O request types are directed to the queue.
-   Whether requests are dispatched in parallel (as soon as they arrive), sequentially (one at a time), or manually (upon driver request).
-   Whether I/O event callback routines are called concurrently or serially.
-   Whether the framework or the driver manages the queue through system and device power transitions.

For more information about creating queues, see [Creating I/O Queues](creating-i-o-queues.md)

 

 





