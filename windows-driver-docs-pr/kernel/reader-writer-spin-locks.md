---
title: Reader/Writer Spin Locks
description: Starting with Windows Vista with Service Pack 1 (SP1), a set of related routines use spin locks to support synchronized access to data structures that are shared by readers and writers.
ms.assetid: E2853F35-590E-4EF5-8647-1261BC4B8D15
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Reader/Writer Spin Locks


Starting with Windows Vista with Service Pack 1 (SP1), a set of related routines use spin locks to support synchronized access to data structures that are shared by readers and writers. A thread that requires only read access to a data structure can use a spin lock to share this structure with other reader threads. A thread that needs to write to a shared data structure must use the spin lock to obtain exclusive access to the data structure before it can write to this structure.

If a reader thread needs to acquire a spin lock for shared access, and the lock is already held for exclusive access by a writer thread, the reader must first wait for the writer to release the lock. Similarly, if a writer thread needs to acquire a spin lock for exclusive access, and the lock is already held for shared access by one or more reader threads, the writer thread must wait for all of these reader threads to release the lock. While the writer waits, no new reader threads can acquire the lock. Instead, a reader that needs to acquire the lock that the writer is waiting for must first wait for the writer to acquire and release the lock.

A thread can switch roles between reader and writer. A thread that already holds a spin lock for shared access can try to convert the access mode of the spin lock from shared mode to exclusive mode. This attempt succeeds if no readers already hold the spin lock for shared access, and if no writer is already waiting to acquire the spin lock for exclusive access.

Recursive acquisition of a spin lock causes deadlock and is not allowed.

The following is a list of the routines that are available to manage reader/writer spin locks starting with Windows Vista with SP1.

| Routine name                                                                                | Description                                                                                                           |
|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [**ExAcquireSpinLockExclusive**](https://msdn.microsoft.com/library/windows/hardware/hh451007)                         | Acquires a spin lock for exclusive access by the caller, and raises the IRQL to DISPATCH\_LEVEL.                      |
| [**ExAcquireSpinLockExclusiveAtDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/hh451009)    | Acquires a spin lock for exclusive access by a caller that is already running at IRQL &gt;= DISPATCH\_LEVEL.          |
| [**ExAcquireSpinLockShared**](https://msdn.microsoft.com/library/windows/hardware/hh451053)                               | Acquires a spin lock for shared access by the caller, and raises the IRQL to DISPATCH\_LEVEL.                         |
| [**ExAcquireSpinLockSharedAtDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/hh451055)           | Acquires a spin lock for shared access by a caller that is already running at IRQL &gt;= DISPATCH\_LEVEL.             |
| [**ExReleaseSpinLockExclusive**](https://msdn.microsoft.com/library/windows/hardware/hh451061)                        | Releases a spin lock that the caller acquired for exclusive access, and restores the original IRQL.                   |
| [**ExReleaseSpinLockExclusiveFromDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/hh451058) | Releases a spin lock that the caller acquired for exclusive access, and does not lower the IRQL.                      |
| [**ExReleaseSpinLockShared**](https://msdn.microsoft.com/library/windows/hardware/hh451067)                              | Releases a spin lock that the caller acquired for shared access, and restores the original IRQL.                      |
| [**ExReleaseSpinLockSharedFromDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/hh451064)      | Releases a spin lock that the caller acquired for shared access, and does not lower the IRQL.                         |
| [**ExTryConvertSharedSpinLockExclusive**](https://msdn.microsoft.com/library/windows/hardware/hh451070)      | Tries to convert the access state of a spin lock that the caller already holds for shared access to exclusive access. |

 

The reader/writer spin lock routines all take, as their first parameter, a pointer to a spin lock, which is an **EX\_SPIN\_LOCK** structure. This structure is opaque to drivers. A driver should allocate the storage for the spin lock from nonpaged system memory, and initialize the lock to zero.

 

 




