---
title: bc (Breakpoint Clear)
description: The bc command permanently removes previously set breakpoints from the system.
ms.assetid: 7bff5261-179f-4fd6-b427-de74e830a8c7
keywords: ["bc (Breakpoint Clear) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- bc (Breakpoint Clear)
api_type:
- NA
ms.localizationpriority: medium
---

# bc (Breakpoint Clear)


The **bc** command permanently removes previously set breakpoints from the system.

```dbgcmd
bc Breakpoints 
```

## <span id="ddk_cmd_breakpoint_clear_dbg"></span><span id="DDK_CMD_BREAKPOINT_CLEAR_DBG"></span>Parameters


<span id="_______Breakpoints______"></span><span id="_______breakpoints______"></span><span id="_______BREAKPOINTS______"></span> *Breakpoints*   
Specifies the ID numbers of the breakpoints to remove. You can specify any number of breakpoints. You must separate multiple IDs by spaces or commas. You can specify a range of breakpoint IDs by using a hyphen (-). You can use an asterisk (\*) to indicate all breakpoints. If you want to use a [numeric expression](numerical-expression-syntax.md) for an ID, enclose it in brackets (\[\]). If you want to use a [string with wildcard characters](string-wildcard-syntax.md) to match a breakpoint's symbolic name, enclose it in quotation marks ( " " ).

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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about how to use breakpoints, other breakpoint commands and methods of controlling breakpoints, and how to set breakpoints in user space from a kernel debugger, see [Using Breakpoints](using-breakpoints.md). For more information about conditional breakpoints, see [Setting a Conditional Breakpoint](setting-a-conditional-breakpoint.md).

Remarks
-------

Use the [**bl (Breakpoint List)**](bl--breakpoint-list-.md) command to list all existing breakpoints, their ID numbers, and their status.

Use the [**.bpcmds (Display Breakpoint Commands)**](-bpcmds--display-breakpoint-commands-.md) command to list all existing breakpoints, their ID numbers, and the commands that were used to create them.

 

 





