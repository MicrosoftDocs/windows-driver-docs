---
title: bushnd
description: The bushnd extension displays a HAL BUS_HANDLER structure.
ms.assetid: dd2cb9c1-9abe-4209-a4fa-dc50965e807e
keywords: ["bushnd Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- bushnd
api_type:
- NA
ms.localizationpriority: medium
---

# !bushnd


The **!bushnd** extension displays a HAL BUS\_HANDLER structure.

```dbgsyntax
    !bushnd [Address] 
```

## <span id="ddk__bushnd_dbg"></span><span id="DDK__BUSHND_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the HAL BUS\_HANDLER structure. If omitted, **!bushnd** displays a list of buses and the base address of the handler.

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

 

 

 





