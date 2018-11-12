---
title: s (Set Current System)
description: The s command sets or displays the current system number.
ms.assetid: 33ad3a63-166f-4669-868c-49100c9b4d8c
keywords: ["s (Set Current System) Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- s (Set Current System)
api_type:
- NA
ms.localizationpriority: medium
---

# ||s (Set Current System)

The **||s** command sets or displays the current system number.

```dbgcmd
     ||System s 
     || s 
```

Do not confuse this command with the [**s (Search Memory)**](s--search-memory-.md), [**~s (Change Current Processor)**](-s--change-current-processor-.md), [**~s (Set Current Thread)**](-s--set-current-thread-.md), or [**|s (Set Current Process)**](-s--set-current-process-.md) command.


## <span id="ddk_cmd_set_current_system_dbg"></span><span id="DDK_CMD_SET_CURRENT_SYSTEM_DBG"></span>Parameters


<span id="_______System______"></span><span id="_______system______"></span><span id="_______SYSTEM______"></span> *System*   
Specifies the system number to activate. For more information about the syntax, see [System Syntax](system-syntax.md).

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>Multiple target debugging</p></td>
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

 

Remarks
-------

The **||s** command is useful when you are debugging multiple targets or working with multiple dump files.  For more information about these kinds of sessions, see [Debugging Multiple Targets](debugging-multiple-targets.md).

If you use the **||s** syntax, the debugger displays information about the current system.

This command also disassembles the current instruction for the current system, process, and thread.

 
**Note**   There are complications, when you debug live targets and dump targets together, because commands behave differently for each type of debugging. For example, if you use the **g (Go)** command when the current system is a dump file, the debugger begins executing, but you cannot break back into the debugger, because the break command is not recognized as valid for dump file debugging.









