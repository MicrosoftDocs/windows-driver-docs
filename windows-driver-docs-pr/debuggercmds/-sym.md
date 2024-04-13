---
title: "!sym (WinDbg)"
description: "The !sym extension controls noisy symbol loading and symbol prompts."
keywords: ["symbols, noisy symbol loading", "symbols, prompts", "!sym Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- sym
api_type:
- NA
---

# !sym

The **!sym** extension controls noisy symbol loading and symbol prompts.

```dbgcmd
!sym 
!sym noisy 
!sym quiet 
!sym prompts 
!sym prompts off
```

## Parameters

<span id="_______noisy______"></span><span id="_______NOISY______"></span> **noisy**   
Activates noisy symbol loading.

<span id="_______quiet______"></span><span id="_______QUIET______"></span> **quiet**   
Deactivates noisy symbol loading.

<span id="_______prompts______"></span><span id="_______PROMPTS______"></span> **prompts**   
Allows authentication dialog boxes to appear when SymSrv receives an authentication request.

<span id="_______prompts_off______"></span><span id="_______PROMPTS_OFF______"></span> **prompts off**   
Suppresses all authentication dialog boxes when SymSrv receives an authentication request. This may result in SymSrv being unable to access symbols over the internet.

## DLL

Dbghelp.dll

## Remarks

If the **!sym** extension is used with no arguments, the current state of noisy symbol loading and symbol prompting is displayed.

The **!sym noisy** and **!sym quiet** extensions control noisy symbol loading. For details and for other methods of displaying and changing this option, see [SYMOPT\_DEBUG](../debugger/symbol-options.md#symopt-debug).

The **!sym prompts** and **!sym prompts off** extensions control whether authentication dialogs are displayed when SymSrv encounters an authentication request. These commands must be followed by [**.reload (Reload Module)**](-reload--reload-module-.md) for them to take effect. Authentication requests may be sent by proxy servers, internet firewalls, smart card readers, and secure websites. For details and for other methods of changing this option, see [Firewalls and Proxy Servers](../debugger/firewalls-and-proxy-servers.md).

**Note**   Noisy symbol loading should not be confused with noisy source loading -- that is controlled by the [**.srcnoisy (Noisy Source Loading)**](-srcnoisy--noisy-source-loading-.md) command.

