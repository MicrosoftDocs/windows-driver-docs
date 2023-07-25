---
title: !cs (WinDbg)
description: The cs extension displays one or more critical sections or the whole critical section tree.
keywords: ["cs Windows Debugging"]
ms.date: 11/15/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- cs
api_type:
- NA
---

# !cs

The **!cs** extension displays one or more critical sections or the whole critical section tree.

```dbgsyntax
!cs [-s] [-l] [-o] 
!cs [-s] [-o] Address 
!cs [-s] [-l] [-o] StartAddress EndAddress 
!cs [-s] [-o] -d InfoAddress 
!cs [-s] -t [TreeAddress] 
!cs -? 
```

## Parameters

Parameter | Description
|---------|-------------|
**-s**  | Displays each critical section's initialization stack trace, if this information is available.
**-l**  |Display only the locked critical sections.
**-o**   |Displays the owner's stack for any locked critical section that is being displayed.
*Address* |Specifies the address of the critical section to display. If you omit this parameter, the debugger displays all critical sections in the current process.
*StartAddress*   | Specifies the beginning of the address range to search for critical sections.
*EndAddress*   | Specifies the end of the address range to search for critical sections.
**-d**    | Displays critical sections that are associated with DebugInfo.
*InfoAddress*   | Specifies the address of the DebugInfo.
**-t**    | Displays a critical section tree. Before you can use the **-t** option, you must activate [Application Verifier](../devtest/application-verifier.md) for the target process and select the **Check lock usage** option.
*TreeAddress*    | Specifies the address of the root of the critical section tree. If you omit this parameter or specify zero, the debugger displays the critical section tree for the current process.
**-?**    | Displays some Help text for this extension in the [Debugger Command window](debugger-command-window.md).

### DLL

Exts.dll

### Additional Information

For other commands and extensions that can display critical section information, see [Displaying a Critical Section](displaying-a-critical-section.md). For more information about critical sections, see the Microsoft Windows SDK documentation, the Windows Driver Kit (WDK) documentation, and *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

#### Remarks

The **!cs** extension requires full symbols (including type information) for the process that is being debugged and for Ntdll.dll.

The following examples shows you how to use **!cs**. The following command displays information about the critical section at address 0x7803B0F8 and shows its initialization stack trace.

```dbgcmd
0:001> !cs -s 0x7803B0F8
Critical section   = 0x7803B0F8 (MSVCRT!__app_type+0x4)
DebugInfo          = 0x6A262080
NOT LOCKED
LockSemaphore      = 0x0
SpinCount          = 0x0

Stack trace for DebugInfo = 0x6A262080:

0x6A2137BD: ntdll!RtlInitializeCriticalSectionAndSpinCount+0x9B
0x6A207A4C: ntdll!LdrpCallInitRoutine+0x14
0x6A205569: ntdll!LdrpRunInitializeRoutines+0x1D9
0x6A20DCE1: ntdll!LdrpInitializeProcess+0xAE5
```

The following command displays information about the critical section whose DebugInfo is at address 0x6A262080.

```dbgcmd
0:001> !cs -d 0x6A262080
DebugInfo          = 0x6A262080
Critical section   = 0x7803B0F8 (MSVCRT!__app_type+0x4)
NOT LOCKED
LockSemaphore      = 0x0
SpinCount          = 0x0
```

The following command displays information about all of the active critical sections in the current process.

```dbgcmd
## 0:001> !cs

DebugInfo          = 0x6A261D60
Critical section   = 0x6A262820 (ntdll!RtlCriticalSectionLock+0x0)
LOCKED
LockCount          = 0x0
OwningThread       = 0x460
RecursionCount     = 0x1
LockSemaphore      = 0x0
## SpinCount          = 0x0

DebugInfo          = 0x6A261D80
Critical section   = 0x6A262580 (ntdll!DeferedCriticalSection+0x0)
NOT LOCKED
LockSemaphore      = 0x7FC
## SpinCount          = 0x0

DebugInfo          = 0x6A262600
Critical section   = 0x6A26074C (ntdll!LoaderLock+0x0)
NOT LOCKED
LockSemaphore      = 0x0
## SpinCount          = 0x0

DebugInfo          = 0x77fbde20
Critical section   = 0x77c8ba60 (GDI32!semColorSpaceCache+0x0)
LOCKED
LockCount          = 0x0
OwningThread       = 0x00000dd8
RecursionCount     = 0x1
LockSemaphore      = 0x0
## SpinCount          = 0x00000000

...
```

The following command displays the critical section tree.

```dbgcmd
0:001> !cs -t

Tree root 00bb08c0

Level     Node       CS    Debug  InitThr EnterThr  WaitThr TryEnThr LeaveThr EnterCnt  WaitCnt
## 


    0 00bb08c0 77c7e020 77fbcae0      4c8      4c8        0        0      4c8        c        0
 1 00dd6fd0 0148cfe8 01683fe0      4c8      4c8        0        0      4c8        2        0
 2 00bb0aa0 008e8b84 77fbcc20      4c8        0        0        0        0        0        0
    3 00bb09e0 008e8704 77fbcba0      4c8        0        0        0        0        0        0
    4 00bb0a40 008e8944 77fbcbe0      4c8        0        0        0        0        0        0
    5 00bb0a10 008e8824 77fbcbc0      4c8        0        0        0        0        0        0
    5 00bb0a70 008e8a64 77fbcc00      4c8        0        0        0        0        0        0
    3 00bb0b00 008e8dc4 77fbcc60      4c8        0        0        0        0        0        0
    4 00bb0ad0 008e8ca4 77fbcc40      4c8        0        0        0        0        0        0
    4 00bb0b30 008e8ee4 77fbcc80      4c8        0        0        0        0        0        0
    5 00dd4fd0 0148afe4 0167ffe0      4c8        0        0        0        0        0        0
    2 00bb0e90 77c2da98 00908fe0      4c8      4c8        0        0      4c8       3a        0
 3 00bb0d70 77c2da08 008fcfe0      4c8        0        0        0        0        0        0
```

The following items appear in this **!cs -t** display:

- **InitThr** is the thread ID for the thread that initialized the CS.

- **EnterThr** is the ID of the thread that called **EnterCriticalSection** last time.

- **WaitThr** is the ID of the thread that found the critical section that another thread owned and waited for it last time.

- **TryEnThr** is the ID of the thread that called **TryEnterCriticalSection** last time.

- **LeaveThr** is the ID of the thread that called **LeaveCriticalSection** last time

- **EnterCnt** is the count of **EnterCriticalSection**.

- **WaitCnt** is the contention count.

## See also

[**!ntsdexts.locks**](-locks---ntsdexts-locks-.md) 

[Displaying a Critical Section](displaying-a-critical-section.md)

[Critical Section Time Outs](critical-section-time-outs.md) (user mode)
