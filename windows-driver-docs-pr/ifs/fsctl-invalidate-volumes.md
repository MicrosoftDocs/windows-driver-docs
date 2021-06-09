---
title: FSCTL_INVALIDATE_VOLUMES control code
description: The FSCTL\_INVALIDATE\_VOLUMES control code finds and removes all the volumes mounted on the device represented by the specified file object or handle.
keywords: ["FSCTL_INVALIDATE_VOLUMES control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_INVALIDATE_VOLUMES
api_location:
- Ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_INVALIDATE\_VOLUMES control code


The **FSCTL\_INVALIDATE\_VOLUMES** control code finds and removes all the volumes mounted on the device represented by the specified file object or handle.

To perform this operation, minifilter drivers call [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile), and file systems, redirectors, and legacy file system filter drivers call [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)), using the following parameters.

**Parameters**

<a href="" id="fileobject"></a>*FileObject*  
Handle to the device. To obtain a device handle, call the [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) function.

<a href="" id="filehandle"></a>*FileHandle*  
Handle to the device. To obtain a device handle, call the [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) function.

<a href="" id="fscontrolcode"></a>*FsControlCode*  
Control code for the operation. Use **FSCTL\_INVALIDATE\_VOLUMES** for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
Not used with this operation; set to **NULL**.

<a href="" id="inputbufferlength"></a>*InputBufferLength*  
Not used with this operation; set to zero.

<a href="" id="outputbuffer"></a>*OutputBuffer*  
Not used with this operation; set to **NULL**.

<a href="" id="outputbufferlength"></a>*OutputBufferLength*  
Not used with this operation; set to zero.

## Status block

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) and [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) return STATUS\_SUCCESS if the operation succeeds or an appropriate NTSTATUS value.

## Remarks

FSCTL\_INVALIDATE\_VOLUMES is sent to the file system's control (that is, named) device object, not to a volume device object. For more information about Control Device Objects, see [Creating the Control Device Object](./creating-the-control-device-object.md).

FAT and NTFS file systems handle surprise removal by responding to IRP\_MJ\_PNP/IRP\_MN\_SURPRISE\_REMOVAL.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ntifs.h (include Ntifs.h)</td>
</tr>
</tbody>
</table>

## See also


[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile)

[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85))

 

