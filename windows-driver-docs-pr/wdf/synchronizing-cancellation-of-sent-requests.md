---
title: Synchronizing Cancellation of Sent Requests
author: windows-driver-content
description: Synchronizing Cancellation of Sent Requests
ms.assetid: e7ec65c9-bc7b-46ea-853d-3e23b1763666
keywords: ["request processing WDK KMDF , canceling requests", "I/O requests WDK KMDF , canceling", "synchronization WDK KMDF", "request processing WDK KMDF , synchronization", "I/O requests WDK KMDF , synchronization", "sent request cancellations WDK KMDF"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Synchronizing%20Cancellation%20of%20Sent%20Requests%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




