---
title: cmreslist
description: The cmreslist extension displays the CM_RESOURCE_LIST structure for the specified device object.
ms.assetid: 56b48f62-c638-4082-95d7-5a0c62c94212
keywords: ["CM_RESOURCE_LIST", "cmreslist Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- cmreslist
api_type:
- NA
ms.localizationpriority: medium
---

# !cmreslist


The **!cmreslist** extension displays the CM\_RESOURCE\_LIST structure for the specified device object.

```dbgsyntax
!cmreslist Address
```

## <span id="ddk__cmreslist_dbg"></span><span id="DDK__CMRESLIST_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the CM\_RESOURCE\_LIST structure.

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

See [Plug and Play Debugging](plug-and-play-debugging.md) for applications of this extension command. For information about the CM\_RESOURCE\_LIST structure, see the Windows Driver Kit (WDK) documentation.

 

 





