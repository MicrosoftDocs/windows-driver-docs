---
title: FSCTL_DELETE_EXTERNAL_BACKING control code
description: The FSCTL\_DELETE\_EXTERNAL\_BACKING control code removes the association of a file with an external backing provider, including the Windows Image Format (WIM) provider or compressed file provider.
ms.assetid: 5C150899-6BCA-49EB-AEEB-0CBEC7BE60BA
keywords: ["FSCTL_DELETE_EXTERNAL_BACKING control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_DELETE_EXTERNAL_BACKING
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_DELETE\_EXTERNAL\_BACKING control code


The **FSCTL\_DELETE\_EXTERNAL\_BACKING** control code removes the association of a file with an external backing provider, including the Windows Image Format (WIM) provider or compressed file provider. As a result of this operation, the entire contents of a backed file are read, decompressed, and written into the file.

To perform this operation, call [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) with the following parameters.

**Parameters**

<a href="" id="instance--in-"></a>*Instance \[in\]*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. An opaque instance pointer for the caller. This parameter is required and cannot be NULL.

<a href="" id="fileobject--in-"></a>*FileObject \[in\]*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. The file pointer object of the file for which backing association is deleted. This parameter is required and cannot be NULL.

<a href="" id="filehandle--in-"></a>*FileHandle \[in\]*  
[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) only. The handle of the file for which backing association is deleted. This parameter is required and cannot be NULL.

<a href="" id="fscontrolcode--in-"></a>*FsControlCode \[in\]*  
The control code for the operation. Use **FSCTL\_DELETE\_EXTERNAL\_BACKING** for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
None. Set to NULL.

<a href="" id="inputbufferlength--in-"></a>*InputBufferLength \[in\]*  
Set to 0.

<a href="" id="outputbuffer--out-"></a>*OutputBuffer \[out\]*  
None. Set to NULL.

<a href="" id="outputbufferlength--out-"></a>*OutputBufferLength \[out\]*  
Set to 0.

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
<td align="left"><p><strong>STATUS_OBJECT_NOT_EXTERNALLY_BACKED</strong></p></td>
<td align="left"><p>The file is not externally backed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_INVALID_DEVICE_REQUEST</strong></p></td>
<td align="left"><p>The backing service is not present or not started.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_ACCESS_DENIED</strong></p></td>
<td align="left"><p>The requestor does not have permission to delete the backing associations for the file.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

As a result of the delete operation, the contents of the file are read from the backing source and the entire file is written to the volume.

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
<td align="left"><p>Available starting with Windows 8.1 Update.</p></td>
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

[**FSCTL\_SET\_EXTERNAL\_BACKING**](fsctl-set-external-backing.md)

 

 






