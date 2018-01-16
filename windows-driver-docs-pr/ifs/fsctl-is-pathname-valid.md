---
title: FSCTL\_IS\_PATHNAME\_VALID control code
description: The FSCTL\_IS\_PATHNAME\_VALID control code performs static analysis of the supplied pathname and returns a status value that indicates whether the pathname is well formed (for example, no illegal characters, acceptable path length, and so on).
ms.assetid: 3f95ae2c-a376-4c68-9e84-dde22aa7e315
keywords: ["FSCTL_IS_PATHNAME_VALID control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_IS_PATHNAME_VALID
api_location:
- Ntifs.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# FSCTL\_IS\_PATHNAME\_VALID control code


The **FSCTL\_IS\_PATHNAME\_VALID** control code performs static analysis of the supplied pathname and returns a status value that indicates whether the pathname is well formed (for example, no illegal characters, acceptable path length, and so on). Because this analysis does not consider the content of the volume, it sometimes gives "false positives." In other words, the analysis might indicate that the pathname is well formed, even when it is not. Negative results are more reliable, but are not guaranteed to be correct.

This control code is not supported with fast FAT file systems, and it is not a meaningful operation in NTFS or UDFS. NTFS and UDFS support such a wide variety of codesets that any string is potentially a valid pathname.

To perform this operation, call [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) with the following parameters.

**Parameters**

<a href="" id="fileobject"></a>*FileObject*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. Not used.

<a href="" id="filehandle"></a>*FileHandle*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. Not used.

<a href="" id="fscontrolcode"></a>*FsControlCode*  
The control code for the operation. Use FSCTL\_IS\_PATHNAME\_VALID for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
A buffer that contains the NULL-terminated pathname string to check.

<a href="" id="inputbufferlength"></a>*InputBufferLength*  
The length, in bytes, of the pathname.

<a href="" id="outputbuffer"></a>*OutputBuffer*  
Not used.

<a href="" id="outputbufferlength"></a>*OutputBufferLength*  
Not used.

Status block
------------

[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) returns STATUS\_SUCCESS if the pathname is well formed. Otherwise, the routine that is used returns the appropriate NTSTATUS error code.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FSCTL_IS_PATHNAME_VALID%20control%20code%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




