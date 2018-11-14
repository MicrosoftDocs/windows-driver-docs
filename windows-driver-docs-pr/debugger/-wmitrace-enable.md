---
title: wmitrace.enable
description: The wmitrace.enable extension enables a provider for the specified Event Tracing for Windows (ETW) trace session.
ms.assetid: 5a27fa00-7d52-43f7-84f4-82c5b5af1c06
keywords: ["wmitrace.enable Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wmitrace.enable
api_type:
- NA
ms.localizationpriority: medium
---

# !wmitrace.enable


The **!wmitrace.enable** extension enables a provider for the specified Event Tracing for Windows (ETW) trace session.

```dbgcmd
!wmitrace.enable { LoggerID | LoggerName } GUID [-level Num] [-matchallkw Num] [-matchanykw Num] [-enableproperty Num] [-flag Num] 
```

## <span id="ddk__wmitrace_strdump_dbg"></span><span id="DDK__WMITRACE_STRDUMP_DBG"></span>Parameters


<span id="_______LoggerID______"></span><span id="_______loggerid______"></span><span id="_______LOGGERID______"></span> *LoggerID*   
Specifies the trace session. *LoggerID* is an ordinal number that the system assigns to each trace session on the computer.

<span id="_______LoggerName______"></span><span id="_______loggername______"></span><span id="_______LOGGERNAME______"></span> *LoggerName*   
Specifies the trace session. *LoggerName* is the text name that was specified when the trace session was started.

<span id="_______GUID______"></span><span id="_______guid______"></span> *GUID*   
Specifies the GUID of the provider to be enabled.

<span id="_______-level_______Num______"></span><span id="_______-level_______num______"></span><span id="_______-LEVEL_______NUM______"></span> **-level** *Num*   
Specifies the level. *Num* can be any integer.

<span id="_______-matchallkw_______Num______"></span><span id="_______-matchallkw_______num______"></span><span id="_______-MATCHALLKW_______NUM______"></span> **-matchallkw** *Num*   
Specifies one or more keywords. If multiple keywords are specified, the provider will be enabled only if all keywords are matched. *Num* can be any integer.

<span id="_______-matchanykw_______Num______"></span><span id="_______-matchanykw_______num______"></span><span id="_______-MATCHANYKW_______NUM______"></span> **-matchanykw** *Num*   
Specifies one or more keywords. If multiple keywords are specified, the provider will be enabled if at least one keyword is matched. *Num* can be any integer. The effects of this parameter overlap with the effects of the -flag parameter.

<span id="_______-enableproperty_______Num______"></span><span id="_______-enableproperty_______num______"></span><span id="_______-ENABLEPROPERTY_______NUM______"></span> **-enableproperty** *Num*   
Specifies the enable property. *Num* can be any integer.

<span id="_______-flag_______Num______"></span><span id="_______-flag_______num______"></span><span id="_______-FLAG_______NUM______"></span> **-flag** *Num*   
Specifies one or more flags. *Num* can be any integer. The effects of this parameter overlap with the effects of the -matchanykw parameter.

### <span id="DLL"></span><span id="dll"></span>DLL

This extension is exported by Wmitrace.dll.

This extension is available in Windows 7 and later versions of Windows.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For a conceptual overview of event tracing, see the Microsoft Windows SDK. For information about tracing tools, see the Windows Driver Kit (WDK).

Remarks
-------

After using this extension, you must resume program execution (for example, by using the [**g (Go)**](g--go-.md) command) in order for it to take effect. After a brief time, the target computer automatically breaks into the debugger again.

To disable a provider, use [**!wmitrace.disable**](-wmitrace-disable.md).

 

 





