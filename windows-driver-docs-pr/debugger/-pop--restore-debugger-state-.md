---
title: .pop (Restore Debugger State)
description: The .pop command restores the state of the debugger to a state that has previously been saved by using the .push (Save Debugger State) command.
ms.assetid: 31f94b2a-3597-40e4-845a-d686274e36c3
keywords: ["Restore Debugger State (.pop) command", ".pop (Restore Debugger State) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .pop (Restore Debugger State)
api_type:
- NA
ms.localizationpriority: medium
---

# .pop (Restore Debugger State)


The **.pop** command restores the state of the debugger to a state that has previously been saved by using the [**.push (Save Debugger State)**](-push--save-debugger-state-.md) command.

```dbgcmd
.pop
.pop /r
.pop /r /q
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="________r______"></span><span id="________R______"></span> **/r**   
Specifies that the saved values of the pseudo-registers $t0 to $t19 should be restored. If **/r** is not included, these values are not affected by the **.pop** command.

<span id="________q______"></span><span id="________Q______"></span> **/q**   
Specifies that the command executes quietly. That is, the command executes without displaying any output.

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

 

Remarks
-------

This command is most useful when used with [scripts](using-script-files.md) and [debugger command programs](using-debugger-command-programs.md) so that they can work with one fixed state. If the command is successful, no output is displayed.

 

 





