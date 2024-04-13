---
title: Run-Down Protection
description: Starting with Windows XP, run-down protection is available to kernel-mode drivers. Drivers can use run-down protection to safely access objects in shared system memory that are created and deleted by another kernel-mode driver.
ai-usage: ai-assisted
ms.date: 02/23/2024
---

# Run-Down Protection


Starting with Windows XP, run-down protection is available to kernel-mode drivers. Drivers can use run-down protection to safely access objects in shared system memory that are created and deleted by another kernel-mode driver.

An object is said to be *run down* if all outstanding accesses of the object are finished and no new requests to access the object will be granted. For example, a shared object might need to be run down so that it can be deleted and replaced with a new object.

The driver that owns the shared object can enable other drivers to acquire and release run-down protection on the object. When run-down protection is in effect, a driver other than the owner can access the object without risk that the owner will delete the object before the access completes. Before the access starts, the accessing driver requests run-down protection on the object. For a long-lived object, this request is nearly always granted. After the access finishes, the accessing driver releases its previously acquired run-down protection on the object.

## Primary run-down protection routines


To start sharing an object, the driver that owns the object calls the [**ExInitializeRundownProtection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinitializerundownprotection) routine to initialize run-down protection on the object. After this call, other drivers that access the object can acquire and release run-down protection on the object.

A driver that accesses the shared object calls the [**ExAcquireRundownProtection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exacquirerundownprotection) routine to request run-down protection on the object. After the access is finished, this driver calls the [**ExReleaseRundownProtection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exreleaserundownprotection) routine to release run-down protection on the object.

If the owning driver determines that the shared object must be deleted, this driver waits to delete the object until all outstanding accesses of the object are finished.

In preparation to delete the shared object, the owning driver calls the [**ExWaitForRundownProtectionRelease**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exwaitforrundownprotectionrelease) routine to wait for the object to run down. During this call, **ExWaitForRundownProtectionRelease** waits for all previously granted instances of run-down protection on the object to be released, but prevents new requests for run-down protection on the object from being granted. After the last protected access finishes and all instances of run-down protection are released, **ExWaitForRundownProtectionRelease** returns, and the owning driver can safely delete the object.

**ExWaitForRundownProtectionRelease** blocks the execution of the calling driver thread until all drivers that hold run-down protection on the shared object release this protection. To prevent **ExWaitForRundownProtectionRelease** from blocking execution for excessively long periods, drivers threads that access the shared object should avoid being suspended while they hold run-down protection on the object. For this reason, accessing drivers should call **ExAcquireRundownProtection** and **ExReleaseRundownProtection** within a critical region or guarded region, or while running at IRQL = APC\_LEVEL.

## Uses for run-down protection


Run-down protection is particularly useful for providing access to a shared object that is nearly always available but might occasionally need to be deleted and replaced. Drivers that access data or that call routines in this object must not try to access the object after it is deleted. Otherwise, these invalid accesses might cause unpredictable behavior, data corruption, or even system failure.

For example, an antivirus driver typically stays loaded in memory when the operating system is running. Occasionally, this driver might need to be unloaded and replaced with an updated release of the driver. Other drivers send I/O requests to the antivirus driver to access the data and routines in this driver. Before sending an I/O request, a kernel component, such as a file system filter manager, can acquire run-down protection to guard against premature unloading of the antivirus driver while it handles the I/O request. After the I/O request completes, run-down protection can be released.

Run-down protection does not serialize accesses to a shared object. If two or more accessing drivers can simultaneously hold run-down protection on an object, and accesses to the object must be serialized, some other mechanism, such as a mutual-exclusion lock, must be used to serialize the accesses.

## The EX\_RUNDOWN\_REF structure


An [**EX\_RUNDOWN\_REF**](./eprocess.md) structure tracks the status of run-down protection on a shared object. This structure is opaque to drivers. The system-supplied run-down protection routines use this structure to count the number of instances of run-down protection that are currently in effect on the object. These routines also use this structure to track whether the object is run down or is in the process of being run down.

To start sharing an object, the driver that owns the object calls **ExInitializeRundownProtection** to initialize the **EX\_RUNDOWN\_REF** structure associated with the object. After initialization, the owning driver can make this structure available to other drivers that require access to the object. The accessing drivers pass this structure as a parameter to the **ExAcquireRundownProtection** and **ExReleaseRundownProtection** calls that acquire and release run-down protection on the object. The owning driver passes this structure as a parameter to the **ExWaitForRundownProtectionRelease** call that waits for the object to run down so that it can be safely deleted.

## Comparison to locks


Run-down protection is one of several ways to guarantee safe access to a shared object. Another approach is to use a mutual-exclusion software lock. If a driver requires access to an object that is currently locked by another driver, the first driver must wait for the second driver to release the lock. However, acquiring and releasing locks can become a performance bottleneck, and locks can consume large amounts of memory. If used incorrectly, locks might cause drivers that compete for the same shared objects to become deadlocked. Efforts to detect and avoid deadlocks typically require the diversion of substantial computing resources.

In contrast to locks, run-down protection has relatively lightweight processing time and memory requirements. A simple reference count is associated with the object to ensure that deletion of the object is deferred until all outstanding accesses of the object are completed. With this approach, atomic, interlocked hardware instructions can be used instead of mutual-exclusion software locks to guarantee safe access to an object. Calls to acquire and release run-down protection are typically very fast. The benefits of using a lightweight mechanism, such as run-down protection, can be significant for a shared object that has a long life and is shared among many drivers.

## Other run-down protection routines


Several other run-down protection routines are available, in addition to those that were mentioned previously. These additional routines might used by some drivers.

The [**ExReInitializeRundownProtection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exreinitializerundownprotection) routine enables a previously used [**EX\_RUNDOWN\_REF**](./eprocess.md) structure to be associated with a new object, and initializes run-down protection on this object.

The [**ExRundownCompleted**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exrundowncompleted) routine updates the **EX\_RUNDOWN\_REF** structure to indicate that the run down of the associated object has completed.

The [**ExAcquireRundownProtectionEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exacquirerundownprotectionex) and [**ExReleaseRundownProtectionEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exreleaserundownprotectionex) routines are similar to [**ExAcquireRundownProtection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exacquirerundownprotection) and [**ExReleaseRundownProtection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exreleaserundownprotection). These four routines increment or decrement the count of the instances of run-down protection that are in effect on a shared object. Whereas **ExAcquireRundownProtection** and **ExReleaseRundownProtection** increment and decrement this count by one, **ExAcquireRundownProtectionEx** and **ExReleaseRundownProtectionEx** increment and decrement the count by arbitrary amounts.

## Cache-aware run-down protection

A rundown reference is a compact and fast data structure, but it can cause cache contention when many processors try to acquire the reference at the same time. This can affect the performance and scalability of your driver.

To avoid this problem, you can use a cache-aware rundown reference to distribute the reference tracking across multiple cache lines. This reduces the cache contention and improves the performance of your driver on multiprocessor computers.

To use a cache-aware rundown reference, follow these steps:

1. Create an **EX_RUNDOWN_REF_CACHE_AWARE** object by doing one of the following:
    * Call [**ExAllocateCacheAwareRundownProtection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatecacheawarerundownprotection). Note that this takes care of initialization.
    * Alternatively, to control the memory allocation, call [**ExSizeOfRundownProtectionCacheAware**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exsizeofrundownprotectioncacheaware), allocate a buffer of the size returned, then pass that buffer and size to [**ExInitializeRundownProtectionCacheAware**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinitializerundownprotectioncacheaware).
1. Request rundown protection on the object before accessing it by calling the [**ExAcquireRundownProtectionCacheAware**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exacquirerundownprotectioncacheaware) routine. This routine returns TRUE if the request is granted, or FALSE if the object is being run down.
1. Release rundown protection on the object after accessing it by calling the [**ExReleaseRundownProtectionCacheAware**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exreleaserundownprotectioncacheaware) routine.
1. Wait for the object to run down before deleting it by calling the [**ExWaitForRundownProtectionReleaseCacheAware**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exwaitforrundownprotectionreleasecacheaware) routine. This routine blocks the current thread until all instances of rundown protection on the object are released.
1. If the driver called  [**ExAllocateCacheAwareRundownProtection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatecacheawarerundownprotection) earlier, it should call [**ExFreeCacheAwareRundownProtection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exfreecacheawarerundownprotection) to free the rundown reference.

To reuse a cache-aware rundown reference, follow these steps:

1. After calling **ExWaitForRundownProtectionReleaseCacheAware**, call [**ExRundownCompletedCacheAware**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exrundowncompletedcacheaware) to indicate that the run down of the old object has completed.
1. Call [**ExReInitializeRundownProtectionCacheAware**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exreinitializerundownprotectioncacheaware) to reinitialize the reference after the associated object is run down.
1. Now the driver can again call [**ExAcquireRundownProtectionCacheAware**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exacquirerundownprotectioncacheaware).

A cache-aware rundown reference has the advantage of better performance and scalability in specific situations, but it consumes more memory than a regular rundown reference. You should consider this trade-off when choosing between the two types of rundown references.
