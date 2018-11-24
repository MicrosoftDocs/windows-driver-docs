---
title: FSCTL_DELETE_REPARSE_POINT control code
description: The FSCTL\_DELETE\_REPARSE\_POINT control code deletes a reparse point from the specified file or directory. Using FSCTL\_DELETE\_REPARSE\_POINT does not delete the file or directory.
ms.assetid: c8a06477-457b-47e5-b5c5-48d798fe08b3
keywords: ["FSCTL_DELETE_REPARSE_POINT control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_DELETE_REPARSE_POINT
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_DELETE\_REPARSE\_POINT control code


The FSCTL\_DELETE\_REPARSE\_POINT control code deletes a reparse point from the specified file or directory. Using FSCTL\_DELETE\_REPARSE\_POINT does not delete the file or directory.

To perform this operation, call [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) with the following parameters.

Minifilters should use [**FltUntagFile**](https://msdn.microsoft.com/library/windows/hardware/ff544608) instead of FSCTL\_DELETE\_REPARSE\_POINT to delete a reparse point.

For more information about reparse points and the FSCTL\_DELETE\_REPARSE\_POINT control code, see the Microsoft Windows SDK documentation.

**Parameters**

<a href="" id="filehandle"></a>*FileHandle*  
File handle for the file or directory from which the reparse point is to be deleted. The caller must have write access to the file or directory. This parameter is required and cannot be **NULL**.

<a href="" id="fscontrolcode"></a>*FsControlCode*  
Control code for the operation. Use FSCTL\_DELETE\_REPARSE\_POINT for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
Pointer to a [**REPARSE\_GUID\_DATA\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff552014) or [**REPARSE\_DATA\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff552012) structure. The tag specified in the **ReparseTag** member of this structure must match the tag of the reparse point to be deleted, and the **ReparseDataLength** member must be zero. In addition, if the reparse point is a third-party (non-Microsoft) reparse point, the GUID specified in the **ReparseGuid** member of the REPARSE\_GUID\_DATA\_BUFFER structure must match the GUID of the reparse point to be deleted.

<a href="" id="inputbufferlength"></a>*InputBufferLength*  
Size, in bytes, of the buffer pointed to by the **InputBuffer** parameter. For a REPARSE\_GUID\_DATA\_BUFFER structure, this value must be exactly **sizeof**(REPARSE\_GUID\_DATA\_BUFFER\_HEADER\_SIZE). For a REPARSE\_DATA\_BUFFER structure, this value must be exactly **sizeof**(REPARSE\_DATA\_BUFFER\_HEADER\_SIZE).

<a href="" id="outputbuffer"></a>*OutputBuffer*  
Not used with this operation; set to **NULL**.

<a href="" id="outputbufferlength"></a>*OutputBufferLength*  
Not used with this operation; set to zero.

Status block
------------

[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) returns STATUS\_SUCCESS or an appropriate NTSTATUS value such as one of the following:

<a href="" id="status-io-reparse-data-invalid"></a>STATUS\_IO\_REPARSE\_DATA\_INVALID  
One of the specified parameter values was invalid. This is an error code.

<a href="" id="status-io-reparse-tag-invalid"></a>STATUS\_IO\_REPARSE\_TAG\_INVALID  
The reparse tag specified by the caller was invalid. This is an error code.

<a href="" id="status-io-reparse-tag-mismatch"></a>STATUS\_IO\_REPARSE\_TAG\_MISMATCH  
The reparse tag specified by the caller did not match the tag of the reparse point to be deleted. This is an error code.

<a href="" id="status-reparse-attribute-conflict"></a>STATUS\_REPARSE\_ATTRIBUTE\_CONFLICT  
The reparse point is a third-party reparse point, and the reparse GUID specified by the caller did not match the GUID of the reparse point to be deleted. This is an error code.

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


[**FLT\_PARAMETERS for IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](flt-parameters-for-irp-mj-file-system-control.md)

[**FltTagFile**](https://msdn.microsoft.com/library/windows/hardware/ff544589)

[**FltUntagFile**](https://msdn.microsoft.com/library/windows/hardware/ff544608)

[**FSCTL\_GET\_REPARSE\_POINT**](fsctl-get-reparse-point.md)

[**FSCTL\_SET\_REPARSE\_POINT**](fsctl-set-reparse-point.md)

[**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](irp-mj-file-system-control.md)

[**IsReparseTagMicrosoft**](https://msdn.microsoft.com/library/windows/hardware/ff549452)

[**IsReparseTagNameSurrogate**](https://msdn.microsoft.com/library/windows/hardware/ff549462)

[**REPARSE\_DATA\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff552012)

[**REPARSE\_GUID\_DATA\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff552014)

[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462)

 

 






