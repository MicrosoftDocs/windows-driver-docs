---
title: FSCTL_MARK_AS_SYSTEM_HIVE control code
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
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





