---
title: DispatchCleanup Routines
description: DispatchCleanup Routines
ms.assetid: 1ba001b8-92e0-453f-b9f6-6099cedf6439
keywords: ["dispatch routines WDK kernel , DispatchCleanup routine", "DispatchCleanup routine", "IRP_MJ_CLEANUP I/O function code", "deallocating resources WDK kernel", "unmapping hardware memory", "unmapping user-mode memory", "unlocking user-mode memory", "cleaning up resources WDK kernel", "spin locks WDK kernel", "cleanup dispatch routines WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# DispatchCleanup Routines





A driver's [*DispatchCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff543233) routine handles IRPs for the [**IRP\_MJ\_CLEANUP**](https://msdn.microsoft.com/library/windows/hardware/ff550718) I/O function code.

Drivers can use a *DispatchCleanup* routine to perform any cleanup operations that are needed after all of the handles to a file object have been closed. Note that *DispatchCleanup* is called in the process context of the process that closed the final handle; this process might be different from the process that initially opened the handle. (Typically this difference happens because another process uses the **DuplicateHandle** user-mode routine to duplicate the processes handles.) Drivers that must perform cleanup in the original process context can use the [**PsSetCreateProcessNotifyRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff559951) routine to register a callback routine for that purpose, but keep in mind that such callbacks are a limited system resource.

In general, a *DispatchCleanup* routine must process an **IRP\_MJ\_CLEANUP** request by doing the following for every IRP that is currently in the device queue (or in the driver's internal queue of IRPs), for the target device object, and is associated with the file object:

-   Call [**IoSetCancelRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549674) to set the [*Cancel*](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine pointer to **NULL**.

-   Cancel every IRP that is currently in the queue for the target device object, if the file object that is specified in the driver's I/O stack location of the queued IRP matches the file object that was received in the I/O stack location of the **IRP\_MJ\_CLEANUP** request.

-   Call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) to complete the IRP, and return STATUS\_SUCCESS.

While processing an **IRP\_MJ\_CLEANUP** request, a driver can receive additional requests, such as [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794) or [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819). Therefore, a driver that must deallocate resources must also synchronize execution of its *DispatchCleanup* routine with other dispatch routines, such as [*DispatchRead*](https://msdn.microsoft.com/library/windows/hardware/ff543376) and [*DispatchWrite*](https://msdn.microsoft.com/library/windows/hardware/ff544034).

 

 




