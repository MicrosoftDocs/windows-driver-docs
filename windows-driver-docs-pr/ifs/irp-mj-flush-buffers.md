---
title: IRP_MJ_FLUSH_BUFFERS (IFS)
description: IRP\_MJ\_FLUSH\_BUFFERS
keywords: ["IRP_MJ_FLUSH_BUFFERS Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_FLUSH_BUFFERS
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# IRP\_MJ\_FLUSH\_BUFFERS (IFS)


## When Sent


The IRP\_MJ\_FLUSH\_BUFFERS request is sent by the I/O Manager and other operating system components, as well as other kernel-mode drivers, when buffered data needs to be flushed to disk. It can be sent, for example, when a user-mode application has called a Microsoft Win32 function such as **FlushFileBuffers**. (For file system drivers and file system filter drivers, calling [**CcFlushCache**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ccflushcache) is usually preferable to sending an IRP.)

All file system and filter drivers that maintain internal buffers for data must handle this IRP so that changes to file data or metadata can be preserved across system shutdowns.

## Operation: File System Drivers


The file system driver should flush to disk any important data or metadata associated with the file object and complete the IRP. For more information about how to handle this IRP, study the FASTFAT sample.

## Operation: File System Filter Drivers


The filter driver should flush to disk any important data or metadata associated with the file object and pass this IRP down to the next-lower driver on the stack.

## Parameters


A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) with the given IRP to get a pointer to its own [**stack location**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a flush buffers request:

<a href="" id="deviceobject"></a>*DeviceObject*  
Pointer to the target device object.

<a href="" id="irp--iostatus"></a>*Irp-&gt;IoStatus*  
Pointer to an [**IO\_STATUS\_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation.

<a href="" id="irpsp--fileobject"></a>*IrpSp-&gt;FileObject*  
Pointer to the file object that is associated with *DeviceObject*.

The *IrpSp-&gt;FileObject* parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE\_OBJECT structure. The **RelatedFileObject** field of the FILE\_OBJECT structure is not valid during the processing of IRP\_MJ\_FLUSH\_BUFFERS and should not be used.

<a href="" id="irpsp--majorfunction"></a>*IrpSp-&gt;MajorFunction*  
Specifies IRP\_MJ\_FLUSH\_BUFFERS.

## See also


[**CcFlushCache**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ccflushcache)

[**IO\_STACK\_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO\_STATUS\_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[**IRP\_MJ\_FLUSH\_BUFFERS (WDK Kernel Reference)**](../kernel/irp-mj-flush-buffers.md)

 

