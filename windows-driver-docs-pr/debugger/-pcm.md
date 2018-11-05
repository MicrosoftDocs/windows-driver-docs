---
title: pcm
description: The pcm extension displays the specified private cache map. This extension is only available in Windows 2000.
ms.assetid: a6880ad0-5326-4bea-ac84-3311a2ec01da
keywords: ["private cache map", "cache manager", "pcm Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- pcm
api_type:
- NA
ms.localizationpriority: medium
---

# !pcm


The **!pcm** extension displays the specified private cache map. This extension is only available in Windows 2000.

```dbgcmd
!pcm Address
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the private cache map.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Kdextx86.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Unavailable (see Remarks section)</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about cache management, see the Microsoft Windows SDK documentation and *Microsoft Windows Internals* by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

For information about other cache management extensions, see the [**!cchelp**](-cchelp.md) extension reference.

Remarks
-------

This extension is supported only in Windows 2000. In Windows XP and later versions of Windows, use the [**dt nt!\_PRIVATE\_CACHE\_MAP Address**](dt--display-type-.md) command.

 

 





