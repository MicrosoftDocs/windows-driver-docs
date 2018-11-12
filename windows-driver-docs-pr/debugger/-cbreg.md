---
title: cbreg
description: The cbreg extension displays CardBus Socket registers and CardBus Exchangable Card Architecture (ExCA) registers.
ms.assetid: 7943e152-b1c9-464c-a0ad-3beac48884d2
keywords: ["CardBus", "ExCA registers", "cbreg Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- cbreg
api_type:
- NA
ms.localizationpriority: medium
---

# !cbreg


The **!cbreg** extension displays CardBus Socket registers and CardBus Exchangable Card Architecture (ExCA) registers.

```dbgsyntax
    !cbreg [%%]Address 
```

## <span id="ddk__cbreg_dbg"></span><span id="DDK__CBREG_DBG"></span>Parameters


<span id="_______________"></span> **%%**   
Indicates that *Address* is a physical address rather than a virtual address.

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the register to be displayed.

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
Kext.dll
Kdextx86.dll</td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kext.dll</p></td>
</tr>
</tbody>
</table>

 

The **!cbreg** extension is only available for an x86-based target computer.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

The [**!exca**](-exca.md) extension can be used to display PCIC ExCA registers by socket number.

 

 





