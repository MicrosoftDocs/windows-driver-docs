---
title: memlist
description: The memlist extension scans physical memory lists from the page frame number (PFN) database in order to check them for consistency.
ms.assetid: 9d5307df-5e46-4d95-8c96-ab6da0f54cd0
keywords: ["PFN database", "memlist Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- memlist
api_type:
- NA
ms.localizationpriority: medium
---

# !memlist


The **!memlist** extension scans physical memory lists from the page frame number (PFN) database in order to check them for consistency.

```dbgcmd
!memlist Flags
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies which memory lists to verify. At present, only one value has been implemented:

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Causes the zeroed pages list to be verified.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

At present, this extension will only check the zeroed pages list to make sure that all pages in that list are zeroed. The appropriate syntax is:

```dbgcmd
kd> !memlist 1
```

 

 





