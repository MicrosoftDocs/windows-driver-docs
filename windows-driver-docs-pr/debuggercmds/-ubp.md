---
title: "!ubp (WinDbg)"
description: "The !ubp extension sets a breakpoint in user space."
keywords: ["!ubp Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ubp
api_type:
- NA
---

# !ubp

The **!ubp** extension sets a breakpoint in user space.

```dbgcmd
!ubp Address 
```

## Parameters

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal virtual address of the location in user space where the breakpoint is to be set.

### DLL

Kdexts.dll

## Remarks

The **!ubp** extension sets a breakpoint in user space. The breakpoint is set on the actual physical page, not just the virtual page.

Setting a physical breakpoint will simultaneously modify every virtual copy of a page, with unpredictable results. One possible consequence is corruption of the system state, possibly followed by a bug check or other system crash. Therefore, these breakpoints should be used cautiously, if at all.

This extension cannot be used to set breakpoints on pages that have been swapped out of memory. If a page is swapped out of memory after a breakpoint is set, the breakpoint ceases to exist.

It is not possible to set a breakpoint inside a page table or a page directory.

Each breakpoint is assigned a *breakpoint number*. To find out the breakpoint number assigned, use [**!ubl**](-ubl.md). Breakpoints are enabled upon creation. To step over a breakpoint, you must first disable it by using [**!ubd**](-ubd.md). To clear a breakpoint, use [**!ubc**](-ubc.md).

## See also

[**!ubc**](-ubc.md)

[**!ubd**](-ubd.md)

[**!ube**](-ube.md)

[**!ubl**](-ubl.md)

[User Space and System Space](../debugger/user-space-and-system-space.md)
