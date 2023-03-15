---
title: IRP_MJ_CLEANUP (FS and FS filters)
description: IRP_MJ_CLEANUP
keywords: ["IRP_MJ_CLEANUP Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_CLEANUP
api_type:
- NA
ms.date: 03/13/2023
ms.topic: reference
---

# IRP_MJ_CLEANUP (FS and FS filters)

## When Sent

Receipt of the IRP_MJ_CLEANUP request indicates that the handle reference count on a file object has reached zero. (In other words, all handles to the file object have been closed.) Often it's sent when a user-mode application has called the Win32 **CloseHandle** function (or when a kernel-mode driver has called [**ZwClose**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose)) on the last outstanding handle to a file object.

It's important to note that the file object might still be being used when all handles to a file object have been closed. System components, such as the Cache Manager and the Memory Manager, might hold outstanding references to the file object. These components can still read to or write from a file, even after an IRP_MJ_CLEANUP request is received.

## Operation: File System Drivers

If the target device object is the file system's control device object, the file system driver must complete the IRP.

Otherwise, the file system driver should process the cleanup request.

## Operation: Legacy File System Filter Drivers

If the target device object is the filter driver's control device object, the filter driver must complete the IRP.

Otherwise, the filter driver should pass the IRP down to the next-lower driver on the stack after performing any needed processing.

File system filter driver writers should note that [**IoCreateStreamFileObject**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocreatestreamfileobject) causes an IRP_MJ_CLEANUP request to be sent to the file system driver stack for the volume. Because file systems often create stream file objects as a side effect of operations other than IRP_MJ_CREATE, it's difficult for filter drivers to reliably detect stream file object creation. Thus a filter driver should expect to receive IRP_MJ_CLEANUP and IRP_MJ_CLOSE requests for previously unseen file objects.

Filter driver writers should also note that, unlike [**IoCreateStreamFileObject**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocreatestreamfileobject), [**IoCreateStreamFileObjectLite**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocreatestreamfileobjectlite) doesn't cause an IRP_MJ_CLEANUP request to be sent to the file system driver stack. For this reason, and because file systems often create stream file objects as a side effect of operations other than IRP_MJ_CREATE, it's difficult for filter drivers to reliably detect stream file object creation. Thus filter drivers should expect to receive IRP_MJ_CLOSE requests for previously unseen file objects.

## Parameters

A file system or Legacy filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) with the given IRP to get a pointer to its own [**stack location**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location) in the IRP, shown in the following list as **IrpSp**. (The IRP is shown as **Irp**.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a cleanup request.

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

  Specifies IRP_MJ_CLEANUP.

## See also

[**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoCreateStreamFileObject**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocreatestreamfileobject)

[**IoCreateStreamFileObjectLite**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocreatestreamfileobjectlite)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[**IRP_MJ_CLEANUP (WDK Kernel Reference)**](../kernel/irp-mj-cleanup.md)

[**IRP_MJ_CLOSE**](irp-mj-close.md)

[**IRP_MJ_CREATE**](irp-mj-create.md)

[**ZwClose**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose)
