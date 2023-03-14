---
title: FSCTL_QUERY_FILE_LAYOUT control code
description: The FSCTL_QUERY_FILE_LAYOUT control code retrieves file layout information for a file system volume.
keywords: ["FSCTL_QUERY_FILE_LAYOUT control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_QUERY_FILE_LAYOUT
api_location:
- Ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FSCTL_QUERY_FILE_LAYOUT control code

The FSCTL_QUERY_FILE_LAYOUT control code retrieves file layout information for a file system volume. The results of this request are a collection of file layout information entries. The type of entries returned is controlled by setting inclusion flags in the [**QUERY_FILE_LAYOUT_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_query_file_layout_input) structure. You can optionally filter the results by providing a set of file extents to restrict the selection of layout information.

To perform this operation, call [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with the following parameters.

## Parameters

- **FileObject** [in]: [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. A file object pointer for the file system volume. This parameter is required and cannot be **NULL**.

- **FileHandle** [in]: [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) only. A file handle for the file system volume. This parameter is required and cannot be **NULL**.

- **FsControlCode** [in]: The control code for the operation. Use The FSCTL_QUERY_FILE_LAYOUT control code for this operation.

- **InputBuffer** [in]: A pointer to a caller-allocated [**QUERY_FILE_LAYOUT_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_query_file_layout_input) structure. This structure contains the selection options. The optional file extents are included after **QUERY_FILE_LAYOUT_INPUT**.

- **InputBufferLength** [in]: The size, in bytes, of the buffer pointed to by the *InputBuffer* parameter. The size of *InputBuffer* must be at least **sizeof**(QUERY_FILE_LAYOUT_INPUT) + (**sizeof**(*Filter*) \* (*NumberOfPairs* - 1)), when *NumberOfPairs* &gt; 0. Otherwise, set *InputBufferLength* = **sizeof**(QUERY_FILE_LAYOUT_INPUT).

- **OutputBuffer** [out]: A pointer to a caller-allocated [**QUERY_FILE_LAYOUT_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_query_file_layout_output) structure. This is the header for the file layout entries that follow in this buffer.

- **OutputBufferLength** [out]: The size, in bytes, of the buffer pointed to by the *OutputBuffer* parameter. The size of *OutputBuffer* must be large enough to contain a [**QUERY_FILE_LAYOUT_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_query_file_layout_output) along with the file layout and stream layout structures returned.

## Status block

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) returns STATUS_SUCCESS or an appropriate NTSTATUS value, such as one of these values:

| Code | Meaning |
| ---- | ------- |
| STATUS_INVALID_PARAMETER | The file system volume is not an open user volume, or a buffer length value is incorrect, or an invalid query option is set. |
| STATUS_ACCESS_DENIED | The caller cannot access the file system volume. |
| STATUS_INVALID_USER_BUFFER | The pointer for either **InputBuffer** or **OutputBuffer** is not properly aligned. |
| STATUS_BUFFER_TOO_SMALL | The value in **OutputBufferLength** indicates that **OutputBuffer** is too small to contain at least one layout entry. |
| STATUS_END_OF_FILE | The pointer for either **InputBuffer** or **OutputBuffer** is not properly aligned. |

## Remarks

To retrieve all the layout entries for a volume, the FSCTL_QUERY_FILE_LAYOUT request is issued multiple times until **STATUS_END_OF_FILE** is returned. While **STATUS_SUCCESS** is returned, a caller can continue to send an FSCTL_QUERY_FILE_LAYOUT request for the remaining layout entries.

The enumeration of layout entries may be restarted at any time by including the **QUERY_FILE_LAYOUT_RESTART** flag in the **Flags** member of [**QUERY_FILE_LAYOUT_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_query_file_layout_input). Also, after FSCTL_QUERY_FILE_LAYOUT has returned **STATUS_END_OF_FILE**, it is necessary to include the **QUERY_FILE_LAYOUT_RESTART** flag in the next FSCTL_QUERY_FILE_LAYOUT request to begin another layout entry enumeration.

This code is not supported by ReFS.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Minimum supported client | Windows 8.1 Update |
| Header | *Ntifs.h* (include *Ntifs.h* or *Fltkernel.h*) |

## See also

[**QUERY_FILE_LAYOUT_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_query_file_layout_input)

[**QUERY_FILE_LAYOUT_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_query_file_layout_output)

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile)

[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85))
