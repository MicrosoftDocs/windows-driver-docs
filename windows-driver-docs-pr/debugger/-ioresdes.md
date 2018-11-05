---
title: ioresdes
description: The ioresdes extension displays the IO_RESOURCE_DESCRIPTOR structure at the specified address.
ms.assetid: a57dd414-16d6-4515-9eee-dac91398906b
keywords: ["ioresdes Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ioresdes
api_type:
- NA
ms.localizationpriority: medium
---

# !ioresdes


The **!ioresdes** extension displays the IO\_RESOURCE\_DESCRIPTOR structure at the specified address.

```dbgcmd
!ioresdes Address 
```

## <span id="ddk__ioresdes_dbg"></span><span id="DDK__IORESDES_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the IO\_RESOURCE\_DESCRIPTOR structure.

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

See [Plug and Play Debugging](plug-and-play-debugging.md) for applications of this extension command. For information about the IO\_RESOURCE\_DESCRIPTOR structure, see the Windows Driver Kit (WDK) documentation.

 

 





