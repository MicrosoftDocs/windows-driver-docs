---
title: FSCTL_MANAGE_BYPASS_IO control code
description: The FSCTL_MANAGE_BYPASS_IO control code performs a BypassIO operation on the specified file handle.
keywords: ["FSCTL_MANAGE_BYPASS_IO control code"]
topic_type:
- apiref
api_name:
- FSCTL_MANAGE_BYPASS_IO
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 06/29/2021
ms.localizationpriority: medium
---

# FSCTL_MANAGE_BYPASS_IO control code

The FSCTL_MANAGE_BYPASS_IO control code controls BypassIO operations on a given file in the filter and file system stacks.

To perform this operation, call [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with the following parameters.

**Parameters**

*FileHandle*  
For [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) only. File handle for the file on which to perform a BypassIO operation. This parameter is required and cannot be **NULL**.

*FsControlCode*  
A control code for the operation. Use **FSCTL_MANAGE_BYPASS_IO** for this operation.

*InputBuffer*  
A pointer to a caller-allocated [**FS_BPIO_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-fs_bpio_input.md) structure.

*InputBufferLength*  
Size of the buffer that *InputBuffer* points to, in bytes.

*OutputBuffer*

A pointer to a caller-allocated [**FS_BPIO_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-fs_bpio_output.md) structure.

*OutputBufferLength*  
Size, in bytes, of the buffer pointed to by the *OutputBuffer* parameter. This value must be at least ```sizeof(FS_BPIO_OUTPUT)```

## Status block

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following:

| Value | Description |
| ----- | ----------- |
| STATUS_NOT_SUPPORTED | BypassIO is not supported. |
| STATUS_INVALID_BUFFER_SIZE | The input and/or output buffer size is invalid. |

## Requirements

|   |   |
| - | - |
| Header | Ntifs.h (include Ntifs.h or Fltkernel.h) |

## See also

[**FS_BPIO_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-fs_bpio_input.md)

[**FS_BPIO_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-fs_bpio_output.md)
