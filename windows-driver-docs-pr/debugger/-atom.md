---
title: atom
description: The atom extension displays the formatted atom table for the specified atom or for all atoms of the current process.
ms.assetid: b4127e4f-a20b-497f-ad84-efea0df0dc80
keywords: ["atom Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- atom
api_type:
- NA
ms.localizationpriority: medium
---

# !atom


The **!atom** extension displays the formatted atom table for the specified atom or for all atoms of the current process.

```dbgcmd
    !atom [Address] 
```

## <span id="ddk__atom_dbg"></span><span id="DDK__ATOM_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal virtual address of the atom to display. If you omit this parameter or specify zero, the atom table for the current process is displayed. This table lists all atoms for the process.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p></p>
Kdextx86.dll
Ntsdexts.dll</td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Exts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about atoms and atom tables, see the Microsoft Windows SDK documentation.

 

 





