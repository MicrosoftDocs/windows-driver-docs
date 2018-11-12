---
title: .restart (Restart Kernel Connection)
description: The .restart command restarts the kernel connection.Do not confuse this command with the .restart (Restart Target Application) command, which works only in user mode.
ms.assetid: 2c81625b-d75f-4c5f-9437-9619bf33b500
keywords: [".restart (Restart Kernel Connection) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .restart (Restart Kernel Connection)
api_type:
- NA
ms.localizationpriority: medium
---

# .restart (Restart Kernel Connection)


The **.restart** command restarts the kernel connection.

Do not confuse this command with the [**.restart (Restart Target Application)**](-restart--restart-target-application-.md) command, which works only in user mode.

```dbgcmd
.restart 
```

## <span id="ddk_meta_restart_kernel_connection_dbg"></span><span id="DDK_META_RESTART_KERNEL_CONNECTION_DBG"></span>


### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

You can use the **.restart** command only in KD.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>Kernel mode only</p></td>
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

For more information about reestablishing contact with the target, see [Synchronizing with the Target Computer](synchronizing-with-the-target-computer.md).

Remarks
-------

The **.restart** command is similar to the [**CTRL+R (Re-synchronize)**](ctrl-r--re-synchronize-.md) command, except that **.restart** is even more extensive in its effect. This command is equivalent to ending the debugger and then attaching a new debugger to the target computer.

The **.restart** command is most useful when you are performing [remote debugging through remote.exe](remote-debugging-through-remote-exe.md) and ending and restarting the debugger might be difficult. However, you cannot use **.restart** from a debugging client if you are performing remote debugging through the debugger.

 

 





