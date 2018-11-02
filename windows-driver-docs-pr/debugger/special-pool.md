---
title: Special Pool
description: Special Pool
ms.assetid: 8904913d-78ed-4e5f-acef-3c21eeb87b8d
keywords: ["Special Pool", "Special Pool, overview", "GFlags, Special Pool"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Special Pool


The **Special Pool** feature configures Windows to request memory allocations from a reserved memory pool when the memory is allocated with a specified pool tag or is within a specified size range.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>spp</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>(None)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>(None)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>System-wide registry entry</p>
<p>(Windows Vista and later) System-wide registry entry, kernel flag</p></td>
</tr>
</tbody>
</table>

 

### <span id="selecting_a_pool_tag"></span><span id="SELECTING_A_POOL_TAG"></span>Selecting a Pool Tag

When requesting special pool for a particular pool tag, make sure that your driver or other kernel-mode program uses a unique pool tag.

Also, when creating a pool tag (such as by using **ExAllocatePoolWithTag**), consider entering the tag characters in reverse order. For example, if the tag is **Fred**, consider entering it as **derF** (0x64657246). Pool tags are stored in the registry and displayed in the debugger and other tools in reverse (lower endian) order. If you enter them in reverse order, they are displayed in forward order (0x46726564)

If you suspect that your driver is consuming all of the special pool, consider using multiple pool tags in your code. You can then test your driver several times, assigning special pool to one pool tag in each test.

Also, select a pool tag with a hexadecimal value that is greater than the page size of the system. For kernel mode code, if you enter a pool tag that has a value less than PAGE\_SIZE, Gflags requests special pool for all allocations whose size is within the corresponding range and requests special pool for allocations with an equivalent pool tag. For example, if you select a size of **30**, special pool will be used for all allocations between 17 and 32 bytes in size, and for allocations with the pool tag 0x0030.

### <span id="selecting_an_allocation_size"></span><span id="SELECTING_AN_ALLOCATION_SIZE"></span>Selecting an Allocation Size

Use the following guidelines to select an allocation size for the Special Pool feature.

On a computer with an x86 processor, PAGE\_SIZE is 0x1000 and the allocation size ranges are 8 bytes in length. To configure the Special Pool feature for all allocations with sizes in this range, enter a number equal to the maximum of this range plus 8. (This number is always a multiple of 8.) The following table illustrates these values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Size range</th>
<th align="left">Enter this number</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1 to 8 bytes</p></td>
<td align="left"><p>10 (decimal 16)</p></td>
</tr>
<tr class="even">
<td align="left"><p>9 to 16 bytes</p></td>
<td align="left"><p>18 (decimal 24)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>17 to 24 bytes</p></td>
<td align="left"><p>20 (decimal 32)</p></td>
</tr>
<tr class="even">
<td align="left"><p>...</p></td>
<td align="left"><p>...</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xFE9 to 0xFF0 bytes</p></td>
<td align="left"><p>FF8 (decimal 4088)</p></td>
</tr>
</tbody>
</table>

 

On a computer with an AMD x86-64 processor, PAGE\_SIZE is 0x1000 and the allocation size ranges are 16 bytes in length. To configure the Special Pool feature for all allocations with sizes in this range, enter a number equal to the maximum of this range plus 16. (This number is always a multiple of 16.) The following table illustrates these values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Size range</th>
<th align="left">Enter this number</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1 to 16 bytes</p></td>
<td align="left"><p>20 (decimal 32)</p></td>
</tr>
<tr class="even">
<td align="left"><p>17 to 32 bytes</p></td>
<td align="left"><p>30 (decimal 48)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>33 to 48 bytes</p></td>
<td align="left"><p>40 (decimal 64)</p></td>
</tr>
<tr class="even">
<td align="left"><p>...</p></td>
<td align="left"><p>...</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xFD1 to 0xFE0 bytes</p></td>
<td align="left"><p>FF0 (decimal 4080)</p></td>
</tr>
</tbody>
</table>

 

On a computer with any processor, you can use an asterisk ( **\\*** ) or 0x2A (decimal 42) to configure the Special Pool feature for all memory allocations on the system.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

For information about configuring the Special Pool feature in the Global Flags Dialog Box, see [Configuring Special Pool](configuring-special-pool.md). For information about configuring the Special Pool feature at the command line, see [**GFlags Commands**](gflags-commands.md). For an example, see [Example 14: Configuring Special Pool](example-14---configuring-special-pool.md).

The Special Pool feature of Gflags directs Windows to request memory allocations from a reserved memory pool when the memory is allocated with a specified pool tag or is within a specified size range. To request special pool for all allocations by a particular driver, use Driver Verifier. For more information, see the "Special Pool" topic in the "Driver Verifier" section of the Windows Driver Kit (WDK).

The special pool features of Gflags and Driver Verifier help you to detect and identify the source of errors in kernel pool use, such as writing beyond the allocated memory space, or referring to memory that has already been freed.

Not all special pool requests are fulfilled. Each allocation from the special pool uses one page of nonpageable physical memory and two pages of virtual address space. If the special pool is exhausted, memory is allocated from the standard pool until the special pool becomes available again. When a special pool request is filled from the standard pool, the requesting function returns a success status. It does not return an error, because the allocation has succeeded, even though it was not filled from special pool.

The size of the special pool increases with the amount of physical memory on the system; ideally this should be at least 1 Gigabyte (GB). On x86 machines, because virtual (in addition to physical) space is consumed, do not use the **/3GB** boot option when using special pool. It is also a good idea to increase the pagefile minimum/maximum quantities by a factor of two or three.

You can also configure the Special Pool feature to align memory allocation to detect references to memory preceding the allocation ("underruns") or references to memory beyond the allocation ("overruns"). This feature is available only in the Global Flags dialog box on all versions of Windows. For details, see [Detecting Overruns and Underruns](detecting-overruns-and-underruns.md).

On Windows Vista and later versions of Windows, you can configure the Special Pool feature as a registry setting that requires a reboot, but remains effective until you change it, or as a kernel flag setting that does not require a reboot, but is effective only until you reboot or shut down Windows. In earlier versions of Windows, Special Pool is only available as a registry setting.

On Windows Vista and later versions of Windows, you can configure the Special Pool feature either by using the Global Flags dialog box or at the command line. In earlier version of Windows, this feature is available only in the Global Flags dialog box.

 

 





