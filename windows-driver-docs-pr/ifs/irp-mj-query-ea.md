---
title: IRP_MJ_QUERY_EA (FS and Filter Drivers)
description: IRP_MJ_QUERY_EA
keywords: ["IRP_MJ_QUERY_EA Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_QUERY_EA
api_type:
- NA
ms.date: 03/13/2023
ms.topic: reference
---

# IRP_MJ_QUERY_EA (FS and filter drivers)

## When Sent

The I/O Manager, other operating system components, and other kernel-mode drivers send IRP_MJ_QUERY_EA requests when a user-mode application has requested information about a file's extended attributes.

## Operation: File System Drivers

If the file system supports extended attributes, the file system driver should process the query and complete the IRP. Otherwise, it should return STATUS_EAS_NOT_SUPPORTED.

## Operation: Legacy File System Filter Drivers

The filter driver should pass this IRP down to the next-lower driver on the stack.

## Parameters

A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) for the given IRP to get a pointer to its own stack location in the IRP. In the following parameters, **Irp** points to the [**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp) and **IrpSp** points to the [**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location). The driver can use the information that is set in the following members of the IRP and the IRP stack location to process an IRP_MJ_QUERY_EA request:

- **DeviceObject** is a pointer to the target device object.

- **Irp->AssociatedIrp.SystemBuffer** points to a system-supplied output buffer to be used as an intermediate system buffer. Used for METHOD_BUFFERED I/O.

- **Irp->IoStatus** points to an [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation.

- **Irp->MdlAddress** is the address of a memory descriptor list (MDL) describing an output buffer that receives the extended attribute information. Used for METHOD_DIRECT I/O.

- **Irp->UserBuffer** points to a caller-supplied [**FILE_FULL_EA_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_full_ea_information)-structured output buffer that receives the extended attribute information. Used for METHOD_NEITHER I/O.

- **IrpSp->FileObject** points to the file object that is associated with *DeviceObject*.

  The **IrpSp->FileObject** parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE_OBJECT structure. The **RelatedFileObject** field of the FILE_OBJECT structure isn't valid during the processing of IRP_MJ_QUERY_EA and shouldn't be used.

- **IrpSp->Flags** can be one or more of the following values.

| Flag | Meaning |
| ---- | ------- |
| SL_INDEX_SPECIFIED | Begin the scan at the entry in the extended attribute list whose index is given by **IrpSp->Parameters.QueryEa.EaIndex**. |
| SL_RESTART_SCAN    | Begin the scan at the first entry in the list. If this flag isn't set, resume the scan from a previous IRP_MJ_QUERY_EA request. |
| SL_RETURN_SINGLE_ENTRY | Return only the first entry that is found. |

- **IrpSp->MajorFunction** is set to IRP_MJ_QUERY_EA.

- **IrpSp->Parameters.QueryEa.EaIndex** is the index of the entry at which to begin scanning the extended-attribute list. This parameter is ignored if the SL_INDEX_SPECIFIED flag isn't set or if **IrpSp->Parameters.QueryEa.EaList** points to a nonempty list.

- **IrpSp->Parameters.QueryEa.EaList** points to a caller-supplied [**FILE_GET_EA_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_get_ea_information)-structured input buffer specifying the extended attributes to be queried.

- **IrpSp->Parameters.QueryEa.EaListLength** is the length in bytes of the buffer pointed to by **IrpSp->Parameters.QueryEa.EaList**.

- **IrpSp->Parameters.QueryEa.Length** is the length in bytes of the output buffer.

## Remarks

When a short buffer is supplied and STATUS_BUFFER_OVERFLOW is returned, NTFS returns the last whole FILE_FULL_EA_INFORMATION entry that fits. When a short buffer is supplied and STATUS_BUFFER_TOO_SMALL is returned, NTFS couldn't fit any FILE_FULL_EA_INFORMATION entries.

On Windows Vista and later, FAT16 no longer supports extended attributes.

## See also

[**FILE_FULL_EA_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_full_ea_information)

[**FILE_GET_EA_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_get_ea_information)

[**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoCheckEaBufferValidity**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocheckeabuffervalidity)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[**IRP_MJ_SET_EA**](irp-mj-set-ea.md)
