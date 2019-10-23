---
title: FSCTL_SET_REPARSE_POINT_EX control code
description: The FSCTL_SET_REPARSE_POINT_EX control code sets a reparse point on a file or directory.
tech.root:
ms.assetid: 5867cbe3-5aab-43f8-b5bf-eaa29857359f
keywords: ["FSCTL_SET_REPARSE_POINT_EX control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_SET_REPARSE_POINT_EX
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 05/31/2019
ms.localizationpriority: medium
---

# FSCTL_SET_REPARSE_POINT_EX control code

The FSCTL_SET_REPARSE_POINT_EX control code sets a reparse point on a file or directory.

Minifilters should use [**FltTagFileEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-flttagfileex) instead of FSCTL_SET_REPARSE_POINT_EX to set a reparse point.

For more information about reparse points, see the Microsoft Windows SDK documentation.

To perform this operation, call [**ZwFsControlFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntfscontrolfile) with the following parameters.

## Parameters

*FileHandle*  
File handle for the file or directory on which to set a reparse point. This parameter is required and cannot be **NULL**.

*Event*
Not used with this operation; set to **NULL**.

*ApcRoutine*
Not used with this operation; set to **NULL**.

*ApcContext*
Not used with this operation; set to **NULL**.

*IoStatusBlock*
Pointer to an IO_STATUS_BLOCK structure that receives the final completion status and information about the operation.

*FsControlCode*  
Control code for the operation. Use FSCTL_SET_REPARSE_POINT_EX for this operation.

*InputBuffer*  
Pointer to a caller-allocated [REPARSE_DATA_BUFFER_EX](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_reparse_data_buffer_ex) structure that contains the reparse point data.

*InputBufferLength*  
Size, in bytes, of the buffer pointed to by the *InputBuffer* parameter. This value must be at least REPARSE_GUID_DATA_BUFFER_HEADER_SIZE, plus the size of the user-defined data, and it must be less than or equal to MAXIMUM_REPARSE_DATA_BUFFER_SIZE.

*OutputBuffer*  
Not used with this operation; set to **NULL**.

*OutputBufferLength*  
Not used with this operation; set to zero.

Status block
------------
[**ZwFsControlFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntfscontrolfile) returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Term</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>STATUS_DIRECTORY_NOT_EMPTY</strong></p></td>
<td align="left"><p>A reparse point cannot be set on a nonempty directory. This is an error code.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_EAS_NOT_SUPPORTED</strong></p></td>
<td align="left"><p>A reparse point cannot be set on a file if this request is in a transaction. This is an error code.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_IO_REPARSE_DATA_INVALID</strong></p></td>
<td align="left"><p>One of the specified parameter values was invalid. This is an error code.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_IO_REPARSE_TAG_MISMATCH</strong></p></td>
<td align="left"><p>The reparse tag specified by the caller did not match the tag of the reparse point to be modified. This is an error code.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_NOT_A_REPARSE_POINT</strong></p></td>
<td align="left"><p>The file or directory is not a reparse point. This is an error code.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_REPARSE_ATTRIBUTE_CONFLICT</strong></p></td>
<td align="left"><p>The reparse point is a third-party reparse point, and the reparse GUID specified by the caller did not match the GUID of the reparse point to be modified. This is an error code.</p></td>
</tr>
</tbody>
</table>

## Requirements
------------
<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ntifs.h (include Ntifs.h or Fltkernel.h)</td>
</tr>
</tbody>
</table>

## See also

[**FLT_PARAMETERS for IRP_MJ_FILE_SYSTEM_CONTROL**](https://docs.microsoft.com/windows-hardware/drivers/ifs/flt-parameters-for-irp-mj-file-system-control)

[**FltTagFileEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-flttagfileex)

[**FltUntagFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltuntagfile)

[**FSCTL\_DELETE\_REPARSE\_POINT**](fsctl-delete-reparse-point.md)

[**FSCTL\_GET\_REPARSE\_POINT**](fsctl-get-reparse-point.md)

[**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](irp-mj-file-system-control.md)

[**IsReparseTagMicrosoft**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-isreparsetagmicrosoft)

[**IsReparseTagNameSurrogate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-isreparsetagnamesurrogate)

[**REPARSE\_DATA\_BUFFER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_reparse_data_buffer_ex)

[**REPARSE\_GUID\_DATA\_BUFFER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_reparse_guid_data_buffer)

[**ZwFsControlFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntfscontrolfile)