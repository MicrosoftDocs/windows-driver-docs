---
title: Using a Driver-Supplied Spin Lock
description: Using a Driver-Supplied Spin Lock
ms.assetid: e81d5c93-47d6-407c-80a2-b2d55f9eb717
keywords: ["spin locks WDK kernel", "driver-supplied spin locks WDK kernel", "global cancel spin locks WDK kernel"]
ms.date: 05/09/2018
ms.localizationpriority: medium
---

# Using a Driver-Supplied Spin Lock





Drivers that manage their own queues of IRPs can use a driver-supplied spin lock, instead of the system cancel spin lock, to synchronize access to the queues. You can improve performance by avoiding use of the cancel spin lock except when absolutely necessary. Because the system has only one cancel spin lock, a driver might sometimes have to wait for that spin lock to become available. Using a driver-supplied spin lock eliminates this potential delay and makes the cancel spin lock available for the I/O manager and other drivers. Although the system still acquires the cancel spin lock when it calls the driver's [*Cancel*](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine, a driver can use its own spin lock to protect its queue of IRPs.

Even if a driver does not queue pending IRPs, but retains ownership in some other way, that driver must set a *Cancel* routine for the IRP and must use a spin lock to protect the IRP pointer. For example, suppose a driver marks an IRP pending, then passes the IRP pointer as context to an [*IoTimer*](https://msdn.microsoft.com/library/windows/hardware/ff550381) routine. The driver must set a *Cancel* routine that cancels the timer and must use the same spin lock in both the *Cancel* routine and the timer callback when accessing the IRP.

Any driver that queues its own IRPs and uses its own spin lock must do the following:

-   Create a spin lock to protect the queue.

-   Set and clear the *Cancel* routine only while holding this spin lock.

-   If the *Cancel* routine starts running while the driver is dequeuing an IRP, allow the *Cancel* routine to complete the IRP.

-   Acquire the lock that protects the queue in the *Cancel* routine.

To create the spin lock, the driver calls [**KeInitializeSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff552160). In the following example, the driver saves the spin lock in a **DEVICE\_CONTEXT** structure along with the queue it has created:

```cpp
typedef struct {
    LIST_ENTRYirpQueue;
    KSPIN_LOCK irpQueueSpinLock;
    ...
} DEVICE_CONTEXT;

VOID InitDeviceContext(DEVICE_CONTEXT *deviceContext)
{
    InitializeListHead(&deviceContext->irpQueue);
    KeInitializeSpinLock(&deviceContext->irpQueueSpinLock);
}
```

To queue an IRP, the driver acquires the spin lock, calls [**InsertTailList**](https://msdn.microsoft.com/library/windows/hardware/ff547823), and then marks the IRP pending, as in the following example:

```cpp
NTSTATUS QueueIrp(DEVICE_CONTEXT *deviceContext, PIRP Irp)
{
   PDRIVER_CANCEL  oldCancelRoutine;
   KIRQL  oldIrql;
   NTSTATUS  status;

   KeAcquireSpinLock(&deviceContext->irpQueueSpinLock, &oldIrql);

   // Queue the IRP and call IoMarkIrpPending to indicate
   // that the IRP may complete on a different thread.
   // N.B. It is okay to call these inside the spin lock
   // because they are macros, not functions.
   IoMarkIrpPending(Irp);
   InsertTailList(&deviceContext->irpQueue, &Irp->Tail.Overlay.ListEntry);

   // Must set a Cancel routine before checking the Cancel flag.
   oldCancelRoutine = IoSetCancelRoutine(Irp, IrpCancelRoutine);
   ASSERT(oldCancelRoutine == NULL);

   if (Irp->Cancel) {
      // The IRP was canceled. Check whether our cancel routine was called.
      oldCancelRoutine = IoSetCancelRoutine(Irp, NULL);
      if (oldCancelRoutine) {
         // The cancel routine was NOT called.  
         // So dequeue the IRP now and complete it after releasing the spin lock.
         RemoveEntryList(&Irp->Tail.Overlay.ListEntry);
         // Drop the lock before completing the request.
         KeReleaseSpinLock(&deviceContext->irpQueueSpinLock, oldIrql);
         Irp->IoStatus.Status = STATUS_CANCELLED; 
         Irp->IoStatus.Information = 0;
         IoCompleteRequest(Irp, IO_NO_INCREMENT);
         return STATUS_PENDING;

      } else {
         // The Cancel routine WAS called.  
         // As soon as we drop our spin lock, it will dequeue and complete the IRP.
         // So leave the IRP in the queue and otherwise do not touch it.
         // Return pending since we are not completing the IRP here.
         
      }
   }

   KeReleaseSpinLock(&deviceContext->irpQueueSpinLock, oldIrql);

   // Because the driver called IoMarkIrpPending while it held the IRP,
   // it must return STATUS_PENDING from its dispatch routine.
   return STATUS_PENDING;
}
```

As the example shows, the driver holds its spin lock while it sets and clears the *Cancel* routine. The sample queuing routine contains two calls to [**IoSetCancelRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549674).

The first call sets the *Cancel* routine for the IRP. However, because the IRP might have been canceled while the queuing routine is running, the driver must check the **Cancel** member of the IRP.

-   If **Cancel** is set, then cancellation has been requested, and the driver must make a second call to **IoSetCancelRoutine** to see whether the previously set *Cancel* routine was called.

-   If the IRP has been canceled but the *Cancel* routine has not yet been called, then the current routine dequeues the IRP and completes it with STATUS\_CANCELLED.

-   If the IRP has been canceled and the *Cancel* routine has already been called, then the current return marks the IRP pending and returns STATUS\_PENDING. The *Cancel* routine will complete the IRP.

The following example shows how to remove an IRP from the previously created queue:

```cpp
PIRP DequeueIrp(DEVICE_CONTEXT *deviceContext)
{
   KIRQL oldIrql;
   PIRP nextIrp = NULL;

   KeAcquireSpinLock(&deviceContext->irpQueueSpinLock, &oldIrql);

   while (!nextIrp && !IsListEmpty(&deviceContext->irpQueue)) {
      PDRIVER_CANCEL oldCancelRoutine;
      PLIST_ENTRY listEntry = RemoveHeadList(&deviceContext->irpQueue);

      // Get the next IRP off the queue.
      nextIrp = CONTAINING_RECORD(listEntry, IRP, Tail.Overlay.ListEntry);

      // Clear the IRP&#39;s cancel routine.
      oldCancelRoutine = IoSetCancelRoutine(nextIrp, NULL);

      // IoCancelIrp() could have just been called on this IRP. What interests us
      // is not whether IoCancelIrp() was called (nextIrp->Cancel flag set), but
      // whether IoCancelIrp() called (or is about to call) our Cancel routine.
      // For that, check the result of the test-and-set macro IoSetCancelRoutine.
      if (oldCancelRoutine) {
         // Cancel routine not called for this IRP. Return this IRP.
         ASSERT(oldCancelRoutine == IrpCancelRoutine);
      } else {
         // This IRP was just canceled and the cancel routine was (or will be)
         // called. The Cancel routine will complete this IRP as soon as we
         // drop the spin lock, so do not do anything with the IRP.
         // Also, the Cancel routine will try to dequeue the IRP, so make 
         // the IRP&#39;s ListEntry point to itself.
         ASSERT(nextIrp->Cancel);
         InitializeListHead(&nextIrp->Tail.Overlay.ListEntry);
         nextIrp = NULL;
      }
   }

   KeReleaseSpinLock(&deviceContext->irpQueueSpinLock, oldIrql);

   return nextIrp;
}
```

In the example, the driver acquires the associated spin lock before it accesses the queue. While holding the spin lock, it checks that the queue is not empty and gets the next IRP off the queue. Then it calls **IoSetCancelRoutine** to reset the *Cancel* routine for the IRP. Because the IRP could be canceled while the driver dequeues the IRP and resets the *Cancel* routine, the driver must check the value returned by **IoSetCancelRoutine**. If **IoSetCancelRoutine** returns **NULL**, which indicates that the *Cancel* routine either has been or will soon be called, then the dequeuing routine lets the *Cancel* routine complete the IRP. It then releases the lock that protects the queue and returns.

Note the use of [**InitializeListHead**](https://msdn.microsoft.com/library/windows/hardware/ff547799) in the preceding routine. The driver could requeue the IRP, so that the *Cancel* routine can dequeue it, but it is simpler to call **InitializeListHead**, which reinitializes the IRP's **ListEntry** field so that it points to the IRP itself. Using the self-referencing pointer is important because the structure of the list could change before the *Cancel* routine acquires the spin lock. And if the list structure changes, possibly making the original value of **ListEntry** invalid, the *Cancel* routine could corrupt the list when it dequeues the IRP. But if **ListEntry** points to the IRP itself, then the *Cancel* routine will always use the correct IRP.

The *Cancel* routine, in turn, simply does the following:

```cpp
VOID IrpCancelRoutine(IN PDEVICE_OBJECT DeviceObject, IN PIRP Irp)
{
   DEVICE_CONTEXT  *deviceContext = DeviceObject->DeviceExtension;
   KIRQL  oldIrql;

   // Release the global cancel spin lock.  
   // Do this while not holding any other spin locks so that we exit at the right IRQL.
   IoReleaseCancelSpinLock(Irp->CancelIrql);

   // Dequeue and complete the IRP.  
   // The enqueue and dequeue functions synchronize properly so that if this cancel routine is called, 
   // the dequeue is safe and only the cancel routine will complete the IRP. Hold the spin lock for the IRP
   // queue while we do this.

   KeAcquireSpinLock(&deviceContext->irpQueueSpinLock, &oldIrql);

   RemoveEntryList(&Irp->Tail.Overlay.ListEntry);

   KeReleaseSpinLock(&deviceContext->irpQueueSpinLock, oldIrql);

   // Complete the IRP. This is a call outside the driver, so all spin locks must be released by this point.
   Irp->IoStatus.Status = STATUS_CANCELLED;
   IoCompleteRequest(Irp, IO_NO_INCREMENT);
   return;
}
```

The I/O manager always acquires the global cancel spin lock before it calls a *Cancel* routine, so the first task of the *Cancel* routine is to release this spin lock. It then acquires the spin lock that protects the driver's queue of IRPs, removes the current IRP from the queue, releases its spin lock, completes the IRP with STATUS\_CANCELLED and no priority boost, and returns.

For more information about canceling spin locks, see the [Cancel Logic in Windows Drivers](http://go.microsoft.com/fwlink/p/?linkid=59531) white paper.

 

 




