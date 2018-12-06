---
title: FSCTL_ADD_OVERLAY control code
description: The FSCTL\_ADD\_OVERLAY control code adds a new external backing source to a volume’s namespace. This backing source can be a Windows Image Format (WIM) file.
ms.assetid: 0507ECDE-49C6-4EC4-87D6-76D6475620F4
keywords: ["FSCTL_ADD_OVERLAY control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_ADD_OVERLAY
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_ADD\_OVERLAY control code


The **FSCTL\_ADD\_OVERLAY** control code adds a new external backing source to a volume’s namespace. This backing source can be a Windows Image Format (WIM) file.

To perform this operation, call [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) with the following parameters.

**Parameters**

<a href="" id="instance--in-"></a>*Instance \[in\]*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. An opaque instance pointer for the caller. This parameter is required and cannot be NULL.

<a href="" id="fileobject--in-"></a>*FileObject \[in\]*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. The file pointer object of the volume for which the overlay is added to. This parameter is required and cannot be NULL.

<a href="" id="filehandle--in-"></a>*FileHandle \[in\]*  
[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) only. The handle of the volume for which the overlay is added to. This parameter is required and cannot be NULL.

<a href="" id="fscontrolcode--in-"></a>*FsControlCode \[in\]*  
The control code for the operation. Use **FSCTL\_ADD\_OVERLAY** for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
A pointer to the input buffer, which must contain a [**WOF\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632452) structure. When required, additional provider specific data is included immediately after **WOF\_EXTERNAL\_INFO**.

<a href="" id="inputbufferlength--in-"></a>*InputBufferLength \[in\]*  
Set to **sizeof**([**WOF\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632452)) plus the size of any additional provider input data.

<a href="" id="outputbuffer--out-"></a>*OutputBuffer \[out\]*  
A pointer to the output buffer, which contains any resultant information from the add operation.

<a href="" id="outputbufferlength--out-"></a>*OutputBufferLength \[out\]*  
Size of the buffer pointed to by *OutputBuffer*.

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
<td align="left"><p>The length of the output buffer pointed to by <em>OutputBuffer</em>, and specified by <em>OutputBufferLength</em>, is too small.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_INTERNAL_ERROR</strong></p></td>
<td align="left"><p>The requested volume is not accessible.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_INVALID_DEVICE_REQUEST</strong></p></td>
<td align="left"><p>The backing service is not present or not started.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

When the backing source added is a Windows Imaging Format (WIM) file, the input buffer will contain a [**WOF\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632452) structure followed by a [**WIM\_PROVIDER\_ADD\_OVERLAY\_INPUT**](https://msdn.microsoft.com/library/windows/hardware/dn632447) structure. The *InputBufferLength* in this case will be **sizeof**(**WOF\_EXTERNAL\_INFO**) + **sizeof**(**WIM\_PROVIDER\_ADD\_OVERLAY\_INPUT**). On completion of the request, the data pointed to by *OutputBuffer* contains a single LARGE\_INTEGER value which is the new data source identifier for the WIM file.

Other backing providers will define their own specific input parameter structures and output data types.

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


[**FSCTL\_REMOVE\_OVERLAY**](fsctl-remove-overlay.md)

[**FSCTL\_SUSPEND\_OVERLAY**](fsctl-suspend-overlay.md)

[**FSCTL\_UPDATE\_OVERLAY**](fsctl-update-overlay.md)

[**FSCTL\_GET\_EXTERNAL\_BACKING**](fsctl-get-external-backing.md)

[**FSCTL\_SET\_EXTERNAL\_BACKING**](fsctl-set-external-backing.md)

 

 






