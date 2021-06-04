---
title: FSCTL_QUERY_PERSISTENT_VOLUME_STATE control code
description: The FSCTL\_QUERY\_PERSISTENT\_VOLUME\_STATE control code retrieves persistent settings for a file system volume.
keywords: ["FSCTL_QUERY_PERSISTENT_VOLUME_STATE control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_QUERY_PERSISTENT_VOLUME_STATE
api_location:
- Ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_QUERY\_PERSISTENT\_VOLUME\_STATE control code


The **FSCTL\_QUERY\_PERSISTENT\_VOLUME\_STATE** control code retrieves persistent settings for a file system volume. Persistent settings remain on a file system volume between reboots of the computer.

To perform this operation, call [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with the following parameters.

**Parameters**

<a href="" id="fileobject"></a>*FileObject*  
[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. A file object pointer for the file system volume. This parameter is required and cannot be **NULL**.

<a href="" id="filehandle"></a>*FileHandle*  
[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) only. A file handle for the file system volume. This parameter is required and cannot be **NULL**.

<a href="" id="fscontrolcode"></a>*FsControlCode*  
The control code for the operation. Use **FSCTL\_QUERY\_PERSISTENT\_VOLUME\_STATE** for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
A pointer to a caller-allocated [**FILE\_FS\_PERSISTENT\_VOLUME\_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_fs_persistent_volume_information) structure.

<a href="" id="inputbufferlength"></a>*InputBufferLength*  
The size, in bytes, of the buffer pointed to by the *InputBuffer* parameter.

<a href="" id="outputbuffer"></a>*OutputBuffer*  
A pointer to a caller-allocated [**FILE\_FS\_PERSISTENT\_VOLUME\_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_fs_persistent_volume_information) structure that receives the persistent settings for a file system volume.

<a href="" id="outputbufferlength"></a>*OutputBufferLength*  
The size, in bytes, of the buffer pointed to by the *OutputBuffer* parameter.

## Status block

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) returns STATUS\_SUCCESS or an appropriate NTSTATUS value such as one of the following:

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
<td align="left"><p><strong>STATUS_NOT_SUPPORTED</strong></p></td>
<td align="left"><p>The caller specified an incorrect version number in the <strong>Version</strong> member of <a href="/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_fs_persistent_volume_information" data-raw-source="[&lt;strong&gt;FILE_FS_PERSISTENT_VOLUME_INFORMATION&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_fs_persistent_volume_information)"><strong>FILE_FS_PERSISTENT_VOLUME_INFORMATION</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_INVALID_PARAMETER</strong></p></td>
<td align="left"><p>The file system volume is not an open user volume, or the caller specified an invalid flag in the <strong>FlagMask</strong> member of <a href="/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_fs_persistent_volume_information" data-raw-source="[&lt;strong&gt;FILE_FS_PERSISTENT_VOLUME_INFORMATION&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_fs_persistent_volume_information)"><strong>FILE_FS_PERSISTENT_VOLUME_INFORMATION</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_BUFFER_TOO_SMALL</strong></p></td>
<td align="left"><p>The buffer that the <em>InputBuffer</em> parameter points to is not large enough (that is, the buffer is less than <strong>sizeof</strong>(FILE_FS_PERSISTENT_VOLUME_INFORMATION)). In this case, no persistent-settings data is returned. This is an error code.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_ACCESS_DENIED</strong></p></td>
<td align="left"><p>The caller cannot access the file system volume.</p></td>
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
<td align="left"><p>The file system volume is read only.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available starting with Windows 7.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntifs.h (include Ntifs.h)</td>
</tr>
</tbody>
</table>

## See also


[**FILE\_FS\_PERSISTENT\_VOLUME\_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_fs_persistent_volume_information)

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile)

[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85))

