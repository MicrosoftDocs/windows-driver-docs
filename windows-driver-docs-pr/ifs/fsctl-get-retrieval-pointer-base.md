---
title: FSCTL_GET_RETRIEVAL_POINTER_BASE control code
description: The FSCTL\_GET\_RETRIEVAL\_POINTER\_BASE returns the sector offset to the first logical cluster number (LCN) of the file system relative to the start of the volume.
ms.assetid: 2c342e58-ef9a-487a-beb9-4353dcbc8115
keywords: ["FSCTL_GET_RETRIEVAL_POINTER_BASE control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_GET_RETRIEVAL_POINTER_BASE
api_location:
- Ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_GET\_RETRIEVAL\_POINTER\_BASE control code


The **FSCTL\_GET\_RETRIEVAL\_POINTER\_BASE** returns the sector offset to the first logical cluster number (LCN) of the file system relative to the start of the volume.

To perform this operation, call the [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) function or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) function with the following parameters.

**Parameters**

<a href="" id="fileobject--in-"></a>*FileObject \[in\]*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. A file object pointer for the volume for which **FSCTL\_GET\_RETRIEVAL\_POINTER\_BASE** is to retrieve the base. This parameter is required and cannot be **NULL**.

<a href="" id="filehandle"></a>*FileHandle*  
[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) only. A file handle for the volume for which **FSCTL\_GET\_RETRIEVAL\_POINTER\_BASE** is to retrieve the base. This parameter is required and cannot be **NULL**.

This handle must be opened with the SE\_MANAGE\_VOLUME\_NAME access rights. For more information, see [File Security and Access Rights](https://msdn.microsoft.com/library/windows/desktop/aa364399).

<a href="" id="fscontrolcode--in-"></a>*FsControlCode \[in\]*  
A control code for the operation. Use **FSCTL\_GET\_RETRIEVAL\_POINTER\_BASE** for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
Not used with this operation. Set to **NULL**.

<a href="" id="inputbufferlength--in-"></a>*InputBufferLength \[in\]*  
Not used with this operation. Set to zero.

<a href="" id="outputbuffer--out-"></a>*OutputBuffer \[out\]*  
A pointer to a LARGE\_INTEGER, which receives the sector offset to the first LCN of the file system relative to the start of the volume.

<a href="" id="outputbufferlength--in-"></a>*OutputBufferLength \[in\]*  
The size of the output buffer, in bytes. This value must be 8.

Status block
------------

[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) returns STATUS\_SUCCESS or an appropriate NTSTATUS value such as one of the following:

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
<td align="left"><p><strong>STATUS_SUCCESS</strong></p></td>
<td align="left"><p>The operation was successful. OutputBuffer contains the sector offset to the first LCN of the file system relative to the start of the volume.</p></td>
</tr>
<tr class="even">
<td align="left"><p> <strong>STATUS_ACCESS_DENIED</strong></p></td>
<td align="left"><p>The user does not have SE_MANAGE_VOLUME access.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_BUFFER_TOO_SMALL</strong></p></td>
<td align="left"><p>OutputBuffer is not large enough for the result. No information has been written to the buffer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_INVALID_PARAMETER</strong></p></td>
<td align="left"><p>A parameter was not valid; for example, the handle used is not a valid volume handle.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Adding the value retrieved by FSCTL\_GET\_RETRIEVAL\_POINTER\_BASE to the value retrieved by the FSCTL\_GET\_RETRIEVAL\_POINTERS control code results in a volume-relative file extent offset.

The FSCTL\_GET\_RETRIEVAL\_POINTER\_BASE control code can be used on FastFAT and exFAT devices. This capability supports the use of BitLocker for devices such as flash drives.

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
<td align="left"><p>Windows Server 2008 R2, Windows 7</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntifs.h</td>
</tr>
</tbody>
</table>

## See also


[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988)

[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462)

 

 






