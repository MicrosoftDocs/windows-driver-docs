---
title: ubd (WinDbg)
description: The ubd extension temporarily disables a user-space breakpoint.
keywords: ["ubd Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ubd
api_type:
- NA
---

# !ubd


The **!ubd** extension temporarily disables a user-space breakpoint.

```dbgcmd
!ubd BreakpointNumber 
```

## <span id="ddk__ubd_dbg"></span><span id="DDK__UBD_DBG"></span>Parameters


<span id="_______BreakpointNumber______"></span><span id="_______breakpointnumber______"></span><span id="_______BREAKPOINTNUMBER______"></span> *BreakpointNumber*   
Specifies the number of the breakpoint to be disabled. An asterisk (\*) indicates all breakpoints.

### DLL

Kdexts.dll

 

## Remarks

Disabled breakpoints will be ignored. Use [**!ube**](-ube.md) to re-enable the breakpoint.

## <span id="see_also"></span>See also


[**!ubc**](-ubc.md)

[**!ube**](-ube.md)

[**!ubl**](-ubl.md)

[**!ubp**](-ubp.md)

[User Space and System Space](user-space-and-system-space.md)

 

 






