---
title: FSCTL_IS_PATHNAME_VALID control code
description: The FSCTL\_IS\_PATHNAME\_VALID control code performs static analysis of the supplied pathname and returns a status value that indicates whether the pathname is well formed (for example, no illegal characters, acceptable path length, and so on).
ms.assetid: 3f95ae2c-a376-4c68-9e84-dde22aa7e315
keywords: ["FSCTL_IS_PATHNAME_VALID control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_IS_PATHNAME_VALID
api_location:
- Ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_IS\_PATHNAME\_VALID control code


The **FSCTL\_IS\_PATHNAME\_VALID** control code performs static analysis of the supplied pathname and returns a status value that indicates whether the pathname is well formed (for example, no illegal characters, acceptable path length, and so on). Because this analysis does not consider the content of the volume, it sometimes gives "false positives." In other words, the analysis might indicate that the pathname is well formed, even when it is not. Negative results are more reliable, but are not guaranteed to be correct.

This control code is not supported with fast FAT file systems, and it is not a meaningful operation in NTFS or UDFS. NTFS and UDFS support such a wide variety of codesets that any string is potentially a valid pathname.

To perform this operation, call [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) with the following parameters.

**Parameters**

<a href="" id="fileobject"></a>*FileObject*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. Not used.

<a href="" id="filehandle"></a>*FileHandle*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. Not used.

<a href="" id="fscontrolcode"></a>*FsControlCode*  
The control code for the operation. Use FSCTL\_IS\_PATHNAME\_VALID for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
A buffer that contains the NULL-terminated pathname string to check.

<a href="" id="inputbufferlength"></a>*InputBufferLength*  
The length, in bytes, of the pathname.

<a href="" id="outputbuffer"></a>*OutputBuffer*  
Not used.

<a href="" id="outputbufferlength"></a>*OutputBufferLength*  
Not used.

Status block
------------

[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) returns STATUS\_SUCCESS if the pathname is well formed. Otherwise, the routine that is used returns the appropriate NTSTATUS error code.

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

 

 





