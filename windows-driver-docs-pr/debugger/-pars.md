---
title: pars
description: The pars extension displays a specified processor application registers file.
ms.assetid: cd952f00-a135-411c-99e0-20153f2539cd
keywords: ["processor application register", "pars Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- pars
api_type:
- NA
ms.localizationpriority: medium
---

# !pars


The **!pars** extension displays a specified processor application registers file.

```dbgcmd
!pars Address
```

**Important**  This command has been deprecated in the Windows Debugger Version 10.0.14257 and later, and is no longer available.

 

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of a processor application registers file.

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

 

This extension command can only be used with an Itanium-based target computer.

 

 





