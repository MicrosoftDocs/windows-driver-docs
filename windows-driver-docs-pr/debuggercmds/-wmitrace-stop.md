---
title: "!wmitrace.stop"
description: "The !wmitrace.stop extension stops the Event Tracing for Windows (ETW) logger on the target computer."
keywords: ["!wmitrace.stop Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wmitrace.stop
api_type:
- NA
---

# !wmitrace.stop

The **!wmitrace.stop** extension stops the Event Tracing for Windows (ETW) logger on the target computer.

```dbgcmd
!wmitrace.stop { LoggerID | LoggerName } 
```

## Parameters

<span id="_______LoggerID______"></span><span id="_______loggerid______"></span><span id="_______LOGGERID______"></span> *LoggerID*   
Specifies the trace session. *LoggerID* is an ordinal number that the system assigns to each trace session on the computer.

<span id="_______LoggerName______"></span><span id="_______loggername______"></span><span id="_______LOGGERNAME______"></span> *LoggerName*   
Specifies the trace session. *LoggerName* is the text name that was specified when the trace session was started.

## DLL

Wmitrace.dll

This extension is available in Windows 7 and later versions of Windows.

## Additional Information

For a conceptual overview of event tracing, see the Microsoft Windows SDK. For information about tracing tools, see the Windows Driver Kit (WDK).

## Remarks

After using this extension, you must resume program execution (for example, by using the [**g (Go)**](g--go-.md) command) in order for it to take effect. After a brief time, the target computer automatically breaks into the debugger again.

To start the ETW logger, use [**!wmitrace.start**](-wmitrace-start.md).
