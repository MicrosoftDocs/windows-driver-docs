---
title: FSCTL_SET_REPARSE_POINT Control Code
description: The FSCTL_SET_REPARSE_POINT control code sets a reparse point on a file or directory.
keywords: ["FSCTL_SET_REPARSE_POINT control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_SET_REPARSE_POINT
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FSCTL_SET_REPARSE_POINT control code

The FSCTL_SET_REPARSE_POINT control code sets a reparse point on a file or directory.

To perform this operation, call [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with the following parameters.

Minifilters should use [**FltTagFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-flttagfile) instead of FSCTL_SET_REPARSE_POINT to set a reparse point.

For more information about reparse points and the FSCTL_SET_REPARSE_POINT control code, see the Microsoft Windows SDK documentation.

## Parameters

- **FileHandle** [in]: File handle for the file or directory on which to set a reparse point. This parameter is required and cannot be **NULL**.

- **FsControlCode** [in]: Control code for the operation. Use FSCTL_SET_REPARSE_POINT for this operation.

- **InputBuffer** [in]: Pointer to a caller-allocated [**REPARSE_GUID_DATA_BUFFER**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_reparse_guid_data_buffer) or [**REPARSE_DATA_BUFFER**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_reparse_data_buffer) structure that contains the reparse point data. If an existing reparse point is being modified, the tag specified in the **ReparseTag** member of this structure must match the tag of the reparse point to be modified. In addition, if the reparse point is a third-party (non-Microsoft) reparse point, the GUID specified in the **ReparseGuid** member of the structure is a REPARSE_GUID_DATA_BUFFER structure must match the GUID of the reparse point to be modified.

- **InputBufferLength** [in]: Size, in bytes, of the buffer pointed to by the *InputBuffer* parameter. For a REPARSE_GUID_DATA_BUFFER structure, this value must be at least REPARSE_GUID_DATA_BUFFER_HEADER_SIZE, plus the size of the user-defined data, and it must be less than or equal to MAXIMUM_REPARSE_DATA_BUFFER_SIZE. For a REPARSE_DATA_BUFFER structure, this value must be at least REPARSE_DATA_BUFFER_HEADER_SIZE, plus the size of the user-defined data, and it must be less than or equal to MAXIMUM_REPARSE_DATA_BUFFER_SIZE.

- **OutputBuffer** [out]: Not used with this operation; set to **NULL**.

- **OutputBufferLength** [out]: Not used with this operation; set to zero.

## Status block

[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following:

| Code | Meaning |
| ---- | ------- |
| STATUS_DIRECTORY_NOT_EMPTY | A reparse point cannot be set on a nonempty directory. This is an error code. |
| STATUS_EAS_NOT_SUPPORTED | A reparse point cannot be set on a file if this request is in a transaction. This is an error code. |
| STATUS_IO_REPARSE_DATA_INVALID | One of the specified parameter values was invalid. This is an error code. |
| STATUS_IO_REPARSE_TAG_MISMATCH | The reparse tag specified by the caller did not match the tag of the reparse point to be modified. This is an error code. |
| STATUS_NOT_A_REPARSE_POINT | The file or directory is not a reparse point. This is an error code. |
| STATUS_REPARSE_ATTRIBUTE_CONFLICT | The reparse point is a third-party reparse point, and the reparse GUID specified by the caller did not match the GUID of the reparse point to be modified. This is an error code. |

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Ntifs.h* (include *Ntifs.h* or *Fltkernel.h*) |

## See also

[**FLT_PARAMETERS for IRP_MJ_FILE_SYSTEM_CONTROL**](flt-parameters-for-irp-mj-file-system-control.md)

[**FltTagFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-flttagfile)

[**FltUntagFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltuntagfile)

[**FSCTL_DELETE_REPARSE_POINT**](fsctl-delete-reparse-point.md)

[**FSCTL_GET_REPARSE_POINT**](fsctl-get-reparse-point.md)

[**IRP_MJ_FILE_SYSTEM_CONTROL**](irp-mj-file-system-control.md)

[**IsReparseTagMicrosoft**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-isreparsetagmicrosoft)

[**IsReparseTagNameSurrogate**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-isreparsetagnamesurrogate)

[**REPARSE_DATA_BUFFER**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_reparse_data_buffer)

[**REPARSE_GUID_DATA_BUFFER**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_reparse_guid_data_buffer)

[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85))
