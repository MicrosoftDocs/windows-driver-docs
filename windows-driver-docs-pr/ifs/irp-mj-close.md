---
title: IRP_MJ_CLOSE
description: IRP\_MJ\_CLOSE
ms.assetid: 62bb28de-7f89-4009-9ea9-0aa3d6bca0ed
keywords: ["IRP_MJ_CLOSE Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_CLOSE
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# IRP\_MJ\_CLOSE


## When Sent


Receipt of the IRP\_MJ\_CLOSE request indicates that the reference count on a file object has reached zero, usually because a file system driver or other kernel-mode component has called [**ObDereferenceObject**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-obdereferenceobject) on the file object. This request normally follows a cleanup request. However, this does not necessarily mean that the close request will be received immediately after the cleanup request.

## Operation: File System Drivers


If the target device object is the file system's control device object, the file system driver must complete the IRP after performing any needed processing.

Otherwise, the file system driver should process the close request.

## Operation: File System Filter Drivers


If the target device object is the filter driver's control device object, the filter driver should do what is necessary to end communication with the control device object and complete the IRP.

Otherwise, the filter driver should pass the IRP down to the next-lower driver on the stack after performing any needed processing, such as deleting the per-file and per-file object context information that is maintained by the filter driver.

File system filter driver writers should note that [**IoCreateStreamFileObject**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocreatestreamfileobject) causes an [**IRP\_MJ\_CLEANUP**](irp-mj-cleanup.md) request to be sent to the file system driver stack for the volume. Because file systems often create stream file objects as a side effect of operations other than [**IRP\_MJ\_CREATE**](irp-mj-create.md), it is difficult for filter drivers to reliably detect stream file object creation. Thus a filter driver should expect to receive **IRP\_MJ\_CLEANUP** and [**IRP\_MJ\_CLOSE**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-close) requests for previously unseen file objects.

Filter driver writers should also note that, unlike [**IoCreateStreamFileObject**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocreatestreamfileobject), [**IoCreateStreamFileObjectLite**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocreatestreamfileobjectlite) does not cause an [**IRP\_MJ\_CLEANUP**](irp-mj-cleanup.md) request to be sent to the file system driver stack. For this reason, and because file systems often create stream file objects as a side effect of operations other than [**IRP\_MJ\_CREATE**](irp-mj-create.md), it is difficult for filter drivers to reliably detect stream file object creation. Thus filter drivers should expect to receive **IRP\_MJ\_CLOSE** requests for previously unseen file objects.

## Parameters


A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) with the given IRP to get a pointer to its own [**stack location**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a close request:

<a href="" id="deviceobject"></a>*DeviceObject*  
Pointer to the target device object.

<a href="" id="irp--flags"></a>*Irp-&gt;Flags*  
The following flags are set for this request:

IRP\_CLOSE\_OPERATION

IRP\_SYNCHRONOUS\_API

<a href="" id="irp--iostatus"></a>*Irp-&gt;IoStatus*
Pointer to an [**IO\_STATUS\_BLOCK**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation.

<a href="" id="irpsp--fileobject"></a>*IrpSp-&gt;FileObject*
Pointer to the file object that is associated with *DeviceObject*.

The *IrpSp-&gt;FileObject* parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE\_OBECT structure. The **RelatedFileObject** field of the FILE\_OBJECT structure is not valid during the processing of IRP\_MJ\_CLOSE and should not be used.

<a href="" id="irpsp--majorfunction"></a>*IrpSp-&gt;MajorFunction*
Specifies IRP\_MJ\_CLOSE.

## See also


[**IO\_STACK\_LOCATION**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO\_STATUS\_BLOCK**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoCreateStreamFileObject**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocreatestreamfileobject)

[**IoCreateStreamFileObjectLite**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocreatestreamfileobjectlite)

[**IoGetCurrentIrpStackLocation**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IRP**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[**IRP\_MJ\_CLOSE (WDK Kernel Reference)**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-close)

[**IRP\_MJ\_CLEANUP**](irp-mj-cleanup.md)

[**IRP\_MJ\_CREATE**](irp-mj-create.md)

[**ObDereferenceObject**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-obdereferenceobject)

 

 






