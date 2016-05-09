---
title: Pool Allocation and Free Routines
author: windows-driver-content
description: Pool Allocation and Free Routines
ms.assetid: 757eebc0-ebd4-49a1-acea-6c27956b4b23
keywords: ["RDBSS WDK file systems , pool allocations", "Redirected Drive Buffering Subsystem WDK file systems , pool allocations", "pool allocations WDK RDBSS", "RDBSS WDK file systems , free routines", "Redirected Drive Buffering Subsystem WDK file systems , free routines", "free routines WDK RDBSS"]
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
<td align="left"><p>[<strong>_RxAllocatePoolWithTag</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557355)</p></td>
<td align="left"><p>This routine allocates memory from a pool with a four-byte tag at the beginning of the block that can help catch memory problems.</p>
<p>It is recommended that the <strong>RxAllocatePoolWithTag</strong> macro be called instead of using this routine directly.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>_RxCheckMemoryBlock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557358)</p></td>
<td align="left"><p>This routine checks a memory block for a special RX_POOL_HEADER header signature. Note that a network mini-redirector driver would need to add this special signature block to memory allocated in order to use the routine.</p>
<p>This routine should not be used since this special header block has not been implemented.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>_RxFreePool</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557363)</p></td>
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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Pool%20Allocation%20and%20Free%20Routines%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


