---
title: FSCTL_OFFLOAD_READ control code
description: The FSCTL\_OFFLOAD\_READ control code initiates an offload read for a block of data in a storage system that supports offload read primitives.
ms.assetid: D9A22A8F-9B7E-4BF7-8FBD-267BE4C8DC59
keywords: ["FSCTL_OFFLOAD_READ control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_OFFLOAD_READ
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_OFFLOAD\_READ control code


The **FSCTL\_OFFLOAD\_READ** control code initiates an offload read for a block of data in a storage system that supports offload read primitives.

To perform this operation, call [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) with the following parameters.

**Parameters**

<a href="" id="instance--in-"></a>*Instance \[in\]*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. An opaque instance pointer for the caller. This parameter is required and cannot be NULL.

<a href="" id="fileobject--in-"></a>*FileObject \[in\]*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. The file pointer object specifying the file to read from. This parameter is required and cannot be NULL.

<a href="" id="filehandle--in-"></a>*FileHandle \[in\]*  
[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) only. The file handle of the file to read from. This parameter is required and cannot be NULL.

<a href="" id="fscontrolcode--in-"></a>*FsControlCode \[in\]*  
The control code for the operation. Use **FSCTL\_OFFLOAD\_READ** for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
A pointer to a [**FSCTL\_OFFLOAD\_READ\_INPUT**](https://msdn.microsoft.com/library/windows/hardware/hh451104) structure, which contains the size and offset of a data block to read.

<a href="" id="inputbufferlength--in-"></a>*InputBufferLength \[in\]*  
The size, in bytes, of the buffer pointed to by *InputBuffer*. This value is **sizeof**(FSCTL\_OFFLOAD\_READ\_INPUT).

<a href="" id="outputbuffer--out-"></a>*OutputBuffer \[out\]*  
A pointer to a [**FSCTL\_OFFLOAD\_READ\_OUTPUT**](https://msdn.microsoft.com/library/windows/hardware/hh451109) structure, which receives the results of the offload read operation.

<a href="" id="outputbufferlength--out-"></a>*OutputBufferLength \[out\]*  
The size, in bytes, of the buffer pointed to by the *OutputBuffer* parameter. This value must be at least **sizeof**(FSCTL\_OFFLOAD\_READ\_OUTPUT).

Status block
------------

[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) returns STATUS\_SUCCESS if the operation succeeds. Otherwise, the appropriate function might return one of the following NTSTATUS values.

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
<td align="left"><p><strong>STATUS_INVALID_DEVICE_REQUEST</strong></p></td>
<td align="left"><p>The handle specified is not a valid file handle.</p></td>
</tr>
<tr class="even">
<td align="left"><p> <strong>STATUS_INVALID_PARAMETER</strong></p></td>
<td align="left"><p>File size is less than PAGE_SIZE.</p>
<p>-or-</p>
<p><em>InputBufferLength</em> &lt; <strong>sizeof</strong>(FSCTL_OFFLOAD_READ_INPUT).</p>
<p>-or-</p>
<p>One or more of these members of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451104" data-raw-source="[&lt;strong&gt;FSCTL_OFFLOAD_READ_INPUT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451104)"><strong>FSCTL_OFFLOAD_READ_INPUT</strong></a> are incorrect:</p>
<strong>FileOffset</strong> is not a multiple of the logical sector size of the volume.
<strong>CopyLength</strong> is not a multiple of the logical sector size of the volume.
<strong>Size</strong> is not the size of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451104" data-raw-source="[&lt;strong&gt;FSCTL_OFFLOAD_READ_INPUT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451104)"><strong>FSCTL_OFFLOAD_READ_INPUT</strong></a> structure.
<strong>FileOffset</strong> + <strong>CopyLength</strong> &gt; <strong>MAXULONGLONG</strong>.</td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_VOLUME_DISMOUNTED</strong></p></td>
<td align="left"><p>The file system volume is dismounted.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_NOT_SUPPORTED</strong></p></td>
<td align="left"><p>Offload read operations are not supported on this volume.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_OFFLOAD_READ_FILE_NOT_SUPPORTED</strong></p></td>
<td align="left"><p>The requested file type is not supported. Offload operations are not supported on these file types:</p>
<ul>
<li>A transacted file (TxF)</li>
<li>Non-user files</li>
<li>Compressed files</li>
<li>Encrypted files</li>
<li>Sparse files</li>
<li>NTFS Metatdata files</li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_FILE_DELETED</strong></p></td>
<td align="left"><p>The data stream for this file is invalid.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_FILE_CLOSED</strong></p></td>
<td align="left"><p>The file handle is closed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_INVALID_HANDLE</strong></p></td>
<td align="left"><p>The file handle specified is invalid.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_FILE_LOCK_CONFLICT</strong></p></td>
<td align="left"><p>Insufficient read access due to the current file locking state.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_END_OF_FILE</strong></p></td>
<td align="left"><p>The<strong>FileOffset</strong> member of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451104" data-raw-source="[&lt;strong&gt;FSCTL_OFFLOAD_READ_INPUT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451104)"><strong>FSCTL_OFFLOAD_READ_INPUT</strong></a> begins after end-of-file (EOF).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_DISMOUNTED_VOLUME</strong></p></td>
<td align="left"><p>An offload read cannot occur on a dismounted volume.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_INSUFFICIENT_RESOUCES</strong></p></td>
<td align="left"><p>Insufficient resources are available to complete the request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_BUFFER_TOO_SMALL</strong></p></td>
<td align="left"><p><em>OutputBufferLength</em> is too small for <em>OutputBuffer</em> to receive an <a href="https://msdn.microsoft.com/library/windows/hardware/hh451109" data-raw-source="[&lt;strong&gt;FSCTL_OFFLOAD_READ_OUTPUT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451109)"><strong>FSCTL_OFFLOAD_READ_OUTPUT</strong></a> structure.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Offload read is available for normal files only. See the description for **STATUS\_OFFLOAD\_READ\_FILE\_NOT\_SUPPORTED** for a list of unsupported file types.

It is possible for reads to start beyond the Valid Data Length (VDL), but not beyond EOF.

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
<td align="left"><p>Available starting with Windows 8.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntifs.h (include Ntifs.h or Fltkernel.h)</td>
</tr>
</tbody>
</table>

## See also


[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988)

[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462)

[**FSCTL\_OFFLOAD\_READ\_INPUT**](https://msdn.microsoft.com/library/windows/hardware/hh451104)

[**FSCTL\_OFFLOAD\_READ\_OUTPUT**](https://msdn.microsoft.com/library/windows/hardware/hh451109)

 

 






