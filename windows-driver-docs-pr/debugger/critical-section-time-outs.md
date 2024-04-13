---
title: Critical Section Time Outs
description: Critical Section Time Outs
keywords: ["critical section, debugging critical section time outs"]
ms.date: 07/24/2023
---

# Critical Section Time Outs

Some types of critical section time outs can be identified when the stack trace that shows the routine **RtlpWaitForCriticalSection** near the top of the stack. Another variety of critical section time outs is a possible deadlock application error.

As with resource time outs, the **!ntsdexts.locks** extension will give a list of locks currently held and the threads that own them. Unlike resource time outs, the thread IDs given are not immediately useful. These are system IDs that do not map directly to the thread numbers.

Just as with <strong>ExpWaitForResource*Xxx</strong><em>, the lock identifier is the first parameter to **RtlpWaitForCriticalSection</em>*. Continue tracing the chain of waits until either a loop is found or the final thread is not waiting for a critical section time out.

### Additional Information

For other commands and extensions that can display critical section information, see [Displaying a Critical Section](displaying-a-critical-section.md). For more information about critical sections, see the Microsoft Windows SDK documentation, and *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

### Example of Debugging a Critical Time Out

Start by displaying the stack:

```dbgcmd
0:024> kb

ChildEBP RetAddr  Args to Child
0569fca4 77f79c78 77f71000 002a6b88 7fffffff ntdll!_DbgBreakPoint
0569fd04 77f71048 5ffa9f9c 5fef0b4b 5ffa9f9c ntdll!_RtlpWaitForCriticalSection+0x89
0569fd0c 5fef0b4b 5ffa9f9c 002a6b88 002a0019 ntdll!_RtlEnterCriticalSection+0x48
0569fd70 5fedf83f 002a6b88 0569fdc0 0000003e winsrv!_StreamScrollRegion+0x1f0
0569fd8c 5fedfa5b 002a6b88 00190000 00000000 winsrv!_AdjustCursorPosition+0x8e
0569fdc0 5fedf678 0569ff18 0031c200 0335ee88 winsrv!_DoWriteConsole+0x104

0569fefc 5fe6311b 0569ff18 0569ffd0 00000005 winsrv!_SrvWriteConsole+0x96
0569fff4 00000000 00000000 00000024 00000024 csrsrv!_CsrApiRequestThread+0x4ff 
```

Now use the [**!ntsdexts.locks**](../debuggercmds/-locks---ntsdexts-locks-.md) extension to find the critical section:

```dbgcmd
0:024> !locks 
CritSec winsrv!_ScrollBufferLock at 5ffa9f9c        5ffa9f9c is the first one 
LockCount          5
RecursionCount     1
OwningThread       88         // here's the owning thread ID 
EntryCount         11c
ContentionCount    135
*** Locked

CritSec winsrv!_gcsUserSrv+0 at 5ffa91b4     //second critical section found below 

LockCount          8
RecursionCount     1
OwningThread       6d         // second owning thread 
EntryCount         1d6c
ContentionCount    1d47
*** Locked 
```

Now search for the thread that has the ID number 0x6D:

```dbgcmd
0:024> ~ 
  0  id: 16.15   Teb 7ffdd000 Unfrozen
  1  id: 16.13   Teb 7ffdb000 Unfrozen
  2  id: 16.30   Teb 7ffda000 Unfrozen
  3  id: 16.2f   Teb 7ffd9000 Unfrozen
  4  id: 16.2e   Teb 7ffd8000 Unfrozen
  5  id: 16.6c   Teb 7ff6c000 Unfrozen
  6  id: 16.6d   Teb 7ff68000 Unfrozen    // this thread owns the second critical section
  7  id: 16.2d   Teb 7ffd7000 Unfrozen
  8  id: 16.33   Teb 7ffd6000 Unfrozen
  9  id: 16.42   Teb 7ff6f000 Unfrozen
 10  id: 16.6f   Teb 7ff6e000 Unfrozen
 11  id: 16.6e   Teb 7ffd5000 Unfrozen
 12  id: 16.52   Teb 7ff6b000 Unfrozen
 13  id: 16.61   Teb 7ff6a000 Unfrozen
 14  id: 16.7e   Teb 7ff69000 Unfrozen
 15  id: 16.43   Teb 7ff67000 Unfrozen
 16  id: 16.89   Teb 7ff50000 Unfrozen
 17  id: 16.95   Teb 7ff65000 Unfrozen
 18  id: 16.90   Teb 7ff64000 Unfrozen
 19  id: 16.71   Teb 7ff63000 Unfrozen
 20  id: 16.bb   Teb 7ff62000 Unfrozen
 21  id: 16.88   Teb 7ff61000 Unfrozen    // this thread owns the first critical section
 22  id: 16.cd   Teb 7ff5e000 Unfrozen
 23  id: 16.c1   Teb 7ff5f000 Unfrozen
 24  id: 16.bd   Teb 7ff5d000 Unfrozen 
```

Thread 21 owns the first critical section. Make that the active thread and get a stack trace:

```dbgcmd
0:024> ~21s
ntdll!_ZwWaitForSingleObject+0xb:
77f71bfb c20c00           ret     0xc

0:021> kb

ChildEBP RetAddr  Args to Child
0556fc44 77f79c20 00000110 00000000 77fa4700 ntdll!_ZwWaitForSingleObject+0xb
0556fcb0 77f71048 5ffa91b4 5feb4f7e 5ffa91b4 ntdll!_RtlpWaitForCriticalSection+0x31
0556fcb8 5feb4f7e 5ffa91b4 0556fd70 77f71000 ntdll!_RtlEnterCriticalSection+0x48
0556fcf4 5fef0b76 01302005 00000000 fffffff4 winsrv!__ScrollDC+0x14
0556fd70 5fedf83f 002bd880 0556fdc0 00000025 winsrv!_StreamScrollRegion+0x21b
0556fd8c 5fedfa5b 002bd880 00190000 00000000 winsrv!_AdjustCursorPosition+0x8e

0556fdc0 5fedf678 0556ff18 002bdf70 002a4d58 winsrv!_DoWriteConsole+0x104
0556fefc 5fe6311b 0556ff18 0556ffd0 00000005 winsrv!_SrvWriteConsole+0x96
0556fff4 00000000 00000000 00000024 00000024 csrsrv!_CsrApiRequestThread+0x4ff 
```

Thread 6 owns the second critical section. Examine its stack as well:

```dbgcmd
0:021> ~6s
winsrv!_PtiFromThreadId+0xd:
5fe8429a 394858           cmp     [eax+0x58],ecx    ds:0023:7f504da8=000000f8

0:006> kb

ChildEBP RetAddr  Args to Child
01ecfeb4 5fecd0d7 00000086 00000000 7f5738e0 winsrv!_PtiFromThreadId+0xd
01ecfed0 5feccf62 00000086 01ecfff4 00000113 winsrv!__GetThreadDesktop+0x12
01ecfefc 5fe6311b 01ecff18 01ecffd0 00000005 winsrv!___GetThreadDesktop+0x8b
01ecfff4 00000000 00000000 00000024 00000024 csrsrv!_CsrApiRequestThread+0x4ff 
```

Thread 21 has **RtlpWaitForCriticalSection** near the top of its stack. Thread 6 does not. So thread 21 should be investigated further to determine what it is waiting on. Examine the source code associated with  the locked threads, to see that locks are held and released properly.

## Application Verifier

Application verifier can intercept and wrap calls to detect incorrect lock usage. Application verifier can help locate the following issues.

- Using un-initialized Critical Sections.
- Thread releasing a Critical Section it doesn’t own.
- Re-initialization of a Critical Section.
- Over-releasing a Critical Section.
- Thread in a state where it shouldn’t own locks (ExitThread, TerminateThread, ThreadPool, RPC Threads) but it actually owns locks.

For more information, see [Application Verifier - Overview](../devtest/application-verifier.md).

## See also

For a code sample and example debugging session of an orphaned critical section, see *Advanced Windows Debugging* by Mario Hewardt and Daniel Pravat.

[Displaying a Critical Section](displaying-a-critical-section.md)

[Critical Section Time Outs](critical-section-time-outs.md) (user mode)

[**!ntsdexts.locks**](../debuggercmds/-locks---ntsdexts-locks-.md) 

[!cs ](../debuggercmds/-cs.md)
