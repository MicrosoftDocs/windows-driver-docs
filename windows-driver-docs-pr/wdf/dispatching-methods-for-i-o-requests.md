---
title: Dispatching Methods for I/O Requests
description: Dispatching Methods for I/O Requests
ms.assetid: 3e91aa7c-bccf-4eeb-8b68-b1277a690f8c
keywords:
- I/O queues WDK KMDF , creating
- I/O queues WDK KMDF , dispatching methods
- dispatching methods WDK KMDF
- sequential dispatching WDK KMDF
- synchronous dispatching WDK KMDF
- parallel dispatching WDK KMDF
- asynchronous dispatching WDK KMDF
- manual dispatching WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Dispatching Methods for I/O Requests





When a driver calls [**WdfIoQueueCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547401) to create an I/O queue, it specifies a dispatching method for the queue. The framework provides three dispatching methods: [sequential](#sequential-dispatching), [parallel](#parallel-dispatching), and [manual](#manual-dispatching). The driver can specify any of these dispatching methods for any I/O queue, including a device's [default I/O queue](creating-i-o-queues.md).

The driver sets a queue's dispatching method by specifying a [**WDF\_IO\_QUEUE\_DISPATCH\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff552362)-typed value in the queue's [**WDF\_IO\_QUEUE\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552359) structure.

For example uses of each dispatching method, see [Example Uses of I/O Queues](example-uses-of-i-o-queues.md).

### <a href="" id="sequential-dispatching"></a> Sequential Dispatching

If your driver or device can process only one I/O request from a queue at a time, you should set up the device's I/O queues to use *sequential dispatching*, which is also called *synchronous dispatching*. With this type of dispatching, the framework delivers requests to the driver one at a time. The framework does not deliver the next request until the driver [completes](completing-i-o-requests.md), [cancels](canceling-i-o-requests.md), or [requeues](requeuing-i-o-requests.md) the previous request.

After the framework delivers a request to one of the driver's [request handlers](request-handlers.md), the driver [processes the request](processing-i-o-requests.md). If the driver forwards the request to a [general I/O target](general-i-o-targets.md), it typically calls one of the I/O target object's synchronous methods. For more information about these methods, see [Sending I/O Requests Synchronously](sending-i-o-requests-synchronously.md). The driver must eventually [complete](completing-i-o-requests.md) or [cancel](canceling-i-o-requests.md) every request that it receives from an I/O queue.

A driver that has set up an I/O queue for sequential dispatching can call [**WdfIoQueueRetrieveNextRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548462) or [**WdfIoQueueRetrieveRequestByFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff548470) to obtain another request from the queue before the last received request has been completed or canceled. You might want to do this in a function driver, so that the driver can start the next hardware operation while the driver's [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback function is still processing data from the previous hardware operation.

If you create several I/O queues and set them all up for sequential dispatching, the framework dispatches requests from each queue sequentially, but the queues run in parallel. If your driver or device can process only one request at a time of any type, you must use a single I/O queue with an [*EvtIoDefault*](https://msdn.microsoft.com/library/windows/hardware/ff541757) callback function.

### <a href="" id="parallel-dispatching"></a> Parallel Dispatching

If your driver and device can process multiple I/O requests simultaneously, you can set up the device's I/O queues to use *parallel dispatching* so that the driver can process the requests asynchronously. This dispatching method is also called *asynchronous dispatching*.

If a driver sets up an I/O queue to use parallel dispatching, the framework delivers I/O requests to the driver as soon as they are available in the queue. The result is that the driver might have to process several requests at once.

Each time one of the driver's [request handlers](request-handlers.md) receives a request, the driver must [process the request](processing-i-o-requests.md) and then [complete](completing-i-o-requests.md) the request. If the driver forwards the request to a [general I/O target](general-i-o-targets.md), it typically calls one of the I/O target object's asynchronous methods. For more information about these methods, see [Sending I/O Requests Asynchronously](sending-i-o-requests-asynchronously.md). The driver must eventually [complete](completing-i-o-requests.md) or [cancel](canceling-i-o-requests.md) every request that it receives from an I/O queue.

A driver that uses parallel dispatching can call [**WdfIoQueueStop**](https://msdn.microsoft.com/library/windows/hardware/ff548482) or [**WdfIoQueueStopSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548489) to temporarily stop a queue, and then call [**WdfIoQueueStart**](https://msdn.microsoft.com/library/windows/hardware/ff548478) to restart the queue.

### <a href="" id="manual-dispatching"></a> Manual Dispatching

If you want your driver to have complete control over the delivery of I/O requests, you can set up a device's I/O queue to use *manual dispatching*, which means that the framework does not deliver requests to the driver unless the driver explicitly asks for one.

To obtain a request from a manual queue, the driver can call [**WdfIoQueueRetrieveNextRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548462) or [**WdfIoQueueRetrieveRequestByFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff548470) in a loop that polls the queue. Alternatively, the driver can call [**WdfIoQueueReadyNotify**](https://msdn.microsoft.com/library/windows/hardware/ff548452) to register a callback function that the framework will call when one or more requests are available in the queue. After the framework calls the callback function, the driver can call **WdfIoQueueRetrieveNextRequest** or **WdfIoQueueRetrieveRequestByFileObject** in a loop to retrieve the requests.

After the driver obtains a request from the queue, it must [process the request](processing-i-o-requests.md). The driver must eventually [complete](completing-i-o-requests.md) or [cancel](canceling-i-o-requests.md) each request.

 

 





