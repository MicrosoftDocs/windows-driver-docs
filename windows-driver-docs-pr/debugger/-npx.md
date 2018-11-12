---
title: npx
description: The npx extension displays the contents of the floating-point register save area.
ms.assetid: 1601e4fe-0aba-4507-90a1-402c02fba59d
keywords: ["registers, floating-point register save area", "npx Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- npx
api_type:
- NA
ms.localizationpriority: medium
---

# !npx


The **!npx** extension displays the contents of the floating-point register save area.

```dbgcmd
!npx Address
```

## <span id="ddk__npx_dbg"></span><span id="DDK__NPX_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the FLOATING\_SAVE\_AREA structure.

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
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

This extension command can only be used with an x86-based target computer.

 

 





