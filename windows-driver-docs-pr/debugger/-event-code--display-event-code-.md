---
title: .event_code (Display Event Code)
description: The .event_code command displays the current event instructions.
ms.assetid: f2ab0f4d-493c-4b8b-a7a0-82c10586d485
keywords: [".event_code (Display Event Code) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .event_code (Display Event Code)
api_type:
- NA
ms.localizationpriority: medium
---

# .event\_code (Display Event Code)


The **.event\_code** command displays the current event instructions.

```dbgcmd
.event_code 
```

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
<td align="left"><p>Live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **.event\_code** command displays the hexadecimal instructions at the current event's instruction pointer. The display includes up to 64 bytes of instructions if they are available.

 

 





