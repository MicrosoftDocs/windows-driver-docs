---
title: "!winrterr (WinDbg)"
description: "The !winrterr extension sets the debugger reporting mode for Windows Runtime errors."
keywords: ["!winrterr Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- winrterr
api_type:
- NA
---

# !winrterr

The **!winrterr** extension sets the debugger reporting mode for Windows Runtime errors.

```dbgcmd
!winrterr Mode
!winrterr
```

## Parameters

<span id="Mode"></span><span id="mode"></span><span id="MODE"></span>*Mode*  
The following table describes the possible values for *Mode*.

|Value|Description|
|---- |---------- |
|report|When a Windows Runtime error occurs, the error and related text are displayed in the debugger, but execution contunues. This is the default mode.|
|break|When a Windows Runtime error occurs, the error and related text are displayed in the debugger, and execution stops.|
|quiet|When a Windows Runtime error occurs, nothing is displayed in the debugger, and execution continues.|

If *Mode* is omitted, **!winrterr** displays the current reporting mode. If the debugger has broken in as a result of a Windows Runtime error, the error and related text are also displayed.

## See also

[Windows Runtime Debugger Commands](../debugger/windows-runtime-debugger-commands.md)

[**!hstring**](-hstring.md)

[**!hstring2**](-hstring2.md)
