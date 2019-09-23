---
title: FSCTL_GET_REPARSE_POINT control code
description: The FSCTL\_GET\_REPARSE\_POINT control code retrieves the reparse point data associated with the specified file or directory.
ms.assetid: 8d56a4c5-46c3-42b7-a532-eaf0d792b519
keywords: ["FSCTL_GET_REPARSE_POINT control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_GET_REPARSE_POINT
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_GET\_REPARSE\_POINT control code


The FSCTL\_GET\_REPARSE\_POINT control code retrieves the reparse point data associated with the specified file or directory.

To perform this operation, call [**FltFsControlFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) with the following parameters.

For more information about reparse points and the FSCTL\_GET\_REPARSE\_POINT control code, see the Microsoft Windows SDK documentation.

**Parameters**

<a href="" id="fileobject"></a>*FileObject*  
[**FltFsControlFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/nf-fltkernel-fltfscontrolfile) only. File object pointer for the file or directory from which to retrieve the reparse point data. This parameter is required and cannot be **NULL**.

<a href="" id="filehandle"></a>*FileHandle*  
[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) only. File handle for the file or directory from which to retrieve the reparse point data. This parameter is required and cannot be **NULL**.

<a href="" id="fscontrolcode"></a>*FsControlCode*  
A control code for the operation. Use **FSCTL\_GET\_REPARSE\_POINT** for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
Not used with this operation; set to **NULL**.

<a href="" id="inputbufferlength"></a>*InputBufferLength*  
Not used with this operation; set to zero.

<a href="" id="outputbuffer"></a>*OutputBuffer*  
Pointer to a caller-allocated [**REPARSE\_GUID\_DATA\_BUFFER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntifs/ns-ntifs-_reparse_guid_data_buffer) or [**REPARSE\_DATA\_BUFFER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntifs/ns-ntifs-_reparse_data_buffer) structure that receives the reparse point data.

<a href="" id="outputbufferlength"></a>*OutputBufferLength*  
Size, in bytes, of the buffer pointed to by the *OutputBuffer* parameter. For a REPARSE\_GUID\_DATA\_BUFFER structure, this value must be at least REPARSE\_GUID\_DATA\_BUFFER\_HEADER\_SIZE, plus the size of the expected user-defined data, and it must be less than or equal to MAXIMUM\_REPARSE\_DATA\_BUFFER\_SIZE. For a REPARSE\_DATA\_BUFFER structure, this value must be at least REPARSE\_DATA\_BUFFER\_HEADER\_SIZE, plus the size of the expected user-defined data, and it must be less than or equal to MAXIMUM\_REPARSE\_DATA\_BUFFER\_SIZE.

Status block
------------

[**FltFsControlFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) returns STATUS\_SUCCESS or an appropriate NTSTATUS value such as one of the following:

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
<td align="left"><p><strong>STATUS_BUFFER_OVERFLOW</strong></p></td>
<td align="left"><p>The buffer that the <em>OutputBuffer</em> parameter points to is large enough to hold the fixed portion of the REPARSE_GUID_DATA_BUFFER or REPARSE_DATA_BUFFER structure but not the user-defined data. In this case, only the fixed portion of the reparse point data is returned in the <em>OutputBuffer</em> buffer. The <em>LengthReturned</em> parameter to <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/nf-fltkernel-fltfscontrolfile" data-raw-source="[&lt;strong&gt;FltFsControlFile&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/nf-fltkernel-fltfscontrolfile)"><strong>FltFsControlFile</strong></a> receives the actual length, in bytes, of data returned. This is a warning code.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_BUFFER_TOO_SMALL</strong></p></td>
<td align="left"><p>The buffer that the <em>OutputBuffer</em> parameter points to is not large enough to hold the reparse point data. The <em>LengthReturned</em> parameter to <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/nf-fltkernel-fltfscontrolfile" data-raw-source="[&lt;strong&gt;FltFsControlFile&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/nf-fltkernel-fltfscontrolfile)"><strong>FltFsControlFile</strong></a> (or the <strong>Information</strong> member of the <em>IoStatus</em> parameter to <a href="https://msdn.microsoft.com/library/windows/hardware/ff566462" data-raw-source="[&lt;strong&gt;ZwFsControlFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566462)"><strong>ZwFsControlFile</strong></a>) receives the required buffer size. In this case, no reparse point data is returned. This is an error code.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_IO_REPARSE_DATA_INVALID</strong></p></td>
<td align="left"><p>One of the specified parameter values was invalid. This is an error code.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_NOT_A_REPARSE_POINT</strong></p></td>
<td align="left"><p>The file or directory is not a reparse point. This is an error code.</p></td>
</tr>
</tbody>
</table>

 

Requirements
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


[**FLT\_CALLBACK\_DATA**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT\_PARAMETERS for IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](flt-parameters-for-irp-mj-file-system-control.md)

[**FLT\_TAG\_DATA\_BUFFER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/ns-fltkernel-_flt_tag_data_buffer)

[**FltFsControlFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/nf-fltkernel-fltfscontrolfile)

[**FltTagFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/nf-fltkernel-flttagfile)

[**FltUntagFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/nf-fltkernel-fltuntagfile)

[**FSCTL\_DELETE\_REPARSE\_POINT**](fsctl-delete-reparse-point.md)

[**FSCTL\_SET\_REPARSE\_POINT**](fsctl-set-reparse-point.md)

[**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](irp-mj-file-system-control.md)

[**IsReparseTagMicrosoft**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntifs/nf-ntifs-isreparsetagmicrosoft)

[**IsReparseTagNameSurrogate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntifs/nf-ntifs-isreparsetagnamesurrogate)

[**REPARSE\_DATA\_BUFFER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntifs/ns-ntifs-_reparse_data_buffer)

[**REPARSE\_GUID\_DATA\_BUFFER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntifs/ns-ntifs-_reparse_guid_data_buffer)

[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462)

 

 






