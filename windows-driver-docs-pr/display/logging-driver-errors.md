---
title: Logging Driver Errors
description: Logging Driver Errors
keywords:
- error logs WDK display
- errors WDK display
- logging errors WDK display
ms.date: 10/27/2020
ms.localizationpriority: medium
---

# Logging Driver Errors

The Microsoft DirectX graphics kernel subsystem (*Dxgkrnl.sys*) records display driver-related errors, assertions, warnings, and events to an internal-use log (*Watchdog.sys*).

In addition to recording information to a log, by default, the checked-build version of the DirectX graphics kernel subsystem breaks into the attached debugger if errors or assertions occur. By default, the free-build version of the DirectX graphics kernel subsystem only records errors and assertions to the log and does not break into the debugger if errors or assertions occur. You can change this default behavior by first creating the following REG_DWORD entries in the registry:

```registry
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Watchdog\Logging\BreakOnAssertion
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Watchdog\Logging\BreakOnError
```

To make the debugger start if errors or assertions occur, you should set the value of **BreakOnError** or **BreakOnAssertion** to 1 (TRUE) respectively. To make the debugger not start if errors or assertions occur, you should set the value of **BreakOnError** or **BreakOnAssertion** to 0 (FALSE) respectively.

> [!NOTE]
> Checked builds were available on older versions of Windows, before Windows 10 version 1803. Use tools such as Driver Verifier and GFlags to check driver code in later versions of Windows.
