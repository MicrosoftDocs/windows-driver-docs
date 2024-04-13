---
title: "!ubc (WinDbg)"
description: "The !ubc extension clears a user-space breakpoint."
keywords: ["!ubc Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ubc
api_type:
- NA
---

# !ubc

The **!ubc** extension clears a user-space breakpoint.

```dbgcmd
!ubc BreakpointNumber 
```

## Parameters

<span id="_______BreakpointNumber______"></span><span id="_______breakpointnumber______"></span><span id="_______BREAKPOINTNUMBER______"></span> *BreakpointNumber*   
Specifies the number of the breakpoint to be cleared. An asterisk (\*) indicates all breakpoints.

### DLL

Kdexts.dll

## Remarks

This will permanently delete a breakpoint set with [**!ubp**](-ubp.md).

## See also

[**!ubd**](-ubd.md)

[**!ube**](-ube.md)

[**!ubl**](-ubl.md)

[**!ubp**](-ubp.md)

[User Space and System Space](../debugger/user-space-and-system-space.md)
