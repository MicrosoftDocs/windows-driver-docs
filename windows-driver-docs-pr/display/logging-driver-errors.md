---
title: Logging Driver Errors
description: Logging Driver Errors
ms.assetid: 7deb2a9a-70aa-4660-a0c8-e118e03eef3b
keywords:
- error logs WDK display
- errors WDK display
- logging errors WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Logging Driver Errors


The Microsoft DirectX graphics kernel subsystem (*Dxgkrnl.sys*) records display driver-related errors, assertions, warnings, and events to a log in memory (in *Watchdog.sys*).

In addition to recording information to a log, by default, the checked-build version of the DirectX graphics kernel subsystem breaks into the attached debugger if errors or assertions occur. By default, the free-build version of the DirectX graphics kernel subsystem only records errors and assertions to the log and does not break into the debugger if errors or assertions occur. You can change this default behavior by first creating the following REG\_DWORD entries in the registry:

```registry
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Watchdog\Logging\BreakOnAssertion
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Watchdog\Logging\BreakOnError
```

To make the debugger start if errors or assertions occur, you should set the value of **BreakOnError** or **BreakOnAssertion** to 1 (TRUE) respectively. To make the debugger not start if errors or assertions occur, you should set the value of **BreakOnError** or **BreakOnAssertion** to 0 (FALSE) respectively.

 

 





