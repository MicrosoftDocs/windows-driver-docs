---
title: Types of APCs
description: Types of APCs
keywords: ["asynchronous procedure calls WDK kernel", "APCs WDK kernel", "user APCs WDK kernel", "normal kernel APCs WDK kernel", "special kernel APCs WDK kernel"]
ms.date: 01/07/2022
ms.custom: contperf-fy23q3
---

# Types of APCs


An [asynchronous procedure call (APC)](/windows/win32/sync/asynchronous-procedure-calls) is a function that executes asynchronously.
APCs are similar to [deferred procedure calls (DPCs)](/windows-hardware/drivers/kernel/introduction-to-dpc-objects), but unlike DPCs, APCs execute within the context of a particular thread.
Drivers (other than file systems and file-system filter drivers) do not use APCs directly, but other parts of the operating system do, so you need to be aware of how APCs work.

The Windows operating system uses three kinds of APCs:

-   *User APCs* run strictly in user mode and only when the current thread is in an alertable wait state. The operating system uses user APCs to implement mechanisms such as [overlapped I/O](./handling-overlapped-i-o-operations.md) and the [**QueueUserApc**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-queueuserapc) Win32 routine.

-   *Normal kernel APCs* run in kernel mode at IRQL = PASSIVE\_LEVEL. A normal kernel APC preempts all user-mode code, including user APCs. Normal kernel APCs are generally used by file systems and file-system filter drivers.

-   *Special kernel APCs* run in kernel mode at IRQL = APC\_LEVEL. A special kernel APC preempts user-mode code and kernel-mode code that executes at IRQL = PASSIVE\_LEVEL, including both user APCs and normal kernel APCs. The operating system uses special kernel APCs to handle operations such as I/O request completion.

 
For a list of IRQLs from lowest to highest priority, see [Managing Hardware Priorities](./managing-hardware-priorities.md).
 
