---
title: pmssa
description: The pmssa extension displays a specified processor Minimal State Save Area (also known as Min-StateSave Area).
ms.assetid: 55d605bd-0621-4366-8b37-62d462ee1f34
keywords: ["processor minstate save area", "pmssa Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- pmssa
api_type:
- NA
ms.localizationpriority: medium
---

# !pmssa


The **!pmssa** extension displays a specified processor Minimal State Save Area (also known as Min-StateSave Area).

This extension can only be used with an Itanium-based target computer.

```dbgcmd
!pmssa Address
```

**Important**  This command has been deprecated in the Windows Debugger Version 10.0.14257 and later, and is no longer available.

 

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of a processor Min-StateSave Area.

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

 

 

 





