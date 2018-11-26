---
title: Canceling I/O Requests in UMDF
description: Canceling I/O Requests in UMDF
ms.assetid: 4f69903b-00ef-4b47-a564-aaa7d076481b
keywords:
- I/O requests WDK UMDF , canceling
- request processing WDK UMDF , canceling requests
- canceling I/O requests WDK UMDF
- in-flight requests WDK UMDF
- I/O requests WDK UMDF , states
- request processing WDK UMDF , states
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Canceling I/O Requests in UMDF


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

A device's in-progress I/O operation (such as a request to read several blocks from a disk) can be canceled by an application, the system, or a driver. If a device's I/O operation is canceled, the I/O Manager attempts to cancel all unprocessed I/O requests that are associated with the I/O operation. The device's drivers can register to be notified when the I/O Manager attempts to cancel I/O requests, and the drivers can cancel the requests that they own by [completing](completing-i-o-requests.md) them with a completion status of HRESULT\_FROM\_WIN32(ERROR\_OPERATION\_ABORTED).

The framework handles some of the cancellation work for framework-based drivers. If a device's I/O operation is canceled, the framework completes--with a completion status of HRESULT\_FROM\_WIN32(ERROR\_OPERATION\_ABORTED)--the following I/O requests that are associated with the canceled operation:

-   Undelivered I/O requests that the framework has placed in the driver's default I/O queue.

-   Undelivered I/O requests that the framework has forwarded to another queue because the driver called [**IWDFIoQueue::ConfigureRequestDispatching**](https://msdn.microsoft.com/library/windows/hardware/ff558946).

Because the framework cancels these requests, it does not deliver them to the driver.

After the framework has delivered an I/O request to the driver, the driver owns the request and the framework cannot cancel it. At this point, only the driver can cancel the I/O request, but the framework must notify the driver that a request should be canceled. Drivers receive this notification by providing an [**IRequestCallbackCancel::OnCancel**](https://msdn.microsoft.com/library/windows/hardware/ff556903) callback function.

Sometimes a driver receives an I/O request from an I/O queue but, instead of processing the request, the driver requeues the request to the same or another I/O queue for later processing. For example, the framework might deliver an I/O request to one of the driver's request handlers, and the driver might subsequently call either [**IWDFIoRequest::ForwardToIoQueue**](https://msdn.microsoft.com/library/windows/hardware/ff559081) to place the request in a different queue or [**IWDFIoRequest2::Requeue**](https://msdn.microsoft.com/library/windows/hardware/ff559028) to place the request back into the same queue.

In these cases, the framework can cancel the I/O request because the request is in an I/O queue. However, if the driver has registered an callback function for the I/O queue in which the request resides, the framework calls the callback function, instead of canceling the request, when the associated I/O operation is being canceled. If the framework calls the driver's callback function, the driver must cancel the request.

In summary, when an I/O operation is canceled, the framework always cancels all associated I/O requests that were never delivered to the driver. If the driver receives a request and then requeues it, the framework will cancel the request (if the request is in the queue) unless the driver provides an callback function for the I/O queue.

### Calling MarkCancelable

A driver can call [**IWDFIoRequest::MarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff559146) to register an [**IRequestCallbackCancel::OnCancel**](https://msdn.microsoft.com/library/windows/hardware/ff556903) callback function. If the driver has called **MarkCancelable**, and if the I/O operation associated with the request is canceled, the framework calls the driver's **OnCancel** callback function so that the driver can cancel the I/O request.

A driver should call **MarkCancelable** if it will own a request for a relatively long time. For example, a driver might have to wait for a device to respond, or it might have to wait for lower drivers to complete a set of requests that the driver created when it received a single request.

If a driver does not call **MarkCancelable**, or if a driver calls [**IWDFIoRequest::UnmarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff559163) after calling **MarkCancelable**, the driver is not aware of the cancellation and therefore handles the request as it typically would.

### Calling IsCanceled

If a driver has not called **MarkCancelable** to register an **OnCancel** callback function, it can call [**IWDFIoRequest2::IsCanceled**](https://msdn.microsoft.com/library/windows/hardware/ff559018) to determine if the I/O Manager has attempted to cancel an I/O request. If **IsCanceled** returns **TRUE**, the driver should cancel the request.

For example, a driver that receives a large read or write request that it breaks into several smaller requests might call **IsCanceled** after the driver's I/O target completes each of the smaller requests, if the driver has not called **MarkCancelable** for the received request.

### Canceling the Request

Canceling an I/O request might involve any of the following:

-   Stopping an in-progress I/O operation.

-   Not forwarding the request to an I/O target.

-   Calling [**IWDFIoRequest::CancelSentRequest**](https://msdn.microsoft.com/library/windows/hardware/ff559067) to attempt to cancel a request that the driver had previously submitted to an I/O target.

If a driver is canceling an I/O request for a request object that the driver received from the framework, the driver must always complete the request by calling [**IWDFIoRequest::Complete**](https://msdn.microsoft.com/library/windows/hardware/ff559070) or [**IWDFIoRequest::CompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff559074), with a *CompletionStatus* parameter of HRESULT\_FROM\_WIN32(ERROR\_OPERATION\_ABORTED). (If the driver called [**IWDFDevice::CreateRequest**](https://msdn.microsoft.com/library/windows/hardware/ff557021) to create a request object, the driver calls [**IWDFObject::DeleteWdfObject**](https://msdn.microsoft.com/library/windows/hardware/ff560210) instead of completing the request.)

 

 





