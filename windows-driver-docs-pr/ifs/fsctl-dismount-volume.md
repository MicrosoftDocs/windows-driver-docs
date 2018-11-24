---
title: FSCTL_DISMOUNT_VOLUME control code
description: The FSCTL\_DISMOUNT\_VOLUME control code attempts to dismount a volume regardless of whether the volume is in use.
ms.assetid: edfff768-3bb3-4b8a-b982-80797ac116fd
keywords: ["FSCTL_DISMOUNT_VOLUME control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_DISMOUNT_VOLUME
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_DISMOUNT\_VOLUME control code


The **FSCTL\_DISMOUNT\_VOLUME** control code attempts to dismount a volume regardless of whether the volume is in use.

To perform this operation, call [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) with the following parameters.

**Parameters**

<a href="" id="instance"></a>*Instance*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. Opaque instance pointer for the caller. This parameter is required and cannot be **NULL**.

<a href="" id="fileobject"></a>*FileObject*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. The file pointer object specifying the volume to be dismounted. This parameter is required and cannot be **NULL**.

<a href="" id="filehandle--in-"></a>*FileHandle \[in\]*  
[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) only. The file handle of the volume to be dismounted. This parameter is required and cannot be **NULL**.

<a href="" id="fscontrolcode--in-"></a>*FsControlCode \[in\]*  
Control code for the operation. Use **FSCTL\_DISMOUNT\_VOLUME** for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
Not used with this operation. Set to **NULL**.

<a href="" id="inputbufferlength--in-"></a>*InputBufferLength \[in\]*  
Not used with this operation. Set to zero.

<a href="" id="outputbuffer--out-"></a>*OutputBuffer \[out\]*  
Not used with this operation. Set to **NULL**.

<a href="" id="outputbufferlength--in-"></a>*OutputBufferLength \[in\]*  
Not used with this operation. Set to zero.

Status block
------------

[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) returns STATUS\_SUCCESS or an appropriate NTSTATUS value.

Remarks
-------

The **FSCTL\_DISMOUNT\_VOLUME** control code will attempt to dismount a volume regardless of whether any other processes are using the volume, which can have unpredictable results for those processes if they do not hold a lock on the volume. For information about locking a volume, see [**FSCTL\_LOCK\_VOLUME**](https://msdn.microsoft.com/library/windows/desktop/aa364575).

The operating system does not detect unmounted volumes. If an attempt is made to access an unmounted volume, the operating system then tries to mount the volume. For example, a call to [**GetLogicalDrives**](https://msdn.microsoft.com/library/windows/desktop/aa364972) triggers the operating system to mount unmounted volumes.

The *FileHandle* handle passed to [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) must be a handle to a volume, opened for direct access. To retrieve a volume handle, call [**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424) with the *ObjectAttributes* parameter set to an *ObjectName* of the following form: *\\\\.\\X:* where *X* is a drive letter of the volume, floppy disk drive, or CD-ROM drive. The application must also specify the FILE\_SHARE\_READ and FILE\_SHARE\_WRITE flags in the *ShareAccess* parameter of **ZwCreateFile**.

If the specified volume is a system volume or contains a page file, the operation fails.

If the specified volume is locked by another process, the operation fails.

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
<td align="left">Ntifs.h</td>
</tr>
</tbody>
</table>

## See also


[**FltCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff541935)

[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988)

[**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424)

[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462)

 

 






