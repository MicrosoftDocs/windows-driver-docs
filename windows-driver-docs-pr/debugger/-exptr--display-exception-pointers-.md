---
title: .exptr (Display Exception Pointers)
description: The .exptr command displays an EXCEPTION_POINTERS structure.
ms.assetid: ef98bf22-10a1-4fd2-80f1-fd7eb75015c1
keywords: [".exptr (Display Exception Pointers) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .exptr (Display Exception Pointers)
api_type:
- NA
ms.localizationpriority: medium
---

# .exptr (Display Exception Pointers)


The **.exptr** command displays an EXCEPTION\_POINTERS structure.

```dbgcmd
.exptr Address
```

## <span id="ddk_meta_display_exception_pointers_dbg"></span><span id="DDK_META_DISPLAY_EXCEPTION_POINTERS_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the EXCEPTION\_POINTERS structure.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

 

 





