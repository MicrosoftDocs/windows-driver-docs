---
title: FSCTL\_ADD\_OVERLAY control code
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FSCTL_ADD_OVERLAY%20control%20code%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





