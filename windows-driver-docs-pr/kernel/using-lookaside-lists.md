---
title: Using Lookaside Lists
description: Using Lookaside Lists
ms.assetid: 07a75b8b-04b9-48ea-bda4-53889dd661a9
keywords: ["memory management WDK kernel , lookaside lists", "lookaside lists WDK kernel", "fixed-size buffer allocations WDK kernel", "ExXxxLookasideList routines WDK", "entries WDK lookaside", "nonpaged lookaside lists WDK kernel", "paged lookaside lists WDK kernel", "Allocate routine WDK memory", "Free routine WDK memory"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using Lookaside Lists





Drivers that must allocate fixed-size buffers dynamically to perform on-demand I/O operations can use the **Ex*Xxx*LookasideListEx** or **Ex*Xxx*LookasideList** support routines. After such a driver initializes its lookaside list, the operating system will hold some number of dynamically allocated buffers of the given size in the driver's lookaside list, effectively reserving a set of reusable, fixed-size buffers for the driver. The format and contents of a driver's fixed-size buffers (also known as *entries*) in its lookaside list are driver-determined.

For example, storage class drivers that must set up SCSI request blocks (SRBs) for the underlying SCSI port/miniport drivers use lookaside lists. Such a class driver allocates buffers for SRBs on an as-needed basis from its lookaside list and releases each SRB buffer back to the lookaside list for the lookaside list to reuse whenever an SRB is returned to the class driver in a completed IRP. Because a storage class driver cannot predetermine how many SRBs it has to use at any time because I/O demand on the driver increases and falls, a lookaside list is a convenient and economical way to manage the allocation and deallocation of buffers for fixed-size SRBs in such a driver.

The operating system maintains state about all paged and nonpaged lookaside lists that are currently being used, dynamically tracking the demand for allocations and deallocations of entries in all lists, and available system pool for new entries. When demand for allocations is high, the operating system increases the number of entries it holds in each lookaside list. When demand falls again, it frees surplus lookaside entries back to system pool.

Lookaside lists are thread-safe. A lookaside list has built-in synchronization to enable multiple, concurrently running threads in a driver to share a lookaside list. These threads can safely allocate buffers from the shared lookaside list and free these buffers to the list without requiring the driver to explicitly synchronize these operations. However, to avoid possible leaks and data corruption, a set of threads that share a lookaside list must explictly synchronize the initialization and deletion of the list.

## Lookaside list interfaces


Starting with Windows Vista, the [**LOOKASIDE\_LIST\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff554329) structure describes a lookaside list that can contain either paged or nonpaged buffers. If a driver provides custom *Allocate* and *Free* routines for this lookaside list, these routines receive a private context as an input parameter. A driver can use this context to collect private data for the lookaside list. For example, the context might be used to count the number of list entries that are dynamically allocated and freed by the list. For a code example that shows how to use a context in this way, see [**ExInitializeLookasideListEx**](https://msdn.microsoft.com/library/windows/hardware/ff545298).

The following system-supplied routines support lookaside lists that are described by a **LOOKASIDE\_LIST\_EX** structure:

[**ExAllocateFromLookasideListEx**](https://msdn.microsoft.com/library/windows/hardware/ff544381)

[**ExDeleteLookasideListEx**](https://msdn.microsoft.com/library/windows/hardware/ff544563)

[**ExFlushLookasideListEx**](https://msdn.microsoft.com/library/windows/hardware/ff544587)

[**ExFreeToLookasideListEx**](https://msdn.microsoft.com/library/windows/hardware/ff544597)

[**ExInitializeLookasideListEx**](https://msdn.microsoft.com/library/windows/hardware/ff545298)

Starting with Windows 2000, the [**PAGED\_LOOKASIDE\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff558775) structure describes a lookaside list that contains paged buffers. If a driver provides custom *Allocate* and *Free* routines for this lookaside list, these routines do not receive a private context as an input parameter. For this reason, if your driver is intended to run only on Windows Vista and later versions of Windows, consider using the **LOOKASIDE\_LIST\_EX** structure instead of the **PAGED\_LOOKASIDE\_LIST** structure for your lookaside lists. The following system-supplied routines support lookaside lists that are described by a **PAGED\_LOOKASIDE\_LIST** structure:

[**ExAllocateFromPagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff544393)

[**ExDeletePagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff544570)

[**ExFreeToPagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff544605)

[**ExInitializePagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff545309)

Starting with Windows 2000, the [**NPAGED\_LOOKASIDE\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff556431) structure describes a lookaside list that contains nonpaged buffers. If a driver provides custom *Allocate* and *Free* routines for this lookaside list, these routines do not receive a private context as an input parameter. Again, if your driver is intended to run only on Windows Vista and later versions of Windows, consider using the **LOOKASIDE\_LIST\_EX** structure instead of the **NPAGED\_LOOKASIDE\_LIST** structure for your lookaside lists. The following system-supplied routines support lookaside lists that are described by an **NPAGED\_LOOKASIDE\_LIST** structure:

[**ExAllocateFromNPagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff544388)

[**ExDeleteNPagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff544566)

[**ExFreeToNPagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff544601)

[**ExInitializeNPagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff545301)

## Implementation guidelines


To implement a lookaside list that uses a **LOOKASIDE\_LIST\_EX** structure, follow these design guidelines:

-   Call **ExInitializeLookasideListEx** to set up a lookaside list. In this call, specify whether the entries in the lookaside list are to be paged or nonpaged buffers. Use nonpaged buffers if the driver itself or any underlying driver to which it passes its lookaside list entries might access these entries at IRQL &gt;= DISPATCH\_LEVEL. Use paged buffers only if accesses to the driver's lookaside list entries always occur at IRQL &lt;= APC\_LEVEL.

-   The **LOOKASIDE\_LIST\_EX** structure for the lookaside list must always reside in nonpaged system memory regardless of whether the entries in the list are paged or nonpaged.

-   For better performance, pass **NULL** pointers for the *Allocate* and *Free* parameters to **ExInitializeLookasideListEx** unless the allocation and deallocation routines must do more than merely allocate and free memory for lookaside list entries. For example, these routines might record information about the driver's usage of dynamically allocated buffers.

-   A driver-supplied *Allocate* routine can pass the input parameters (*PoolType*, *Tag*, and *Size*) that it receives directly to the [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520) or [**ExAllocatePoolWithQuotaTag**](https://msdn.microsoft.com/library/windows/hardware/ff544513) routine to allocate a new buffer.

-   For every call to **ExAllocateFromLookasideListEx**, make the reciprocal call to **ExFreeToLookasideListEx** as soon as possible whenever a previously allocated entry is no longer being used.

Supplying *Allocate* and *Free* routines that do nothing more than call [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520) and [**ExFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff544590), respectively, wastes processor cycles. **ExAllocateFromLookasideListEx** makes the necessary calls to **ExAllocatePoolWithTag** and **ExFreePool** automatically when a driver passes **NULL** *Allocate* and *Free* pointers to **ExInitializeLookasideListEx**.

Any driver-supplied *Allocate* routine must not allocate memory for an entry from paged pool to be held in a nonpaged lookaside list or vice versa. It must also allocate fixed-size entries, because any subsequent driver call to **ExAllocateFromLookasideListEx** returns the first entry currently held in the lookaside list unless the list is empty. That is, a call to **ExAllocateFromLookasideListEx** causes a call to the driver-supplied *Allocate* routine only if the given lookaside list is currently empty. Therefore, at each call to **ExAllocateFromLookasideListEx**, the returned entry will be exactly the size that the driver needs only if all entries in the lookaside list are of a fixed size. A driver-supplied *Allocate* routine should also not change the *Tag* value that the driver originally passed to **ExInitializeLookasideListEx**, because changes in the pool-tag value would make debugging and tracking the driver's memory usage more difficult.

Calls to **ExFreeToLookasideListEx** store previously allocated entries in the lookaside list unless the list is already *full* (that is, the list contains the system-determined maximum number of entries). For better performance, a driver should make a reciprocal call to **ExFreeToLookasideListEx** as quickly as it can for every call that it makes to **ExAllocateFromLookasideListEx**. When a driver frees entries back to its lookaside list quickly, that driver's next call to **ExAllocateFromLookasideListEx** is far less likely to incur the performance penalty of dynamically allocating memory for a new entry.

Similar guidelines apply to a lookaside list that uses a **PAGED\_LOOKASIDE\_LIST** or **NPAGED\_LOOKASIDE\_LIST** structure.

 

 




