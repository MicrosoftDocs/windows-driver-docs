---
title: FSCTL\_IS\_VOLUME\_DIRTY control code
description: The FSCTL\_IS\_VOLUME\_DIRTY control code determines whether the specified volume is dirty.
ms.assetid: 77263957-cf7f-4db1-81b7-c58438202518
keywords: ["FSCTL_IS_VOLUME_DIRTY control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_IS_VOLUME_DIRTY
api_location:
- ntifs.h
api_type:
- HeaderDef
---

# FSCTL\_IS\_VOLUME\_DIRTY control code


The **FSCTL\_IS\_VOLUME\_DIRTY** control code determines whether the specified volume is dirty.

If the volume information file is corrupted, NTFS will return STATUS\_FILE\_CORRUPT\_ERROR.

To perform this operation, minifilter drivers call [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) with the following parameters, and file systems, redirectors, and legacy file system filter drivers call [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) with the following parameters.

**Parameters**

<a href="" id="fileobject"></a>*FileObject*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. File object pointer for the volume. This parameter must represent a user volume open of a mounted file system volume. This parameter is required and cannot be **NULL**.

<a href="" id="filehandle"></a>*FileHandle*  
[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) only. Handle for the volume. This parameter must be a handle for a user volume open of a mounted file system volume. This parameter is required and cannot be **NULL**.

<a href="" id="fscontrolcode"></a>*FsControlCode*  
Control code for the operation. Use FSCTL\_IS\_VOLUME\_DIRTY for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
Not used with this operation; set to **NULL**.

<a href="" id="inputbufferlength"></a>*InputBufferLength*  
Not used with this operation; set to zero.

<a href="" id="outputbuffer"></a>*OutputBuffer*  
Pointer to a caller-allocated, 32-bit-aligned buffer that receives a ULONG bitmask of flags that indicate whether the volume is currently dirty. One or more of the flags in the following table can be set.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>VOLUME_IS_DIRTY</p></td>
<td align="left"><p>The volume is dirty.</p></td>
</tr>
<tr class="even">
<td align="left"><p>VOLUME_UPGRADE_SCHEDULED</p></td>
<td align="left"><p>This value is not currently used.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>All other values</p></td>
<td align="left"><p>Reserved for future use.</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="outputbufferlength"></a>*OutputBufferLength*  
Size, in bytes, of the buffer that is pointed to by the *OutputBuffer* parameter. This size must be at least sizeof(ULONG).

Status block
------------

[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) returns STATUS\_SUCCESS if the operation succeeds. Otherwise, the appropriate function might return one of the following NTSTATUS values:

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
<td align="left"><p><strong>STATUS_INSUFFICIENT_RESOURCES</strong></p></td>
<td align="left"><p>The file system encountered a pool allocation failure. This is an error code.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_INVALID_PARAMETER</strong></p></td>
<td align="left"><p>The buffer that the <em>OutputBuffer</em> parameter points to is <strong>NULL</strong>, or the <em>FileHandle</em> or <em>FileObject</em> parameter does not represent a user volume open. This is an error code.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_INVALID_USER_BUFFER</strong></p></td>
<td align="left"><p>The buffer that the <em>OutputBuffer</em> parameter points to is not large enough to hold the reparse point data, or the <em>FileHandle</em> or <em>FileObject</em> parameter does not represent a user volume open. This is an error code.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_VOLUME_DISMOUNTED</strong></p></td>
<td align="left"><p>The volume is not mounted. This is an error code.</p></td>
</tr>
</tbody>
</table>

 

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
<td align="left">Ntifs.h (include Ntifs.h or Fltkernel.h)</td>
</tr>
</tbody>
</table>

## See also


[**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)

[**FLT\_PARAMETERS for IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](flt-parameters-for-irp-mj-file-system-control.md)

[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988)

[**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](irp-mj-file-system-control.md)

[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FSCTL_IS_VOLUME_DIRTY%20control%20code%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





