---
title: "!runaway (WinDbg)"
description: "The !runaway extension displays information about the time consumed by each thread."
keywords: ["!runaway Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- runaway
api_type:
- NA
---

# !runaway

The **!runaway** extension displays information about the time consumed by each thread.

```dbgcmd
!runaway [Flags]
```

## Parameters

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies the kind of information to be displayed. *Flags* can be any combination of the following bits. The default value is 0x1.

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Causes the debugger to show the amount of user time consumed by each thread.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Causes the debugger to show the amount of kernel time consumed by each thread.

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
Causes the debugger to show the amount of time that has elapsed since each thread was created.

## DLL

Uext.dll

Ntsdexts.dll

## Additional Information

The **!runaway** extension can only be used during live debugging or when debugging crash dump files created by [**.dump /mt**](-dump--create-dump-file-.md) or **.dump /ma**.


For information about threads in user mode, see [Controlling Processes and Threads](../debugger/controlling-processes-and-threads.md). For more information about analyzing processes and threads, see *Microsoft Windows Internals* by Mark Russinovich and David Solomon. 

## Remarks

This extension is a quick way to find out which threads are spinning out of control or consuming too much CPU time.

The display identifies each thread by the debugger's internal thread numbering and by the thread ID in hexadecimal. The debugger IDs are also shown.

Here is an example:

```dbgcmd
0:001> !runaway 7

 User Mode Time
 Thread       Time
 0:55c        0:00:00.0093
 1:1a4        0:00:00.0000

 Kernel Mode Time
 Thread       Time
 0:55c        0:00:00.0140
 1:1a4        0:00:00.0000

 Elapsed Time
 Thread       Time
 0:55c        0:00:43.0533
 1:1a4        0:00:25.0876
```
