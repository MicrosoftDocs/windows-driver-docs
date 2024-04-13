---
title: "!ubl (WinDbg)"
description: "The !ubl extension lists all user-space breakpoints and their current status."
keywords: ["breakpoints, user-space breakpoints", "!ubl Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ubl
api_type:
- NA
---

# !ubl

The **!ubl** extension lists all user-space breakpoints and their current status.

```dbgcmd
!ubl
```

## DLL

Kdexts.dll

## Remarks

Here is an example of the use and display of user-space breakpoints:

```dbgcmd
kd> !ubp 8014a131
This command is VERY DANGEROUS, and may crash your system!
If you don't know what you are doing, enter "!ubc *" now!

kd> !ubp 801544f4

kd> !ubd 1

kd> !ubl
 0: e ffffffff`8014a131 (ffffffff`82deb000) 1 ffffffff
 1: d ffffffff`801544f4 (ffffffff`82dff000) 0 ffffffff
```

Each line in this listing contains the breakpoint number, the status (**e** for enabled or **d** for disabled), the virtual address used to set the breakpoint, the physical address of the actual breakpoint, the byte position, and the contents of this memory location at the time the breakpoint was set.

## See also

[**!ubc**](-ubc.md)

[**!ubd**](-ubd.md)

[**!ube**](-ube.md)

[**!ubp**](-ubp.md)

[User Space and System Space](../debugger/user-space-and-system-space.md)
