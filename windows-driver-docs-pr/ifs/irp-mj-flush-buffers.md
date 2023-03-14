---
title: IRP_MJ_FLUSH_BUFFERS (FS and filter drivers)
description: IRP_MJ_FLUSH_BUFFERS
keywords: ["IRP_MJ_FLUSH_BUFFERS Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_FLUSH_BUFFERS
api_type:
- NA
ms.date: 03/13/2023
ms.topic: reference
---

# IRP_MJ_FLUSH_BUFFERS (FS and filter drivers)

## When Sent

The I/O Manager, other operating system components, and other kernel-mode drivers send IRP_MJ_FLUSH_BUFFERS requests when buffered data needs to be flushed to disk. It can be sent, for example, when a user-mode application has called a Win32 function such as **FlushFileBuffers**. (For file system drivers and file system filter drivers, calling [**CcFlushCache**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ccflushcache) is preferable to sending an IRP.)

All file system and filter drivers that maintain internal buffers for data must handle this IRP so that changes to file data or metadata can be preserved across system shutdowns.

## Operation: File System Drivers

The file system driver should flush to disk any important data or metadata associated with the file object and complete the IRP. For more information about how to handle this IRP, study the FASTFAT sample.

## Operation: Legacy File System Filter Drivers

The filter driver should flush to disk any important data or metadata associated with the file object and pass this IRP down to the next-lower driver on the stack.

## Parameters

A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) with the given IRP to get a pointer to its own [**stack location**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a flush buffers request:

- **DeviceObject** is a pointer to the target device object.

- **Irp->IoStatus** points to an [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation.

- **IrpSp->FileObject** points to the file object that is associated with **DeviceObject**.

  The **IrpSp->FileObject** parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE_OBJECT structure. The **RelatedFileObject** field of the FILE_OBJECT structure isn't valid during the processing of IRP_MJ_FLUSH_BUFFERS and shouldn't be used.

- **IrpSp->MajorFunction** is set to IRP_MJ_FLUSH_BUFFERS.

## See also

[**CcFlushCache**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ccflushcache)

[**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[**IRP_MJ_FLUSH_BUFFERS (WDK Kernel Reference)**](../kernel/irp-mj-flush-buffers.md)
