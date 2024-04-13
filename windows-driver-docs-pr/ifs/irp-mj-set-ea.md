---
title: IRP_MJ_SET_EA (FS and Filter Drivers)
description: IRP_MJ_SET_EA
keywords: ["IRP_MJ_SET_EA Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_SET_EA
api_type:
- NA
ms.date: 03/13/2023
ms.topic: reference
---

# IRP_MJ_SET_EA (FS and filter drivers)

## When Sent

The I/O Manager sends the IRP_MJ_SET_EA request to set a file's extended attributes.

## Operation: File System Drivers

If the file system supports extended attributes, the file system driver should process the request and complete the IRP. Otherwise, the file system driver should return **STATUS_EAS_NOT_SUPPORTED**.

## Operation: Legacy File System Filter Drivers

The filter driver should pass this IRP down to the next-lower driver on the stack.

## Parameters

A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) for the given IRP to get a pointer to its own stack location in the IRP. In the following parameters, **Irp** points to the [**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp) and **IrpSp** points to the [**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location). The driver can use the information that is set in the following members of the IRP and the IRP stack location to process a set extended attributes request:

- **DeviceObject** is a pointer to the target device object.

- **Irp->AssociatedIrp.SystemBuffer** points to a system-supplied input buffer that contains the extended attribute information to be set. Used for METHOD_BUFFERED I/O.

- **Irp->IoStatus** points to an [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation.

- **Irp->MdlAddress** is the address of a memory descriptor list (MDL) describing an input buffer that receives the extended attribute information. Used for METHOD_DIRECT I/O.

- **Irp->UserBuffer** points to a caller-supplied [**FILE_FULL_EA_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_full_ea_information)-structured input buffer that receives the extended attribute information. Used for METHOD_NEITHER I/O.

- **IrpSp->FileObject** points to the file object that is associated with **DeviceObject**.

  The **IrpSp->FileObject** parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE_OBJECT structure. The **RelatedFileObject** field of the FILE_OBJECT structure isn't valid during the processing of IRP_MJ_SET_EA and shouldn't be used.

- **IrpSp->MajorFunction** is set to IRP_MJ_SET_EA.

- **IrpSp->Parameters.SetEa.Length** is the length in bytes of the input buffer.

## See also

[**FILE_FULL_EA_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_full_ea_information)

[**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoCheckEaBufferValidity**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocheckeabuffervalidity)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[**IRP_MJ_QUERY_EA**](irp-mj-query-ea.md)
