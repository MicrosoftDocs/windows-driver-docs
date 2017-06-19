---
title: Using Remove Locks
author: windows-driver-content
description: Using Remove Locks
ms.assetid: 78ca7fe5-ceed-4752-bf1b-d13309097cd8
keywords: ["remove locks WDK PnP", "lock routines WDK PnP"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using Remove Locks


## <a href="" id="ddk-using-remove-locks-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20Remove%20Locks%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


