---
title: Configuring Dispatch Mode for an I/O Queue
description: Configuring Dispatch Mode for an I/O Queue
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: 7603c3fd-a4cb-4174-ad14-f57efedfe9de
keywords: ["synchronization WDK UMDF", "queue dispatch modes WDK UMDF", "dispatch modes WDK UMDF", "I/O queues WDK UMDF", "queues WDK UMDF", "sequential dispatch mode WDK UMDF", "parallel dispatch mode WDK UMDF", "manual dispatch mode WDK UMDF"]
---

# Configuring Dispatch Mode for an I/O Queue


\[This topic applies to UMDF 1.*x*.\]

When I/O requests from applications arrive, the framework places each request in the appropriate I/O queue. How and when the requests are delivered to the driver depend on how the driver configures dispatching for the I/O queue and on how the driver [specifies callback-function synchronization](specifying-a-callback-synchronization-mode.md). The I/O queue also interacts with the PnP and power management subsystem of UMDF to hold I/O requests in the queue until the device reaches the proper state.

**Note**   The dispatch mode for the I/O queue is not related to the [synchronization mode](specifying-a-callback-synchronization-mode.md). The I/O queue's dispatch configuration controls the number of requests that the driver can accept for processing at any given time, while synchronization controls the simultaneous execution of event callback functions that are presenting or canceling requests. However, several modes of operation are created by [combining dispatch and synchronization modes](combining-dispatch-and-synchronization-modes.md).

 

The driver configures dispatching for an I/O queue when the driver calls the [**IWDFDevice::CreateIoQueue**](https://msdn.microsoft.com/library/windows/hardware/ff557020) method to configure the default queue or to create a secondary queue. The driver can specify one of the values from the [**WDF\_IO\_QUEUE\_DISPATCH\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff552362) enumeration type in the *DispatchType* parameter of **IWDFDevice::CreateIoQueue** to identify the dispatch mode. An [I/O queue object](framework-i-o-queue-object.md) can support the following dispatch modes:

-   Sequential

    The sequential dispatch mode is specified using the **WdfIoQueueDispatchSequential** value. In this dispatch mode, a queue in the processing state raises events so that a driver only processes one request at a time. The queue defers any additional requests until the driver finishes processing its current request or calls the [**IWDFIoRequest::ForwardToIoQueue**](https://msdn.microsoft.com/library/windows/hardware/ff559081) method to requeue the request. When the current request completes or is forwarded, the queue raises an event to provide the next request.

-   Parallel

    The parallel dispatch mode is specified using the **WdfIoQueueDispatchParallel** value. In this dispatch mode, a queue in the processing state raises events as soon as I/O requests are ready for the driver. When the driver receives an I/O request, the driver can process the I/O request in one of the following ways:

    -   The driver calls either the [**IWDFIoRequest::Complete**](https://msdn.microsoft.com/library/windows/hardware/ff559070) or [**IWDFIoRequest::CompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff559074) method to complete the I/O request immediately. A driver completes the I/O request immediately if the I/O request is invalid, cannot ever be serviced, or can be completed by copying data from a buffer or cache that has the data.
    -   The driver calls the [**IWDFIoRequest::ForwardToIoQueue**](https://msdn.microsoft.com/library/windows/hardware/ff559081) method to requeue the I/O request.
    -   The driver calls the [**IWDFIoRequest::Send**](https://msdn.microsoft.com/library/windows/hardware/ff559149) method to pass the I/O request to a lower-level driver.
-   Manual

    The manual dispatch mode is specified using the **WdfIoQueueDispatchManual** value. In this dispatch mode, the I/O queue does not automatically notify the driver when requests arrive at the queue. The driver must call the [**IWDFIoQueue::RetrieveNextRequest**](https://msdn.microsoft.com/library/windows/hardware/ff558967) method to retrieve requests manually from the queue. This is a polling model.

    In UMDF versions 1.9 and later, if your driver is using the manual dispatch mode, it can call [**IWDFIoRequest2::Requeue**](https://msdn.microsoft.com/library/windows/hardware/ff559028) to return an I/O request to the head of the I/O queue from which the driver obtained it. After calling **IWDFIoRequest2::Requeue**, the driver's next call to [**IWDFIoQueue::RetrieveNextRequest**](https://msdn.microsoft.com/library/windows/hardware/ff558967) retrieves the requeued request.

For all dispatch modes, the [I/O queue object](framework-i-o-queue-object.md) receives and tracks the request until the driver handles the request or the request is canceled.

If the driver configures the queue for serial or parallel dispatching, the framework notifies the driver of a request through the callback functions that are registered by the driver when the driver creates the queue or configures the default queue. For more information, see [I/O Queue Event Callback Functions](i-o-queue-event-callback-functions.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Configuring%20Dispatch%20Mode%20for%20an%20I/O%20Queue%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




