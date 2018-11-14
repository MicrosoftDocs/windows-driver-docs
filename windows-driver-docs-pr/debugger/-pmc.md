---
title: pmc
description: The pmc extension displays the Performance Monitor Counter (PMC) register at the specified address.
ms.assetid: ff9a03af-f0e9-4aef-b583-c3092eb5f89c
keywords: ["Performance Monitor Counter (PMC)", "pmc Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- pmc
api_type:
- NA
ms.localizationpriority: medium
---

# !pmc


The **!pmc** extension displays the Performance Monitor Counter (PMC) register at the specified address.

This extension is supported only on an Itanium-based target computer.

```dbgcmd
!pmc [- Option] Expression [DisplayLevel]
```

**Important**  This command has been deprecated in the Windows Debugger Version 10.0.14257 and later, and is no longer available.

 

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Option______"></span><span id="_______option______"></span><span id="_______OPTION______"></span> *Option*   
Can be any one of the following values:

<span id="gen"></span><span id="GEN"></span>**gen**  
Displays the register as a generic PMC register.

<span id="btb"></span><span id="BTB"></span>**btb**  
Displays the register as a branch trace buffer (BTB) PMC register.

<span id="_______Expression______"></span><span id="_______expression______"></span><span id="_______EXPRESSION______"></span> *Expression*   
Specifies the hexadecimal address of a PMC. The expressions <strong>@kpfcgen</strong> and <strong>@kpfcbtb</strong> can be used as values for this parameter.

If *Expression* is <strong>@kpfcgen</strong>, the debugger displays the current processor PMC register as a generic PMC register. You can also display the current processor PMC register as a generic PMC register by setting *Option* to **gen** and using <strong>@kpfc4</strong>, <strong>@kpfc5</strong>, <strong>@kpfc6</strong>, or <strong>@kpfc7</strong> for the *Expression* value.

If *Expression* is <strong>@kpfcbtb</strong>, the debugger displays the current processor PMC register as a BTB PMC register. You can also display the current processor PMC register as a BTB PMC register by setting *Option* to **btb** and using @kpfc12 for the *Expression* value.

<span id="_______DisplayLevel______"></span><span id="_______displaylevel______"></span><span id="_______DISPLAYLEVEL______"></span> *DisplayLevel*   
Can be any one of the following values:

<span id="0"></span>**0**  
Displays only the values of each PMC register field. This is the default.

<span id="1"></span>**1**  
Displays detailed information about the PMC register fields that are not reserved or ignored.

<span id="2"></span>**2**  
Displays detailed information about all PMC register fields, including those that are ignored or reserved.

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

 

 

 





