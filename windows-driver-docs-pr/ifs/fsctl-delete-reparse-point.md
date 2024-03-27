---
title: FSCTL_DELETE_REPARSE_POINT Control Code
description: The FSCTL_DELETE_REPARSE_POINT control code deletes a reparse point from the specified file or directory. Using FSCTL_DELETE_REPARSE_POINT does not delete the file or directory.
keywords: ["FSCTL_DELETE_REPARSE_POINT control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_DELETE_REPARSE_POINT
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FSCTL_DELETE_REPARSE_POINT control code

The FSCTL_DELETE_REPARSE_POINT control code deletes a reparse point from the specified file or directory. Using FSCTL_DELETE_REPARSE_POINT does not delete the file or directory.

To perform this operation, call [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with the following parameters.

Minifilters should use [**FltUntagFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltuntagfile) instead of FSCTL_DELETE_REPARSE_POINT to delete a reparse point.

For more information about reparse points and the FSCTL_DELETE_REPARSE_POINT control code, see the Microsoft Windows SDK documentation.

## Parameters

- **FileHandle** [in]: File handle for the file or directory from which the reparse point is to be deleted. The caller must have write access to the file or directory. This parameter is required and cannot be **NULL**.

- **FsControlCode** [in]: Control code for the operation. Use FSCTL_DELETE_REPARSE_POINT for this operation.

- **InputBuffer** [in]: Pointer to a [**REPARSE_GUID_DATA_BUFFER**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_reparse_guid_data_buffer) or [**REPARSE_DATA_BUFFER**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_reparse_data_buffer) structure. The tag specified in the **ReparseTag** member of this structure must match the tag of the reparse point to be deleted, and the **ReparseDataLength** member must be zero. In addition, if the reparse point is a third-party (non-Microsoft) reparse point, the GUID specified in the **ReparseGuid** member of the REPARSE_GUID_DATA_BUFFER structure must match the GUID of the reparse point to be deleted.

- **InputBufferLength** [in]: Size, in bytes, of the buffer pointed to by the **InputBuffer** parameter. For a REPARSE_GUID_DATA_BUFFER structure, this value must be exactly REPARSE_GUID_DATA_BUFFER_HEADER_SIZE. For a REPARSE_DATA_BUFFER structure, this value must be exactly REPARSE_DATA_BUFFER_HEADER_SIZE.

- **OutputBuffer** [out]: None. Set to NULL.

- **OutputBufferLength** [out]: Set to 0.

## Status block

[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following:

| Code | Meaning |
| ---- | ------- |
| STATUS_IO_REPARSE_DATA_INVALID | One of the specified parameter values was invalid. This is an error code. |
| STATUS_IO_REPARSE_TAG_INVALID  | The reparse tag specified by the caller was invalid. This is an error code. |
| STATUS_IO_REPARSE_TAG_MISMATCH  | The reparse tag specified by the caller did not match the tag of the reparse point to be deleted. This is an error code. |
| STATUS_REPARSE_ATTRIBUTE_CONFLICT | The reparse point is a third-party reparse point, and the reparse GUID specified by the caller did not match the GUID of the reparse point to be deleted. This is an error code. |

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Ntifs.h* (include *Ntifs.h* or *Fltkernel.h*) |

## See also

[**FLT_PARAMETERS for IRP_MJ_FILE_SYSTEM_CONTROL**](flt-parameters-for-irp-mj-file-system-control.md)

[**FltTagFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-flttagfile)

[**FltUntagFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltuntagfile)

[**FSCTL_GET_REPARSE_POINT**](fsctl-get-reparse-point.md)

[**FSCTL_SET_REPARSE_POINT**](fsctl-set-reparse-point.md)

[**IRP_MJ_FILE_SYSTEM_CONTROL**](irp-mj-file-system-control.md)

[**IsReparseTagMicrosoft**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-isreparsetagmicrosoft)

[**IsReparseTagNameSurrogate**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-isreparsetagnamesurrogate)

[**REPARSE_DATA_BUFFER**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_reparse_data_buffer)

[**REPARSE_GUID_DATA_BUFFER**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_reparse_guid_data_buffer)

[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85))
