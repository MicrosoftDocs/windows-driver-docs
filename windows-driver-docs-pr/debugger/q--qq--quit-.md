---
title: q, qq (Quit)
description: The q and qq commands end the debugging session.
ms.assetid: 94d35997-8b21-4d25-b2ae-4b2a78240153
keywords: ["q, qq (Quit) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- q, qq (Quit)
api_type:
- NA
ms.localizationpriority: medium
---

# q, qq (Quit)


The **q** and **qq** commands end the debugging session. (In CDB and KD, this command also exits the debugger itself. In WinDbg, this command returns the debugger to dormant mode.)

```dbgcmd
q 
qq 
```

## <span id="ddk_cmd_quit_dbg"></span><span id="DDK_CMD_QUIT_DBG"></span>


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

In user-mode debugging, the **q** command ends the debugging session and closes the target application.

In kernel-mode debugging, the **q** command saves the log file and ends the debugging session. The target computer remains locked.

If this command does not work in KD, press [**CTRL+R+ENTER**](ctrl-r--re-synchronize-.md) on the debugger keyboard, and then retry the **q** command. If this action does not work, you must use CTRL+B+ENTER to exit the debugger.

The **qq** command behaves exactly like the **q** command, unless you are performing remote debugging. During remote debugging, the **q** command has no effect, but the **qq** command ends the debugging server. For more information about this effect, see [Remote Debugging Through the Debugger](remote-debugging-through-the-debugger.md).

 

 





