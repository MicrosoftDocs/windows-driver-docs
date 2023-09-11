---
title: ube (WinDbg)
description: The ube extension re-enables a user-space breakpoint.
keywords: ["ube Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ube
api_type:
- NA
---

# !ube


The **!ube** extension re-enables a user-space breakpoint.

```dbgcmd
!ube BreakpointNumber 
```

## <span id="ddk__ube_dbg"></span><span id="DDK__UBE_DBG"></span>Parameters


<span id="_______BreakpointNumber______"></span><span id="_______breakpointnumber______"></span><span id="_______BREAKPOINTNUMBER______"></span> *BreakpointNumber*   
Specifies the number of the breakpoint to be enabled. An asterisk (\*) indicates all breakpoints.

### DLL

Kdexts.dll

 

## Remarks

This is used to re-enable a breakpoint that was disabled by [**!ubd**](-ubd.md).

## <span id="see_also"></span>See also


[**!ubc**](-ubc.md)

[**!ubd**](-ubd.md)

[**!ubl**](-ubl.md)

[**!ubp**](-ubp.md)

[User Space and System Space](user-space-and-system-space.md)

 

 






