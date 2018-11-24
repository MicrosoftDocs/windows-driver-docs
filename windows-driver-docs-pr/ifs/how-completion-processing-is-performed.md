---
title: How Completion Processing Is Performed
description: How Completion Processing Is Performed
ms.assetid: 5741c226-9781-4d9a-b6dd-d8ecc17c4c6f
keywords:
- IRP completion routines WDK file system , processing stages
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How Completion Processing Is Performed


## <span id="ddk_how_completion_processing_is_performed_if"></span><span id="DDK_HOW_COMPLETION_PROCESSING_IS_PERFORMED_IF"></span>


Completion processing is performed in two stages. The first stage is performed in an arbitrary thread context, at IRQL &lt;= DISPATCH\_LEVEL. In this stage, the following tasks are performed:

-   Each completion routine registered for the IRP is called in turn, beginning with the lowest IRP stack location. If a completion routine returns STATUS\_MORE\_PROCESSING\_REQUIRED, completion processing is halted.

-   If the IRP contains a memory descriptor list (MDL), any physical pages mapped by the MDL are unlocked.

-   The second phase of I/O completion is queued to the target (requesting) thread as a special kernel APC.

The second stage is performed in the context of the thread that originated the I/O request. It is executed as a special kernel APC and therefore runs at IRQL APC\_LEVEL. In this stage, the following tasks are performed:

-   If the IRP represents a buffered operation, the contents of **Irp-&gt;AssociatedIrp.SystemBuffer** are copied to **Irp-&gt;UserBuffer**.

-   If the IRP contains an MDL, the MDL is freed.

-   The contents of **Irp-&gt;IoStatus** are copied to **Irp-&gt;UserIosb** so that the originator of the I/O request can see the final status of the operation.

-   If an event has been supplied in **Irp-&gt;UserEvent**, it is signaled. Otherwise, if there is a file object for this IRP, its event is signaled.

-   If the IRP was created by calling [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318) or [**IoBuildSynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548330), it is dequeued from the thread's pending I/O request list.

-   A user APC is queued, if the caller requested one.

-   The IRP is freed.

**Note**   If completion processing for an IRP is halted because a completion routine returned STATUS\_MORE\_PROCESSING\_REQUIRED, it can be resumed by calling [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) on the same IRP. When this happens, first-stage processing resumes, beginning with the completion routine for the driver immediately above the one whose completion routine returned STATUS\_MORE\_PROCESSING\_REQUIRED.

 

 

 




