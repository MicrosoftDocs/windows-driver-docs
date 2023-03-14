---
title: FSCTL_GET_RETRIEVAL_POINTER_BASE control code
description: The FSCTL_GET_RETRIEVAL_POINTER_BASE returns the sector offset to the first logical cluster number (LCN) of the file system relative to the start of the volume.
keywords: ["FSCTL_GET_RETRIEVAL_POINTER_BASE control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_GET_RETRIEVAL_POINTER_BASE
api_location:
- Ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FSCTL_GET_RETRIEVAL_POINTER_BASE control code

The **FSCTL_GET_RETRIEVAL_POINTER_BASE** returns the sector offset to the first logical cluster number (LCN) of the file system relative to the start of the volume.

To perform this operation, call the [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) function or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) function with the following parameters.

## Parameters

- **FileObject** [in]: [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. A file object pointer for the volume for which **FSCTL_GET_RETRIEVAL_POINTER_BASE** is to retrieve the base. This parameter is required and cannot be **NULL**.

- **FileHandle** [in]: [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) only. A file handle for the volume for which **FSCTL_GET_RETRIEVAL_POINTER_BASE** is to retrieve the base. This parameter is required and cannot be **NULL**.

This handle must be opened with the SE_MANAGE_VOLUME_NAME access rights. For more information, see [File Security and Access Rights](/windows/desktop/FileIO/file-security-and-access-rights).

- **FsControlCode** [in]: A control code for the operation. Use **FSCTL_GET_RETRIEVAL_POINTER_BASE** for this operation.

- **InputBuffer** [in]: Not used with this operation. Set to **NULL**.

- **InputBufferLength** [in]: Not used with this operation. Set to zero.

- **OutputBuffer** [out]: A pointer to a LARGE_INTEGER, which receives the sector offset to the first LCN of the file system relative to the start of the volume.

- **OutputBufferLength** [out]: The size of the output buffer, in bytes. This value must be 8.

## Status block

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following:

| Code | Meaning |
| ---- | ------- |
| STATUS_SUCCESS | The operation was successful. OutputBuffer contains the sector offset to the first LCN of the file system relative to the start of the volume. |
| STATUS_ACCESS_DENIED | The user does not have SE_MANAGE_VOLUME access. |
| STATUS_BUFFER_TOO_SMALL | OutputBuffer is not large enough for the result. No information has been written to the buffer. |
| STATUS_INVALID_PARAMETER | A parameter was not valid; for example, the handle used is not a valid volume handle. |

## Remarks

Adding the value retrieved by FSCTL_GET_RETRIEVAL_POINTER_BASE to the value retrieved by the FSCTL_GET_RETRIEVAL_POINTERS control code results in a volume-relative file extent offset.

The FSCTL_GET_RETRIEVAL_POINTER_BASE control code can be used on FastFAT and exFAT devices. This capability supports the use of BitLocker for devices such as flash drives.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Minimum supported client | Windows 7 |
| Minimum supported server | Windows Server 2008 R2 |
| Header | *Ntifs.h* (include *Ntifs.h* or *Fltkernel.h*) |

## See also

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile)

[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85))
