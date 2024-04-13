---
title: ".suspend_ui (Suspend WinDbg Interface)"
description: "The .suspend_ui command suspends the refresh of WinDbg debugging information windows."
keywords: [".suspend_ui (Suspend WinDbg Interface) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .suspend_ui (Suspend WinDbg Interface)
api_type:
- NA
---

# .suspend\_ui (Suspend WinDbg Interface)

The **.suspend\_ui** command suspends the refresh of WinDbg debugging information windows.

```dbgcmd
.suspend_ui 0 
.suspend_ui 1 
.suspend_ui 
```

## Parameters

<span id="_______0______"></span> **0**   
Suspends the refresh of WinDbg debugging information windows.

<span id="_______1______"></span> **1**   
Enables the refresh of WinDbg debugging information windows.

## Environment

This command is available only in WinDbg and cannot be used in script files.

|  Item       | Description       |
|-----------|------------------|
| Modes     | kernel mode only |
| Targets   | live, crash dump |
| Platforms | all              |

## Remarks

Without any parameters, **.suspend\_ui** displays whether debugging information windows are currently suspended.

By default, debugging information windows are refreshed every time the information they display changes.

Suspending the refresh of these windows can speed up WinDbg during a sequence of quick operations -- for example, when tracing or stepping many times in quick succession.

