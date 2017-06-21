---
title: DispatchCleanup Routines
author: windows-driver-content
description: DispatchCleanup Routines
ms.assetid: 1ba001b8-92e0-453f-b9f6-6099cedf6439
keywords: ["dispatch routines WDK kernel , DispatchCleanup routine", "DispatchCleanup routine", "IRP_MJ_CLEANUP I/O function code", "deallocating resources WDK kernel", "unmapping hardware memory", "unmapping user-mode memory", "unlocking user-mode memory", "cleaning up resources WDK kernel", "spin locks WDK kernel", "cleanup dispatch routines WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DispatchCleanup Routines


## <a href="" id="ddk-dispatchcleanup-routines-kg"></a>


A driver's [*DispatchCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff543233) routine handles IRPs for the [**IRP\_MJ\_CLEANUP**](https://msdn.microsoft.com/library/windows/hardware/ff550718) I/O function code.

Drivers can use a *DispatchCleanup* routine to perform any cleanup operations that are needed after all of the handles to a file object have been closed. Note that *DispatchCleanup* is called in the process context of the process that closed the final handle; this process might be different from the process that initially opened the handle. (Typically this difference happens because another process uses the **DuplicateHandle** user-mode routine to duplicate the processes handles.) Drivers that must perform cleanup in the original process context can use the [**PsSetCreateProcessNotifyRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff559951) routine to register a callback routine for that purpose, but keep in mind that such callbacks are a limited system resource.

In general, a *DispatchCleanup* routine must process an **IRP\_MJ\_CLEANUP** request by doing the following for every IRP that is currently in the device queue (or in the driver's internal queue of IRPs), for the target device object, and is associated with the file object:

-   Call [**IoSetCancelRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549674) to set the [*Cancel*](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine pointer to **NULL**.

-   Cancel every IRP that is currently in the queue for the target device object, if the file object that is specified in the driver's I/O stack location of the queued IRP matches the file object that was received in the I/O stack location of the **IRP\_MJ\_CLEANUP** request.

-   Call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) to complete the IRP, and return STATUS\_SUCCESS.

While processing an **IRP\_MJ\_CLEANUP** request, a driver can receive additional requests, such as [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794) or [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819). Therefore, a driver that must deallocate resources must also synchronize execution of its *DispatchCleanup* routine with other dispatch routines, such as [*DispatchRead*](https://msdn.microsoft.com/library/windows/hardware/ff543376) and [*DispatchWrite*](https://msdn.microsoft.com/library/windows/hardware/ff544034).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20DispatchCleanup%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


