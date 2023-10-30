---
title: FSCTL_MARK_VOLUME_DIRTY control code
description: The FSCTL_MARK_VOLUME_DIRTY control code marks a specified volume as dirty, which triggers Autochk.exe to run on the volume during the next system restart.
keywords: ["FSCTL_MARK_VOLUME_DIRTY control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_MARK_VOLUME_DIRTY
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FSCTL_MARK_VOLUME_DIRTY control code

The **FSCTL_MARK_VOLUME_DIRTY** control code marks a specified volume as dirty, which triggers Autochk.exe to run on the volume during the next system restart.

To perform this operation, call [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with the following parameters.

## Parameters

- **Instance** [in]: [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. An opaque instance pointer to the minifilter driver instance that is initiating the FSCTL request.

- **FileObject** [in]: [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. A file pointer object specifying the volume to be marked dirty. This parameter is required and cannot be **NULL**.

- **FileHandle** [in]: [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) only. A handle to the volume that is to be marked dirty. This parameter is required and cannot be **NULL**.

- **FsControlCode** [in]: Control code for the operation. Use **FSCTL_MARK_VOLUME_DIRTY** for this operation.

- **InputBuffer** [in]: Not used with this operation. Set to **NULL**.

- **InputBufferLength** [in]: Not used with this operation. Set to 0.

- **OutputBuffer** [out]: Not used with this operation. Set to **NULL**.

- **OutputBufferLength** [out]: Not used with this operation. Set to 0.

## Status block

The [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) routine returns STATUS_SUCCESS or an appropriate NTSTATUS value.

| Code | Meaning |
| ---- | ------- |
| STATUS_INVALID_PARAMETER | The **FileObject** or **FileHandle** does not represent a valid volume handle or another parameter is invalid. |
| STATUS_ACCESS_DENIED | The caller does not have SE_MANAGE_VOLUME access rights. |
| STATUS_VOLUME_DISMOUNTED | The file system volume is dismounted. |
| STATUS_TOO_LATE | The file system volume is shut down. |
| STATUS_MEDIA_WRITE_PROTECTED | The file system volume is read-only. |

## Remarks

This code is not supported by ReFS.

## Requirements

<| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Ntifs.h* (include *Ntifs.h* or *FltKernel.h*) |

## See also

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile)

[**FSCTL_IS_VOLUME_DIRTY**](fsctl-is-volume-dirty.md)

[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85))
