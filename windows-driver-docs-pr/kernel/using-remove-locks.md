---
title: Using Remove Locks
description: Using Remove Locks
ms.assetid: 78ca7fe5-ceed-4752-bf1b-d13309097cd8
keywords: ["remove locks WDK PnP", "lock routines WDK PnP"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using Remove Locks





The [remove lock routines](https://msdn.microsoft.com/library/windows/hardware/ff561042) provide a way to track the number of outstanding I/O operations on a device, and to determine when it is safe to detach and delete a driver's device object. The system provides these routines to driver writers as an alternative to implementing their own tracking mechanism.

A driver can use this mechanism for two purposes:

1.  To ensure that the driver's [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine will not complete an [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) request while the lock is held (for example, while another driver routine is accessing the device).

2.  To count the number of reasons why the driver should not delete its device object, and to set an event when that count goes to zero.

To initialize a remove lock, a driver should allocate an **IO\_REMOVE\_LOCK** structure in its [device extension](device-extensions.md) and then call [**IoInitializeRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff549324). A driver typically calls **IoInitializeRemoveLock** in its [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine, when the driver initializes the rest of the device extension for a device object.

Your driver must call [**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204) each time it starts an I/O operation. The driver must call [**IoReleaseRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff549560) each time it finishes an I/O operation. A driver can acquire the lock more than once. The remove lock routines maintain a count of the outstanding acquisitions of the lock. Each call to **IoAcquireRemoveLock** increments the count, and **IoReleaseRemoveLock** decrements the count.

Your driver should also call **IoAcquireRemoveLock** when it passes out a reference to its code (for timers, DPCs, callbacks, and so on). The driver then must call **IoReleaseRemoveLock** when the event has returned.

In its dispatch code for [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738), the driver must acquire the lock once more and then call [**IoReleaseRemoveLockAndWait**](https://msdn.microsoft.com/library/windows/hardware/ff549567). This routine does not return until all outstanding acquisitions of the lock have been released. To allow queued I/O operations to complete, each driver should call **IoReleaseRemoveLockAndWait** *after* it passes the **IRP\_MN\_REMOVE\_DEVICE** request to the next-lower driver, and *before* it releases memory, calls [**IoDetachDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549087), or calls [**IoDeleteDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549083). After **IoReleaseRemoveLockAndWait** has been called for a particular remove lock, all subsequent calls to **IoAcquireRemoveLock** for the same remove lock will fail.

After **IoReleaseRemoveLockAndWait** returns, the driver should consider the device to be in a state in which it is ready to be removed and cannot perform I/O operations. Therefore, the driver must not call **IoInitializeRemoveLock** to re-initialize the remove lock. Violation of this rule while the driver is being verified by [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) will result in a bug check.

Because a driver stores an **IO\_REMOVE\_LOCK** structure in the device extension of a device object, the remove lock is deleted when the driver deletes the device extension while processing an **IRP\_MN\_REMOVE\_DEVICE** request.

 

 




