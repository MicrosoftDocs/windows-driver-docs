---
title: "!wmitrace.logger"
description: "The !wmitrace.logger extension displays data about the trace session, including the session configuration data. This extension does not display trace messages generated during the session."
keywords: ["!wmitrace.logger Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wmitrace.logger
api_type:
- NA
---

# !wmitrace.logger

The **!wmitrace.logger** extension displays data about the trace session, including the session configuration data. This extension does not display trace messages generated during the session.

```dbgcmd
!wmitrace.logger [ LoggerID | LoggerName ]
```

## Parameters

<span id="_______LoggerID______"></span><span id="_______loggerid______"></span><span id="_______LOGGERID______"></span> *LoggerID*   
Specifies the trace session. *LoggerID* is an ordinal number that the system assigns to each trace session on the computer. If no parameter is specified, the trace session with ID equal to 1 is used.

<span id="_______LoggerName______"></span><span id="_______loggername______"></span><span id="_______LOGGERNAME______"></span> *LoggerName*   
Specifies the trace session. *LoggerName* is the text name that was specified when the trace session was started.

## DLL

Wmitrace.dll

This extension is available in Windows 2000 and later versions of Windows. If you want to use this extension with Windows 2000, you must first copy the Wmitrace.dll file from the winxp subdirectory of the Debugging Tools for Windows installation directory to the w2kfre subdirectory.

## Additional Information

For a conceptual overview of event tracing, see the Microsoft Windows SDK.

## Remarks

This extension is designed for performance logs and events, which cannot be formatted for human-readable display. To display the trace messages in a trace session buffer, along with header data, use [**!wmitrace.logdump**](-wmitrace-logdump.md).

To find the logger ID of a trace session, use the [**!wmitrace.strdump**](-wmitrace-strdump.md) extension. Alternatively, you can use the Tracelog command tracelog -l to list the trace sessions and their basic properties, including the logger ID.
