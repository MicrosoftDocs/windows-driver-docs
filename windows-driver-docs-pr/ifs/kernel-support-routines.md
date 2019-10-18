---
title: Kernel Support Routines
description: Kernel Support Routines
ms.assetid: aa4a1a16-06df-4795-ac26-5728e6f2df11
ms.date: 09/30/2019
ms.localizationpriority: medium
---

# Kernel Support Routines

The following table lists the subset of system-supplied kernel support routines that can be used by kernel-mode file systems and file system (minifilter and legacy) filter drivers, with some reserved for system use. The routines below cannot be used by device drivers.

In addition to the routines documented here, file systems and file system filter drivers can also call any of the **Ke**_Xxx_ routines that are described in the Kernel-Mode Driver Architecture Reference section and that are declared in *ntifs.h*.

**Header File:** *ntifs.h*

**Prefix: Ke**_Xxx_

| Function or Macro | Description |
| ----------------- | ----------- |
| **KeAcquireQueuedSpinLock** | Reserved for system use. |
| **KeAttachProcess** | Obsolete. Use **KeStackAttachProcess** instead. |
| **KeDetachProcess** | Obsolete. Use **KeUnstackAttachProcess** instead. |
| **KeInitializeMutant** | Reserved for system use. See **KeInitializeMutex**. |
| **KeInitializeQueue** | Initializes a queue object on which threads can wait for entries. |
| **KeInsertHeadQueue** | Inserts an entry at the head of the given queue if it cannot immediately use the entry to satisfy a thread wait.|
| **KeInsertQueue** | Inserts an entry at the tail of the given queue if it cannot immediately use the entry to satisfy a thread wait. |
| **KeReadStateMutant** | Reserved for system use. See **KeReadStateMutex**. |
| **KeReadStateQueue** | Reserved for system use. |
| **KeReleaseMutant** | Reserved for system use. See **KeReleaseMutex**. |
| **KeReleaseQueuedSpinLock** | Reserved for system use. |
| **KeRemoveQueue** | Gives the calling thread a pointer to a dequeued entry from the given queue object or allows the caller to wait, up to an optional timeout interval, on the queue object. |
| **KeRundownQueue** | Cleans up a queue object, flushing any queued entries. |
| **KeSetIdealProcessorThread** | Reserved for system use. |
| **KeStackAttachProcess** | Attaches the current thread to the address space of the target process. |
| **KeTryToAcquireQueuedSpinLock** | Reserved for system use. |
| **KeUnstackDetachProcess** | Detaches the current thread from the address space of a process and restores the previous attach state. Use this routine with extreme caution. (See the Remarks section.) |
