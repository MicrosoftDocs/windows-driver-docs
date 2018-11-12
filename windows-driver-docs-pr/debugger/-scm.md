---
title: scm
description: The scm extension displays the specified shared cache map.
ms.assetid: 4333ee14-ca28-43af-b132-210996328af2
keywords: ["shared cache map", "cache manager", "scm Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- scm
api_type:
- NA
ms.localizationpriority: medium
---

# !scm


The **!scm** extension displays the specified shared cache map.

```dbgcmd
!scm Address
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the shared cache map.

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
<td align="left"><p>Unavailable</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about cache management, see the Microsoft Windows SDK documentation and *Microsoft Windows Internals* by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

For information about other cache management extensions, see the [**!cchelp**](-cchelp.md) extension.

Remarks
-------

In Windows XP and later versions of Windows, use the [**dt nt!\_SHARED\_CACHE\_MAP Address**](dt--display-type-.md) command instead of **!scm**.

 

 





