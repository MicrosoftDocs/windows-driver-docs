---
title: Porting I/O Queues
description: Porting I/O Queues
ms.date: 04/20/2017
---

# Porting I/O Queues


WDF drivers create queues and register I/O event callbacks in the [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback. By default, each I/O queue object is the child of a device object. The WDF driver can configure the following tasks for each queue:

-   Which I/O request types are directed to the queue.
-   Whether requests are dispatched in parallel (as soon as they arrive), sequentially (one at a time), or manually (upon driver request).
-   Whether I/O event callback routines are called concurrently or serially.
-   Whether the framework or the driver manages the queue through system and device power transitions.

For more information about creating queues, see [Creating I/O Queues](creating-i-o-queues.md)

 

