---
title: Synchronizing IRP Cancellation
author: windows-driver-content
description: Synchronizing IRP Cancellation
MS-HAID:
- 'IRPs\_2f3a8c50-8b9f-48fe-8f40-9cead67f9585.xml'
- 'kernel.synchronizing\_irp\_cancellation'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a110c6ad-794d-4b8a-a89d-bceb08ea82b8
keywords: ["canceling IRPs, synchronization", "Cancel routines, synchronization", "synchronization WDK IRPs", "cancelable IRPs WDK kernel"]
---

# Synchronizing IRP Cancellation


## <a href="" id="ddk-synchronizing-irp-cancellation-kg"></a>


From a driver's perspective, an IRP can be canceled at any time. IRP cancellation occurs asynchronously; therefore, drivers must be able to handle a number of potential race conditions, created if the IRP is canceled at any of the following points:

-   After a driver routine is called, but before it queues an IRP.

-   After a driver routine is called, but before it tries to process an IRP. For example, an IRP might be canceled after a driver's [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine is called, but before the *StartIo* routine removes the IRP from the device queue.

-   After the driver routine dequeues the IRP, but before it starts the requested I/O.

Note that after a driver queues an IRP and releases any spin locks that protect the queue, another thread can access and change the IRP. When the original thread resumes—even as soon as the next line of code—the IRP might have already been canceled or otherwise changed.

Driver can use the cancel-safe IRP queue framework to implement IRP queuing. The system then registers a [*Cancel*](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine for the driver that automatically handles synchronization to safely cancel IRPs. See [Cancel-Safe IRP Queues](cancel-safe-irp-queues.md) for more information. Otherwise, drivers must implement their own synchronization.

The following members of an IRP contain information about cancellation:

-   **Irp-&gt;Cancel** indicates whether an IRP is being canceled or should be canceled.

-   **Irp-&gt;CancelRoutine** indicates whether an IRP is cancelable. If this member contains a pointer to a cancel routine, then the IRP is cancelable. If this member is **NULL**, then the IRP is not cancelable. If this member is **NULL**, but **Irp-&gt;Cancel** is set, that indicates that the cancel routine is running and the IRP is in the process of being canceled.

If a driver handles cancelable IRPs, it is responsible for setting the appropriate *Cancel* routine in each IRP that it holds in a cancelable state.

This section includes the following topics on synchronizing IRP cancellation.

[Using the System's Cancel Spin Lock](using-the-system-s-cancel-spin-lock.md)

[Synchronizing Cancellation in Driver Routines that Process IRPs](synchronizing-cancellation-in-driver-routines-that-process-irps.md)

[Synchronizing Cancellation in Higher-Level Drivers without Cancel Routines](synchronizing-cancellation-in-higher-level-drivers-without-cancel-rout.md)

[Using a Driver-Supplied Spin Lock](using-a-driver-supplied-spin-lock.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Synchronizing%20IRP%20Cancellation%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


