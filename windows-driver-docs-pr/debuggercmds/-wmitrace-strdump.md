---
title: "!wmitrace.strdump"
description: "The !wmitrace.strdump extension displays the WMI event trace structures. You can limit the display to the structures for a particular trace session."
keywords: ["!wmitrace.strdump Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wmitrace.strdump
api_type:
- NA
---

# !wmitrace.strdump

The **!wmitrace.strdump** extension displays the WMI event trace structures. You can limit the display to the structures for a particular trace session.

```dbgcmd
!wmitrace.strdump [ LoggerID | LoggerName ] 
```

## Parameters

<span id="_______LoggerID______"></span><span id="_______loggerid______"></span><span id="_______LOGGERID______"></span> *LoggerID*   
Limits the display to the event trace structures for the specified trace session. *LoggerID* specifies the trace session. It is an ordinal number that the system assigns to each trace session on the computer. If no parameter is specified, all trace sessions are displayed.

<span id="_______LoggerName______"></span><span id="_______loggername______"></span><span id="_______LOGGERNAME______"></span> *LoggerName*   
Limits the display to the event trace structures for the specified trace session. *LoggerName* is the text name that was specified when the trace session was started. If no parameter is specified, all trace sessions are displayed.

## DLL

Wmitrace.dll

This extension is available in Windows 2000 and later versions of Windows. If you want to use this extension with Windows 2000, you must first copy the Wmitrace.dll file from the winxp subdirectory of the Debugging Tools for Windows installation directory to the w2kfre subdirectory.

## Additional Information

For a conceptual overview of event tracing, see the Microsoft Windows SDK. For information about Tracelog, see the "Tracelog" topic in the Windows Driver Kit (WDK).

## Remarks

To find the logger ID of a trace session, use the **!wmitrace.strdump** extension. Alternatively, you can use the Tracelog command tracelog -l to list the trace sessions and their basic properties, including the logger ID.
