---
title: IRP_MJ_SET_QUOTA (FS and Filter Drivers)
description: IRP_MJ_SET_QUOTA
keywords: ["IRP_MJ_SET_QUOTA Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_SET_QUOTA
api_type:
- NA
ms.date: 03/13/2023
ms.topic: reference
---

# IRP_MJ_SET_QUOTA (FS and filter drivers)

## When Sent

The I/O Manager sends the IRP_MJ_SET_QUOTA request. It can be sent, for example, when a user-mode application has called a Win32 method such as **IDiskQuotaControl::SetQuotaState**.

## Operation: File System Drivers

IRP_MJ_SET_QUOTA and IRP_MJ_QUERY_QUOTA existed in Windows NT 4.0 but weren't used by file systems. On Windows 2000 and later systems, they're used for disk quota support in NTFS. Support for these IRPs by new file systems is optional.

## Operation: Legacy File System Filter Drivers

The filter driver should pass this IRP down to the next-lower driver on the stack, unless it needs to explicitly override quota behavior.

## Parameters

A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) for the given IRP to get a pointer to its own stack location in the IRP. In the following parameters, **Irp** points to the [**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp) and **IrpSp** points to the [**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location). The driver can use the information that is set in the following members of the IRP and the IRP stack location to process a set quota information request:

- **DeviceObject** is a pointer to the target device object.

- **DeviceObject->Flags** : If the DO_BUFFERED_IO flag is set, the caller has requested METHOD_BUFFERED I/O. Otherwise, the caller has requested METHOD_NEITHER I/O.

- **Irp->AssociatedIrp.SystemBuffer** points to a system-supplied buffer to be used as an intermediate system buffer, if the DO_BUFFERED_IO flag is set in **DeviceObject->Flags**. Otherwise, this member is set to **NULL**.

- **Irp->IoStatus** points to an [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation.

- **Irp->UserBuffer** points to a caller-supplied buffer that contains the quota entries to be added or modified for the volume.

- **IrpSp->FileObject** points to the file object that is associated with **DeviceObject**.

The *IrpSp->FileObject* parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE_OBJECT structure. The **RelatedFileObject** field of the FILE_OBJECT structure isn't valid during the processing of IRP_MJ_SET_QUOTA and shouldn't be used.

- **IrpSp->MajorFunction** is set to IRP_MJ_SET_QUOTA.

- **IrpSp->Parameters.SetQuota.Length** is the length, in bytes, of the buffer pointed to by **Irp->UserBuffer**.

## See also

[**FILE_QUOTA_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_quota_information)

[**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoCheckQuotaBufferValidity**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocheckquotabuffervalidity)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[**IRP_MJ_QUERY_QUOTA**](irp-mj-query-quota.md)
