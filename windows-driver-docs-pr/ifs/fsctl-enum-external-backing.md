---
title: FSCTL_ENUM_EXTERNAL_BACKING control code
description: The FSCTL\_ENUM\_EXTERNAL\_BACKING control code begins or continues an enumeration of files on a volume that have a backing source.
ms.assetid: 86B07858-2F10-48EF-AEB5-7F4A23A55F7F
keywords: ["FSCTL_ENUM_EXTERNAL_BACKING control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_ENUM_EXTERNAL_BACKING
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_ENUM\_EXTERNAL\_BACKING control code


The **FSCTL\_ENUM\_EXTERNAL\_BACKING** control code begins or continues an enumeration of files on a volume that have a backing source. For each successful completion of the request, an identifier for the backed file is returned. All backed files are enumerated regardless of which external provider is backing it. Successive **FSCTL\_ENUM\_EXTERNAL\_BACKING** requests are required to enumerate all the backed files on the volume.

To perform this operation, call [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) with the following parameters.

**Parameters**

<a href="" id="instance--in-"></a>*Instance \[in\]*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. Opaque instance pointer for the caller. This parameter is required and cannot be **NULL**.

<a href="" id="fileobject--in-"></a>*FileObject \[in\]*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. The file pointer object specifying the volume to be dismounted. This parameter is required and cannot be **NULL**.

<a href="" id="filehandle--in-"></a>*FileHandle \[in\]*  
[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) only. The file handle of the volume to be dismounted. This parameter is required and cannot be **NULL**.

<a href="" id="fscontrolcode--in-"></a>*FsControlCode \[in\]*  
Control code for the operation. Use **FSCTL\_ENUM\_EXTERNAL\_BACKING** for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
None. Set to **NULL**.

<a href="" id="inputbufferlength--in-"></a>*InputBufferLength \[in\]*  
Set to 0.

<a href="" id="outputbuffer--out-"></a>*OutputBuffer \[out\]*  
A pointer to the output buffer, which must have a size large enough to receive one or more **WOF\_EXTERNAL\_FILE\_ID** structures.

<a href="" id="outputbufferlength--out-"></a>*OutputBufferLength \[out\]*  
Size of the output buffer pointed to by *OutputBuffer*. *OutputBufferLength* must be &gt;= **sizeof**(WOF\_EXTERNAL\_FILE\_ID).

<a href="" id="lengthreturned--out-"></a>*LengthReturned \[out\]*  
Specifies the number of bytes written into *OutputBuffer* on successful completion.

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
<td align="left"><p><strong>STATUS_ACCESS_DENIED</strong></p></td>
<td align="left"><p>The requestor does not have administrative privileges.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_BUFFER_TOO_SMALL</strong></p></td>
<td align="left"><p>The length of the output buffer pointed to by <em>OutputBuffer</em> and specified by <em>OutputBufferLength</em> is too small.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_NO_MORE_FILES</strong></p></td>
<td align="left"><p>No more files on the volume have a backing source.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_INTERNAL_ERROR</strong></p></td>
<td align="left"><p>The requested volume is not accessible.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_INVALID_DEVICE_REQUEST</strong></p></td>
<td align="left"><p>The backing service is not present or not started.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **WOF\_EXTERNAL\_FILE\_ID** structure returned in *OutputBuffer* contains unique file identifiers for backed files. The structure is defined in ntifs.h as the following.

```ManagedCPlusPlus
typedef struct _WOF_EXTERNAL_FILE_ID {
    FILE_ID_128 FileId;
} WOF_EXTERNAL_FILE_ID, *PWOF_EXTERNAL_FILE_ID;
```

A **FSCTL\_ENUM\_EXTERNAL\_BACKING** request is issued successively to retrieve the identifiers for each file on the volume having backing source. When all the files are enumerated, the STATUS\_NO\_MORE\_FILES status code is returned.

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

[**FSCTL\_GET\_EXTERNAL\_BACKING**](fsctl-get-external-backing.md)

 

 






