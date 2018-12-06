---
title: Pool Allocation and Free Routines
description: Pool Allocation and Free Routines
ms.assetid: 757eebc0-ebd4-49a1-acea-6c27956b4b23
keywords:
- RDBSS WDK file systems , pool allocations
- Redirected Drive Buffering Subsystem WDK file systems , pool allocations
- pool allocations WDK RDBSS
- RDBSS WDK file systems , free routines
- Redirected Drive Buffering Subsystem WDK file systems , free routines
- free routines WDK RDBSS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Pool Allocation and Free Routines


## <span id="ddk_pool_allocation_and_free_functions_if"></span><span id="DDK_POOL_ALLOCATION_AND_FREE_FUNCTIONS_IF"></span>


RDBSS provides a number of routines to use for pool allocation. Normally, these routines are called using macros, not by calling these routines directly. The macros automatically handle the differences between retail and checked builds.

On a checked build, these routines were designed to add wrappers around the normal kernel allocation and free routines. These wrappers for pool allocation and free routines provide additional debugging information and call a set of routines that perform various kinds of checking and guarding before calling the kernel pool allocation and free routines. However, these features are not currently implemented in these allocation and free routines, but might be added in future releases.

On a free build, these routines become direct calls to the kernel allocation and free routines, [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520) and [**ExFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff544590).

The following table lists the RDBSS pool allocation and free routines.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Routine</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557355" data-raw-source="[&lt;strong&gt;_RxAllocatePoolWithTag&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557355)"><strong>_RxAllocatePoolWithTag</strong></a></p></td>
<td align="left"><p>This routine allocates memory from a pool with a four-byte tag at the beginning of the block that can help catch memory problems.</p>
<p>It is recommended that the <strong>RxAllocatePoolWithTag</strong> macro be called instead of using this routine directly.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557358" data-raw-source="[&lt;strong&gt;_RxCheckMemoryBlock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557358)"><strong>_RxCheckMemoryBlock</strong></a></p></td>
<td align="left"><p>This routine checks a memory block for a special RX_POOL_HEADER header signature. Note that a network mini-redirector driver would need to add this special signature block to memory allocated in order to use the routine.</p>
<p>This routine should not be used since this special header block has not been implemented.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557363" data-raw-source="[&lt;strong&gt;_RxFreePool&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557363)"><strong>_RxFreePool</strong></a></p></td>
<td align="left"><p>This routine frees a memory pool.</p>
<p>It is recommended that the <strong>RxFreePool</strong> macro be called instead of using this routine directly.</p></td>
</tr>
</tbody>
</table>

 

A number of macros, which are defined in the *ntrxdef.h* header file, call these routines. Instead of calling the routines listed in the previous table directly, the following macros are normally used.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Macro</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>RxAllocatePoolWithTag</strong> (<em>type</em>, <em>size</em>, <em>tag</em>)</p></td>
<td align="left"><p>On checked builds, this macro allocates memory from a pool with a four-byte tag at the beginning of the block that can help catch instances of memory trashing.</p>
<p>On retail builds, this macro becomes a direct call to <strong>ExAllocatePoolWithTag</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>RxCheckMemoryBlock</strong> (<em>ptr</em>)</p></td>
<td align="left"><p>On checked builds, this macro checks a memory block for a special RX_POOL_HEADER header signature.</p>
<p>On retail builds, this macro does nothing.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>RxFreePool</strong> (<em>ptr</em>)</p></td>
<td align="left"><p>On checked builds, this macro frees a memory pool.</p>
<p>On retail builds, this macro becomes a direct call to <strong>ExFreePool</strong>.</p></td>
</tr>
</tbody>
</table>

 

 

 




