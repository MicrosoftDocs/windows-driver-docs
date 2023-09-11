---
title: ENTER (Repeat Last Command)
description: The ENTER key repeats the last command that you typed.
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


### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

In CDB and KD, pressing the ENTER key by itself at a command prompt reissues the command that you previously entered.

In WinDbg, the ENTER key can have no effect or you can use it to repeat the previous command. You can set this option in the **Options** dialog box. (To open the **Options** dialog box, click **Options** on the **View** menu or click the **Options** button (![screen shot of the options button.](images/tbopt.png)) on the toolbar.)

If you set ENTER to repeat the last command, but you want to create white space in the [Debugger Command window](debugger-command-window.md), use the [**\* (Comment Line Specifier)**](----comment-line-specifier-.md) token and then press ENTER several times.

 

 





