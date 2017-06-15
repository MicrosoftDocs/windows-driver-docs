---
title: Preventing Errors and Deadlocks While Using Spin Locks
author: windows-driver-content
description: Preventing Errors and Deadlocks While Using Spin Locks
MS-HAID:
- 'Synchro\_f74a900d-aad5-4473-8f46-00531c9ade89.xml'
- 'kernel.preventing\_errors\_and\_deadlocks\_while\_using\_spin\_locks'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1df563e6-7ad2-4684-9778-ffa1b845ac31
keywords: ["deadlocks WDK kernel", "recursion WDK kernel", "nested spin lock acquisitions WDK kernel", "pageable data locking WDK kernel", "spin locks WDK kernel"]
---

# Preventing Errors and Deadlocks While Using Spin Locks


## <a href="" id="ddk-preventing-errors-and-deadlocks-while-using-spin-locks-kg"></a>


While a driver routine holds a spin lock, it cannot cause a hardware exception or raise a software exception without bringing down the system. In other words, a driver's ISR and any *SynchCritSection* routine that the driver supplies in a call to [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302) must not cause a fault or trap, such as a page fault or an arithmetic exception, and cannot raise a software exception. A routine that calls [**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917) or [**KeAcquireInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551899) also cannot cause a hardware exception or raise a software exception until it has released its executive spin lock and is no longer running at IRQL = DISPATCH\_LEVEL.

### Pageable Data and Support Routines

While holding a spin lock, drivers must not call routines that access pageable data. Remember that drivers can call certain support routines that access pageable data if and only if their calls occur while executing at an IRQL strictly less than DISPATCH\_LEVEL. This IRQL restriction precludes calling these support routines while holding a spin lock. For IRQL requirements for any specific support routine, see the routine's reference page.

### Recursion

Attempting to acquire a spin lock recursively is guaranteed to cause a deadlock: the holding instantiation of a recursive routine cannot release the spin lock while a second instantiation spins, trying to acquire the same spin lock.

The following guidelines describe how you use spin locks with recursive routines:

-   The recursive routine must not call itself while holding a spin lock, or must not attempt to acquire the same spin lock on subsequent calls.

-   While the recursive routine holds a spin lock, another driver routine must not call the recursive routine if recursion might cause a deadlock or could cause the caller to hold the spin lock for longer than 25 microseconds.

For more information about recursive driver routines, see [Using the Kernel Stack](using-the-kernel-stack.md).

### Nested Spin Lock Acquisitions

Attempting to acquire a second spin lock while holding another spin lock also can cause deadlocks or poor driver performance.

The following guidelines describe how drivers should hold spin locks:

-   The driver must not call a support routine that uses a spin lock unless a deadlock cannot occur.

-   Even if a deadlock cannot occur, the driver should not call a support routine that uses a spin lock unless alternate coding techniques cannot provide comparable driver performance and functionality.

-   If a driver makes nested calls to acquire spin locks, it must always acquire the spin locks in the same order each time they are acquired. This order helps avoid deadlocks.

In general, avoid using nested spin locks to protect overlapping subsets or discrete sets of shared data and resources. Consider what can happen if a driver uses two executive spin locks to protect discrete resources, such as a pair of timer objects that might be set individually and collectively by various driver routines. The driver would deadlock intermittently in an SMP machine, whenever either of two routines, each holding one spin lock, tried to acquire the other spin lock.

For more information about acquiring nested spin locks, see the [Locks, Deadlocks, and Synchronization](http://go.microsoft.com/fwlink/p/?linkid=57456 ) article in the MSDN Library.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Preventing%20Errors%20and%20Deadlocks%20While%20Using%20Spin%20Locks%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


