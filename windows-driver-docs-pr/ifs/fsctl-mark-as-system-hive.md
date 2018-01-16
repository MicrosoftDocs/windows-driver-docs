---
title: FSCTL\_MARK\_AS\_SYSTEM\_HIVE control code
description: The FSCTL\_MARK\_AS\_SYSTEM\_HIVE control code informs the file system that the specified file contains the registry's system hive.
ms.assetid: de3cb340-2485-4bc5-bc2a-3c34cee2d6b3
keywords: ["FSCTL_MARK_AS_SYSTEM_HIVE control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_MARK_AS_SYSTEM_HIVE
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

# FSCTL\_MARK\_AS\_SYSTEM\_HIVE control code


The **FSCTL\_MARK\_AS\_SYSTEM\_HIVE** control code informs the file system that the specified file contains the registry's system hive. The file system must flush system hive data to disk at just the right moment to avoid deadlocks and to ensure data integrity. Do not use this file system control code with any file other than the file that contains the registry's system hive. This control code does not work with a directory or volume handle. File system redirectors that access files on remote machines treat this control code as a no-op.

Only kernel-level components can use this filesystem control code.

To perform this operation, call [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) with the following parameters.

**Parameters**

<a href="" id="fileobject"></a>*FileObject*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. File object pointer for the user file. This parameter is required and cannot be **NULL**.

<a href="" id="filehandle"></a>*FileHandle*  
[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) only. Handle for the user file. This parameter is required and cannot be **NULL**.

<a href="" id="fscontrolcode"></a>*FsControlCode*  
The control code for the operation. Use **FSCTL\_MARK\_AS\_SYSTEM\_HIVE** for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
Not used. Assign a value of **NULL** to this parameter.

<a href="" id="inputbufferlength"></a>*InputBufferLength*  
Not used.

<a href="" id="outputbuffer"></a>*OutputBuffer*  
Not used. Assign a value of **NULL** to this parameter.

<a href="" id="outputbufferlength"></a>*OutputBufferLength*  
Not used.

Status block
------------

[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) returns STATUS\_SUCCESS if the operation succeeds. Otherwise, the appropriate function returns the appropriate NTSTATUS error code.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FSCTL_MARK_AS_SYSTEM_HIVE%20control%20code%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




