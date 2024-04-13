---
title: "be (Breakpoint Enable)"
description: "The be command restores one or more breakpoints that were previously disabled."
keywords: ["be (Breakpoint Enable) Windows Debugging"]
ms.date: 09/18/2019
topic_type:
- apiref
ms.topic: reference
api_name:
- be (Breakpoint Enable)
api_type:
- NA
---

# be (Breakpoint Enable)

The **be** command restores one or more breakpoints that were previously disabled.

```dbgcmd
be Breakpoints 
```

## <span id="ddk_cmd_breakpoint_enable_dbg"></span><span id="DDK_CMD_BREAKPOINT_ENABLE_DBG"></span>Parameters

<span id="_______Breakpoints______"></span><span id="_______breakpoints______"></span><span id="_______BREAKPOINTS______"></span> *Breakpoints*   
Specifies the ID numbers of the breakpoints to enable. You can specify any number of breakpoints. You must separate multiple IDs by spaces or commas. You can specify a range of breakpoint IDs by using a hyphen (-). You can use an asterisk (\*) to indicate all breakpoints. If you want to use a [numeric expression](numerical-expression-syntax.md) for an ID, enclose it in brackets (\[ \]). If you want to use a [string with wildcard characters](string-wildcard-syntax.md) to match a breakpoint's symbolic name, enclose it in quotation marks (" ").

## Environment

|  Item       | Description               |
|-----------|------------------------|
| Modes     | user mode, kernel mode |
| Targets   | live debugging only    |
| Platforms | all                    |

## Additional Information

For more information about and examples of how to use breakpoints, other breakpoint commands and methods of controlling breakpoints, and how to set breakpoints in user space from a kernel debugger, see [Using Breakpoints](../debugger/using-breakpoints.md). For more information about conditional breakpoints, see [Setting a Conditional Breakpoint](../debugger/setting-a-conditional-breakpoint.md).

## Remarks

Use the [**bl (Breakpoint List)**](bl--breakpoint-list-.md) command to list all existing breakpoints, their ID numbers, and their status.

Use the [**.bpcmds (Display Breakpoint Commands)**](-bpcmds--display-breakpoint-commands-.md) command to list all existing breakpoints, their ID numbers, and the commands that were used to create them.

