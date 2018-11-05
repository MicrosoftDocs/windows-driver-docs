---
title: .remote_exit (Exit Debugging Client)
description: The .remote_exit command exits the debugging client but does not end the debugging session.
ms.assetid: 9e15a842-6864-4ff9-97bc-f6cc8549a422
keywords: ["Exit Debugging Client (.remote_exit) command", "remote debugging through the debugger, Exit Debugging Client (.remote_exit) command", ".remote_exit (Exit Debugging Client) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .remote_exit (Exit Debugging Client)
api_type:
- NA
ms.localizationpriority: medium
---

# .remote\_exit (Exit Debugging Client)


The **.remote\_exit** command exits the debugging client but does not end the debugging session.

```dbgcmd
.remote_exit [FinalCommands]
```

## <span id="ddk_meta_exit_debugging_client_dbg"></span><span id="DDK_META_EXIT_DEBUGGING_CLIENT_DBG"></span>Parameters


<span id="_______FinalCommands______"></span><span id="_______finalcommands______"></span><span id="_______FINALCOMMANDS______"></span> *FinalCommands*   
Specifies a command string to pass to the debugging server. You should separate multiple commands by using semicolons. These commands are passed to the debugging server and the connection is then broken.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

You can use the **.remote\_exit** command only in a script file. You can use it in KD and CDB, but you cannot use it in WinDbg.

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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about script files, see [Using Script Files](using-script-files.md). For more information about debugging clients and debugging servers, see [Remote Debugging Through the Debugger](remote-debugging-through-the-debugger.md).

Remarks
-------

If you are using KD or CDB directly, instead of using a script, you can exit from the debugging client by using the [**CTRL+B**](ctrl-b--quit-local-debugger-.md) key.

You cannot exit from a debugging client through a script that is executed in WinDbg.

 

 





