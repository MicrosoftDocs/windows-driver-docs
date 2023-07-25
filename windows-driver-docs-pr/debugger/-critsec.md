---
title: critsec (WinDbg)
description: The critsec extension displays a critical section.
keywords: ["critsec Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- critsec
api_type:
- NA
---

# !critsec


The **!critsec** extension displays a critical section.

```dbgsyntax
!critsec Address 
```

## <span id="ddk__critsec_dbg"></span><span id="DDK__CRITSEC_DBG"></span>Parameters

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*

Specifies the hexadecimal address of the critical section.

### DLL

Ntsdexts.dll

### dditional Information

For other commands and extensions that can display critical section information, see [Displaying a Critical Section](displaying-a-critical-section.md). For information about critical sections, see the Microsoft Windows SDK documentation, the Windows Driver Kit (WDK) documentation, and *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

## Remarks

If you do not know the address of the critical section, you should use the [**!ntsdexts.locks**](-locks---ntsdexts-locks-.md) extension. This displays all critical sections that have been initialized by calling **RtlInitializeCriticalSection**.

Here is an example:

```dbgcmd
0:000> !critsec 3a8c0e9c

CritSec +3a8c0e9c at 3A8C0E9C
LockCount          1
RecursionCount     1
OwningThread       99
EntryCount         472
ContentionCount    1
*** Locked
```

## See also

[Displaying a Critical Section](displaying-a-critical-section.md)

[Critical Section Time Outs](critical-section-time-outs.md) (user mode)

[!cs ](-cs.md)
