---
title: FSCTL\_MARK\_VOLUME\_DIRTY control code
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FSCTL_MARK_VOLUME_DIRTY%20control%20code%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





