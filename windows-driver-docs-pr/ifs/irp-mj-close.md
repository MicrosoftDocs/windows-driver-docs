---
title: IRP_MJ_CLOSE (FS and Filter Drivers)
description: IRP_MJ_CLOSE
keywords: ["IRP_MJ_CLOSE Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_CLOSE
api_type:
- NA
ms.date: 03/13/2023
ms.topic: reference
---

# IRP_MJ_CLOSE (FS and filter drivers)

## When Sent

The I/O Manager sends an IRP_MJ_CLOSE request to indicate that the reference count on a file object has reached zero, usually because a file system driver or other kernel-mode component has called [**ObDereferenceObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obdereferenceobject) on the file object. This request normally follows a cleanup request. However, though the close request might not be received immediately after the cleanup request.

## Operation: File System Drivers

If the target device object is the file system's control device object, the file system driver must complete the IRP after performing any needed processing.

Otherwise, the file system driver should process the close request.

## Operation: Legacy File System Filter Drivers

If the target device object is the filter driver's control device object, the filter driver should do what is necessary to end communication with the control device object and then complete the IRP.

Otherwise, the filter driver should perform any needed processing and then pass the IRP down to the next-lower driver on the stack. Processing could include operations such as deleting the per-file and per-file object context information that the filter maintains.

File system filter driver writers should note that [**IoCreateStreamFileObject**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocreatestreamfileobject) causes an [**IRP_MJ_CLEANUP**](irp-mj-cleanup.md) request to be sent to the file system driver stack for the volume. Because file systems often create stream file objects as a side effect of operations other than [**IRP_MJ_CREATE**](irp-mj-create.md), it's difficult for filter drivers to reliably detect stream file object creation. Thus a filter driver should expect to receive **IRP_MJ_CLEANUP** and [**IRP_MJ_CLOSE**](../kernel/irp-mj-close.md) requests for previously unseen file objects.

Filter driver writers should also note that, unlike [**IoCreateStreamFileObject**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocreatestreamfileobject), [**IoCreateStreamFileObjectLite**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocreatestreamfileobjectlite) doesn't cause an [**IRP_MJ_CLEANUP**](irp-mj-cleanup.md) request to be sent to the file system driver stack. For this reason, and because file systems often create stream file objects as a side effect of operations other than [**IRP_MJ_CREATE**](irp-mj-create.md), it's difficult for filter drivers to reliably detect stream file object creation. Thus filter drivers should expect to receive **IRP_MJ_CLOSE** requests for previously unseen file objects.

## Parameters

A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) with the given IRP to get a pointer to its own [**stack location**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location) in the IRP, shown in the following list as **IrpSp**. (The IRP is shown as **Irp**.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a close request.

* **DeviceObject**

  Pointer to the target device object.

* **Irp->Flags**

  The following flags are set for this request:
  
  * IRP_CLOSE_OPERATION
  * IRP_SYNCHRONOUS_API

* **Irp->IoStatus**

  Pointer to an [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation.

* **Irp->FileObject**

  Pointer to the file object that is associated with **DeviceObject**.

  The **Irp->FileObject** parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE_OBJECT structure. The **RelatedFileObject** field of the FILE_OBJECT structure isn't valid during the processing of IRP_MJ_CLEANUP and shouldn't be used.

* **Irp->MajorFunction**

  Specifies IRP_MJ_CLOSE.

## See also

[**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoCreateStreamFileObject**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocreatestreamfileobject)

[**IoCreateStreamFileObjectLite**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocreatestreamfileobjectlite)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[**IRP_MJ_CLOSE (WDK Kernel Reference)**](../kernel/irp-mj-close.md)

[**IRP_MJ_CLEANUP**](irp-mj-cleanup.md)

[**IRP_MJ_CREATE**](irp-mj-create.md)

[**ObDereferenceObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obdereferenceobject)
