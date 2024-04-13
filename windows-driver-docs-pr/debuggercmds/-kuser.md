---
title: "!kuser (WinDbg)"
description: "The !kuser extension displays the shared user-mode page (KUSER_SHARED_DATA)."
keywords: ["!kuser Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- kuser
api_type:
- NA
---

# !kuser

The **!kuser** extension displays the shared user-mode page (KUSER\_SHARED\_DATA).

```dbgcmd
!kuser 
```

## DLL

Exts.dll

## Remarks

The KUSER\_SHARED\_DATA page gives resource and other information about the user who is currently logged on.

Here is an example. Note that, in this example, the tick count is displayed in both its raw form and in a more user-friendly form, which is in parentheses. The user-friendly display is available only in Windows XP and later.

```dbgcmd
kd> !kuser
_KUSER_SHARED_DATA at 7ffe0000
TickCount:    fa00000 * 00482006 (0:20:30:56.093)
TimeZone Id: 2
ImageNumber Range: [14c .. 14c]
Crypto Exponent: 0
SystemRoot: 'F:\WINDOWS'
```
