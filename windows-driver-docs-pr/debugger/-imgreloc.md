---
title: imgreloc
description: The imgreloc extension displays the addresses of each loaded module and indicates their former addresses before they were relocated.
ms.assetid: 79b729bd-7e4f-4167-b049-8a5c23cb8787
keywords: ["imgreloc Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- imgreloc
api_type:
- NA
ms.localizationpriority: medium
---

# !imgreloc


The **!imgreloc** extension displays the addresses of each loaded module and indicates their former addresses before they were relocated.

```dbgcmd
!imgreloc Address 
```

## <span id="ddk__imgreloc_dbg"></span><span id="DDK__IMGRELOC_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the base address of the image.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Here is an example:

```dbgcmd
0:000> !imgreloc 00400000
00400000 Prymes - at preferred address
010e0000 appvcore - RELOCATED from 00400000
5b2f0000 verifier - at preferred address
5d160000 ShimEng - at preferred address
```

 

 





