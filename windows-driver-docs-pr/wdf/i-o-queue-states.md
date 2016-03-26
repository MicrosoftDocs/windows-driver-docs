---
title: I/O Queue States
description: I/O Queue States
ms.assetid: 99519d1c-20e5-4a32-8462-19ec9f907506
keywords: ["I/O queues WDK KMDF , states", "states WDK I/O queue", "current I/O queue state WDK KMDF", "idle I/O queue state WDK KMDF", "ready I/O queue state WDK KMDF", "stopped I/O queue state WDK KMDF", "drained I/O queue state WDK KMDF", "purged I/O queue state WDK KMDF"]
---

# I/O Queue States


The framework defines the following states for I/O queues:

<a href="" id="idle"></a>*Idle*  
The I/O queue contains no I/O requests, and the driver is not processing any requests that it received from the I/O queue.

<a href="" id="ready"></a>*Ready*  
The I/O queue can receive I/O requests from the framework, and it can deliver I/O requests to the driver.

<a href="" id="stopped"></a>*Stopped*  
The I/O queue can receive I/O requests from the framework, but it cannot deliver I/O requests to the driver, and the driver is not processing any requests that it received from the I/O queue.

<a href="" id="drained"></a>*Drained*  
The I/O queue is empty, it cannot receive new I/O requests from the framework, and all I/O requests that were in the I/O queue have been delivered to the driver.

<a href="" id="purged"></a>*Purged*  
The I/O queue is empty, it cannot receive new I/O requests from the framework, and all I/O requests that were in the I/O queue have been canceled.

The framework can set a new I/O queue to the ready state after your driver calls [**WdfIoQueueCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547401). However, [power-managed I/O queues](using-power-managed-i-o-queues.md) enter the ready state only if the device is in its working (D0) state.

Your driver can change an I/O queue's state by:

-   Calling [**WdfIoQueueStop**](https://msdn.microsoft.com/library/windows/hardware/ff548482) or [**WdfIoQueueStopSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548489) to place the queue in its stopped state.

-   Calling [**WdfIoQueueDrain**](https://msdn.microsoft.com/library/windows/hardware/ff547406) or [**WdfIoQueueDrainSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff547412) to place the queue in its drained state.

-   Calling [**WdfIoQueuePurge**](https://msdn.microsoft.com/library/windows/hardware/ff548442) or [**WdfIoQueuePurgeSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548449) to place the queue in its purged state.

-   Calling [**WdfIoQueueStart**](https://msdn.microsoft.com/library/windows/hardware/ff548478) to return the queue to its ready state.

To obtain an I/O queue's current state, your driver can call [**WdfIoQueueGetState**](https://msdn.microsoft.com/library/windows/hardware/ff548437).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20I/O%20Queue%20States%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




