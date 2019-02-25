---
title: Returning Status from Dispatch Routines
description: Returning Status from Dispatch Routines
ms.assetid: 76bd651a-344f-4e22-a435-b62fdf2d7ddc
keywords:
- IRP dispatch routines WDK file system , returning status
- status values WDK file system
- success status values WDK file system
- returning status WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Returning Status from Dispatch Routines


## <span id="ddk_returning_status_from_dispatch_routines_if"></span><span id="DDK_RETURNING_STATUS_FROM_DISPATCH_ROUTINES_IF"></span>


Except when completing an IRP, a dispatch routine that does not set a completion routine should always return the NTSTATUS value returned by [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336). Unless this value is STATUS\_PENDING, it must match the value of **Irp-&gt;IoStatus.Status** set by the driver that completed the IRP.

A dispatch routine that sets a completion routine that might post the IRP to a work queue should do one of the following:

-   Return the NTSTATUS value that was returned by **IoCallDriver**.

-   Wait for the completion routine to signal an event and return the value of **Irp-&gt;IoStatus.Status**.

-   Mark the IRP pending, post it to a work queue, and return STATUS\_PENDING.

-   If the completion routine might post the IRP to a work queue, the dispatch routine must mark the IRP pending and return STATUS\_PENDING.

Which of these behaviors is correct, or even possible, depends on the specific operation. Some operations, such as directory change notification, cannot be made synchronous; and some, such as oplocks, cannot be made asynchronous.

For more information about returning status from a dispatch routine, see [Constraints on Dispatch Routines](constraints-on-dispatch-routines.md).

 

 




