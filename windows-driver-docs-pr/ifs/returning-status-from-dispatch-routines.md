---
title: Returning Status from Dispatch Routines
description: Returning Status from Dispatch Routines
keywords:
- IRP dispatch routines WDK file system , returning status
- status values WDK file system
- success status values WDK file system
- returning status WDK file system
ms.date: 02/23/2023
---

# Returning Status from Dispatch Routines

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

Except when completing an IRP, a dispatch routine that doesn't set a completion routine should always return the NTSTATUS value returned by [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver). Unless this value is STATUS_PENDING, it must match the value of **Irp->IoStatus.Status** set by the driver that completed the IRP.

A dispatch routine that sets a completion routine that might post the IRP to a work queue should do one of the following actions:

- Return the NTSTATUS value that was returned by **IoCallDriver**.
- Wait for the completion routine to signal an event and return the value of **Irp-&gt;IoStatus.Status**.
- Mark the IRP pending, post it to a work queue, and return STATUS_PENDING.
- If the completion routine might post the IRP to a work queue, the dispatch routine must mark the IRP pending and return STATUS_PENDING.

Which of these behaviors is correct or even possible depends on the specific operation. Some operations, such as directory change notifications, can't be made synchronous; and some operations, such as oplocks, can't be made asynchronous.

For more information about returning status from a dispatch routine, see [Constraints on Dispatch Routines](constraints-on-dispatch-routines.md).
