---
title: Synchronizing Cancellation of Sent Requests
description: Synchronizing Cancellation of Sent Requests
ms.assetid: e7ec65c9-bc7b-46ea-853d-3e23b1763666
keywords:
- request processing WDK KMDF , canceling requests
- I/O requests WDK KMDF , canceling
- synchronization WDK KMDF
- request processing WDK KMDF , synchronization
- I/O requests WDK KMDF , synchronization
- sent request cancellations WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Synchronizing Cancellation of Sent Requests


When a driver attempts to cancel an I/O request that it has forwarded to an I/O target, the driver must ensure that it passes a valid request handle to the [**WdfRequestCancelSentRequest**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestcancelsentrequest) method. The request handle becomes invalid if the I/O target completes the request, because the driver's [*CompletionRoutine*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nc-wdfrequest-evt_wdf_request_completion_routine) callback function will call [**WdfRequestComplete**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestcomplete) (which attempts to delete the request object).

To avoid this problem, the driver can keep track of the requests that it has sent to the I/O target by, for example, creating a [collection](framework-object-collections.md) of request objects. The driver can call [**WdfSpinLockAcquire**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff550040(v=vs.85)) to synchronize access to the collection.

When the driver's [*CompletionRoutine*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nc-wdfrequest-evt_wdf_request_completion_routine) callback function is called, it acquires the lock, removes the completed request's handle from the collection, and calls [**WdfSpinLockRelease**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff550044(v=vs.85)) to release the lock.

Before attempting to cancel a request that the driver has forwarded to an I/O target, the driver can:

1.  Call [**WdfSpinLockAcquire**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff550040(v=vs.85)) to acquire a spin lock.

2.  Find the request object's handle in the collection, to ensure that driver's completion routine hasn't completed the request and removed the handle from the collection.

3.  Call [**WdfObjectReference**](https://docs.microsoft.com/windows-hardware/drivers/wdf/wdfobjectreference) to increment the request object's reference count so that the object cannot be deleted.

4.  Call [**WdfSpinLockRelease**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff550044(v=vs.85)) to release the spin lock.

5.  Call [**WdfRequestCancelSentRequest**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestcancelsentrequest).

6.  Call [**WdfObjectDereference**](https://docs.microsoft.com/windows-hardware/drivers/wdf/wdfobjectdereference) to decrement the object's reference count.

This sequence ensures that if the I/O target completes the request before the driver calls [**WdfRequestCancelSentRequest**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestcancelsentrequest), the request's handle is still valid (because of the incremented reference count) even if the driver's [*CompletionRoutine*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nc-wdfrequest-evt_wdf_request_completion_routine) callback function calls [**WdfRequestComplete**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestcomplete).

 

 





