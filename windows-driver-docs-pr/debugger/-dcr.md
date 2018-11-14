---
title: dcr
description: The dcr extension displays the default control register (DCR) at the specified address.
ms.assetid: 294fc3a9-5182-47ae-a261-53be6389bcf1
keywords: ["DCR (default control register)", "dcr Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- dcr
api_type:
- NA
ms.localizationpriority: medium
---

# !dcr


The **!dcr** extension displays the default control register (DCR) at the specified address.

```dbgcmd
!dcr Expression [DisplayLevel]
```

**Important**  This command has been deprecated in the Windows Debugger Version 10.0.14257 and later, and is no longer available.

 

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Expression______"></span><span id="_______expression______"></span><span id="_______EXPRESSION______"></span> *Expression*   
Specifies the hexadecimal address of the DCR to display. The expression <strong>@dcr</strong> can also be used for this parameter. In that case, information about the current processor DCR is displayed.

<span id="_______DisplayLevel______"></span><span id="_______displaylevel______"></span><span id="_______DISPLAYLEVEL______"></span> *DisplayLevel*   
Can be any one of the following options:

<span id="0"></span>**0**  
Causes only the values of each DCR field to be displayed. This is the default value.

<span id="1"></span>**1**  
Causes the display to include more in-depth information about each of the DCR fields that is not reserved or ignored.

<span id="2"></span>**2**  
Causes the display to include more in-depth information about all of the DCR fields, including those that are ignored or reserved.

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

Remarks
-------

The DCR specifies default parameters for the processor status register values on interruption. The DCR also specifies some additional global controls, as well as whether or not speculative load faults can be deferred.

Here are a couple of examples:

```dbgcmd
kd> !dcr @dcr
dcr:pp be lc dm dp dk dx dr da dd
1 0 1 1 1 1 1 1 1 1

kd> !dcr @dcr 2

  pp : 1 : Privileged Performance Monitor Default
  be : 0 : Big-Endian Default
  lc : 1 : IA-32 Lock check Enable
  rv : 0 : reserved1
  dm : 1 : Defer TLB Miss faults only
  dp : 1 : Defer Page Not Present faults only
  dk : 1 : Defer Key Miss faults only
  dx : 1 : Defer Key Permission faults only
  dr : 1 : Defer Access Rights faults only
  da : 1 : Defer Access Bit faults only
  dd : 0 : Defer Debug faults only
  rv : 0 : reserved2
```

 

 





