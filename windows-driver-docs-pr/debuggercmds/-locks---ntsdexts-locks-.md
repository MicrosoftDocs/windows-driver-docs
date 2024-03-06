---
title: locks ntsdexts.locks
description: The locks extension in Ntsdexts.dll displays a list of critical sections associated with the current process.This extension command should not be confused with the kdext*.locks extension command.
keywords: ["locks ( ntsdexts.locks) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- locks ( ntsdexts.locks)
api_type:
- NA
---

# !locks (!ntsdexts.locks)

The **!locks** extension in Ntsdexts.dll displays a list of critical sections associated with the current process.

This extension command should not be confused with the [**!kdext\*.locks**](-locks---kdext--locks-.md) extension command.

```dbgcmd
    !locks [Options] 
```

## Parameters

*Options*

Specifies the amount of information to be displayed. Any combination of the following options can be used:

<span id="-v"></span><span id="-V"></span>**-v**  
Causes the display to include all critical sections, even those that are not currently owned.

<span id="-o"></span><span id="-O"></span>**-o**  
Causes the display to only include orphaned information (pointers that do not actually point to valid critical sections).

### DLL

Ntsdexts.dll

### Additional Information

For other commands and extensions that can display critical section information, see [Displaying a Critical Section](../debugger/displaying-a-critical-section.md). For information about critical sections, see the Microsoft Windows SDK documentation and *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

## Remarks

This extension command shows all critical sections that have been initialized by calling **RtlInitializeCriticalSection**. If there are no critical sections, then no output will result.

Here is an example:

```dbgcmd
0:000> !locks

CritSec w3svc!g_pWamDictator+a0 at 68C2C298
LockCount          0
RecursionCount     1
OwningThread       d1
EntryCount         1
ContentionCount    0
*** Locked

CritSec SMTPSVC+66a30 at 67906A30
LockCount          0
RecursionCount     1
OwningThread       d0
EntryCount         1
ContentionCount    0
*** Locked
```

## See also

[Displaying a Critical Section](../debugger/displaying-a-critical-section.md)

[Critical Section Time Outs](../debugger/critical-section-time-outs.md) (user mode)
