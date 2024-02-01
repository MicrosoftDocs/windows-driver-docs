---
title: FSCTL_SET_ZERO_DATA Control Code
description: The FSCTL_SET_ZERO_DATA control code fills a specified range of a file with zeros (0).
keywords: ["FSCTL_SET_ZERO_DATA control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_SET_ZERO_DATA
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FSCTL_SET_ZERO_DATA control code

The **FSCTL_SET_ZERO_DATA** control code fills a specified range of a file with zeros (0). If the file is sparse or compressed, the NTFS file system may deallocate disk space in the file. This sets the range of bytes to zeros (0) without extending the file size.

To perform this operation from a driver, call [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) with the following parameters.

## Parameters

- **Instance**: Opaque instance pointer for the caller. This parameter is required and cannot be **NULL**.

- **FileObject** [in]: File object pointer to the file in which to write zeros to. This parameter is required and cannot be **NULL**.

- **FsControlCode** [in]: The control code for the operation.

Use **FSCTL_SET_ZERO_DATA** for this operation.

- **InputBuffer** [in]: A pointer to a [**FILE_ZERO_DATA_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_zero_data_information) or [**FILE_ZERO_DATA_INFORMATION_EX**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_zero_data_information_ex) structure that specifies the range of the file to set to zeros.

The **FileOffset** member is the byte offset of the first byte to set to zeros (0), and the **BeyondFinalZero** member is the byte offset of the first byte beyond the last zero (0) byte.

The **Flags** member in [**FILE_ZERO_DATA_INFORMATION_EX**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_zero_data_information_ex) specifies modifiers to the operation. For example, when **Flags** is set to **FILE_ZERO_DATA_INFORMATION_FLAG_PRESERVE_CACHED_DATA**, the contents of the cache corresponding to this range of the file are not purged.

- **InputBufferLength** [in]: The size of the input buffer, in bytes.

- **OutputBuffer** [out]: Not used with this operation; set to **NULL**.

- **OutputBufferLength** [out]: Not used with this operation; set to zero.

## Status block

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) returns **STATUS_SUCCESS** or an appropriate NTSTATUS value.

| Return code | Meaning |
| ----------- | ------- |
| **STATUS _INSUFFICIENT_RESOURCES** | There is not enough memory to complete the operation. |
| **STATUS_INVALID_PARAMETER**       | The **InputBufferLength** is smaller than the size of the **FILE_ZERO_DATA_INFORMATION** structures or the file specified is a system metadata file or a directory. |
| **STATUS_ACCESS_DENIED**           | The **FILE_ZERO_DATA_INFORMATION_FLAG_PRESERVE_CACHED_DATA** is set from user mode. |
| **STATUS_MEDIA_WRITE_PROTECTED**   | The volume is currently write protected. |

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Ntifs.h* (include *Ntifs.h*) |

## See also

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile)

[**FILE_ZERO_DATA_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_zero_data_information)

[**FILE_ZERO_DATA_INFORMATION_EX**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_zero_data_information_ex)
