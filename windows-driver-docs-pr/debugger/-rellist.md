---
title: rellist
description: The rellist extension displays a Plug and Play relation list.
ms.assetid: ecbf7e35-91c0-4ff4-82a4-53a935920915
keywords: ["rellist Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- rellist
api_type:
- NA
ms.localizationpriority: medium
---

# !rellist


The **!rellist** extension displays a Plug and Play relation list.

```dbgcmd
!rellist Address [Flags] 
```

## <span id="ddk__rellist_dbg"></span><span id="DDK__RELLIST_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the relation list.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies additional information to include in the display. This can be any combination of the following bits (the default is zero):

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Causes the display to include the CM\_RESOURCE\_LIST. The display also includes the boot resources list, if it is available.

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
Causes the display to include the resource requirements list (IO\_RESOURCE\_LIST).

<span id="Bit_3__0x8_"></span><span id="bit_3__0x8_"></span><span id="BIT_3__0X8_"></span>Bit 3 (0x8)  
Causes the display to include the translated CM\_RESOURCE\_LIST.

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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

See [Plug and Play Debugging](plug-and-play-debugging.md) for applications of this extension command. For information about these list structures, see the Windows Driver Kit (WDK) documentation.

 

 





