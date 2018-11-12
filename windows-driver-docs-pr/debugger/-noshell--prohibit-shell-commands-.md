---
title: .noshell (Prohibit Shell Commands)
description: The .noshell command prevents you from using .shell commands.
ms.assetid: 49a83e46-1390-4b60-bd61-a5da80c513e3
keywords: [".noshell (Prohibit Shell Commands) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .noshell (Prohibit Shell Commands)
api_type:
- NA
ms.localizationpriority: medium
---

# .noshell (Prohibit Shell Commands)


The **.noshell** command prevents you from using [**.shell**](-shell--command-shell-.md) commands.

```dbgcmd
.noshell 
```

## <span id="ddk_meta_prohibit_shell_commands_dbg"></span><span id="DDK_META_PROHIBIT_SHELL_COMMANDS_DBG"></span>


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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about the command shell and for other ways to disable shell commands, see [Using Shell Commands](using-shell-commands.md).

Remarks
-------

If you use the **.noshell** command, you cannot use [**.shell (Command Shell)**](-shell--command-shell-.md) commands as long as the debugger is running, even if you start a new debugging session.

If you are performing remote debugging, this command is useful for security purposes.

 

 





