---
title: How Completion Processing Is Performed
description: How Completion Processing Is Performed
keywords:
- IRP completion routines WDK file system , processing stages
ms.date: 02/23/2023
---

# How Completion Processing Is Performed

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

Completion processing is performed in two stages. The first stage is performed in an arbitrary thread context, at IRQL <= DISPATCH_LEVEL. In this stage, the following tasks are performed:

- Each completion routine registered for the IRP is called in turn, beginning with the lowest IRP stack location. If a completion routine returns STATUS_MORE_PROCESSING_REQUIRED, completion processing is halted.

- If the IRP contains a memory descriptor list (MDL), any physical pages mapped by the MDL are unlocked.

- The second phase of I/O completion is queued to the target (requesting) thread as a special kernel APC.

The second stage is performed in the context of the thread that originated the I/O request. It's executed as a special kernel APC and therefore runs at IRQL APC_LEVEL. In this stage, the following tasks are performed:

- If the IRP represents a buffered operation, the contents of **Irp->AssociatedIrp.SystemBuffer** are copied to **Irp->UserBuffer**.

- If the IRP contains an MDL, the MDL is freed.

- The contents of **Irp->IoStatus** are copied to **Irp->UserIosb** so that the originator of the I/O request can see the final status of the operation.

- If an event has been supplied in **Irp->UserEvent**, it's signaled. Otherwise, if there's a file object for this IRP, its event is signaled.

- If the IRP was created by calling [**IoBuildDeviceIoControlRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuilddeviceiocontrolrequest) or [**IoBuildSynchronousFsdRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuildsynchronousfsdrequest), it's dequeued from the thread's pending I/O request list.

- A user APC is queued, if the caller requested one.

- The IRP is freed.

If completion processing for an IRP is halted because a completion routine returned STATUS_MORE_PROCESSING_REQUIRED, it can be resumed by calling [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) on the same IRP. When this situation happens, first-stage processing resumes, beginning with the completion routine for the driver immediately above the one whose completion routine returned STATUS_MORE_PROCESSING_REQUIRED.
