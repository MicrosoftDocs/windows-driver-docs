---
title: FSCTL_OFFLOAD_WRITE Control Code
description: The FSCTL_OFFLOAD_WRITE control code initiates an offload write for a block of data in a storage system that supports offload write primitives.
keywords: ["FSCTL_OFFLOAD_WRITE control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_OFFLOAD_WRITE
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FSCTL_OFFLOAD_WRITE control code

The **FSCTL_OFFLOAD_WRITE** control code initiates an offload write for a block of data in a storage system that supports offload write primitives.

To perform this operation, minifilter drivers call [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) with the following parameters, and file systems, redirectors, and legacy file system filter drivers call [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with the following parameters.

## Parameters

- **Instance** [in]: [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. An opaque instance pointer for the caller. This parameter is required and cannot be NULL.

- **FileObject** [in]: [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. The file pointer object specifying the file to write to. This parameter is required and cannot be NULL.

- **FileHandle** [in]: [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) only. The file handle of the file to write to. This parameter is required and cannot be NULL.

- **FsControlCode** [in]: The control code for the operation. Use **FSCTL_OFFLOAD_WRITE** for this operation.

- **InputBuffer** [in]: A pointer to a [**FSCTL_OFFLOAD_WRITE_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsctl_offload_write_input) structure, which contains the size and offset of a data block to read.

- **InputBufferLength** [in]: The size, in bytes, of the buffer pointed to by *InputBuffer*. This value is **sizeof**(FSCTL_OFFLOAD_WRITE_INPUT).

- **OutputBuffer** [out]: A pointer to a [**FSCTL_OFFLOAD_WRITE_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsctl_offload_write_input) structure, which contains the size and offset of a data block to read.

- **OutputBufferLength** [out]: The size, in bytes, of the buffer pointed to by the *OutputBuffer* parameter. This value must be at least **sizeof**(FSCTL_OFFLOAD_READ_OUTPUT).

## Status block

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) returns STATUS_SUCCESS if the operation succeeds. Otherwise, the appropriate function might return one of the following NTSTATUS values.

| Code | Meaning |
| ---- | ------- |
| STATUS_INVALID_DEVICE_REQUEST | The handle specified is not a valid file handle. |
| STATUS_INVALID_PARAMETER | A parameter is invalid. See Remarks. |
| STATUS_NOT_SUPPORTED | Offload read operations are not supported on this volume. |
| STATUS_OFFLOAD_WRITE_FILE_NOT_SUPPORTED | The requested file type is not supported. Offload operations are not supported on these file types: A transacted file (TxF); Non-user files; Compressed files; Encrypted files; Sparse files; NTFS Metatdata files. |
| STATUS_TOO_LATE | A write operation was attempted to a volume after it was dismounted. |
| STATUS_FILE_DELETED | The data stream for this file is invalid. |
| STATUS_FILE_CLOSED | The file handle is closed. |
| STATUS_INVALID_HANDLE | The file handle specified is invalid. |
| STATUS_FILE_LOCK_CONFLICT | Read or write access cannot be granted due to the current file locking state. |
| STATUS_END_OF_FILE | The **FileOffset** member of[**FSCTL_OFFLOAD_WRITE_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsctl_offload_write_input) begins after end-of-file (EOF). |
| STATUS_DISMOUNTED_VOLUME | An offload write cannot occur on a dismounted volume. |
| STATUS_MEDIA_WRITE_PROTECTED | The volume is read only. |
| STATUS_INSUFFICIENT_RESOUCES | Insufficient resources are available to complete the request. |
| STATUS_BUFFER_TOO_SMALL | **InputBufferLength** is too small for **InputBuffer** to contain an[**FSCTL_OFFLOAD_WRITE_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsctl_offload_write_input) structure, or **OutputBufferLength** is too small for **OutputBuffer** to receive an [**FSCTL_OFFLOAD_WRITE_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsctl_offload_write_output) structure. |

## Remarks

Offload read is available for normal files only. See the description for **STATUS_OFFLOAD_WRITE_FILE_NOT_SUPPORTED** for a list of unsupported file types.

When STATUS_INVALID_PARAMETER is returned, the error could be one of the following invalid parameters:

- File size is less than PAGE_SIZE.
- **InputBufferLength** < ```sizeof(FSCTL_OFFLOAD_READ_OUTPUT)```.
- One or more of these members of[**FSCTL_OFFLOAD_WRITE_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsctl_offload_write_input) are incorrect:</p>
**FileOffset** is not a multiple of the logical sector size of the volume.
**CopyLength** is not a multiple of the logical sector size of the volume.
**TransferOffset** is not a multiple of the logical sector size of the volume.
**Size** is not the size of the[**FSCTL_OFFLOAD_WRITE_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsctl_offload_write_input) structure.
**FileOffset** &gt; Valid Data Length (VDL) for the file.
**FileOffset** + **CopyLength** &gt; **MAXULONGLONG**.</td>

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Minimum supported client | Windows 8 |
| Header | *Ntifs.h* (include *Ntifs.h* or *Fltkernel.h*) |

## See also

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile)

[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85))

[**FSCTL_OFFLOAD_WRITE_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsctl_offload_write_input)

[**FSCTL_OFFLOAD_WRITE_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsctl_offload_write_output)
