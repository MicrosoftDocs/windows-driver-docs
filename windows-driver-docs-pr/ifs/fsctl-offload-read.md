---
title: FSCTL_OFFLOAD_READ Control Code
description: The FSCTL_OFFLOAD_READ control code initiates an offload read for a block of data in a storage system that supports offload read primitives.
keywords: ["FSCTL_OFFLOAD_READ control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_OFFLOAD_READ
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FSCTL_OFFLOAD_READ control code

The **FSCTL_OFFLOAD_READ** control code initiates an offload read for a block of data in a storage system that supports offload read primitives.

To perform this operation, call [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with the following parameters.

## Parameters

- **Instance** [in]: [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. An opaque instance pointer for the caller. This parameter is required and cannot be NULL.

- **FileObject** [in]: [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. The file pointer object specifying the file to read from. This parameter is required and cannot be NULL.

- **FileHandle** [in]: [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) only. The file handle of the file to read from. This parameter is required and cannot be NULL.

- **FsControlCode** [in]: The control code for the operation. Use **FSCTL_OFFLOAD_READ** for this operation.

- **InputBuffer** [in]: A pointer to a [**FSCTL_OFFLOAD_READ_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsctl_offload_read_input) structure, which contains the size and offset of a data block to read.

- **InputBufferLength** [in]: The size, in bytes, of the buffer pointed to by **InputBuffer**. This value is **sizeof**(FSCTL_OFFLOAD_READ_INPUT).

- **OutputBuffer** [out]: A pointer to a [**FSCTL_OFFLOAD_READ_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsctl_offload_read_output) structure, which receives the results of the offload read operation.

- **OutputBufferLength** [out]: The size, in bytes, of the buffer pointed to by the **OutputBuffer** parameter. This value must be at least **sizeof**(FSCTL_OFFLOAD_READ_OUTPUT).

## Status block

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) returns STATUS_SUCCESS if the operation succeeds. Otherwise, the appropriate function might return one of the following NTSTATUS values.

| Code | Meaning |
| ---- | ------- |
| STATUS_INVALID_DEVICE_REQUEST | The handle specified is not a valid file handle |
| STATUS_INVALID_PARAMETER | A parameter is invalid. See Remarks. |
| STATUS_VOLUME_DISMOUNTED | The file system volume is dismounted. |
| STATUS_NOT_SUPPORTED | Offload read operations are not supported on this volume. |
| STATUS_OFFLOAD_READ_FILE_NOT_SUPPORTED | The requested file type is not supported. Offload operations are not supported on these file types: A transacted file (TxF); Non-user files; Compressed files; Encrypted files; Sparse files; NTFS Metatdata files. |
| STATUS_FILE_DELETED | The data stream for this file is invalid. |
| STATUS_FILE_CLOSED | The file handle is closed. |
| STATUS_INVALID_HANDLE | The file handle specified is invalid. |
| STATUS_FILE_LOCK_CONFLICT | Insufficient read access due to the current file locking state. |
| STATUS_END_OF_FILE | The **FileOffset** member of [**FSCTL_OFFLOAD_READ_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsctl_offload_read_input) begins after end-of-file (EOF). |
| STATUS_DISMOUNTED_VOLUME | An offload read cannot occur on a dismounted volume. |
| STATUS_INSUFFICIENT_RESOUCES | Insufficient resources are available to complete the request. |
| STATUS_BUFFER_TOO_SMALL | **OutputBufferLength** is too small for **OutputBuffer** to receive an [**FSCTL_OFFLOAD_READ_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsctl_offload_read_output) structure. |

## Remarks

Offload read is available for normal files only. See the description for **STATUS_OFFLOAD_READ_FILE_NOT_SUPPORTED** for a list of unsupported file types.

It is possible for reads to start beyond the Valid Data Length (VDL), but not beyond EOF.

When STATUS_INVALID_PARAMETER is returned, the error could be one of the following invalid parameters:

- File size is less than PAGE_SIZE.
- **InputBufferLength** < ```sizeof(FSCTL_OFFLOAD_READ_INPUT)```.
- One or more of these members of [**FSCTL_OFFLOAD_READ_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsctl_offload_read_input) are incorrect:
  - **FileOffset** is not a multiple of the logical sector size of the volume.
  - **CopyLength** is not a multiple of the logical sector size of the volume.
  - **Size** is not the size of the [**FSCTL_OFFLOAD_READ_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsctl_offload_read_input) structure.
  - **FileOffset** + **CopyLength** > **MAXULONGLONG**.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Minimum supported client | Windows 8 |
| Header | *Ntifs.h* (include *Ntifs.h* or *Fltkernel.h*) |

## See also

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile)

[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85))

[**FSCTL_OFFLOAD_READ_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsctl_offload_read_input)

[**FSCTL_OFFLOAD_READ_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsctl_offload_read_output)
