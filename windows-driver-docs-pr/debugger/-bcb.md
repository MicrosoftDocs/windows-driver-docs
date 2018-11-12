---
title: bcb
description: The bcb extension displays the specified buffer control block.
ms.assetid: 4e98e900-5e9d-40a4-9c39-4dc3611d8ea3
keywords: ["cache manager", "bcb Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- bcb
api_type:
- NA
ms.localizationpriority: medium
---

# !bcb


The **!bcb** extension displays the specified buffer control block.

```dbgcmd
!bcb Address
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the buffer control block.

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

For information about other cache management extensions, use the [**!cchelp**](-cchelp.md) extension.

Remarks
-------

This extension is available for Windows 2000 only. In Windows XP or later, use the [**dt nt!\_BCB Address**](dt--display-type-.md) command to display the buffer control block directly.

 

 





