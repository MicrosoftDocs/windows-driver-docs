---
title: Bug Check 0x1A MEMORY_MANAGEMENT
description: The MEMORY_MANAGEMENT bug check has a value of 0x0000001A. This indicates that a severe memory management error occurred.
keywords: ["Bug Check 0x1A MEMORY_MANAGEMENT", "MEMORY_MANAGEMENT"]
ms.date: 02/04/2020
topic_type:
- apiref
api_name:
- MEMORY_MANAGEMENT
api_type:
- NA
ms.localizationpriority: high 
---

# Bug Check 0x1A: MEMORY\_MANAGEMENT

The MEMORY\_MANAGEMENT bug check has a value of 0x0000001A. This indicates that a severe memory management error occurred.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## MEMORY\_MANAGEMENT Parameters

Parameter 1 identifies the exact violation.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 1</th>
<th align="left">Cause of Error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x1</p></td>
<td align="left"><p>The fork clone block reference count is corrupt. This only occurs on checked builds of Windows. Checked builds were available on older versions of Windows, before Windows 10 version 1803.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x31</p></td>
<td align="left"><p>The image relocation fix-up table or code stream has been corrupted. This is probably a hardware error.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x3f</p></td>
<td align="left"><p>An inpage operation failed with a CRC error. Parameter 2 contains the pagefile offset. Parameter 3 contains the page CRC value. Parameter 4 contains the expected CRC value.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x403</p></td>
<td align="left"><p>The page table and PFNs are out of sync . This is probably a hardware error, especially if parameters 3 & 4 differ by only a single bit.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x404</p></td>
<td align="left"><p>In the process of deleting a system page there was an inconsistency between the Page Frame Number (PFN) and the current Page Table Entry (PTE) pointer. Parameter 2 is the expected PTE. Parameter 3 is the PTE contents and parameter 4 is the PFN’s PTE.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x411</p></td>
<td align="left"><p>A page table entry (PTE) has been corrupted. Parameter 2 is the address of the PTE.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x777</p></td>
<td align="left"><p>The caller is unlocking a system cache address that is not currently locked. (This address was either never mapped or is being unlocked twice.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x778</p></td>
<td align="left"><p>The system is using the very last system cache view address, instead of preserving it.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x780</p>
<p>0x781</p></td>
<td align="left"><p>The PTEs mapping the argument system cache view have been corrupted.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1000</p></td>
<td align="left"><p>A caller of <strong>MmGetSystemAddressForMdl*</strong> tried to map a fully-cached physical page as non-cached. This action would cause a conflicting hardware translation buffer entry, and so it was refused by the operating system. Since the caller specified "bug check on failure" in the requesting MDL, the system had no choice but to issue a bug check in this instance.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1010</p></td>
<td align="left"><p>The caller is unlocking a pageable section that is not currently locked. (This section was either never locked or is being unlocked twice.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1233</p></td>
<td align="left"><p>A driver tried to map a physical memory page that was not locked. This is illegal because the contents or attributes of the page can change at any time. This is a bug in the code that made the mapping call. Parameter 2 is the page frame number of the physical page that the driver attempted to map.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1234</p></td>
<td align="left"><p>The caller is trying lock a nonexistent pageable section.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1235</p></td>
<td align="left"><p>The caller is trying to protect an MDL with an invalid mapping.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1236</p></td>
<td align="left"><p>The caller specified an MDL that contains an unlocked (or invalid) physical page. Parameter 2 contains a pointer to the MDL. Parameter 3 contains a pointer to the invalid PFN. Parameter 4 contains the invalid PFN value.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1240</p></td>
<td align="left"><p>It is illegal for callers to build an MDL for a virtual address range that is not resident. Parameter 2 is the Memory Descriptor List (MDL) and Parameter 3 is  the PTE pointer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1241</p></td>
<td align="left"><p>The virtual address for the MDL was unexpectedly asynchronously unmapped midway through the call to build the MDL. Parameter 2 is the MDL, Parameter 3 is  the PTE pointer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x3300</p></td>
<td align="left"><p>In the process of performing a write, the referenced virtual address is mistakenly marked as copy on write. Parameter 2 is the FaultingAddress.  Parameter 3 is the PTE contents. Parameter 4 indicates the virtual address space type.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x3451</p></td>
<td align="left"><p>The PTEs of a kernel thread stack that has been swapped out are corrupted.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x3453</p></td>
<td align="left"><p>All the page table pages of an exited process could not be deleted due to outstanding references.  This typically indicates corruption in the process’ page table structures.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x3470</p></td>
<td align="left"><p>A cached kernel stack was corrupted while on the freelist – this memory corruption indicates a serious problem of which the calling stack may be a victim or a culprit. Parameter 2 is Virtual Address (VA), Parameter 3 is the VA Cookie.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x4477</p></td>
<td align="left"><p>A driver tried to write to an unallocated address in the user space of the system process. Parameter 2 contains the address of the attempted write.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x5003</p></td>
<td align="left"><p>The working set free list is corrupt. This is probably a hardware error.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x5100</p></td>
<td align="left"><p>The allocation bitmap is corrupt. The memory manager is about to overwrite a virtual address that was already in use.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x5200</p></td>
<td align="left"><p>A page on a free pool SLIST has been corrupted. This can be the result of a write-after-free bug in a driver, or an overrun from a previous page. Parameter 2 contains the address of a free pool block. Parameter 4 contains the value that was expected to be at that address. Parameter 3 contains the actual value that was found.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x5305</p></td>
<td align="left"><p>The caller is specifying an invalid pool address (parameter 2) to free. Parameter 2 is  Virtual Address (VA) being evaluated, Parameter 3 is the region size.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x6001</p></td>
<td align="left"><p>The memory store component’s private memory range is corrupted, causing it to become inaccessible. Parameter 2 is the returned status.  Parameter 3 is the virtual address in the store’s private memory range. Parameter 4 is the MemoryDescriptorList.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x8884</p><p>0x8885</p><p>0x8886</p><p>0x8887</p></td>
<td align="left"><p>(Windows 7 and later). Two pages on the standby list that were supposed to have identical page priority values do not, in fact, have identical page priority values. The differing values are captured in parameter 4.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x8888</p><p>0x8889</p></td>
<td align="left"><p>Internal memory management structures are corrupted.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x888A</p></td>
<td align="left"><p>Internal memory management structures (likely the PTE or PFN) are corrupted.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x9696</p></td>
<td align="left"><p>A PFN (parameter 2) was encountered with a corrupted linkage no longer connected to its top level process.  This indicates corruption in the PFN structures.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x15000</p></td>
<td align="left"><p>The caller is supplying either the wrong address or is calling this routine in the wrong process context.  Both are illegal because we cannot unsecure a range we cannot find due to this error. Parameter 2 is the Virtual Address (VA) being evaluated.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x15001</p></td>
<td align="left"><p>An error occurred In the process of un-securing memory that was previously secured.  This can happen when the caller mistakenly invoked  MmUnsecureVirtualMemory in the wrong process context.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x41201</p></td>
<td align="left"><p>In the process of querying a virtual address, there was an inconsistency between the Page Frame Number(PFN) and the current Page Table Entry (PTE) pointer. Parameter 2 is the corresponding PTE. Parameter 3 is the PTE contents and parameter 4 is the virtual address descriptor.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x41202</p></td>
<td align="left"><p>In the process of determining  the page protection of a non-zero PTE, it was determined that the PTE is corrupt.  Parameter 2 is the PTE pointer, Parameter 3 is the PTE contents and Parameter 4 is Virtual Address Descriptor (VAD).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x41283</p></td>
<td align="left"><p>The working set index encoded in the PTE is corrupted.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x41284</p></td>
<td align="left"><p>A PTE or the working set list is corrupted.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x41286</p></td>
<td align="left"><p>The caller is trying to free an invalid pool address.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x41785</p></td>
<td align="left"><p>The working set list is corrupted.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x41287</p></td>
<td align="left"><p>An illegal page fault occurred while holding working set synchronization. Parameter 2 contains the referenced virtual address.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x41790</p></td>
<td align="left"><p>A page table page has been corrupted. On a 64 bit version of Windows, parameter 2 contains the address of the PFN for the corrupted page table page. On a 32 bit version of Windows, parameter 2 contains a pointer to the number of used PTEs, and parameter 3 contains the number of used PTEs.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x41792</p></td>
<td align="left"><p>A corrupted PTE has been detected. Parameter 2 contains the address of the PTE. Parameters 3/4 contain the low/high parts of the PTE.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x41793</p></td>
<td align="left"><p> A page table page has been corrupted. Parameter 2 contains a pointer to the last processed PTE. Parameter 3 contains the number of non-zero PTEs found. Parameter 4 contains the expected number of non-zero PTEs in the page table.</p><p>This memory parameter has been deprecated and is no longer available after Windows 10 version 1803.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x61940</p></td>
<td align="left"><p>A PDE has been unexpectedly invalidated.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x61941</p></td>
<td align="left"><p>The paging hierarchy is corrupt. Parameter 2 is a pointer to the virtual address which caused the fault.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x61946</p></td>
<td align="left"><p>The MDL being created is flawed. This almost always means the driver calling <strong>MmProbeAndLockPages</strong> is at fault. Typically the driver is attempting to create a Write MDL when it is being asked to process a paging Read.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x61948</p></td>
<td align="left"><p>In the process of decrementing the reference counts for an I/O space region, its accounting node could not be found.  Typically this means the argument range was never locked or has already been unlocked.  Parameter 2 is the base I/O frame. Parameter 3 is the number of pages in the region, and parameter 4 is the specific I/O frame whose node could not be found.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x61949</p></td>
<td align="left"><p>The IoPageFrameNode is null. Parameter 2 is PageFrameIndex.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x6194A</p></td>
<td align="left"><p>An error occurred when decrementing the reference counts on I/O space physical pages which are being unmapped. An entry which is not currently referenced is being dereferenced.  Parameter 2 and 3 describe the caller’s I/O space range being unmapped, and parameter 4 is the I/O space physical page which is expected to be referenced but is not. </p></td>
</tr>
<tr class="even">
<td align="left"><p>0x03030303</p></td>
<td align="left"><p>The boot loader is broken. (This value applies only to Intel Itanium machines.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x03030308</p></td>
<td align="left"><p>The range to remove (or truncate) is in use by the loader so it cannot be safely removed, so the system must issue a stop code.  Parameter 2 is HighestPhysicalPage.</p></td>
</tr>
</tbody>
</table>

## Resolution

The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.

Running the Windows Memory Diagnostic tool could be useful as well to exclude any kind of problem affecting the physical memory modules.
