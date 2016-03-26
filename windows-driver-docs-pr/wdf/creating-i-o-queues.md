---
title: Creating I/O Queues
description: Creating I/O Queues
ms.assetid: 03b09c94-6b72-4234-b21f-203f93b7a2e8
keywords: ["I/O queues WDK KMDF , creating", "I/O queues WDK KMDF , default", "default I/O queues WDK KMDF", "creating I/O queues WDK KMDF"]
---

# Creating I/O Queues


## <a href="" id="ddk-creating-an-i-o-queue-df"></a>


Most drivers create I/O queues in their [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function. To create an I/O queue for a device, the driver calls the framework queue object's [**WdfIoQueueCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547401) method (which creates a framework queue object). The driver supplies a [**WDF\_IO\_QUEUE\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552359) structure to the method. This structure contains configuration information about the queue, such as the queue's [dispatching method](dispatching-methods-for-i-o-requests.md) and pointers to [request handlers](request-handlers.md) that the framework calls when requests are available in the queue. The structure also indicates whether the queue will be [power-managed](using-power-managed-i-o-queues.md) and whether the driver supports zero-length buffers for the queue's I/O requests.

If the driver sets the **DefaultQueue** member of the [**WDF\_IO\_QUEUE\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552359) structure to **TRUE**, the queue becomes the device's *default I/O queue*. If your driver creates a default I/O queue, the framework places all of the device's I/O requests in this queue, unless you create additional queues to receive some of the requests. A driver can obtain a handle to a device's default I/O queue by calling the [**WdfDeviceGetDefaultQueue**](https://msdn.microsoft.com/library/windows/hardware/ff545965) method.

If you want to use more than one I/O queue for a device, the driver can call [**WdfIoQueueCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547401) to create as many queue objects as you need. If a driver creates multiple queues, it can call [**WdfDeviceConfigureRequestDispatching**](https://msdn.microsoft.com/library/windows/hardware/ff545920), which instructs the framework to direct different types of requests to different queues. For example, you can specify that all read requests will be delivered to one queue and all write requests will be delivered to another queue.

If your driver creates a set of I/O queues and calls [**WdfDeviceConfigureRequestDispatching**](https://msdn.microsoft.com/library/windows/hardware/ff545920) to direct each type of request that your driver can receive to a specific queue, the driver does not need a default queue.

If a driver does not provide an I/O queue for requests of a particular type, and if your driver is a function driver, the framework completes requests of that type with a completion status value of STATUS\_INVALID\_DEVICE\_REQUEST. If your driver is a filter driver and has called [**WdfFdoInitSetFilter**](https://msdn.microsoft.com/library/windows/hardware/ff547273), the framework automatically forwards these requests to the next-lower driver in the driver stack. Thus, for example, a filter driver that does not process read requests does not have to provide an I/O queue that receives read requests.

For examples of how drivers can use I/O queues, see [Example Uses of I/O Queues](example-uses-of-i-o-queues.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Creating%20I/O%20Queues%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




