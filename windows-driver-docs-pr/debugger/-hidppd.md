---
title: hidppd
description: The hidppd extension displays the contents of the HIDP_PREPARSED_DATA structure.
ms.assetid: 9d92d254-442d-4e42-8a6f-ce8b7ff6312c
keywords: ["HIDP_PREPARSED_DATA", "hidppd Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- hidppd
api_type:
- NA
ms.localizationpriority: medium
---

# !hidppd


The **!hidppd** extension displays the contents of the HIDP\_PREPARSED\_DATA structure.

```dbgcmd
!hidppd Address
```

## <span id="ddk__hidppd_dbg"></span><span id="DDK__HIDPPD_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the HIDP\_PREPARSED\_DATA structure.

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

For information about human input devices (HID), see the Windows Driver Kit (WDK) documentation.

 

 





