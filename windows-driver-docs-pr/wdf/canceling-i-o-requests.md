---
title: Canceling I/O Requests
description: Canceling I/O Requests
keywords:
- request processing WDK KMDF , canceling requests
- I/O requests WDK KMDF , canceling
- canceling I/O requests WDK KMDF
- undelivered I/O requests WDK KMDF
- forwarding I/O requests WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Canceling I/O Requests





A device's in-progress I/O operation (such as a request to read several blocks from a disk) can be canceled by an application, the system, or a driver. If a device's I/O operation is canceled, the I/O manager attempts to cancel all unprocessed I/O requests that are associated with the I/O operation. The device's drivers can register to be notified when the I/O manager attempts to cancel I/O requests, and the drivers can cancel the requests that they own by [completing](completing-i-o-requests.md) them with a completion status of STATUS\_CANCELLED.

The framework handles some of the cancellation work for framework-based drivers. If a device's I/O operation is canceled, the framework completes the following I/O requests (with a completion status of STATUS\_CANCELLED) that are associated with the canceled operation:

-   Undelivered I/O requests that the framework has placed in the driver's default I/O queue.

-   Undelivered I/O requests that the framework has forwarded to another queue because the driver called [**WdfDeviceConfigureRequestDispatching**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceconfigurerequestdispatching).

Because the framework cancels these requests, it does not deliver them to the driver.

After the framework has delivered an I/O request to the driver, the driver [owns](request-ownership.md) the request and the framework cannot cancel it. At this point, only the driver can cancel the I/O request, but the framework must notify the driver that a request should be canceled. Drivers receive this notification by providing an [*EvtRequestCancel*](/windows-hardware/drivers/ddi/wdfrequest/nc-wdfrequest-evt_wdf_request_cancel) callback function.

Sometimes a driver receives an I/O request from an I/O queue but, instead of processing the request, the driver requeues the request to the same or another I/O queue for later processing. Examples of this situation include the following:

-   The framework delivers an I/O request to one of the driver's [request handlers](request-handlers.md), and the driver subsequently calls either [**WdfRequestForwardToIoQueue**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestforwardtoioqueue) (or [**WdfRequestForwardToParentDeviceIoQueue**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestforwardtoparentdeviceioqueue)) to place the request in a different queue or [**WdfRequestRequeue**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestrequeue) to place the request back into the same queue.

-   The framework delivers an I/O request to the driver's [*EvtIoInCallerContext*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_io_in_caller_context) callback function, the driver calls [**WdfDeviceEnqueueRequest**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceenqueuerequest) to pass the request back to the framework, and the framework subsequently places the request in one of the driver's I/O queues.

In these cases, the framework can cancel the I/O request because the request is in an I/O queue. However, if the driver has registered an [*EvtIoCanceledOnQueue*](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_canceled_on_queue) callback function for the I/O queue in which the request resides, the framework calls the callback function, instead of canceling the request, when the associated I/O operation is being canceled. If the framework calls the driver's *EvtIoCanceledOnQueue* callback function, the driver must [complete](completing-i-o-requests.md) the request.

In summary, when an I/O operation is canceled, the framework always cancels all associated I/O requests that were never delivered to the driver. If the driver receives a request and then requeues it, the framework will cancel the request (if the request is in the queue) unless the driver provides an [*EvtIoCanceledOnQueue*](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_canceled_on_queue) callback function for the I/O queue.

### Calling WdfRequestMarkCancelable or WdfRequestMarkCancelableEx

A driver can call [**WdfRequestMarkCancelable**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelable) or [**WdfRequestMarkCancelableEx**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelableex) to register an [*EvtRequestCancel*](/windows-hardware/drivers/ddi/wdfrequest/nc-wdfrequest-evt_wdf_request_cancel) callback function. If the driver has called **WdfRequestMarkCancelable** or **WdfRequestMarkCancelableEx**, and if the I/O operation associated with the request is canceled, the framework calls the driver's *EvtRequestCancel* callback function so the driver can cancel the I/O request.

A driver should call [**WdfRequestMarkCancelable**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelable) or [**WdfRequestMarkCancelableEx**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelableex) if it will own a request for a relatively long time. For example, a driver might have to wait for a device to respond, or it might wait for lower drivers to complete a set of requests that the driver created when it received a single request.

If a driver does not call [**WdfRequestMarkCancelable**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelable) or [**WdfRequestMarkCancelableEx**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelableex), or if a driver calls [**WdfRequestUnmarkCancelable**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestunmarkcancelable) after calling **WdfRequestMarkCancelable** or **WdfRequestMarkCancelableEx**, the driver is not aware of the cancellation and therefore handles the request as it normally would.

### Calling WdfRequestIsCanceled

If a driver has not called [**WdfRequestMarkCancelable**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelable) or [**WdfRequestMarkCancelableEx**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelableex) to register an [*EvtRequestCancel*](/windows-hardware/drivers/ddi/wdfrequest/nc-wdfrequest-evt_wdf_request_cancel) callback function, it can call [**WdfRequestIsCanceled**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestiscanceled) to determine if the I/O manager has attempted to cancel an I/O request. If **WdfRequestIsCanceled** returns **TRUE** and the driver owns the request, the driver should cancel the request. If the driver does not own the request, it should not call **WdfRequestIsCanceled**.

A driver that has not called [**WdfRequestMarkCancelable**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelable) or [**WdfRequestMarkCancelableEx**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelableex) might call [**WdfRequestIsCanceled**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestiscanceled) in the following circumstances:

-   A driver that waits for device interrupts might call [**WdfRequestIsCanceled**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestiscanceled) from its [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) callback function.

-   A driver that polls its device might call [**WdfRequestIsCanceled**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestiscanceled) from it polling thread.

-   A driver that breaks a [DMA transaction](dma-transactions-and-dma-transfers.md) into several smaller transfers might call [**WdfRequestIsCanceled**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestiscanceled) after each transfer is finished.

-   A driver that receives a large read or write request that it breaks into several smaller requests might call [**WdfRequestIsCanceled**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestiscanceled) after the driver's I/O target completes each of the smaller requests, if the driver has not called [**WdfRequestMarkCancelable**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelable) or [**WdfRequestMarkCancelableEx**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelableex) for the received request.

### Canceling the Request

Canceling an I/O request might involve any of the following:

-   Stopping an in-progress I/O operation.

-   Not forwarding the request to an I/O target.

-   Calling [**WdfRequestCancelSentRequest**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcancelsentrequest) to attempt to cancel a request that the driver had previously submitted to an I/O target.

If a driver is canceling an I/O request for a request object that the driver received from the framework, the driver must always complete the request by calling [**WdfRequestComplete**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcomplete), [**WdfRequestCompleteWithInformation**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcompletewithinformation), or [**WdfRequestCompleteWithPriorityBoost**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcompletewithpriorityboost), with a *Status* parameter of STATUS\_CANCELLED. (If the driver called [**WdfRequestCreate**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcreate) to create a request object, the driver calls [**WdfObjectDelete**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete) instead of completing the request.)

### Synchronizing Cancellation

For information about synchronizing code that cancels I/O requests, see:

-   [Synchronizing Cancel and Completion Code](synchronizing-cancel-and-completion-code.md)

-   [Synchronizing Cancellation of Sent Requests](synchronizing-cancellation-of-sent-requests.md)

 

