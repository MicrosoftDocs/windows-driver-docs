---
title: wmitrace.eventlogdump
description: The wmitrace.eventlogdump extension displays the contents of the specified logger. The display is formatted like an event log.
ms.assetid: 27254b36-b413-45f0-9834-ff55fbb787c7
keywords: ["wmitrace.eventlogdump Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wmitrace.eventlogdump
api_type:
- NA
ms.localizationpriority: medium
---

# !wmitrace.eventlogdump


The **!wmitrace.eventlogdump** extension displays the contents of the specified logger. The display is formatted like an event log.

```dbgcmd
!wmitrace.eventlogdump { LoggerID | LoggerName }
```

## <span id="ddk__wmitrace_strdump_dbg"></span><span id="DDK__WMITRACE_STRDUMP_DBG"></span>Parameters


<span id="_______LoggerID______"></span><span id="_______loggerid______"></span><span id="_______LOGGERID______"></span> *LoggerID*   
Specifies the trace session. *LoggerID* is an ordinal number that the system assigns to each trace session on the computer.

<span id="_______LoggerName______"></span><span id="_______loggername______"></span><span id="_______LOGGERNAME______"></span> *LoggerName*   
Specifies the trace session. *LoggerName* is the text name that was specified when the trace session was started.

### <span id="DLL"></span><span id="dll"></span>DLL

This extension is exported by Wmitrace.dll.

This extension is available in Windows 2000 and later versions of Windows. If you want to use this extension with Windows 2000, you must first copy the Wmitrace.dll file from the winxp subdirectory of the Debugging Tools for Windows installation directory to the w2kfre subdirectory.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For a conceptual overview of event tracing, see the Microsoft Windows SDK. For information about tracing tools, see the Windows Driver Kit (WDK).

Remarks
-------

This extension is similar to the [**!wmitrace.logdump**](-wmitrace-logdump.md) extension, except that the output of **!wmitrace.eventlogdump** is formatted in event log style, and the output of **!wmitrace.logdump** is formatted in Windows software trace preprocessor (WPP) style. You should choose the extension whose format is appropriate for the data you wish to display.

To find the logger ID of a trace session, use the [**!wmitrace.strdump**](-wmitrace-strdump.md) extension. Alternatively, you can use the Tracelog command tracelog -l to list the trace sessions and their basic properties, including the logger ID.

 

 





