---
title: Introduction to ERESOURCE Routines
description: Introduction to ERESOURCE Routines
ms.assetid: 5c7759db-aeb5-47f3-8adc-ddedb74b5cb4
keywords: ["ERESOURCE structures", "exclusive waiters WDK kernel", "shared waiters WDK kernel", "exclusive/shared synchronization WDK kernel", "synchronization WDK kernel , exclusive/shared", "waiters WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Introduction to ERESOURCE Routines





The system provides routines to acquire and release ERESOURCE structures, as well as to examine their current state.

### Acquiring and Releasing an ERESOURCE Structure

Drivers can use the ERESOURCE structures to implement *exclusive/shared synchronization*. Exclusive/shared synchronization works as follows:

-   Any number of threads can acquire an ERESOURCE as shared.

-   Only one thread can acquire an ERESOURCE exclusively. The ERESOURCE can only be acquired exclusively if no threads have already acquired it as shared.

A thread that cannot currently acquire an ERESOURCE can optionally be put in a wait state until the ERESOURCE can be acquired. The system maintains two lists of threads that are waiting for an ERESOURCE: a list of *exclusive waiters* and a list of *shared waiters*.

A typical use for exclusive/shared synchronization is to implement a read/write lock. A read/write lock allows several threads to perform a read operation, but only one thread can write at a time. This can be implemented directly in terms of acquiring an ERESOURCE.

A driver allocates the storage for an ERESOURCE and initializes it with [**ExInitializeResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545317). The system maintains a list of all ERESOURCE structures in use. When the driver no longer requires a particular ERESOURCE, it must call [**ExDeleteResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff544578) to delete it from the system's list. The driver can also reuse an ERESOURCE by calling [**ExReinitializeResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545542).

Drivers can perform the following basic operations on an ERESOURCE:

-   Acquire an ERESOURCE as shared with [**ExAcquireResourceSharedLite**](https://msdn.microsoft.com/library/windows/hardware/ff544363). This routine acquires the resource only if the resource has not been acquired exclusively and there are no exclusive waiters.

-   Acquire an ERESOURCE exclusively with [**ExAcquireResourceExclusiveLite**](https://msdn.microsoft.com/library/windows/hardware/ff544351). This routine acquires the resource as long as it has not been acquired either exclusively or as shared.

-   Convert an exclusive acquisition to a shared acquisition with [**ExConvertExclusiveToSharedLite**](https://msdn.microsoft.com/library/windows/hardware/ff544558).

-   Release an acquired resource with [**ExReleaseResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545597).

The *Wait* parameter of [**ExAcquireResourceSharedLite**](https://msdn.microsoft.com/library/windows/hardware/ff544363) and [**ExAcquireResourceExclusiveLite**](https://msdn.microsoft.com/library/windows/hardware/ff544351) determines whether the current thread waits for the ERESOURCE to be acquired. If you specify a value of **FALSE** and the ERESOURCE cannot be acquired, then the routine returns **FALSE**. If you specify a value of **TRUE**, then the current thread is put on the appropriate wait list for the ERESOURCE.

### Examining the State of an ERESOURCE Structure

A driver can also determine the current state of an ERESOURCE, as follows:

-   Use [**ExIsResourceAcquiredLite**](https://msdn.microsoft.com/library/windows/hardware/ff545466) or [**ExIsResourceAcquiredSharedLite**](https://msdn.microsoft.com/library/windows/hardware/ff545477) to determine if the ERESOURCE has already been acquired as either shared or exclusive. Use [**ExIsResourceAcquiredExclusiveLite**](https://msdn.microsoft.com/library/windows/hardware/ff545458) to check whether the ERESOURCE has been specifically acquired exclusively.

-   Use [**ExGetSharedWaiterCount**](https://msdn.microsoft.com/library/windows/hardware/ff545290) to determine the number of shared waiters for the ERESOURCE, and use [**ExGetExclusiveWaiterCount**](https://msdn.microsoft.com/library/windows/hardware/ff544618) to determine the number of exclusive waiters for the ERESOURCE.

 

 




