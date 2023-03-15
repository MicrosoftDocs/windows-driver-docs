---
title: FSCTL_REQUEST_FILTER_OPLOCK control code
description: The FSCTL_REQUEST_FILTER_OPLOCK control code requests a filter opportunistic lock (oplock) on a file.
keywords: ["FSCTL_REQUEST_FILTER_OPLOCK control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_REQUEST_FILTER_OPLOCK
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FSCTL_REQUEST_FILTER_OPLOCK control code

The **FSCTL_REQUEST_FILTER_OPLOCK** control code requests a filter opportunistic lock (oplock) on a file.

To process this control code, a minifilter calls [**FltOplockFsctrl**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltoplockfsctrl) with the following parameters. A file system or legacy filter driver calls [**FsRtlOplockFsctrl**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtloplockfsctrl).

For more information about opportunistic locking and about the **FSCTL_REQUEST_FILTER_OPLOCK** control code, see the Microsoft Windows SDK documentation.

## Parameters

- **Oplock**: Opaque oplock object pointer for the file.

- **CallbackData**: [**FltOplockFsctrl**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltoplockfsctrl) only. Callback data ([**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure for an IRP_MJ_FILE_SYSTEM_CONTROL FSCTL request. The *FsControlCode* parameter for the operation must be FSCTL_REQUEST_FILTER_OPLOCK.

- **Irp**: [**FsRtlOplockFsctrl**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtloplockfsctrl) only. IRP for an IRP_MJ_FILE_SYSTEM_CONTROL FSCTL request. The *FsControlCode* parameter for the operation must be FSCTL_REQUEST_FILTER_OPLOCK.

- **OpenCount**: Number of user handles for the file.

## Status block

[**FltOplockFsctrl**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltoplockfsctrl) returns FLT_PREOP_PENDING for this operation if the oplock was granted. Otherwise, it returns FLT_PREOP_COMPLETE.

[**FsRtlOplockFsctrl**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtloplockfsctrl) returns one of the following NTSTATUS values for this operation:

| Code | Meaning |
| ---- | ------- |
| STATUS_PENDING | The oplock was granted. This is a success code. |
| STATUS_CANCELLED | The IRP was canceled before the FSCTL_REQUEST_BATCH_OPLOCK operation was completed. This is an error code. |
| STATUS_OPLOCK_NOT_GRANTED | The oplock could not be granted. This is an error code. |

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Ntifs.h* (include *Ntifs.h* or *Fltkernel.h*) |

## See also

[**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[**FLT_PARAMETERS for IRP_MJ_FILE_SYSTEM_CONTROL**](flt-parameters-for-irp-mj-file-system-control.md)

[**FltOplockFsctrl**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltoplockfsctrl)

[**FSCTL_OPBATCH_ACK_CLOSE_PENDING**](fsctl-opbatch-ack-close-pending.md)

[**FSCTL_OPLOCK_BREAK_ACK_NO_2**](fsctl-oplock-break-ack-no-2.md)

[**FSCTL_OPLOCK_BREAK_ACKNOWLEDGE**](fsctl-oplock-break-acknowledge.md)

[**FSCTL_OPLOCK_BREAK_NOTIFY**](fsctl-oplock-break-notify.md)

[**FSCTL_REQUEST_BATCH_OPLOCK**](fsctl-request-batch-oplock.md)

[**FSCTL_REQUEST_OPLOCK_LEVEL_1**](fsctl-request-oplock-level-1.md)

[**FSCTL_REQUEST_OPLOCK_LEVEL_2**](fsctl-request-oplock-level-2.md)

[**FsRtlOplockFsctrl**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtloplockfsctrl)

[**IRP_MJ_FILE_SYSTEM_CONTROL**](irp-mj-file-system-control.md)
