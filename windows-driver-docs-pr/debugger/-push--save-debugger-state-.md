---
title: .push (Save Debugger State)
description: The .push command saves the current state of the debugger.
ms.assetid: 2e0b45d6-35b8-4c86-9c54-df8d16b4dcc2
keywords: [".push (Save Debugger State) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .push (Save Debugger State)
api_type:
- NA
ms.localizationpriority: medium
---

# .push (Save Debugger State)


The **.push** command saves the current state of the debugger.

```dbgcmd
.push
.push /r
.push /r /q
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="________r______"></span><span id="________R______"></span> **/r**   
Specifies that the current values in the pseudo-registers **$t0** to **$t19** should be saved. If the **/r** parameter is not used, these values are not saved by the **.push** command.

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

This command is most useful when used with [scripts](using-script-files.md) and [debugger command programs](using-debugger-command-programs.md) so that they can work with one fixed state. To restore the debugger to a state that was previously saved using this command, use the [**.pop (Restore Debugger State)**](-pop--restore-debugger-state-.md) command. If the command is successful, no output is displayed.









