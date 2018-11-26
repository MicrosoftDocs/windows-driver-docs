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


When a driver attempts to cancel an I/O request that it has forwarded to an I/O target, the driver must ensure that it passes a valid request handle to the [**WdfRequestCancelSentRequest**](https://msdn.microsoft.com/library/windows/hardware/ff549941) method. The request handle becomes invalid if the I/O target completes the request, because the driver's [*CompletionRoutine*](https://msdn.microsoft.com/library/windows/hardware/ff540745) callback function will call [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945) (which attempts to delete the request object).

To avoid this problem, the driver can keep track of the requests that it has sent to the I/O target by, for example, creating a [collection](framework-object-collections.md) of request objects. The driver can call [**WdfSpinLockAcquire**](https://msdn.microsoft.com/library/windows/hardware/ff550040) to synchronize access to the collection.

When the driver's [*CompletionRoutine*](https://msdn.microsoft.com/library/windows/hardware/ff540745) callback function is called, it acquires the lock, removes the completed request's handle from the collection, and calls [**WdfSpinLockRelease**](https://msdn.microsoft.com/library/windows/hardware/ff550044) to release the lock.

Before attempting to cancel a request that the driver has forwarded to an I/O target, the driver can:

1.  Call [**WdfSpinLockAcquire**](https://msdn.microsoft.com/library/windows/hardware/ff550040) to acquire a spin lock.

2.  Find the request object's handle in the collection, to ensure that driver's completion routine hasn't completed the request and removed the handle from the collection.

3.  Call [**WdfObjectReference**](https://msdn.microsoft.com/library/windows/hardware/ff548758) to increment the request object's reference count so that the object cannot be deleted.

4.  Call [**WdfSpinLockRelease**](https://msdn.microsoft.com/library/windows/hardware/ff550044) to release the spin lock.

5.  Call [**WdfRequestCancelSentRequest**](https://msdn.microsoft.com/library/windows/hardware/ff549941).

6.  Call [**WdfObjectDereference**](https://msdn.microsoft.com/library/windows/hardware/ff548739) to decrement the object's reference count.

This sequence ensures that if the I/O target completes the request before the driver calls [**WdfRequestCancelSentRequest**](https://msdn.microsoft.com/library/windows/hardware/ff549941), the request's handle is still valid (because of the incremented reference count) even if the driver's [*CompletionRoutine*](https://msdn.microsoft.com/library/windows/hardware/ff540745) callback function calls [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945).

 

 





