---
title: Introduction to Threaded DPCs
description: A *threaded DPC* is a DPC that the system executes at IRQL equal to PASSIVE_LEVEL.
keywords: ["threaded DPCs WDK kernel", "real-time threads WDK kernel", "preempted DPCs WDK kernel"]
ms.date: 07/22/2021
---

# Introduction to Threaded DPCs

Threaded DPCs are available in Windows Vista and later versions of Windows.

A *threaded DPC* is a DPC that the system executes at IRQL equal to PASSIVE_LEVEL. Threaded DPCs are enabled by default, but you can disable them by setting the **HKLM\\System\\CCS\\Control\\SessionManager\\Kernel\\ThreadDpcEnable** registry key to zero. When threaded DPCs are disabled, they execute as ordinary DPCs.

An ordinary DPC preempts the execution of all threads, and cannot be preempted by a thread or by another DPC. If the system has a large number of ordinary DPCs queued, or if one of those DPCs runs for a long time, every thread will remain paused for an arbitrarily long time. Thus, each ordinary DPC increases system latency, which can hurt the performance of time-sensitive applications, such as audio or video playback.

Conversely, a threaded DPC can be preempted by an ordinary DPC, but not by other threads. Therefore, you should use threaded DPCs rather than ordinary DPCs—unless a particular DPC must not be preempted, not even by another DPC.

The system represents threaded DPCs (and ordinary DPCs) as [**KDPC**](./eprocess.md) structures. To initialize a **KDPC** structure for a threaded DPC, call the [**KeInitializeThreadedDpc**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializethreadeddpc) routine, and pass it a *CustomThreadedDpc* routine that performs the action of the DPC.

Because a *CustomThreadedDpc* routine can execute at either PASSIVE_LEVEL or DISPATCH_LEVEL, you must ensure that your *CustomThreadedDpc* routine correctly synchronizes at both IRQLs. For more information about how to do so, see [Synchronization and Threaded DPCs](synchronization-and-threaded-dpcs.md).

In addition, you must ensure that your *CustomThreadedDpc* routine obeys all the restrictions for DISPATCH_LEVEL code. If threaded DPCs are enabled, they run at IRQL = PASSIVE_LEVEL but are still subject to the same restrictions as ordinary DPCs. All of the code that executes in a threaded DPC—including all functions that are called by the *CustomThreadedDpc* routine—must conform to the restrictions of the DPC environment. For example, code must not block on passive-level synchronization objects, such as [KEVENT objects](defining-and-using-an-event-object.md). Many existing device stacks, such as networking and USB, do not support threaded DPC processing, and they might try to block if they detect that they are called at PASSIVE_LEVEL. For similar reasons, the [Kernel-Mode Driver Framework](../wdf/index.md) (KMDF) does not support threaded DPC processing, and KMDF drivers should not try to use threaded DPCs. For more information about the DPC environment, see [Writing DPC Routines](writing-dpc-routines.md).

To add a threaded DPC to the DPC queue, call [**KeInsertQueueDpc**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinsertqueuedpc). To remove a threaded DPC from the queue before it executes, call [**KeRemoveQueueDpc**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keremovequeuedpc).
