---
title: "!for_each_frame"
description: "The !for_each_frame extension executes a debugger command one time for each frame in the stack of the current thread."
keywords: ["!for_each_frame Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- for_each_frame
api_type:
- NA
---

# !for_each_frame

The **!for\_each\_frame** extension executes a debugger command one time for each frame in the stack of the current thread.

```dbgcmd
!for_each_frame ["CommandString"] 
!for_each_frame -?
```

## Parameters

<span id="_______CommandString______"></span><span id="_______commandstring______"></span><span id="_______COMMANDSTRING______"></span> *CommandString*   
Specifies the debugger commands to execute one time for each frame. If *CommandString* includes multiple commands, you must separate them with semicolons and enclose *CommandString* in quotation marks. If you include multiple commands, the individual commands within *CommandString* cannot contain quotation marks. If you want to refer to the index of the current frame within *CommandString*, use the @$frame pseudoregister.

<span id="_______-_______"></span> **-?**   
Displays some Help text for this extension in the [Debugger Command window](../debugger/debugger-command-window.md).

## DLL

Ext.dll

## Additional Information

For more information about the local context, see [Changing Contexts](../debugger/changing-contexts.md).

## Remarks

If you do not specify any arguments, the **!for\_each\_frame** extension displays a list of all frames and their frame indexes. For a more detailed list of all frames, use the [**k (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command.

The [**k**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command walks up to 256 frames. For each enumerated frame, that frame temporarily becomes the current local context (similar to the [**.frame (Set Local Context)**](-frame--set-local-context-.md) command). After the context has been set, *CommandString* is executed. After all frames have been used, the local context is reset to the value that it had before you used the **!for\_each\_frame** extension.

If you include *CommandString*, the debugger displays the frame and its index before the command is executed for that frame.

The following command displays all local variables for the current stack.

```dbgcmd
!for_each_frame !for_each_local dt @#Local
```
