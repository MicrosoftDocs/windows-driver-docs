---
title: FSCTL\_GET\_BOOT\_AREA\_INFO control code
description: The FSCTL\_GET\_BOOT\_AREA\_INFO control code retrieves the locations of boot sectors for a volume.
ms.assetid: 0e842609-65f9-4a61-ab7f-f525650dfd14
keywords: ["FSCTL_GET_BOOT_AREA_INFO control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_GET_BOOT_AREA_INFO
api_location:
- Ntifs.h
api_type:
- HeaderDef
---

# FSCTL\_GET\_BOOT\_AREA\_INFO control code


The **FSCTL\_GET\_BOOT\_AREA\_INFO** control code retrieves the locations of boot sectors for a volume.

To perform this operation, call the [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) function or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) function with the following parameters.

**Parameters**

<a href="" id="fileobject"></a>*FileObject*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. A file object pointer for the volume for which **FSCTL\_GET\_BOOT\_AREA\_INFO** will retrieve the boot information. This parameter is required and cannot be **NULL**.

<a href="" id="filehandle"></a>*FileHandle*  
[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) only. A file handle for the volume for which **FSCTL\_GET\_BOOT\_AREA\_INFO** will retrieve the boot information. This parameter is required and cannot be **NULL**.

This handle must be opened with the SE\_MANAGE\_VOLUME\_NAME access rights. For more information, see [File Security and Access Rights](https://msdn.microsoft.com/library/windows/desktop/aa364399).

<a href="" id="fscontrolcode"></a>*FsControlCode*  
A control code for the operation. Use **FSCTL\_GET\_BOOT\_AREA\_INFO** for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
Not used with this operation. Set to **NULL**.

<a href="" id="inputbufferlength"></a>*InputBufferLength*  
Not used with this operation. Set to zero.

<a href="" id="outputbuffer"></a>*OutputBuffer*  
A pointer to a [**BOOT\_AREA\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff728836) structure, which receives the location of the volume's boot sectors.

<a href="" id="outputbufferlength"></a>*OutputBufferLength*  
The size of the output buffer, in bytes.

Status block
------------

[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) returns an appropriate NTSTATUS value such as one of the following:

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
<td align="left"><p>The operation was successful. OutputBuffer contains a pointer to a [<strong>BOOT_AREA_INFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff728836) structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_INVALID_PARAMETER</strong></p></td>
<td align="left"><p>A parameter was not valid; for example, the handle used is not a valid volume handle.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_BUFFER_TOO_SMALL</strong></p></td>
<td align="left"><p>OutputBuffer is not large enough for the result. No information has been written to the buffer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_ACCESS_DENIED</strong></p></td>
<td align="left"><p>The user does not have SE_MANAGE_VOLUME access.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

**FSCTL\_GET\_BOOT\_AREA\_INFO** control code can be used on FastFAT and exFAT devices. This capability supports the use of BitLocker for devices such as flash drives.

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


[**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FSCTL_GET_BOOT_AREA_INFO%20control%20code%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





