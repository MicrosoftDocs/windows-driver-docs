---
title: FSCTL_SET_REPARSE_POINT_EX control code
description: The FSCTL_SET_REPARSE_POINT_EX control code sets a reparse point on a file or directory.
keywords: ["FSCTL_SET_REPARSE_POINT_EX control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_SET_REPARSE_POINT_EX
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 11/25/2020
---

# FSCTL_SET_REPARSE_POINT_EX control code

The FSCTL_SET_REPARSE_POINT_EX control code sets a reparse point on a file or directory.

To perform this operation, call [**ZwFsControlFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwfscontrolfile) with the following parameters.

Minifilters should use [**FltTagFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-flttagfile) instead of FSCTL_SET_REPARSE_POINT_EX to set a reparse point.

For more information about reparse points and the FSCTL_SET_REPARSE_POINT_EX control code, see the Microsoft Windows SDK documentation.

## Parameters

*FileHandle*  
File handle for the file or directory on which to set a reparse point. This parameter is required and cannot be **NULL**.

*FsControlCode*  
Control code for the operation. Use FSCTL_SET_REPARSE_POINT_EX for this operation.

*InputBuffer*  
Pointer to a caller-allocated [**REPARSE_GUID_DATA_BUFFER**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_reparse_guid_data_buffer) or [**REPARSE_DATA_BUFFER_EX**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_reparse_data_buffer_ex) structure that contains the reparse point data.

*InputBufferLength*  
Size, in bytes, of the buffer pointed to by the *InputBuffer* parameter. For a REPARSE_GUID_DATA_BUFFER structure, this value must be at least REPARSE_GUID_DATA_BUFFER_HEADER_SIZE, plus the size of the user-defined data, and it must be less than or equal to MAXIMUM_REPARSE_DATA_BUFFER_SIZE. For a REPARSE_DATA_BUFFER_EX structure, this value must be at least REPARSE_DATA_BUFFER_HEADER_SIZE, plus the size of the user-defined data, and it must be less than or equal to MAXIMUM_REPARSE_DATA_BUFFER_SIZE.

*OutputBuffer*  
Not used with this operation; set to **NULL**.

*OutputBufferLength*  
Not used with this operation; set to zero.

## Status block

[**ZwFsControlFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwfscontrolfile) returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following:

| Value | Description |
| ----- | ----------- |
| STATUS_DIRECTORY_NOT_EMPTY | A reparse point cannot be set on a nonempty directory. This is an error code.|
| STATUS_EAS_NOT_SUPPORTED | A reparse point cannot be set on a file if this request is in a transaction. This is an error code.|
 | STATUS_IO_REPARSE_DATA_INVALID | One of the specified parameter values was invalid. This is an error code.|
| STATUS_IO_REPARSE_TAG_MISMATCH | The reparse tag specified by the caller did not match the tag of the reparse point to be modified. This is an error code.|
 | STATUS_NOT_A_REPARSE_POINT | The file or directory is not a reparse point. This is an error code.|
| STATUS_REPARSE_ATTRIBUTE_CONFLICT | The reparse point is a third-party reparse point, and the reparse GUID specified by the caller did not match the GUID of the reparse point to be modified. This is an error code.|

### Requirements

* Header: Ntifs.h (include Ntifs.h or Fltkernel.h)

## See also

[**FLT_PARAMETERS for IRP_MJ_FILE_SYSTEM_CONTROL**](flt-parameters-for-irp-mj-file-system-control.md)

[**FltTagFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-flttagfile)

[**FltUntagFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltuntagfile)

[**FSCTL_DELETE_REPARSE_POINT**](fsctl-delete-reparse-point.md)

[**FSCTL_GET_REPARSE_POINT**](fsctl-get-reparse-point.md)

[**IRP_MJ_FILE_SYSTEM_CONTROL**](irp-mj-file-system-control.md)

[**IsReparseTagMicrosoft**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-isreparsetagmicrosoft)

[**IsReparseTagNameSurrogate**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-isreparsetagnamesurrogate)

[**REPARSE_DATA_BUFFER_EX**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_reparse_data_buffer_ex)

[**REPARSE_GUID_DATA_BUFFER**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_reparse_guid_data_buffer)

[**ZwFsControlFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwfscontrolfile)
