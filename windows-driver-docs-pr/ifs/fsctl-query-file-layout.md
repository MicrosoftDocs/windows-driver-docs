---
title: FSCTL_QUERY_FILE_LAYOUT control code
description: The FSCTL\_QUERY\_FILE\_LAYOUT control code retrieves file layout information for a file system volume.
ms.assetid: C0094741-72C1-409C-89E6-BAD60A94EFD6
keywords: ["FSCTL_QUERY_FILE_LAYOUT control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_QUERY_FILE_LAYOUT
api_location:
- Ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_QUERY\_FILE\_LAYOUT control code


The FSCTL\_QUERY\_FILE\_LAYOUT control code retrieves file layout information for a file system volume. The results of this request are a collection of file layout information entries. The type of entries returned is controlled by setting inclusion flags in the [**QUERY\_FILE\_LAYOUT\_INPUT**](https://msdn.microsoft.com/library/windows/hardware/hh439457) structure. You can optionally filter the results by providing a set of file extents to restrict the selection of layout information.

To perform this operation, call [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) with the following parameters.

**Parameters**

<a href="" id="fileobject"></a>*FileObject*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. A file object pointer for the file system volume. This parameter is required and cannot be **NULL**.

<a href="" id="filehandle"></a>*FileHandle*  
[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) only. A file handle for the file system volume. This parameter is required and cannot be **NULL**.

<a href="" id="fscontrolcode"></a>*FsControlCode*  
The control code for the operation. Use The FSCTL\_QUERY\_FILE\_LAYOUT control code for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
A pointer to a caller-allocated [**QUERY\_FILE\_LAYOUT\_INPUT**](https://msdn.microsoft.com/library/windows/hardware/hh439457) structure. This structure contains the selection options. The optional file extents are included after **QUERY\_FILE\_LAYOUT\_INPUT**.

<a href="" id="inputbufferlength"></a>*InputBufferLength*  
The size, in bytes, of the buffer pointed to by the *InputBuffer* parameter. The size of *InputBuffer* must be at least **sizeof**(QUERY\_FILE\_LAYOUT\_INPUT) + (**sizeof**(*Filter*) \* (*NumberOfPairs* - 1)), when *NumberOfPairs* &gt; 0. Otherwise, set *InputBufferLength* = **sizeof**(QUERY\_FILE\_LAYOUT\_INPUT).

<a href="" id="outputbuffer"></a>*OutputBuffer*  
A pointer to a caller-allocated [**QUERY\_FILE\_LAYOUT\_OUTPUT**](https://msdn.microsoft.com/library/windows/hardware/hh439461) structure. This is the header for the file layout entries that follow in this buffer.

<a href="" id="outputbufferlength"></a>*OutputBufferLength*  
The size, in bytes, of the buffer pointed to by the *OutputBuffer* parameter. The size of *OutputBuffer* must be large enough to contain a [**QUERY\_FILE\_LAYOUT\_OUTPUT**](https://msdn.microsoft.com/library/windows/hardware/hh439461) along with the file layout and stream layout structures returned.

Status block
------------

[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) returns STATUS\_SUCCESS or an appropriate NTSTATUS value, such as one of these values:

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
<td align="left"><p><strong>STATUS_INVALID_PARAMETER</strong></p></td>
<td align="left"><p>The file system volume is not an open user volume, or a buffer length value is incorrect, or an invalid query option is set.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_ACCESS_DENIED</strong></p></td>
<td align="left"><p>The caller cannot access the file system volume.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_INVALID_USER_BUFFER</strong></p></td>
<td align="left"><p>The pointer for either <em>InputBuffer</em> or <em>OutputBuffer</em> is not properly aligned.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_BUFFER_TOO_SMALL</strong></p></td>
<td align="left"><p>The value in <em>OutputBufferLength</em> indicates that <em>OutputBuffer</em> is too small to contain at least one layout entry.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_END_OF_FILE</strong></p></td>
<td align="left"><p>The pointer for either <em>InputBuffer</em> or <em>OutputBuffer</em> is not properly aligned.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

To retrieve all the layout entries for a volume, the FSCTL\_QUERY\_FILE\_LAYOUT request is issued multiple times until **STATUS\_END\_OF\_FILE** is returned. While **STATUS\_SUCCESS** is returned, a caller can continue to send an FSCTL\_QUERY\_FILE\_LAYOUT request for the remaining layout entries.

The enumeration of layout entries may be restarted at any time by including the **QUERY\_FILE\_LAYOUT\_RESTART** flag in the **Flags** member of [**QUERY\_FILE\_LAYOUT\_INPUT**](https://msdn.microsoft.com/library/windows/hardware/hh439457). Also, after FSCTL\_QUERY\_FILE\_LAYOUT has returned **STATUS\_END\_OF\_FILE**, it is necessary to include the **QUERY\_FILE\_LAYOUT\_RESTART** flag in the next FSCTL\_QUERY\_FILE\_LAYOUT request to begin another layout entry enumeration.

**ReFS:  **This code is not supported.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available starting in Windows 8.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntifs.h (include Ntifs.h)</td>
</tr>
</tbody>
</table>

## See also


[**QUERY\_FILE\_LAYOUT\_INPUT**](https://msdn.microsoft.com/library/windows/hardware/hh439457)

[**QUERY\_FILE\_LAYOUT\_OUTPUT**](https://msdn.microsoft.com/library/windows/hardware/hh439461)

[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988)

[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462)

 

 






