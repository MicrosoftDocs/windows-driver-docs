---
title: Errors in a Multiprocessor Environment
description: Errors in a Multiprocessor Environment
ms.assetid: 8a76b8d6-14d8-4709-8b15-e8b6b5094a1b
keywords: ["reliability WDK kernel , race conditions", "race conditions WDK kernel", "reliability WDK kernel , multiprocessor environment errors", "multiprocessor environment errors WDK kernel", "locking WDK kernel", "multiple I/O request handling WDK kernel", "I/O requests WDK kernel", "thread conflicts WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Errors in a Multiprocessor Environment





On the NT-based operating system, drivers are multithreaded; they can receive multiple I/O requests from different threads at the same time. In designing a driver, you must assume that it will be run on an SMP system and take the appropriate measures to ensure data integrity.

Specifically, whenever a driver changes global or file object data, it must use a lock or an interlocked sequence to prevent race conditions.

### Encountering a race condition when referencing global or file object-specific data

In the following code snippet, a race condition could occur when the driver accesses the global data at **Data.LpcInfo**:

```cpp
   PLPC_INFO pLpcInfo = &Data.LpcInfo; //Pointer to global data
   ...
   ...
   // This saved pointer may be overwritten by another thread.
   pLpcInfo->LpcPortName.Buffer = ExAllocatePool(
                                     PagedPool,
                                     arg->PortName.Length);
```

Multiple threads entering this code as a result of an IOCTL call could cause a memory leak as the pointer is overwritten. To avoid this problem, the driver should use the **ExInterlocked*Xxx*** routines or some type of lock when it changes the global data. The driver's requirements determine the acceptable types of locks. For further information, see [Spin Locks](spin-locks.md), [Kernel Dispatcher Objects](kernel-dispatcher-objects.md), and [**ExAcquireResourceSharedLite**](https://msdn.microsoft.com/library/windows/hardware/ff544363).

The following example attempts to reallocate a file-specific buffer (**Endpoint-&gt;LocalAddress**) to hold the endpoint address:

```cpp
   Endpoint = FileObject->FsContext;

    if ( Endpoint->LocalAddress != NULL &&
         Endpoint->LocalAddressLength <
                   ListenEndpoint->LocalAddressLength ) {

      FREE_POOL (Endpoint->LocalAddress,
                 LOCAL_ADDRESS_POOL_TAG
                 );
      Endpoint->LocalAddress  = NULL;
   }

    if ( Endpoint->LocalAddress == NULL ) {
       Endpoint->LocalAddress =
            ALLOCATE_POOL (NonPagedPool,
                           ListenEndpoint->LocalAddressLength,
                           LOCAL_ADDRESS_POOL_TAG);
   }
```

In this example, a race condition could occur with accesses to the file object. Because the driver does not hold any locks, two requests for the same file object can enter this function. The result might be references to freed memory, multiple attempts to free the same memory, or memory leaks. To avoid these errors, the two **if** statements should be enclosed in a spin lock.








