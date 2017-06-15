---
title: Introduction to ERESOURCE Routines
author: windows-driver-content
description: Introduction to ERESOURCE Routines
MS-HAID:
- 'Synchro\_a5795386-5b23-48aa-ade1-de3a29a31b06.xml'
- 'kernel.introduction\_to\_eresource\_routines'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5c7759db-aeb5-47f3-8adc-ddedb74b5cb4
keywords: ["ERESOURCE structures", "exclusive waiters WDK kernel", "shared waiters WDK kernel", "exclusive/shared synchronization WDK kernel", "synchronization WDK kernel , exclusive/shared", "waiters WDK kernel"]
---

# Introduction to ERESOURCE Routines


## <a href="" id="ddk-introduction-to-eresource-routines-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Introduction%20to%20ERESOURCE%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


