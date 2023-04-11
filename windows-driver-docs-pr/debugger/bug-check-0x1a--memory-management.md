---
title: Bug Check 0x1A MEMORY_MANAGEMENT
description: The MEMORY_MANAGEMENT bug check has a value of 0x0000001A and indicates that a severe memory management error occurred.
keywords: ["Bug check 0x1A MEMORY_MANAGEMENT", "MEMORY_MANAGEMENT"]
ms.date: 04/06/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- MEMORY_MANAGEMENT
api_type:
- NA
---

# Bug Check 0x1A: MEMORY\_MANAGEMENT

The MEMORY\_MANAGEMENT bug check has a value of 0x0000001A. The bug check indicates that a severe memory management error occurred.

> [!IMPORTANT]
> This article is for programmers. If you're a Microsoft customer and your computer displays a blue screen error code, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## MEMORY_MANAGEMENT parameters

Parameter 1 identifies the exact violation.

| Parameter 1 | Cause of error |
|-------------|----------------|
| 0x31 | The image relocation fix-up table or code stream has been corrupted. The error probably is a hardware error. |
| 0x3f | An inpage operation failed with a cyclic redundancy check (CRC) error. Parameter 2 contains the pagefile offset. Parameter 3 contains the page CRC value. Parameter 4 contains the expected CRC value. |
| 0x403 | The page table and page frame numbers (PFNs) are out of sync. The error probably is a hardware error, especially if parameters 3 and 4 differ by only one bit. |
| 0x404 | In the process of deleting a system page, an inconsistency between the PFN and the current page table entry (PTE) pointer was found. Parameter 2 is the expected PTE. Parameter 3 is the PTE contents. Parameter 4 is the PFN’s PTE. |
| 0x411 | A PTE has been corrupted. Parameter 2 is the address of the PTE. |
| 0x1010 | The caller is unlocking a pageable section that's not currently locked. (This section was either never locked or it's being unlocked twice.) |
| 0x1233 | A driver tried to map a physical memory page that wasn't locked. This action is illegal because the contents or attributes of the page can change at any time. A bug in the code made the mapping call. Parameter 2 is the PFN of the physical page that the driver attempted to map. |
| 0x1234 | The caller is trying to lock a nonexistent pageable section. |
| 0x1235 | The caller is trying to protect an MDL with an invalid mapping. |
| 0x1236 | The caller specified an MDL that contains an unlocked (or invalid) physical page. Parameter 2 contains a pointer to the MDL. Parameter 3 contains a pointer to the invalid PFN. Parameter 4 contains the invalid PFN value. |
| 0x1240 | It's illegal for callers to build an MDL for a virtual address range that isn't resident. Parameter 2 is the MDL. Parameter 3 is the PTE pointer. |
| 0x3300 | During a write action, the referenced virtual address is mistakenly marked as "copy on write". Parameter 2 is the value for `FaultingAddress`. Parameter 3 is the PTE contents. Parameter 4 indicates the virtual address space type. |
| 0x3451 | The PTEs of a kernel thread stack that has been swapped out are corrupted. |
| 0x3453 | Not all the page table pages of an exited process could be deleted because of outstanding references. This error typically indicates corrupted process page table structures. |
| 0x3470 | A cached kernel stack was corrupted while it was on the free list. This memory corruption indicates a serious problem, and the calling stack might be either a victim or a culprit. Parameter 2 is the virtual address. Parameter 3 is the virtual address cookie. |
| 0x4477 | A driver tried to write to an unallocated address in the user space of the system process. Parameter 2 contains the address of the attempted write. |
| 0x5100 | The allocation bitmap is corrupted. The memory manager is about to overwrite a virtual address that was already in use. |
| 0x5305 | The caller is specifying an invalid pool address (parameter 2) to free. Parameter 2 is the virtual address that's being evaluated. Parameter 3 is the region size. |
| 0x6001 | The memory store component’s private memory range is corrupted, so it has become inaccessible. Parameter 2 is the returned status.  Parameter 3 is the virtual address in the store's private memory range. Parameter 4 is the MDL. |
| 0x8886</br>0x8887 | (Windows 7 and later). Two pages on the standby list that were supposed to have identical page priority values don't have identical page priority values. The differing values are captured in parameter 4. |
| 0x8888</br>0x8889 | Internal memory management structures are corrupted. |
| 0x888A | Internal memory management structures (likely the PTE or PFN) are corrupted. |
| 0x9696 | A PFN (parameter 2) was encountered with a corrupted linkage that's no longer connected to its top-level process. This error indicates corrupted PFN structures. |
| 0x15000 | The caller is either supplying the wrong address or calling this routine in the wrong process context. Both actions are illegal because we can't unsecure a range that we can't find due to this error. Parameter 2 is the virtual address that's being evaluated. |
| 0x15001 | An error occurred in the process of unsecuring memory that previously was secured. This error might happen if the caller mistakenly invoked `MmUnsecureVirtualMemory` in the wrong process context. |
| 0x41202 | In the process of determining  the page protection of a non-zero PTE, it was determined that the PTE is corrupted. Parameter 2 is the PTE pointer. Parameter 3 is the PTE contents. Parameter 4 is the virtual address descriptor. |
| 0x41286 | The caller is trying to free an invalid pool address. |
| 0x41785 | The working set list is corrupted. |
| 0x41287 | An illegal page fault occurred while holding working set synchronization. Parameter 2 contains the referenced virtual address. |
| 0x41790 | A page table page has been corrupted. On a 64-bit version of Windows, parameter 2 contains the address of the PFN for the corrupted page table page. On a 32-bit version of Windows, parameter 2 contains a pointer to the number of used PTEs, and parameter 3 contains the number of used PTEs. |
| 0x41792 | A corrupted PTE has been detected. Parameter 2 contains the address of the PTE. Parameters 3 and 4 contain the low and high parts of the PTE. |
| 0x61941 | The paging hierarchy is corrupted. Parameter 2 is a pointer to the virtual address that caused the fault. |
| 0x61948 | In the process of decrementing the reference counts for an I/O space region, the region's accounting node couldn't be found. Typically, this error means that the argument range was never locked or that it's already been unlocked.  Parameter 2 is the base I/O frame. Parameter 3 is the number of pages in the region. Parameter 4 is the specific I/O frame for which a node couldn't be found. |
| 0x61949 | The `IoPageFrameNode` value is null. Parameter 2 is `PageFrameIndex`. |
| 0x6194A | An error occurred while decrementing the reference counts on I/O space physical pages that are being unmapped. An entry that isn't currently referenced is being dereferenced. Parameters 2 and 3 describe the caller's I/O space range that's being unmapped. Parameter 4 is the I/O space physical page that's expected to be referenced, but which isn't referenced. |
| 0x03030308 | The range to remove (or truncate) is in use by the loader. It can't be safely removed, so the system must issue a stop code.  Parameter 2 is `HighestPhysicalPage`. |

These parameter 1 values were used in previous versions of Windows.

| Parameter 1 | Cause of error |
|-------------|----------------|
| 0x777 | The caller is unlocking a system cache address that's not currently locked. (The address was either never mapped or it's being unlocked twice.) |
| 0x778 | The system is using the last system cache view address instead of preserving it. |
| 0x780</br>0x781 | The PTEs that map the argument system cache view have been corrupted. |
| 0x1000 | A caller of `MmGetSystemAddressForMdl*` tried to map a fully cached physical page as non-cached. This action would cause a conflicting hardware translation buffer entry, so it was refused by the operating system. Because the caller specified "bug check on failure" in the requesting Memory Descriptor List (MDL), the system issued a bug check. |
| 0x1241 | The virtual address for the MDL was unexpectedly asynchronously unmapped during the call to build the MDL. Parameter 2 is the MDL. Parameter 3 is the PTE pointer. |
| 0x5003 | The working set free list is corrupted. It's probably a hardware error. |
| 0x5200 | A page on a free pool SLIST has been corrupted. This error might be the result of a write-after-free bug in a driver or an overrun from a previous page. Parameter 2 contains the address of a free pool block. Parameter 4 contains the value that was expected to be at that address. Parameter 3 contains the actual value that was found. |
| 0x8884</br>0x8885</br> | (Windows 7 and later). Two pages on the standby list that were supposed to have identical page priority values don't have identical page priority values. The differing values are captured in parameter 4. |
| 0x41201 | In the process of querying a virtual address, inconsistency between the PFN and the current PTE pointer was found. Parameter 2 is the corresponding PTE. Parameter 3 is the PTE contents. Parameter 4 is the virtual address descriptor. |
| 0x41283 | The working set index encoded in the PTE is corrupted. |
| 0x41284 | A PTE or the working set list is corrupted. |
| 0x41793 | A page table page has been corrupted. Parameter 2 contains a pointer to the last processed PTE. Parameter 3 contains the number of non-zero PTEs found. Parameter 4 contains the expected number of non-zero PTEs in the page table.</br>This memory parameter has been deprecated and is no longer available after Windows 10 version 1803. |
| 0x61940 | A PDE has been unexpectedly invalidated. |
| 0x61946 | The MDL that's being created is flawed. This error almost always means that the driver calling `MmProbeAndLockPages` is at fault. Typically, the driver is attempting to create a write MDL when it's being asked to process a paging read. |
| 0x03030303 | The boot loader is broken. (This value applies only to Intel Itanium machines.) |

## Resolution

The [!analyze](-analyze.md) debug extension displays information about the bug check. The information in the debug extension might help you identify the root cause.

You also might find it helpful to run the Windows Memory Diagnostic tool to check for problems that affect physical memory modules.

## See also

[Bug Check code reference](bug-check-code-reference2.md)
