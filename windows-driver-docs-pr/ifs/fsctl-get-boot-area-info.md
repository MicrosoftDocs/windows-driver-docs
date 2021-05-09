---
title: FSCTL_GET_BOOT_AREA_INFO control code
description: The FSCTL\_GET\_BOOT\_AREA\_INFO control code retrieves the locations of boot sectors for a volume.
keywords: ["FSCTL_GET_BOOT_AREA_INFO control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_GET_BOOT_AREA_INFO
api_location:
- Ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_GET\_BOOT\_AREA\_INFO control code


The **FSCTL\_GET\_BOOT\_AREA\_INFO** control code retrieves the locations of boot sectors for a volume.

To perform this operation, call the [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) function or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) function with the following parameters.

**Parameters**

<a href="" id="fileobject"></a>*FileObject*  
[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. A file object pointer for the volume for which **FSCTL\_GET\_BOOT\_AREA\_INFO** will retrieve the boot information. This parameter is required and cannot be **NULL**.

<a href="" id="filehandle"></a>*FileHandle*  
[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) only. A file handle for the volume for which **FSCTL\_GET\_BOOT\_AREA\_INFO** will retrieve the boot information. This parameter is required and cannot be **NULL**.

This handle must be opened with the SE\_MANAGE\_VOLUME\_NAME access rights. For more information, see [File Security and Access Rights](/windows/desktop/FileIO/file-security-and-access-rights).

<a href="" id="fscontrolcode"></a>*FsControlCode*  
A control code for the operation. Use **FSCTL\_GET\_BOOT\_AREA\_INFO** for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
Not used with this operation. Set to **NULL**.

<a href="" id="inputbufferlength"></a>*InputBufferLength*  
Not used with this operation. Set to zero.

<a href="" id="outputbuffer"></a>*OutputBuffer*  
A pointer to a [**BOOT\_AREA\_INFO**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_boot_area_info) structure, which receives the location of the volume's boot sectors.

<a href="" id="outputbufferlength"></a>*OutputBufferLength*  
The size of the output buffer, in bytes.

## Status block

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) returns an appropriate NTSTATUS value such as one of the following:

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
<td align="left"><p>The operation was successful. OutputBuffer contains a pointer to a <a href="/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_boot_area_info" data-raw-source="[&lt;strong&gt;BOOT_AREA_INFO&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_boot_area_info)"><strong>BOOT_AREA_INFO</strong></a> structure.</p></td>
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

 

## Remarks

**FSCTL\_GET\_BOOT\_AREA\_INFO** control code can be used on FastFAT and exFAT devices. This capability supports the use of BitLocker for devices such as flash drives.

## Requirements

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


[**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol)

