---
title: IRP_MJ_SHUTDOWN
description: IRP\_MJ\_SHUTDOWN
ms.assetid: 4f7ba339-87f5-4011-8981-de6c31a9239a
keywords: ["IRP_MJ_SHUTDOWN Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_SHUTDOWN
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# IRP\_MJ\_SHUTDOWN


## When Sent


The IRP\_MJ\_SHUTDOWN request is sent by the I/O Manager or by a file system driver when the system is being shut down.

## Operation: File System Drivers


The file system should perform any necessary cleanup and complete the IRP with STATUS\_SUCCESS.

## Operation: File System Filter Drivers


The filter driver should pass this IRP down to the next-lower driver on the stack.

## Parameters


A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iogetcurrentirpstacklocation) with the given IRP to get a pointer to its own [**stack location**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/ns-wdm-_io_stack_location) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a shutdown request:

<a href="" id="deviceobject"></a>*DeviceObject*  
Pointer to the target device object.

<a href="" id="irp--iostatus"></a>*Irp-&gt;IoStatus*  
Pointer to an [**IO\_STATUS\_BLOCK**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation.

<a href="" id="irpsp--majorfunction"></a>*IrpSp-&gt;MajorFunction*  
Specifies IRP\_MJ\_SET\_SHUTDOWN.

## See also


[**IO\_STACK\_LOCATION**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/ns-wdm-_io_stack_location)

[**IO\_STATUS\_BLOCK**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/ns-wdm-_io_status_block)

[**IoGetCurrentIrpStackLocation**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IRP**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/ns-wdm-_irp)

[**IRP\_MJ\_SHUTDOWN (WDK Kernel Reference)**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-shutdown)

 

 






