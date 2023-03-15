---
title: FSCTL_IS_VOLUME_DIRTY control code
description: The FSCTL_IS_VOLUME_DIRTY control code determines whether the specified volume is dirty.
keywords: ["FSCTL_IS_VOLUME_DIRTY control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_IS_VOLUME_DIRTY
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FSCTL_IS_VOLUME_DIRTY control code

The **FSCTL_IS_VOLUME_DIRTY** control code determines whether the specified volume is dirty.

If the volume information file is corrupted, NTFS will return STATUS_FILE_CORRUPT_ERROR.

To perform this operation, minifilter drivers call [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) with the following parameters, and file systems, redirectors, and legacy file system filter drivers call [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with the following parameters.

## Parameters

- **FileObject** [in]: [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. File object pointer for the volume. This parameter must represent a user volume open of a mounted file system volume. This parameter is required and cannot be **NULL**.

- **FileHandle** [in]: [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) only. Handle for the volume. This parameter must be a handle for a user volume open of a mounted file system volume. This parameter is required and cannot be **NULL**.

- **FsControlCode** [in]: Control code for the operation. Use FSCTL_IS_VOLUME_DIRTY for this operation.

- **InputBuffer** [in]: Not used with this operation; set to **NULL**.

- **InputBufferLength** [in]: Not used with this operation; set to zero.

- **OutputBuffer** [out]: Pointer to a caller-allocated, 32-bit-aligned buffer that receives a ULONG bitmask of flags that indicate whether the volume is currently dirty. One or more of the flags in the following table can be set.

  | Value | Meaning |
  | ----- | ------- |
  | VOLUME_IS_DIRTY | The volume is dirty. |
  | VOLUME_UPGRADE_SCHEDULED | This value is not currently used. |
  | All other values | Reserved for future use. |

- **OutputBufferLength** [out]: Size, in bytes, of the buffer that is pointed to by the *OutputBuffer* parameter. This size must be at least sizeof(ULONG).

## Status block

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) returns STATUS_SUCCESS if the operation succeeds. Otherwise, the appropriate function might return one of the following NTSTATUS values:

| Code | Meaning |
| ---- | ------- |
| STATUS_INSUFFICIENT_RESOURCES | The file system encountered a pool allocation failure. This is an error code. |
| STATUS_INVALID_PARAMETER | The buffer that the **OutputBuffer** parameter points to is NULL, or the **FileHandle** or **FileObject** parameter does not represent a user volume open. This is an error code. |
| STATUS_INVALID_USER_BUFFER | The buffer that the **OutputBuffer** parameter points to is not large enough to hold the reparse point data, or the **FileHandle** or **FileObject** parameter does not represent a user volume open. This is an error code. |
| STATUS_VOLUME_DISMOUNTED | The volume is not mounted. This is an error code. |

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Ntifs.h* (include *Ntifs.h* or *Fltkernel.h*) |

## See also

[**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT_PARAMETERS for IRP_MJ_FILE_SYSTEM_CONTROL**](flt-parameters-for-irp-mj-file-system-control.md)

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile)

[**IRP_MJ_FILE_SYSTEM_CONTROL**](irp-mj-file-system-control.md)

[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85))
