---
title: fileobj
description: The fileobj extension displays detailed information about a FILE_OBJECT structure.
ms.assetid: ee9237e7-8a1f-473c-9e30-f2b0731a7519
keywords: ["FILE_OBJECT", "fileobj Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- fileobj
api_type:
- NA
ms.localizationpriority: medium
---

# !fileobj


The **!fileobj** extension displays detailed information about a FILE\_OBJECT structure.

```dbgcmd
!fileobj FileObject
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______FileObject______"></span><span id="_______fileobject______"></span><span id="_______FILEOBJECT______"></span> *FileObject*   
Specifies the address of a [FILE_OBJECT](https://msdn.microsoft.com/library/windows/hardware/ff545834) structure.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about file objects, see the Microsoft Windows SDK documentation, the Windows Driver Kit (WDK) documentation, and *Microsoft Windows Internals* by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

Remarks
-------

If the FILE\_OBJECT structure has an associated cache, **!fileobj** tries to parse and display cache information..

 

 





