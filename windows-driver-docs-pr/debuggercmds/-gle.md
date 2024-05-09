---
title: "!gle (WinDbg)"
description: "The !gle extension displays the last error value for the current thread."
keywords: ["thread, error value", "error value", "!gle Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- gle
api_type:
- NA
---

# !gle

The **!gle** extension displays the last error value for the current thread.

```dbgcmd
!gle [-all]
```

## Parameters

<span id="_______-all______"></span><span id="_______-ALL______"></span> **-all**   
Displays the last error for each user-mode thread on the target system. If you omit this parameter in user mode, the debugger displays the last error for the current thread. If you omit this parameter in kernel mode, the debugger displays the last error for the thread that the current [register context](../debugger/changing-contexts.md#register-context) specifies.

## DLL

Exts.dll

## Additional Information

For more information about the [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) routine, see the Windows SDK documentation.

## Remarks

The **!gle** extension displays the value of [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) and tries to decode this value.

In kernel mode, the **!gle** extension work only if the debugger can read the thread environment block (TEB).
