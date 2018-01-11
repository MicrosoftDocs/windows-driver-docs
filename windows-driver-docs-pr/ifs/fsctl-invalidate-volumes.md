---
title: FSCTL\_INVALIDATE\_VOLUMES control code
description: The FSCTL\_INVALIDATE\_VOLUMES control code finds and removes all the volumes mounted on the device represented by the specified file object or handle.
ms.assetid: 26B7EBA2-F3A9-4E5A-961C-C1857AA4FF33
keywords: ["FSCTL_INVALIDATE_VOLUMES control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_INVALIDATE_VOLUMES
api_location:
- Ntifs.h
api_type:
- HeaderDef
---

# FSCTL\_INVALIDATE\_VOLUMES control code


The **FSCTL\_INVALIDATE\_VOLUMES** control code finds and removes all the volumes mounted on the device represented by the specified file object or handle.

To perform this operation, minifilter drivers call [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988), and file systems, redirectors, and legacy file system filter drivers call [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462), using the following parameters.

**Parameters**

<a href="" id="fileobject"></a>*FileObject*  
Handle to the device. To obtain a device handle, call the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) function.

<a href="" id="filehandle"></a>*FileHandle*  
Handle to the device. To obtain a device handle, call the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) function.

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

Status block
------------

[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) and [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) return STATUS\_SUCCESS if the operation succeeds or an appropriate NTSTATUS value.

Remarks
-------

FSCTL\_INVALIDATE\_VOLUMES is sent to the file system's control (that is, named) device object, not to a volume device object. For more information about Control Device Objects, see [Creating the Control Device Object](https://msdn.microsoft.com/library/windows/hardware/ff540060).

FAT and NTFS file systems handle surprise removal by responding to IRP\_MJ\_PNP/IRP\_MN\_SURPRISE\_REMOVAL.

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
<td align="left">Ntifs.h (include Ntifs.h)</td>
</tr>
</tbody>
</table>

## See also


[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988)

[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FSCTL_INVALIDATE_VOLUMES%20control%20code%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





