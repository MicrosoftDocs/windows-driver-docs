---
title: FSCTL_GET_EXTERNAL_BACKING control code
description: The FSCTL\_GET\_EXTERNAL\_BACKING control code gets the backing information for a file from an external backing provider.
ms.assetid: 18A8E71E-CAED-4E0A-95D0-18E99F9733B2
keywords: ["FSCTL_GET_EXTERNAL_BACKING control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_GET_EXTERNAL_BACKING
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_GET\_EXTERNAL\_BACKING control code


The **FSCTL\_GET\_EXTERNAL\_BACKING** control code gets the backing information for a file from an external backing provider. Backing providers include the Windows Image Format (WIM) provider or individual compressed file provider. Content for externally backed files may reside on volumes other than on the volume containing the queried file.

To perform this operation, call [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) with the following parameters.

**Parameters**

<a href="" id="instance--in-"></a>*Instance \[in\]*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. An opaque instance pointer for the caller. This parameter is required and cannot be NULL.

<a href="" id="fileobject--in-"></a>*FileObject \[in\]*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. The file pointer object of the file for which backing information is queried. This parameter is required and cannot be NULL.

<a href="" id="filehandle--in-"></a>*FileHandle \[in\]*  
[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) only. The handle of the file for which backing information is queried. This parameter is required and cannot be NULL.

<a href="" id="fscontrolcode--in-"></a>*FsControlCode \[in\]*  
A control code for the operation. Use **FSCTL\_GET\_EXTERNAL\_BACKING** for this operation.

<a href="" id="inputbuffer--in-"></a>*InputBuffer \[in\]*  
None. Set to **NULL**.

<a href="" id="inputbufferlength--in-"></a>*InputBufferLength \[in\]*  
Set to 0.

<a href="" id="outputbuffer--out-"></a>*OutputBuffer \[out\]*  
A pointer to the output buffer, which must have a size large enough to receive a [**WOF\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632452) structure followed by the provider data. For WIM backed files, **WOF\_EXTERNAL\_INFO** is followed by a [**WIM\_PROVIDER\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632448) structure. For individually compressed files, **WOF\_EXTERNAL\_INFO** is followed by a [**FILE\_PROVIDER\_EXTERNAL\_INFO\_V1**](https://msdn.microsoft.com/library/windows/hardware/mt426732) structure.

<a href="" id="outputbufferlength--out-"></a>*OutputBufferLength \[out\]*  
Size, in bytes, of the buffer pointed to by *OutputBuffer*.

<a href="" id="lengthreturned"></a>*LengthReturned*  
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
<td align="left"><p><strong>STATUS_OBJECT_NOT_EXTERNALLY_BACKED</strong></p></td>
<td align="left"><p>The file is not externally backed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_INVALID_DEVICE_REQUEST</strong></p></td>
<td align="left"><p>The backing service is not present or not started.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

When the backing provider for the data source to update is a WIM file, the output buffer will contain a [**WOF\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632452) structure followed by a [**WIM\_PROVIDER\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632448) structure. The *OutputBufferLength* must be at least **sizeof**(WOF\_EXTERNAL\_INFO) + **sizeof**(WIM\_PROVIDER\_EXTERNAL\_INFO). When the backing provider is an individually compressed file, the output buffer will contain a **WOF\_EXTERNAL\_INFO** structure followed by a [**FILE\_PROVIDER\_EXTERNAL\_INFO\_V1**](https://msdn.microsoft.com/library/windows/hardware/mt426732) structure.

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

[**WIM\_PROVIDER\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632448)

[**WOF\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632452)

 

 






