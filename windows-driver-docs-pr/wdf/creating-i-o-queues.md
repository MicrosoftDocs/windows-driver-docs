---
title: Creating I/O Queues
description: Creating I/O Queues
ms.assetid: 03b09c94-6b72-4234-b21f-203f93b7a2e8
keywords:
- I/O queues WDK KMDF , creating
- I/O queues WDK KMDF , default
- default I/O queues WDK KMDF
- creating I/O queues WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating I/O Queues





Most drivers create I/O queues in their [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function. To create an I/O queue for a device, the driver calls the framework queue object's [**WdfIoQueueCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547401) method (which creates a framework queue object). The driver supplies a [**WDF\_IO\_QUEUE\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552359) structure to the method. This structure contains configuration information about the queue, such as the queue's [dispatching method](dispatching-methods-for-i-o-requests.md) and pointers to [request handlers](request-handlers.md) that the framework calls when requests are available in the queue. The structure also indicates whether the queue will be [power-managed](using-power-managed-i-o-queues.md) and whether the driver supports zero-length buffers for the queue's I/O requests.

If the driver sets the **DefaultQueue** member of the [**WDF\_IO\_QUEUE\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552359) structure to **TRUE**, the queue becomes the device's *default I/O queue*. If your driver creates a default I/O queue, the framework places all of the device's I/O requests in this queue, unless you create additional queues to receive some of the requests. A driver can obtain a handle to a device's default I/O queue by calling the [**WdfDeviceGetDefaultQueue**](https://msdn.microsoft.com/library/windows/hardware/ff545965) method.

If you want to use more than one I/O queue for a device, the driver can call [**WdfIoQueueCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547401) to create as many queue objects as you need. If a driver creates multiple queues, it can call [**WdfDeviceConfigureRequestDispatching**](https://msdn.microsoft.com/library/windows/hardware/ff545920), which instructs the framework to direct different types of requests to different queues. For example, you can specify that all read requests will be delivered to one queue and all write requests will be delivered to another queue.

If your driver creates a set of I/O queues and calls [**WdfDeviceConfigureRequestDispatching**](https://msdn.microsoft.com/library/windows/hardware/ff545920) to direct each type of request that your driver can receive to a specific queue, the driver does not need a default queue.

If a driver does not provide an I/O queue for requests of a particular type, and if your driver is a function driver, the framework completes requests of that type with a completion status value of STATUS\_INVALID\_DEVICE\_REQUEST. If your driver is a filter driver and has called [**WdfFdoInitSetFilter**](https://msdn.microsoft.com/library/windows/hardware/ff547273), the framework automatically forwards these requests to the next-lower driver in the driver stack. Thus, for example, a filter driver that does not process read requests does not have to provide an I/O queue that receives read requests.

For examples of how drivers can use I/O queues, see [Example Uses of I/O Queues](example-uses-of-i-o-queues.md).

 

 





