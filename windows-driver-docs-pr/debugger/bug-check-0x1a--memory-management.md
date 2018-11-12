---
title: Bug Check 0x1A MEMORY_MANAGEMENT
description: The MEMORY_MANAGEMENT bug check has a value of 0x0000001A. This indicates that a severe memory management error occurred.
ms.assetid: 7d3ff54e-e61a-43fa-a378-fb8d32565586
keywords: ["Bug Check 0x1A MEMORY_MANAGEMENT", "MEMORY_MANAGEMENT"]
ms.author: domars
ms.date: 09/12/2018
topic_type:
- apiref
api_name:
- MEMORY_MANAGEMENT
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1A: MEMORY\_MANAGEMENT


The MEMORY\_MANAGEMENT bug check has a value of 0x0000001A. This indicates that a severe memory management error occurred.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## MEMORY\_MANAGEMENT Parameters


Parameter 1 is the only parameter of interest; this identifies the exact violation.

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
<td align="left"><p>The fork clone block reference count is corrupt. (This only occurs on checked builds of Windows.)</p></td>
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
<td align="left"><p>The page table and PFNs are out of sync . This is probably a hardware error, especially if parameters 3 &amp; 4 differ by only a single bit.</p></td>
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
<td align="left"><p>A caller of <strong>MmGetSystemAddressForMdl*</strong> tried to map a fully-cached physical page as non-cached. This action would cause a conflicting hardware translation buffer entry, and so it was refused by the operating system. Since the caller specified &quot;bug check on failure&quot; in the requesting MDL, the system had no choice but to issue a bug check in this instance.</p></td>
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
<tr class="odd">
<td align="left"><p>0x3451</p></td>
<td align="left"><p>The PTEs of a kernel thread stack that has been swapped out are corrupted.</p></td>
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
<td align="left"><p>0x8884</p></td>
<td align="left"><p>(Windows 7 only). Two pages on the standby list that were supposed to have identical page priority values do not, in fact, have identical page priority values. The differing values are captured in parameter 4.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x8888</p>
<p>0x8889</p></td>
<td align="left"><p>Internal memory management structures are corrupted.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x888A</p></td>
<td align="left"><p>Internal memory management structures (likely the PTE or PFN) are corrupted.</p></td>
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
<tr class="even">
<td align="left"><p>0x61949</p></td>
<td align="left"><p>The IoPageFrameNode is null. Parameter 2 is PageFrameIndex.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x03030303</p></td>
<td align="left"><p>The boot loader is broken. (This value applies only to Intel Itanium machines.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x03030308</p></td>
<td align="left"><p>The range to remove (or truncate) is in use by the loader so it cannot be safely removed, so the system must issue a stop code.  Parameter 2 is HighestPhysicalPage.</p></td>
</tr>
</tbody>
</table>

 

 

 




