---
title: FSCTL\_ENUM\_OVERLAY control code
description: The FSCTL\_ENUM\_OVERLAY control code enumerates all the data sources from a backing provider for a specified volume.
ms.assetid: 146A7D77-034F-4C06-99B8-8EBA6E7F0A40
keywords: ["FSCTL_ENUM_OVERLAY control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_ENUM_OVERLAY
api_location:
- ntifs.h
api_type:
- HeaderDef
---

# FSCTL\_ENUM\_OVERLAY control code


The **FSCTL\_ENUM\_OVERLAY** control code enumerates all the data sources from a backing provider for a specified volume.

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
A pointer to the input buffer, which must contain a [**WOF\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632452) structure.

<a href="" id="inputbufferlength--in-"></a>*InputBufferLength \[in\]*  
Set to **sizeof**(WOF\_EXTERNAL\_INFO).

<a href="" id="outputbuffer--out-"></a>*OutputBuffer \[out\]*  
Pointer to an output buffer which will receive one or more [**WIM\_PROVIDER\_OVERLAY\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn632451) structures for data sources backing the volume.

<a href="" id="outputbufferlength--out-"></a>*OutputBufferLength \[out\]*  
Size of the buffer pointed to by *OutputBuffer*, in bytes.

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

When enumerating the data sources for the WIM provider, the output buffer will contain an array of [**WIM\_PROVIDER\_OVERLAY\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn632451) structures. The size of the output buffer must be large enough to contain all the overlay entries or the call will return STATUS\_BUFFER\_TOO\_SMALL.

Additional backing providers will define their own specific enumeration structures.

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

[**FSCTL\_ADD\_OVERLAY**](fsctl-add-overlay.md)

[**WOF\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632452)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FSCTL_ENUM_OVERLAY%20control%20code%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





