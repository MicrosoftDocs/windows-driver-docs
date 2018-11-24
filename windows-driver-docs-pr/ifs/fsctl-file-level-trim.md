---
title: FSCTL_FILE_LEVEL_TRIM control code
description: The FSCTL\_FILE\_LEVEL\_TRIM control code provides a method to trim data ranges with in a file.
ms.assetid: AD8A7A15-8B53-41DA-A6E4-BD1825C8CB45
keywords: ["FSCTL_FILE_LEVEL_TRIM control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_FILE_LEVEL_TRIM
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_FILE\_LEVEL\_TRIM control code


The **FSCTL\_FILE\_LEVEL\_TRIM** control code provides a method to trim data ranges with in a file. The file trim ranges are translated to the underlying storage device allowing it to optimize its resource organization to improve access performance. An **FSCTL\_FILE\_LEVEL\_TRIM** request allows a virtual disk file to remain allocated at a fixed size while trimming physical storage to correspond to data ranges freed on the virtual disk.

To perform this operation, call [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) with the following parameters.

**Parameters**

<a href="" id="instance--in-"></a>*Instance \[in\]*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. Opaque instance pointer for the caller. This parameter is required and cannot be **NULL**.

<a href="" id="fileobject--in-"></a>*FileObject \[in\]*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. The file pointer object specifying the volume to be dismounted. This parameter is required and cannot be **NULL**.

<a href="" id="filehandle--in-"></a>*FileHandle \[in\]*  
[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) only. The file handle of the volume to be dismounted. This parameter is required and cannot be **NULL**.

<a href="" id="fscontrolcode--in-"></a>*FsControlCode \[in\]*  
Control code for the operation. Use **FSCTL\_REMOVE\_OVERLAY** for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
A pointer to the input buffer, which must contain a **FSCTL\_FILE\_LEVEL\_TRIM** structure.

<a href="" id="inputbufferlength--in-"></a>*InputBufferLength \[in\]*  
A pointer to a [**FILE\_LEVEL\_TRIM**](https://msdn.microsoft.com/library/windows/hardware/hh406398) structure which contains an array of trim ranges for the file.

<a href="" id="outputbuffer--out-"></a>*OutputBuffer \[out\]*  
A pointer to an optional [**FILE\_LEVEL\_TRIM\_OUTPUT**](https://msdn.microsoft.com/library/windows/hardware/hh406398) structure which receives the result of the trim operation.

<a href="" id="outputbufferlength--out-"></a>*OutputBufferLength \[out\]*  
Size, in bytes, of the buffer pointed to by the *OutputBuffer* parameter. This value must be at least **sizeof**([**FILE\_LEVEL\_TRIM\_OUTPUT**](https://msdn.microsoft.com/library/windows/hardware/hh406398)) if **FILE\_LEVEL\_TRIM\_OUTPUT** is included in *OutputBuffer*. Otherwise, this is set to 0.

Status block
------------

[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) returns STATUS\_SUCCESS or possibly one of the following values.

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
<td align="left"><p>The file to trim is either compressed or encrypted, the input or output buffer length is invalid, or, no trim ranges are specified.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_INSUFFICIENT_RESOURCES</strong></p></td>
<td align="left"><p>An internal resource allocation failed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_FILE_LOCK_CONFLICT</strong></p></td>
<td align="left"><p>A trim range is part of a previously locked byte range.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_VOLUME_DISMOUNTED</strong></p></td>
<td align="left"><p>The volume where the file resides is not mounted.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_PURGE_FAILED</strong></p></td>
<td align="left"><p>A cache purge failed for a trim range.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_NO_RANGES_PROCESSED</strong></p></td>
<td align="left"><p>No ranges in the trim range array were processed.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Performing trim on certain storage devices can significantly improve their future write performance. Trim also returns resources to the allocation pool in storage systems that are thinly provisioned. When files are deleted on a virtual disk, the size of the virtual disk file itself is not changed. The data ranges freed on the virtual disk are not trimmed on the physical storage where the virtual disk file resides. A virtual disk device can notify the file system that certain data ranges in a virtual disk file can be trimmed on the physical storage device with an **FSCTL\_FILE\_LEVEL\_TRIM** request. The file system will then issue a trim request to the physical storage. An **FSCTL\_FILE\_LEVEL\_TRIM** request could also be issued by service applications managing database or memory swap files.

The **FSCTL\_FILE\_LEVEL\_TRIM** control code will attempt to trim the selected byte ranges of a file from a storage device. The byte ranges are contained in the **Ranges** array in the [**FILE\_LEVEL\_TRIM**](https://msdn.microsoft.com/library/windows/hardware/hh406398) structure. Included in the **Ranges** array are one or more [**FILE\_LEVEL\_TRIM\_RANGE**](https://msdn.microsoft.com/library/windows/hardware/hh406405) structures.

Including overlapping ranges in the range array is not necessarily an error condition. This is dependant on how extent processing is handled by the underlying storage.

Trimmed ranges are purged as pages from the file system cache. In order to match the cache page size, a trim range's length is adjusted down to a multiple of **PAGE\_SIZE**. Also, if a trim range offset does not begin at a page boundary, it is aligned to the next page boundary. With these constraints, trim range lengths will reduce when their offsets are not page aligned or lengths are not a page size multiple. A trim range length may reduce to 0 if the original length is less than two pages and the offset is not page aligned.

If a trim range is specified or page adjusted beyond the end-of-file (EOF), the range is ignored. However, a range offset aligned before EOF but having a length extending past EOF will be adjusted to a page size multiple &lt;= EOF.

File level trim is not supported for compressed or encrypted files (files with **ATTRIBUTE\_FLAG\_COMPRESSION\_MASK** or **ATTRIBUTE\_FLAG\_ENCRYPTED** attributes set).

A file trim is performed outside of any transaction. The trim operation cannot be rolled back.

With sparse files (files with the **ATTRIBUTE\_FLAG\_SPARSE** attribute set), a trim range in an unallocated portion of the file is ignored.

When included in *OutputBuffer*, the **NumRangesProcessed** member of the [**FILE\_LEVEL\_TRIM\_OUTPUT**](https://msdn.microsoft.com/library/windows/hardware/hh406402) will indicate the number of trim ranges successfully processed. If an error occurs during the processing of the trim ranges, **NumRangesProcessed** will specify the starting index of the remaining unprocessed ranges, ending at the **NumRanges** member of [**FILE\_LEVEL\_TRIM**](https://msdn.microsoft.com/library/windows/hardware/hh406398) - 1.

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
<td align="left"><p>Available in Windows 8 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntifs.h (include Ntifs.h or Fltkernel.h)</td>
</tr>
</tbody>
</table>

## See also


[**FILE\_LEVEL\_TRIM**](https://msdn.microsoft.com/library/windows/hardware/hh406398)

[**FILE\_LEVEL\_TRIM\_OUTPUT**](https://msdn.microsoft.com/library/windows/hardware/hh406402)

[**FILE\_LEVEL\_TRIM\_RANGE**](https://msdn.microsoft.com/library/windows/hardware/hh406405)

[**FltCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff541935)

[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988)

[**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424)

[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462)

 

 






