---
title: FSCTL_MARK_VOLUME_DIRTY control code
description: The FSCTL\_MARK\_VOLUME\_DIRTY control code marks a specified volume as dirty, which triggers Autochk.exe to run on the volume during the next system restart.
ms.assetid: 9062b212-fc8a-4467-b32f-047fc3702445
keywords: ["FSCTL_MARK_VOLUME_DIRTY control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_MARK_VOLUME_DIRTY
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_MARK\_VOLUME\_DIRTY control code


The **FSCTL\_MARK\_VOLUME\_DIRTY** control code marks a specified volume as dirty, which triggers Autochk.exe to run on the volume during the next system restart.

To perform this operation, call [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) with the following parameters.

**Parameters**

<a href="" id="instance"></a>*Instance*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. An opaque instance pointer to the minifilter driver instance that is initiating the FSCTL request.

<a href="" id="fileobject"></a>*FileObject*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. A file pointer object specifying the volume to be marked dirty. This parameter is required and cannot be **NULL**.

<a href="" id="filehandle"></a>*FileHandle*  
[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) only. A handle to the volume that is to be marked dirty. This parameter is required and cannot be **NULL**.

<a href="" id="fscontrolcode"></a>*FsControlCode*  
Control code for the operation. Use **FSCTL\_MARK\_VOLUME\_DIRTY** for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
Not used with this operation. Set to **NULL**.

<a href="" id="inputbufferlength"></a>*InputBufferLength*  
Not used with this operation. Set to 0.

<a href="" id="outputbuffer"></a>*OutputBuffer*  
Not used with this operation. Set to **NULL**.

<a href="" id="outputbufferlength"></a>*OutputBufferLength*  
Not used with this operation. Set to 0.

Status block
------------

The [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) routine returns STATUS\_SUCCESS or an appropriate NTSTATUS value.

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
<td align="left"><p>The <em>FileObject</em> or <em>FileHandle</em> does not represent a valid volume handle or another parameter is invalid.</p></td>
</tr>
<tr class="even">
<td align="left"><p> <strong>STATUS_ACCESS_DENIED</strong></p></td>
<td align="left"><p>The caller does not have SE_MANAGE_VOLUME access rights.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_VOLUME_DISMOUNTED</strong></p></td>
<td align="left"><p>The file system volume is dismounted.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_TOO_LATE</strong></p></td>
<td align="left"><p>The file system volume is shut down.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_MEDIA_WRITE_PROTECTED</strong></p></td>
<td align="left"><p>The file system volume is read-only.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

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
<td align="left"><p>Header</p></td>
<td align="left">Ntifs.h (include FltKernel.h or Ntifs.h)</td>
</tr>
</tbody>
</table>

## See also


[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988)

[**FSCTL\_IS\_VOLUME\_DIRTY**](fsctl-is-volume-dirty.md)

[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462)

 

 






