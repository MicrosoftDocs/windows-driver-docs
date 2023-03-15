---
title: FSCTL_OPLOCK_BREAK_NOTIFY control code
description: The FSCTL_OPLOCK_BREAK_NOTIFY control code allows the calling application to wait for completion of an opportunistic lock (oplock) break.
keywords: ["FSCTL_OPLOCK_BREAK_NOTIFY control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_OPLOCK_BREAK_NOTIFY
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FSCTL_OPLOCK_BREAK_NOTIFY control code

The **FSCTL_OPLOCK_BREAK_NOTIFY** control code allows the calling application to wait for completion of an opportunistic lock (oplock) break.

This operation is useful only for an oplock break that was already initiated when the caller's handle was opened. The handle must have been opened with FILE_COMPLETE_IF_OPLOCKED. This operation is meaningless if an oplock is currently held and the oplock break has not started.

To process this control code, a minifilter calls [**FltOplockFsctrl**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltoplockfsctrl) with the following parameters. A file system or legacy filter driver calls [**FsRtlOplockFsctrl**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtloplockfsctrl).

For more information about opportunistic locking and about the **FSCTL_OPLOCK_BREAK_NOTIFY** control code, see the Microsoft Windows SDK documentation.

## Parameters

- **Oplock**: Opaque oplock object pointer for the file.

- **CallbackData**: [**FltOplockFsctrl**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltoplockfsctrl) only. Callback data ([**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure for an IRP_MJ_FILE_SYSTEM_CONTROL FSCTL request. The **FsControlCode** parameter for the operation must be FSCTL_OPLOCK_BREAK_NOTIFY.

- **Irp**: [**FsRtlOplockFsctrl**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtloplockfsctrl) only. IRP for an IRP_MJ_FILE_SYSTEM_CONTROL FSCTL request. The **FsControlCode** parameter for the operation must be FSCTL_OPLOCK_BREAK_NOTIFY.

- **OpenCount**: Not used with this operation; set to zero.

## Status block

[**FltOplockFsctrl**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltoplockfsctrl) returns FLT_PREOP_PENDING if the oplock break is underway, and the IRP will be completed when the oplock break completes. (In this case, the IRP can eventually complete with either STATUS_SUCCESS or STATUS_CANCELLED.) Otherwise, **FltOplockFsctrl** returns FLT_PREOP_COMPLETE.

[**FsRtlOplockFsctrl**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtloplockfsctrl) returns one of the following NTSTATUS values for this operation:

| Code | Meaning |
| ---- | ------- |
| STATUS_SUCCESS | No oplock was held by this handle, or an oplock is held and the oplock break has not started. |
| STATUS_INVALID_OPLOCK_PROTOCOL | The IRP was canceled before the FSCTL_OPLOCK_BREAK_NOTIFY operation was completed. |
| STATUS_PENDING | The oplock break is underway. The IRP will be completed when the oplock break completes. The IRP can eventually complete with either STATUS_SUCCESS or STATUS_CANCELLED. This is a success code. |

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

[**FSCTL_REQUEST_BATCH_OPLOCK**](fsctl-request-batch-oplock.md)

[**FSCTL_REQUEST_FILTER_OPLOCK**](fsctl-request-filter-oplock.md)

[**FSCTL_REQUEST_OPLOCK_LEVEL_1**](fsctl-request-oplock-level-1.md)

[**FSCTL_REQUEST_OPLOCK_LEVEL_2**](fsctl-request-oplock-level-2.md)

[**FsRtlOplockFsctrl**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtloplockfsctrl)

[**IRP_MJ_FILE_SYSTEM_CONTROL**](irp-mj-file-system-control.md)
