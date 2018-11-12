---
title: wmitrace.disable
description: The wmitrace.disable extension disables a provider for the specified Event Tracing for Windows (ETW) trace session.
ms.assetid: b993bfa4-2d3d-4739-9d5e-0cb714369742
keywords: ["wmitrace.disable Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wmitrace.disable
api_type:
- NA
ms.localizationpriority: medium
---

# !wmitrace.disable


The **!wmitrace.disable** extension disables a provider for the specified Event Tracing for Windows (ETW) trace session.

```dbgcmd
!wmitrace.disable { LoggerID | LoggerName } GUID 
```

## <span id="ddk__wmitrace_strdump_dbg"></span><span id="DDK__WMITRACE_STRDUMP_DBG"></span>Parameters


<span id="_______LoggerID______"></span><span id="_______loggerid______"></span><span id="_______LOGGERID______"></span> *LoggerID*   
Specifies the trace session. *LoggerID* is an ordinal number that the system assigns to each trace session on the computer.

<span id="_______LoggerName______"></span><span id="_______loggername______"></span><span id="_______LOGGERNAME______"></span> *LoggerName*   
Specifies the trace session. *LoggerName* is the text name that was specified when the trace session was started.

<span id="_______GUID______"></span><span id="_______guid______"></span> *GUID*   
Specifies the GUID of the provider to be disabled.

### <span id="DLL"></span><span id="dll"></span>DLL

This extension is exported by Wmitrace.dll.

This extension is available in Windows 7 and later versions of Windows.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For a conceptual overview of event tracing, see the Microsoft Windows SDK. For information about tracing tools, see the Windows Driver Kit (WDK).

Remarks
-------

After using this extension, you must resume program execution (for example, by using the [**g (Go)**](g--go-.md) command) in order for it to take effect. After a brief time, the target computer automatically breaks into the debugger again.

To enable a provider, use [**!wmitrace.enable**](-wmitrace-enable.md).

 

 





