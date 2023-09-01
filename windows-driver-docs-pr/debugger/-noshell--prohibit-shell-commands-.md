---
title: .noshell (Prohibit Shell Commands)
description: The .noshell command prevents you from using .shell commands.
keywords: [".noshell (Prohibit Shell Commands) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .noshell (Prohibit Shell Commands)
api_type:
- NA
---

# .noshell (Prohibit Shell Commands)


The **.noshell** command prevents you from using [**.shell**](-shell--command-shell-.md) commands.

```dbgcmd
.noshell 
```

## <span id="ddk_meta_prohibit_shell_commands_dbg"></span><span id="DDK_META_PROHIBIT_SHELL_COMMANDS_DBG"></span>


### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

### Additional Information

For more information about the command shell and for other ways to disable shell commands, see [Using Shell Commands](using-shell-commands.md).

## Remarks

If you use the **.noshell** command, you cannot use [**.shell (Command Shell)**](-shell--command-shell-.md) commands as long as the debugger is running, even if you start a new debugging session.

If you are performing remote debugging, this command is useful for security purposes.

 

 





