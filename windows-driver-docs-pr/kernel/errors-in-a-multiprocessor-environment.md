---
title: Errors in a Multiprocessor Environment
author: windows-driver-content
description: Errors in a Multiprocessor Environment
ms.assetid: 8a76b8d6-14d8-4709-8b15-e8b6b5094a1b
keywords: ["reliability WDK kernel , race conditions", "race conditions WDK kernel", "reliability WDK kernel , multiprocessor environment errors", "multiprocessor environment errors WDK kernel", "locking WDK kernel", "multiple I/O request handling WDK kernel", "I/O requests WDK kernel", "thread conflicts WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Errors in a Multiprocessor Environment


## <a href="" id="ddk-errors-in-a-multiprocessor-environment-kg"></a>


On the NT-based operating system, drivers are multithreaded; they can receive multiple I/O requests from different threads at the same time. In designing a driver, you must assume that it will be run on an SMP system and take the appropriate measures to ensure data integrity.

Specifically, whenever a driver changes global or file object data, it must use a lock or an interlocked sequence to prevent race conditions.

### Encountering a race condition when referencing global or file object-specific data

In the following code snippet, a race condition could occur when the driver accesses the global data at **Data.LpcInfo**:

```
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

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Errors%20in%20a%20Multiprocessor%20Environment%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


