---
title: minipkd.exports
description: The minipkd.exports extension displays the addresses of the miniport exports for the specified adapter.
ms.assetid: 7d92539c-26b5-4cab-84df-b643612a98d0
keywords: ["minipkd.exports Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- minipkd.exports
api_type:
- NA
ms.localizationpriority: medium
---

# !minipkd.exports


The **!minipkd.exports** extension displays the addresses of the miniport exports for the specified adapter.

```dbgcmd
!minipkd.exports Adapter 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Adapter______"></span><span id="_______adapter______"></span><span id="_______ADAPTER______"></span> *Adapter*   
Specifies the address of an adapter.

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
<td align="left"><p>Minipkd.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [SCSI Miniport Debugging](scsi-miniport-debugging.md).

 

 





