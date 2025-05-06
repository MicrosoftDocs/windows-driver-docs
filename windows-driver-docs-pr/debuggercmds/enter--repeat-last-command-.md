---
title: "ENTER (Repeat Last Command)"
description: "The ENTER key repeats the last command that you typed."
keywords: ["ENTER (Repeat Last Command) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ENTER (Repeat Last Command)
api_type:
- NA
---

# ENTER (Repeat Last Command)


The ENTER key repeats the last command that you typed.

```dbgcmd
ENTER
```

## <span id="ddk_cmd_repeat_last_command_dbg"></span><span id="DDK_CMD_REPEAT_LAST_COMMAND_DBG"></span>


## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |


## Remarks

In CDB, KD and WinDbg, pressing the ENTER key by itself at the debugger command prompt reissues the command that you previously entered. For more information, see [Using Debugger Commands](using-debugger-commands.md).

If you want to create white space in the [Debugger Command window](../debugger/debugger-command-window.md), use the [**\* (Comment Line Specifier)**](----comment-line-specifier-.md) token and then press ENTER several times.

