---
title: "!for_each_local"
description: "The !for_each_local extension executes a debugger command one time for each local variable in the current frame."
keywords: ["!for_each_local Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- for_each_local
api_type:
- NA
---

# !for\_each\_local

The **!for\_each\_local** extension executes a debugger command one time for each local variable in the current frame.

```dbgcmd
!for_each_local ["CommandString"] 
!for_each_local -? 
```

## <span id="ddk__for_each_local_dbg"></span><span id="DDK__FOR_EACH_LOCAL_DBG"></span>Parameters

<span id="_______CommandString______"></span><span id="_______commandstring______"></span><span id="_______COMMANDSTRING______"></span> *CommandString*   
Specifies the debugger commands to execute one time for each local variable in the current stack frame. If *CommandString* includes multiple commands, you must separate them with semicolons and enclose *CommandString* in quotation marks. If you include multiple commands, the individual commands in *CommandString* cannot contain quotation marks.

Within *CommandString*, or within any script that the commands in *CommandString* execute, you can use the **@\#Local** alias. This alias is replaced by the name of the local variable. This replacement occurs before *CommandString* is executed and before any other parsing occurs. This alias is case sensitive, and you must add a space before it and add a space after it, even if you enclose the alias in parentheses. If you use C++ expression syntax, you must reference this alias as **@@( @\#Local )**.

This alias is available only during the lifetime of the call to **!for\_each\_local**. Do not confuse this alias with pseudo-registers, fixed-name aliases, or user-named aliases.

<span id="_______-_______"></span> **-?**   
Displays some Help text for this extension in the [Debugger Command window](../debugger/debugger-command-window.md).

## DLL

Ext.dll

## Additional Information

For more information about how to display and change local variables and a description of other memory-related commands, see [Reading and Writing Memory](../debugger/reading-and-writing-memory.md).

## Remarks

If you do not specify any arguments, the **!for\_each\_local** extension lists local variables. For more information about the local variables, use the [**dv (Display Local Variables)**](dv--display-local-variables-.md) command.

If you enable verbose debugger output, the display includes the total number of local variables when the extension is called, and every time that *CommandString* is executed for a local variable, that variable and the text of *CommandString* are echoed.
