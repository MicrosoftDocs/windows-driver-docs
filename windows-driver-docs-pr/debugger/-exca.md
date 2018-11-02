---
title: exca
description: The exca extension displays PC-Card Interrupt Controller (PCIC) Exchangable Card Architecture (ExCA) registers.
ms.assetid: a395f7f3-0e1d-4f4c-80a1-018ca52a20fd
keywords: ["PCIC (PC Card Interrupt Controller)", "ExCA registers", "exca Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- exca
api_type:
- NA
ms.localizationpriority: medium
---

# !exca


The **!exca** extension displays PC-Card Interrupt Controller (PCIC) Exchangable Card Architecture (ExCA) registers.

```dbgcmd
!exca BasePort.SocketNumber
```

## <span id="ddk__exca_dbg"></span><span id="DDK__EXCA_DBG"></span>Parameters


<span id="_______BasePort______"></span><span id="_______baseport______"></span><span id="_______BASEPORT______"></span> *BasePort*   
Specifies the base port of the PCIC.

<span id="_______SocketNumber______"></span><span id="_______socketnumber______"></span><span id="_______SOCKETNUMBER______"></span> *SocketNumber*   
Specifies the socket number of the ExCA register on the PCIC.

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

 

The **!exca** extension is only available for an x86-based target computer.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

The [**!cbreg**](-cbreg.md) extension can be used to display CardBus Socket registers and CardBus ExCA registers by address.

 

 





