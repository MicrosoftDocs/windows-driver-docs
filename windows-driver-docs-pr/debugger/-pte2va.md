---
title: pte2va
description: The pte2va extension displays the virtual address that corresponds to the specified page table entry (PTE).
ms.assetid: 9a94ce3a-dbbc-4566-9ef5-3ec76c1505eb
keywords: ["pte2va Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- pte2va
api_type:
- NA
ms.localizationpriority: medium
---

# !pte2va


The **!pte2va** extension displays the virtual address that corresponds to the specified page table entry (PTE).

```dbgcmd
!pte2va Address
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the PTE.

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

For information about page tables and PTEs, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. (This book may not be available in some languages and countries.)

Remarks
-------

To examine the contents of a specific PTE, use the [**!pte**](-pte.md) extension.

Here is an example of the output from the **!pte2va** extension:

```dbgcmd
kd> !pte2va 9230
000800000248c000 
```

 

 





