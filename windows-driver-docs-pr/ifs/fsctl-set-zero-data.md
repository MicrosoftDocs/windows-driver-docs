---
title: FSCTL_SET_ZERO_DATA control code
description: The FSCTL\_SET\_ZERO\_DATA control code fills a specified range of a file with zeros (0).
ms.assetid: AEC4DAD4-17EB-412B-881B-E54F6A578637
keywords: ["FSCTL_SET_ZERO_DATA control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_SET_ZERO_DATA
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_SET\_ZERO\_DATA control code


The **FSCTL\_SET\_ZERO\_DATA** control code fills a specified range of a file with zeros (0). If the file is sparse or compressed, the NTFS file system may deallocate disk space in the file. This sets the range of bytes to zeros (0) without extending the file size.

To perform this operation from a driver, call [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) with the following parameters.

**Parameters**

<a href="" id="instance"></a>*Instance*  
Opaque instance pointer for the caller. This parameter is required and cannot be **NULL**.

<a href="" id="fileobject"></a>*FileObject*  
File object pointer to the file in which to write zeros to. This parameter is required and cannot be **NULL**.

<a href="" id="fscontrolcode"></a>*FsControlCode*  
The control code for the operation.

Use **FSCTL\_SET\_ZERO\_DATA** for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
A pointer to a [**FILE\_ZERO\_DATA\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/mt668763) or [**FILE\_ZERO\_DATA\_INFORMATION\_EX**](https://msdn.microsoft.com/library/windows/hardware/mt668764) structure that specifies the range of the file to set to zeros.

The **FileOffset** member is the byte offset of the first byte to set to zeros (0), and the **BeyondFinalZero** member is the byte offset of the first byte beyond the last zero (0) byte.

The **Flags** member in [**FILE\_ZERO\_DATA\_INFORMATION\_EX**](https://msdn.microsoft.com/library/windows/hardware/mt668764) specifies modifiers to the operation. For example, when **Flags** is set to **FILE\_ZERO\_DATA\_INFORMATION\_FLAG\_PRESERVE\_CACHED\_DATA**, the contents of the cache corresponding to this range of the file are not purged.

<a href="" id="inputbufferlength"></a>*InputBufferLength*  
The size of the input buffer, in bytes.

<a href="" id="outputbuffer"></a>*OutputBuffer*  
Not used with this operation; set to **NULL**.

<a href="" id="outputbufferlength"></a>*OutputBufferLength*  
Not used with this operation; set to zero.

Status block
------------

[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) returns **STATUS\_SUCCESS** or an appropriate NTSTATUS value.

-   **STATUS \_INSUFFICIENT\_RESOURCES** is returned when there is not enough memory to complete the operation.
-   **STATUS\_INVALID\_PARAMETER** is returned when the *InputBufferLength* is smaller than the size of the **FILE\_ZERO\_DATA\_INFORMATION** structures or the file specified is a system metadata file or a directory.
-   **STATUS\_ACCESS\_DENIED** is returned when the **FILE\_ZERO\_DATA\_INFORMATION\_FLAG\_PRESERVE\_CACHED\_DATA** is set from user mode.
-   **STATUS\_MEDIA\_WRITE\_PROTECTED** is returned if the volume is currently write protected.

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
<td align="left">Ntifs.h (include Ntifs.h)</td>
</tr>
</tbody>
</table>

## See also


[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988)

[**FILE\_ZERO\_DATA\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/mt668763)

[**FILE\_ZERO\_DATA\_INFORMATION\_EX**](https://msdn.microsoft.com/library/windows/hardware/mt668764)

 

 






