---
title: FSCTL_SET_REPARSE_POINT control code
description: The FSCTL\_SET\_REPARSE\_POINT control code sets a reparse point on a file or directory.
keywords: ["FSCTL_SET_REPARSE_POINT control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_SET_REPARSE_POINT
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_SET\_REPARSE\_POINT control code


The FSCTL\_SET\_REPARSE\_POINT control code sets a reparse point on a file or directory.

To perform this operation, call [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with the following parameters.

Minifilters should use [**FltTagFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-flttagfile) instead of FSCTL\_SET\_REPARSE\_POINT to set a reparse point.

For more information about reparse points and the FSCTL\_SET\_REPARSE\_POINT control code, see the Microsoft Windows SDK documentation.

**Parameters**

<a href="" id="filehandle"></a>*FileHandle*  
File handle for the file or directory on which to set a reparse point. This parameter is required and cannot be **NULL**.

<a href="" id="fscontrolcode"></a>*FsControlCode*  
Control code for the operation. Use FSCTL\_SET\_REPARSE\_POINT for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
Pointer to a caller-allocated [**REPARSE\_GUID\_DATA\_BUFFER**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_reparse_guid_data_buffer) or [**REPARSE\_DATA\_BUFFER**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_reparse_data_buffer) structure that contains the reparse point data. If an existing reparse point is being modified, the tag specified in the **ReparseTag** member of this structure must match the tag of the reparse point to be modified. In addition, if the reparse point is a third-party (non-Microsoft) reparse point, the GUID specified in the **ReparseGuid** member of the structure is a REPARSE\_GUID\_DATA\_BUFFER structure must match the GUID of the reparse point to be modified.

<a href="" id="inputbufferlength"></a>*InputBufferLength*  
Size, in bytes, of the buffer pointed to by the *InputBuffer* parameter. For a REPARSE\_GUID\_DATA\_BUFFER structure, this value must be at least REPARSE\_GUID\_DATA\_BUFFER\_HEADER\_SIZE, plus the size of the user-defined data, and it must be less than or equal to MAXIMUM\_REPARSE\_DATA\_BUFFER\_SIZE. For a REPARSE\_DATA\_BUFFER structure, this value must be at least REPARSE\_DATA\_BUFFER\_HEADER\_SIZE, plus the size of the user-defined data, and it must be less than or equal to MAXIMUM\_REPARSE\_DATA\_BUFFER\_SIZE.

<a href="" id="outputbuffer"></a>*OutputBuffer*  
Not used with this operation; set to **NULL**.

<a href="" id="outputbufferlength"></a>*OutputBufferLength*  
Not used with this operation; set to zero.

## Status block

[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) returns STATUS\_SUCCESS or an appropriate NTSTATUS value such as one of the following:

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


[**FLT\_PARAMETERS for IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](flt-parameters-for-irp-mj-file-system-control.md)

[**FltTagFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-flttagfile)

[**FltUntagFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltuntagfile)

[**FSCTL\_DELETE\_REPARSE\_POINT**](fsctl-delete-reparse-point.md)

[**FSCTL\_GET\_REPARSE\_POINT**](fsctl-get-reparse-point.md)

[**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](irp-mj-file-system-control.md)

[**IsReparseTagMicrosoft**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-isreparsetagmicrosoft)

[**IsReparseTagNameSurrogate**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-isreparsetagnamesurrogate)

[**REPARSE\_DATA\_BUFFER**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_reparse_data_buffer)

[**REPARSE\_GUID\_DATA\_BUFFER**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_reparse_guid_data_buffer)

[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85))

 

