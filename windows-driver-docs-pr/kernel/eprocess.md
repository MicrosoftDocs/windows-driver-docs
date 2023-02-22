---
title: Windows kernel opaque structures
description: Windows kernel opaque structures
keywords: ["EPROCESS", "ETHREAD", "EX_RUNDOWN_REF", "EX_TIMER", "FAST_MUTEX", "IO_CSQ", "IO_CSQ_IRP_CONTEXT", "IO_WORKITEM", "KBUGCHECK_CALLBACK_RECORD", "KBUGCHECK_REASON_CALLBACK_RECORD", "KDPC", "KFLOATING_SAVE", "KGUARDED_MUTEX", "KINTERRUPT", "KLOCK_QUEUE_HANDLE", "KTIMER", "LOOKASIDE_LIST_EX", "NPAGED_LOOKASIDE_LIST", "OBJECT_TYPE", "PAGED_LOOKASIDE_LIST", "RTL_BITMAP", "RTL_RUN_ONCE", "SECURITY_SUBJECT_CONTEXT", "SLIST_HEADER", "XSTATE_SAVE"]
ms.date: 02/23/2023
---

# Windows kernel opaque structures

This article lists and describes Windows kernel opaque structures. For many of these structures, drivers shouldn't access or change any members but should instead use system-supplied routines to access the information. See each structure for details.

## EPROCESS

The **EPROCESS** structure is an opaque structure that serves as the process object for a process.

Some routines, such as [**PsGetProcessCreateTimeQuadPart**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-psgetprocesscreatetimequadpart), use **EPROCESS** to identify the process to operate on.
Drivers can use the [**PsGetCurrentProcess**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentprocess) routine to obtain a pointer to the process object for the current process and can use the [**ObReferenceObjectByHandle**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obreferenceobjectbyhandle) routine to obtain a pointer to the process object that is associated with the specified handle. The [**PsInitialSystemProcess**](mm64bitphysicaladdress.md) global variable points to the process object for the system process.

A process object is an Object Manager object. Drivers should use Object Manager routines such as [**ObReferenceObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obfreferenceobject) and [**ObDereferenceObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obdereferenceobject) to maintain the object's reference count.

Header: *Wdm.h*. Include: *Wdm.h*, *Ntddk.h*, *Ntifs.h*.

## ETHREAD

The **ETHREAD** structure is an opaque structure that serves as the thread object for a thread.

Some routines, such as [**PsIsSystemThread**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-psissystemthread), use **ETHREAD** to identify the thread to operate on. Drivers can use the [**PsGetCurrentThread**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-psgetcurrentthread) routine to obtain a pointer to the thread object for the current thread and can use the [**ObReferenceObjectByHandle**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obreferenceobjectbyhandle) routine to obtain a pointer to the thread object that is associated with the specified handle.

A thread object is an Object Manager object. Drivers should use Object Manager routines such as [**ObReferenceObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obfreferenceobject) and [**ObDereferenceObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obdereferenceobject) to maintain the object's reference count.

Header: *Wdm.h*. Include: *Wdm.h*, *Ntddk.h*, *Ntifs.h*.

## EX_RUNDOWN_REF

The **EX_RUNDOWN_REF** structure is an opaque system structure that contains information about the status of run-down protection for an associated shared object.

``` syntax
typedef struct _EX_RUNDOWN_REF {
  
  ...  // opaque
  
} EX_RUNDOWN_REF, *PEX_RUNDOWN_REF;
```

The run-down protection routines listed at the bottom of this page all take a pointer to an **EX_RUNDOWN_REF** structure as their first parameter.

For more information, see [Run-Down Protection](run-down-protection.md).
Header: *Wdm.h*. Include Wdm.h.

## EX_TIMER

The **EX_TIMER** structure is an opaque structure that the operating system uses to represent an **EX_TIMER** timer object.

```typedef struct _EX_TIMER *PEX_TIMER;```

All members of this structure are opaque to drivers.

The following **Ex*Xxx*Timer** routines require a pointer to a system-allocated **EX_TIMER** structure as an input parameter:

* [**ExSetTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exsettimer)
* [**ExCancelTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-excanceltimer)
* [**ExDeleteTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exdeletetimer)

The operating system creates **EX_TIMER**-based timer objects. To get such a timer object, your driver calls the [**ExAllocateTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatetimer) routine. When this object is no longer needed, the driver is responsible for deleting the object by calling **ExDeleteTimer**.

For more information, see [Ex*Xxx*Timer Routines and EX_TIMER Objects](exxxxtimer-routines-and-ex-timer-objects.md).

Header: *Wdm.h*. Include: *Wdm.h*, *Ntddk.h*, *Ntifs.h*.

## FAST_MUTEX

A **FAST_MUTEX** structure is an opaque data structure that represents a fast mutex. The [**ExInitializeFastMutex**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinitializefastmutex) routine initializes this structure.

For more information about fast mutexes, see [Fast Mutexes and Guarded Mutexes](fast-mutexes-and-guarded-mutexes.md).

Header: *Wdm.h*. Include: *Wdm.h*, *Ntddk.h*, *Ntifs.h*.

## IO_CSQ

The **IO_CSQ** structure is an opaque structure used to specify the driver's cancel-safe IRP queue routines. Don't set the members of this structure directly. Use [**IoCsqInitialize**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocsqinitialize) or [**IoCsqInitializeEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocsqinitializeex) to initialize this structure.

For an overview of how to use cancel-safe IRP queues, see [Cancel-Safe IRP Queues](cancel-safe-irp-queues.md).

Available on Microsoft Windows XP and later versions of the Windows operating system.

Header: *Wdm.h*. Include: *Wdm.h*, *Ntddk.h*, *Ntifs.h*.

## IO_CSQ_IRP_CONTEXT

The **IO_CSQ_IRP_CONTEXT** structure is an opaque data structure used to specify the IRP context for an IRP in the driver's cancel-safe IRP queue. The [**IoCsqInsertIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocsqinsertirp), [**IoCsqInsertIrpEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocsqinsertirpex), and [**IoCsqRemoveIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocsqremoveirp) routines use this structure as a key to identify particular IRPs in the queue.

For an overview of how to use cancel-safe IRP queues, see [Cancel-Safe IRP Queues](cancel-safe-irp-queues.md).

Available on Microsoft Windows XP and later versions of the Windows operating system.

Header: *Wdm.h*. Include: *Wdm.h*, *Ntddk.h*, *Ntifs.h*.

## IO_WORKITEM

The **IO_WORKITEM** structure is an opaque structure that describes a work item for a system worker thread.

A driver can allocate a work item by calling [**IoAllocateWorkItem**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateworkitem). Alternatively, a driver can allocate its own buffer, and then call [**IoInitializeWorkItem**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioinitializeworkitem) to initialize that buffer as a work item.

Any work item that **IoAllocateWorkItem** allocates must be freed by [**IoFreeWorkItem**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iofreeworkitem). Any memory initialized by **IoInitializeWorkItem** must be uninitialized by [**IoUninitializeWorkItem**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iouninitializeworkitem) before it can be freed.

For more information about work items, see [System Worker Threads](system-worker-threads.md).

Header: *Wdm.h*. Include: *Wdm.h*, *Ntddk.h*, *Ntifs.h*.

## KBUGCHECK_CALLBACK_RECORD

The **KBUGCHECK_CALLBACK_RECORD** structure is an opaque structure that the [**KeRegisterBugCheckCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keregisterbugcheckcallback) and [**KeDeregisterBugCheckCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kederegisterbugcheckcallback) routines use.

The **KBUGCHECK_CALLBACK_RECORD** structure is used by the [**KeRegisterBugCheckReasonCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keregisterbugcheckreasoncallback) and [**KeDeregisterBugCheckReasonCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kederegisterbugcheckreasoncallback) routines for bookkeeping.

The structure must be allocated in resident memory, such as nonpaged pool. Use the [**KeInitializeCallbackRecord**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializecallbackrecord) routine to initialize the structure before using it.

Header: *Ntddk.h*. Include: *Ntddk.h*.

## KBUGCHECK_REASON_CALLBACK_RECORD

The **KBUGCHECK_REASON_CALLBACK_RECORD** structure is an opaque structure that the [**KeRegisterBugCheckReasonCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keregisterbugcheckreasoncallback) and [**KeDeregisterBugCheckReasonCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kederegisterbugcheckreasoncallback) routines use.

The **KBUGCHECK_REASON_CALLBACK_RECORD** structure is used by the [**KeRegisterBugCheckReasonCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keregisterbugcheckreasoncallback) and [**KeDeregisterBugCheckReasonCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kederegisterbugcheckreasoncallback) routines for bookkeeping.

The structure must be allocated in resident memory, such as nonpaged pool. Use the [**KeInitializeCallbackRecord**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializecallbackrecord) routine to initialize the structure before using it.

Available on Microsoft Windows XP with Service Pack 1 (SP1), Windows Server 2003, and later versions of the Windows operating system.

Header: *Ntddk.h*. Include: *Ntddk.h*.

## KDPC

The **KDPC** structure is an opaque structure that represents a DPC object. Don't set the members of this structure directly. See [DPC Objects and DPCs](introduction-to-dpc-objects.md).

Header: *Wdm.h*. Include: *Wdm.h*, *Ntddk.h*, *Ntifs.h*.

## KFLOATING_SAVE

The **KFLOATING_SAVE** structure is an opaque structure that describes the floating-point state that the [**KeSaveFloatingPointState**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesavefloatingpointstate) routine saved.

Use [**KeRestoreFloatingPointState**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kerestorefloatingpointstate) to restore the floating-point state.

Header: *Wdm.h*. Include: *Wdm.h*, *Ntddk.h*, *Ntifs.h*.

## KGUARDED_MUTEX

The **KGUARDED_MUTEX** structure is an opaque structure that represents a guarded mutex.

Use **KeInitializeGuardedMutex** to initialize a **KGUARDED_MUTEX** structure as a guarded mutex.

Guarded mutexes must be allocated from non-paged pool.

For more information about guarded mutexes, see [Fast Mutexes and Guarded Mutexes](fast-mutexes-and-guarded-mutexes.md).

Header: *Wdm.h*. Include: *Wdm.h*, *Ntddk.h*, *Ntifs.h*.

## KINTERRUPT

A **KINTERRUPT** structure is an opaque structure that represents an interrupt to the system.

[**IoConnectInterruptEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioconnectinterruptex) provides a pointer to the **KINTERRUPT** structure for the interrupt when the driver registers an [**InterruptService**](/windows-hardware/drivers/ddi/wdm/nc-wdm-kservice_routine) or [**InterruptMessageService**](/windows-hardware/drivers/ddi/wdm/nc-wdm-kmessage_service_routine) routine. The driver uses this pointer when acquiring or releasing the interrupt spin lock for the interrupt. The driver also uses this pointer when unregistering an **InterruptService** routine.

Header: *Wdm.h*. Include: *Wdm.h*, *Ntddk.h*, *Ntifs.h*.

## KLOCK_QUEUE_HANDLE

The **KLOCK_QUEUE_HANDLE** structure is an opaque structure that describes a queued spin lock. The driver allocates the **KLOCK_QUEUE_HANDLE** structure, and passes it to [**KeAcquireInStackQueuedSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquireinstackqueuedspinlock) and [**KeAcquireInStackQueuedSpinLockAtDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquireinstackqueuedspinlockatdpclevel) to acquire the queued spin lock. Those routines initialize the structure to represent the queued spin lock. The driver passes the structure to [**KeReleaseInStackQueuedSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleaseinstackqueuedspinlock) and [**KeReleaseInStackQueuedSpinLockFromDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleaseinstackqueuedspinlockfromdpclevel) when releasing the spin lock.

For more information, see [Queued Spin Locks](queued-spin-locks.md).

Header: *Wdm.h*. Include: *Wdm.h*, *Ntddk.h*, *Ntifs.h*.

## KTIMER

The **KTIMER** structure is an opaque structure that represents a timer object. Don't set the members of this structure directly. For more information, see [Timer Objects and DPCs](timer-objects-and-dpcs.md).

Header: *Wdm.h*. Include: *Wdm.h*, *Ntddk.h*, *Ntifs.h*.

## LOOKASIDE_LIST_EX

The **LOOKASIDE_LIST_EX** structure describes a lookaside list.

``` syntax
typedef struct _LOOKASIDE_LIST_EX {
  ...  // opaque
} LOOKASIDE_LIST_EX, *PLOOKASIDE_LIST_EX;
```

A lookaside list is a pool of fixed-size buffers that the driver can manage locally to reduce the number of calls to system allocation routines, which improves performance. The buffers are of uniform size and are stored as entries in the lookaside list.

Drivers should treat the **LOOKASIDE_LIST_EX** structure as opaque. Drivers that access structure members or that have dependencies on the locations of these members might not remain portable and interoperable with other drivers.

The [Related articles](#related-articles) section contains a list of the routines that use this structure.

For more information about lookaside lists, see [Using Lookaside Lists](using-lookaside-lists.md).

On 64-bit platforms, this structure must be 16-byte aligned.

Supported starting with Windows Vista.

Header: *Wdm.h*. Include: *Wdm.h*, *Ntddk.h*, *Ntifs.h*.

## NPAGED_LOOKASIDE_LIST

The **NPAGED_LOOKASIDE_LIST** structure is an opaque structure that describes a lookaside list of fixed-size buffers allocated from nonpaged pool. The system creates new entries and destroys unused entries on the list as necessary. For fixed-size buffers, using a lookaside list is quicker than allocating memory directly.

Use [**ExInitializeNPagedLookasideList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinitializenpagedlookasidelist) to initialize the lookaside list. Use [**ExAllocateFromNPagedLookasideList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatefromnpagedlookasidelist) to allocate a buffer from the list, and [**ExFreeToNPagedLookasideList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exfreetonpagedlookasidelist) to return a buffer to the list.

Drivers must always explicitly free any lookaside lists they create before unloading. It's a serious programming error to do otherwise. Use [**ExDeleteNPagedLookasideList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exdeletenpagedlookasidelist) to free the list.

Drivers can also use lookaside lists for paged pool. Starting with Windows 2000, a **PAGED_LOOKASIDE_LIST** structure describes a lookaside list that contains paged buffers. Starting in Windows Vista, a **LOOKASIDE_LIST_EX** structure can describe a lookaside list that contains either paged or nonpaged buffers. For more information, see [Using Lookaside Lists](using-lookaside-lists.md).

On 64-bit platforms, this structure must be 16-byte aligned.

Supported starting with Windows 2000.

Header: *Wdm.h*. Include: *Wdm.h*, *Ntddk.h*, *Ntifs.h*.

## OBJECT_TYPE

**OBJECT_TYPE** is an opaque structure that specifies the object type of a handle. For more information, see [**ObReferenceObjectByHandle**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obreferenceobjectbyhandle).

Header: *Wdm.h*. Include: *Wdm.h*, *Ntddk.h*, *Ntifs.h*.

## PAGED_LOOKASIDE_LIST

The **PAGED_LOOKASIDE_LIST** structure is an opaque structure that describes a lookaside list of fixed-size buffers allocated from paged pool. The system creates new entries and destroys unused entries on the list as necessary. For fixed-size buffers, using a lookaside list is quicker than allocating memory directly.

Use [**ExInitializePagedLookasideList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinitializepagedlookasidelist) to initialize the lookaside list. Use [**ExAllocateFromPagedLookasideList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatefrompagedlookasidelist) to allocate a buffer from the list, and [**ExFreeToPagedLookasideList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exfreetopagedlookasidelist) to return a buffer to the list.

Drivers must always explicitly free any lookaside lists they create before unloading. It's a serious programming error to do otherwise. Use [**ExDeletePagedLookasideList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exdeletepagedlookasidelist) to free the list.

Drivers can also use lookaside lists for nonpaged pool. Starting with Windows 2000, an **NPAGED_LOOKASIDE_LIST** structure describes a lookaside list that contains nonpaged buffers. Starting with Windows Vista, a **LOOKASIDE_LIST_EX** structure can describe a lookaside list that contains either paged or nonpaged buffers. For more information, see [Using Lookaside Lists](using-lookaside-lists.md).

On 64-bit platforms, this structure must be 16-byte aligned.

Supported starting with Windows 2000.

Header: *Wdm.h*. Include: *Wdm.h*, *Ntddk.h*, *Ntifs.h*.

## RTL_BITMAP

The **RTL_BITMAP** structure is an opaque structure that describes a bitmap.

``` syntax
typedef struct _RTL_BITMAP {
  // opaque
} RTL_BITMAP, *PRTL_BITMAP;
```

Don't directly access the members of this structure. Drivers that have dependencies on member locations or that access member values directly might not remain compatible with future versions of the Windows operating system.

The **RTL_BITMAP** structure serves as a header for a general-purpose, one-dimensional bitmap of arbitrary length. A driver can use such a bitmap as an economical way to keep track of a set of reusable items. For example, a file system can use bitmaps to track which clusters and sectors on a hard disk have already been allocated to hold file data.

For a list of the **Rtl*Xxx*** routines that use **RTL_BITMAP** structures, see the [Related articles](#related-articles) section. The caller of these **Rtl*Xxx*** routines is responsible for allocating the storage for the **RTL_BITMAP** structure and for the buffer that contains the bitmap. This buffer must begin on a four-byte boundary in memory and must be a multiple of four bytes in length. The bitmap begins at the start of the buffer but can contain any number of bits that fit in the allocated buffer.

Before supplying an **RTL_BITMAP** structure as a parameter to an **Rtl*Xxx*** routine, call the [**RtlInitializeBitMap**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlinitializebitmap) routine to initialize the structure. The input parameters to this routine are a pointer to a buffer that contains the bitmap, and the size, in bits, of the bitmap. **RtlInitializeBitMap** doesn't change the contents of this buffer.

If the caller allocates the storage for the **RTL_BITMAP** structure and bitmap in paged memory, the caller must be running at IRQL <= APC_LEVEL when it passes a pointer to this structure as a parameter to any of the **Rtl*Xxx*** routines listed in the [Related articles](#related-articles) section. If the caller allocates the storage from nonpaged memory (or, equivalently, from locked paged memory), the caller can be running at any IRQL when it calls the **Rtl*Xxx*** routine.

Supported in Windows 2000 and later versions of Windows.

Header: *Wdm.h*. Include: *Wdm.h*, *Ntddk.h*, *Ntifs.h*.

## RTL_RUN_ONCE

The **RTL_RUN_ONCE** structure is an opaque structure that stores the information for a one-time initialization.

Drivers must initialize this structure by calling the [**RtlRunOnceInitialize**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-rtlrunonceinitialize) routine before passing it to any other **RtlRunOnce*Xxx*** routines.

Available on Windows Vista and later versions of the Windows operating system.

Header: Ntddk.h. Include: Ntddk.h.

## SECURITY_SUBJECT_CONTEXT

The **SECURITY_SUBJECT_CONTEXT** structure is an opaque structure that represents the security context within which a particular operation is taking place. Drivers must not modify or try to directly access any members of this structure to make security decisions. Instead, to avoid security issues in authorization, pass this opaque structure in calls to [**SeAccessCheck**](/windows-hardware/drivers/wdm/nf-wdm-seaccesscheck) or [**SePrivilegeCheck**](/windows-hardware/drivers/ntifs/nf-ntifs-seprivilegecheck).

Header: *Wdm.h*. Include: *Wdm.h*, *Ntddk.h*, *Ntifs.h*.

## SLIST_HEADER

An **SLIST_HEADER** structure is an opaque structure that serves as the header for a sequenced singly linked list. For more information, see [Singly and Doubly Linked Lists](singly-and-doubly-linked-lists.md).

On 64-bit platforms, **SLIST_HEADER** structures must be 16-byte aligned.

Header: *Wdm.h*. Include: *Wdm.h*, *Ntddk.h*, *Ntifs.h*.

## XSTATE_SAVE

The **XSTATE_SAVE** structure is an opaque structure that describes the extended processor state information that a kernel-mode driver saves and restores.

``` syntax
typedef struct _XSTATE_SAVE {
  ...  // opaque
} XSTATE_SAVE, *PXSTATE_SAVE;
```

All members are opaque.

The [**KeSaveExtendedProcessorState**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesaveextendedprocessorstate) and [**KeRestoreExtendedProcessorState**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kerestoreextendedprocessorstate) routines use this structure.

Supported in Windows 7 and later versions of the Windows operating system.

Header: *Wdm.h*. Include: *Wdm.h*, *Ntddk.h*, *Ntifs.h*.

## Related articles

[**ExAcquireFastMutex**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exacquirefastmutex)  

[**ExAcquireFastMutexUnsafe**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exacquirefastmutexunsafe)  

[**ExAllocateFromLookasideListEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatefromlookasidelistex)  

[**ExAllocateFromNPagedLookasideList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatefromnpagedlookasidelist)  

[**ExAllocateFromPagedLookasideList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatefrompagedlookasidelist)  

[**ExAllocateTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatetimer)  

[**ExDeletePagedLookasideList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exdeletepagedlookasidelist)  

[**ExFreeToPagedLookasideList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exfreetopagedlookasidelist)  

[**ExInitializePagedLookasideList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinitializepagedlookasidelist)  

[**ExCancelTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-excanceltimer)  

[**ExDeleteLookasideListEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exdeletelookasidelistex)  

[**ExDeleteNPagedLookasideList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exdeletenpagedlookasidelist)  

[**ExDeleteTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exdeletetimer)  

[**ExFlushLookasideListEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exflushlookasidelistex)  

[**ExFreeToLookasideListEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exfreetolookasidelistex)  

[**ExFreeToNPagedLookasideList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exfreetonpagedlookasidelist)  

[**ExInitializeLookasideListEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinitializelookasidelistex)  

[**ExInitializeNPagedLookasideList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinitializenpagedlookasidelist)  

[**ExInitializeSListHead**](/windows-hardware/drivers/ddi/wdm/nf-wdm-initializeslisthead)  

[**ExInterlockedFlushSList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinterlockedflushslist)  

[**ExInterlockedPopEntrySList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinterlockedpopentryslist)  

[**ExInterlockedPushEntrySList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinterlockedpushentryslist)  

[**ExQueryDepthSList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exquerydepthslist)  

[**ExReleaseFastMutex**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exreleasefastmutex)  

[**ExReleaseFastMutexUnsafe**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exreleasefastmutexunsafe)  

[**ExSetTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exsettimer)  

[**ExTryToAcquireFastMutex**](/windows-hardware/drivers/ddi/wdm/nf-wdm-extrytoacquirefastmutex)  

[*ExTimerCallback*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ext_callback)  

[**IoAllocateWorkItem**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateworkitem)  

[**IoConnectInterruptEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioconnectinterruptex)  

[**IoCsqInitialize**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocsqinitialize)  

[**IoCsqInitializeEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocsqinitializeex)  

[**IoCsqInsertIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocsqinsertirp)  

[**IoCsqInsertIrpEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocsqinsertirpex)  

[**IoCsqRemoveIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocsqremoveirp)  

[**IoDisconnectInterruptEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iodisconnectinterruptex)  

[**IoFreeWorkItem**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iofreeworkitem)  

[**IoInitializeWorkItem**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioinitializeworkitem)  

[**IoRequestDpc**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iorequestdpc)  

[**IoUninitializeWorkItem**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iouninitializeworkitem)  

[**KeAcquireGuardedMutex**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquireguardedmutex)  

[**KeAcquireGuardedMutexUnsafe**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquireguardedmutexunsafe)  

[**KeAcquireInStackQueuedSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquireinstackqueuedspinlock)  

[**KeAcquireInStackQueuedSpinLockAtDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquireinstackqueuedspinlockatdpclevel)  

[**KeAcquireInterruptSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquireinterruptspinlock)  

[**KeCancelTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kecanceltimer)  

[**KeInitializeCallbackRecord**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializecallbackrecord)  

[**KeInitializeGuardedMutex**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializeguardedmutex)  

[**KeInitializeTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializetimer)  

[**KeInitializeTimerEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializetimerex)  

[**KeReadStateTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereadstatetimer)  

[**KeRestoreExtendedProcessorState**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kerestoreextendedprocessorstate)  

[**KeSaveExtendedProcessorState**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesaveextendedprocessorstate)  

[**KeSetTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesettimer)  

[**KeSetTimerEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesettimerex)  

[**KeDeregisterBugCheckCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kederegisterbugcheckcallback)  

[**KeDeregisterBugCheckReasonCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kederegisterbugcheckreasoncallback)  

[**KeInsertQueueDpc**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinsertqueuedpc)  

[**KeRegisterBugCheckCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keregisterbugcheckcallback)  

[**KeRegisterBugCheckReasonCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keregisterbugcheckreasoncallback)  

[**KeReleaseGuardedMutexUnsafe**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleaseguardedmutexunsafe)  

[**KeReleaseInStackQueuedSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleaseinstackqueuedspinlock)  

[**KeReleaseInStackQueuedSpinLockFromDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleaseinstackqueuedspinlockfromdpclevel)  

[**KeReleaseInterruptSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleaseinterruptspinlock)  

[**KeRestoreFloatingPointState**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kerestorefloatingpointstate)  

[**KeSaveFloatingPointState**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesavefloatingpointstate)  

[**KeSynchronizeExecution**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesynchronizeexecution)  

[*LookasideListAllocateEx*](/windows-hardware/drivers/ddi/wdm/nc-wdm-allocate_function_ex)  

[*LookasideListFreeEx*](/windows-hardware/drivers/ddi/wdm/nc-wdm-free_function_ex)  

[**ObReferenceObjectByHandle**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obreferenceobjectbyhandle)  

[**PsGetCurrentProcess**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentprocess)  

[**PsGetProcessCreateTimeQuadPart**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-psgetprocesscreatetimequadpart)  

[**PsInitialSystemProcess**](mm64bitphysicaladdress.md)  

[**PsIsSystemThread**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-psissystemthread)  

[Reading Bug Check Callback Data](../debugger/reading-bug-check-callback-data.md)

[**RtlRunOnceBeginInitialize**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-rtlrunoncebegininitialize)  

[**RtlRunOnceComplete**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-rtlrunoncecomplete)  

[**RtlRunOnceExecuteOnce**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-rtlrunonceexecuteonce)  

[**RtlRunOnceInitialize**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-rtlrunonceinitialize)  

[*RunOnceInitialization*](/windows-hardware/drivers/ddi/ntddk/nc-ntddk-rtl_run_once_init_fn)  

[Run-Down Protection](run-down-protection.md)  

[**SeAccessCheck**](/windows-hardware/drivers/ddi/wdm/nf-wdm-seaccesscheck)  

[**SeAssignSecurity**](/windows-hardware/drivers/ddi/wdm/nf-wdm-seassignsecurity)  

[**SeAssignSecurityEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-seassignsecurityex)
