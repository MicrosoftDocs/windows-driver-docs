---
title: .show_sym_failures
description: The .show_sym_failures command enables or disables the display of symbol lookup failures and type lookup failures.
ms.assetid: cf0b6cfd-aad2-482f-a382-a3909f5f3cd4
keywords: [".show_sym_failures Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .show_sym_failures
api_type:
- NA
ms.localizationpriority: medium
---

# .show\_sym\_failures


The **.show\_sym\_failures** command enables or disables the display of symbol lookup failures and type lookup failures.

```dbgcmd
.show_sym_failures /s 
.show_sym_failures /S
.show_sym_failures /t
.show_sym_failures /T
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="________s______"></span><span id="________S______"></span> **/s**   
Enables the display of symbol lookup failures.

<span id="________S______"></span><span id="________s______"></span> **/S**   
Disables the display of symbol lookup failures.

<span id="________t______"></span><span id="________T______"></span> **/t**   
Enables the display of type lookup failures.

<span id="________T______"></span><span id="________t______"></span> **/T**   
Disables the display of type lookup failures.

## <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

 

 





