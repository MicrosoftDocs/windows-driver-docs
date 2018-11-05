---
title: psp
description: The psp extension displays the processor state parameter (PSP) register at the specified address.
ms.assetid: 5ed36051-31e0-405f-ac30-88d888f9d915
keywords: ["processor state parameter (PSP)", "PSP register", "psp Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- psp
api_type:
- NA
ms.localizationpriority: medium
---

# !psp


The **!psp** extension displays the processor state parameter (PSP) register at the specified address.

This extension is supported only on Itanium-based target computers.

```dbgcmd
!psp Address [DisplayLevel]
```

**Important**  This command has been deprecated in the Windows Debugger Version 10.0.14257 and later, and is no longer available.

 

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the PSP register to display.

<span id="_______DisplayLevel______"></span><span id="_______displaylevel______"></span><span id="_______DISPLAYLEVEL______"></span> *DisplayLevel*   
Can be any one of the following options:

<span id="0"></span>**0**  
Displays only the values of each PSP field. This is the default.

<span id="1"></span>**1**  
Displays more in-depth information on each of the PSP fields that is not reserved or ignored.

<span id="2"></span>**2**  
Displays more in-depth information on all of the PSP fields, including those that are ignored or reserved.

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

 

 

 





