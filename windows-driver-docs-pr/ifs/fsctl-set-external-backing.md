---
title: FSCTL_SET_EXTERNAL_BACKING control code
description: The FSCTL\_SET\_EXTERNAL\_BACKING control code sets the backing source for a file, such as a Windows Image Format (WIM) file or compressed file, by an external backing provider.
ms.assetid: 5CB9FD4D-AF29-4438-B0B5-49871102968A
keywords: ["FSCTL_SET_EXTERNAL_BACKING control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_SET_EXTERNAL_BACKING
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_SET\_EXTERNAL\_BACKING control code


The **FSCTL\_SET\_EXTERNAL\_BACKING** control code sets the backing source for a file, such as a Windows Image Format (WIM) file or compressed file, by an external backing provider. Content for externally backed files may be sourced on volumes other than on volume where the file resides.

To perform this operation, call [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) with the following parameters.

**Parameters**

<a href="" id="instance--in-"></a>*Instance \[in\]*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. An opaque instance pointer for the caller. This parameter is required and cannot be NULL.

<a href="" id="fileobject--in-"></a>*FileObject \[in\]*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. The file pointer object of the file for which backing is set. This parameter is required and cannot be NULL.

<a href="" id="filehandle--in-"></a>*FileHandle \[in\]*  
[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) only. The handle of the file for which backing is set. This parameter is required and cannot be NULL.

<a href="" id="fscontrolcode--in-"></a>*FsControlCode \[in\]*  
The control code for the operation. Use **FSCTL\_SET\_EXTERNAL\_BACKING** for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
A pointer to the input buffer, which contains [**WOF\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632452) structure followed by the provider data. For WIM backed files, **WOF\_EXTERNAL\_INFO** is followed by a [**WIM\_PROVIDER\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632448) structure.

<a href="" id="inputbufferlength--in-"></a>*InputBufferLength \[in\]*  
Size of the data provided in the *InputBuffer*.

<a href="" id="outputbuffer--out-"></a>*OutputBuffer \[out\]*  
None. Set to NULL.

<a href="" id="outputbufferlength--in-"></a>*OutputBufferLength \[in\]*  
Set to 0.

Status block
------------

[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) returns STATUS\_SUCCESS if the operation succeeds. Otherwise, the appropriate NTSTATUS values is returned.

Remarks
-------

When the backing provider for the data source added is the WIM provider, the input buffer will contain a [**WOF\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632452) structure followed by a [**WIM\_PROVIDER\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632448) structure. The *InputBufferLength* in this case will be **sizeof**(**WOF\_EXTERNAL\_INFO**) + **sizeof**(**WIM\_PROVIDER\_EXTERNAL\_INFO**).

Individually compressed files offer good compression for data which will not be modified, including executable files. If these are opened for write the file will be transparently decompressed. To specify an individually compressed file,, the input buffer will contain a [**WOF\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632452) structure followed by a [**FILE\_PROVIDER\_EXTERNAL\_INFO\_V1**](https://msdn.microsoft.com/library/windows/hardware/mt426732) structure. The *InputBufferLength* in this case will be **sizeof**(**WOF\_EXTERNAL\_INFO**) + **sizeof**(**FILE\_PROVIDER\_EXTERNAL\_INFO\_V1**). Individual compressed files are available starting with Windows 10.

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

[**FSCTL\_DELETE\_EXTERNAL\_BACKING**](fsctl-delete-external-backing.md)

[**FSCTL\_GET\_EXTERNAL\_BACKING**](fsctl-get-external-backing.md)

[**WIM\_PROVIDER\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632448)

[**WOF\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632452)

 

 






