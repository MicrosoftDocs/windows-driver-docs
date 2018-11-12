---
title: Using the Global Flags Utility
description: Using the Global Flags Utility
ms.assetid: 934272e9-867c-4eb4-8bc1-e65e5b3f2aeb
keywords:
- Global Flags utility
- Driver Verifier WDK , Global Flags utility
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using the Global Flags Utility


## <span id="ddk_using_the_global_flags_utility_tools"></span><span id="DDK_USING_THE_GLOBAL_FLAGS_UTILITY_TOOLS"></span>


The Global Flags (gflags.exe) utility provides a simple method of setting certain keys within the system registry, adjusting the kernel settings of the running system, and altering the settings for image files. You can set these keys by using a graphical or command-line interface.

The Global Flags utility can be found in the Windows Support Tools package and in the Debugging Tools for Windows package. For information about the latter, see [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063).

The Global Flags utility can also be used to configure the Special Pool option of Driver Verifier, or to designate the special pool for use in individual memory allocations.

To alter the Special Pool settings, start the Global Flags utility and select the **System Registry** option button in the **Destination** section. The **Kernel Special Pool Tag** section of the dialog box allows certain special pool options to be set.

### <span id="controlling_pool_tag_alignment"></span><span id="CONTROLLING_POOL_TAG_ALIGNMENT"></span>Controlling Pool Tag Alignment

Select the **Verify Start** option button to cause the special pool alignment to focus on underrun detection. Select the **Verify End** option to focus on overrun detection. These buttons control the alignment of all special pool assignments -- whether made by Driver Verifier or by Global Flags.

### <span id="using_special_pool_by_pool_tag_or_allocation_size"></span><span id="USING_SPECIAL_POOL_BY_POOL_TAG_OR_ALLOCATION_SIZE"></span>Using Special Pool by Pool Tag or Allocation Size

Special pool can be used for all allocations with a certain pool tag. To activate this feature, enter the pool tag into the **Pool Tag** text box.

Special pool can also be used for all allocations in a certain size range. Although this use of special pool does not involve pool tags, this feature is nonetheless activated by entering a number into the **Pool Tag** text box. This number must be less than PAGE\_SIZE.

For an x86 processor, PAGE\_SIZE is 0x1000 and the allocation size ranges are 8 bytes in length. To activate special pool for all allocations with sizes in this range, enter a number equal to the maximum of this range plus 8. (This number is always a multiple of 8.) The following table illustrates these values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Size range</th>
<th align="left">Enter this number in the Pool Tag text box</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1 to 8 bytes</p></td>
<td align="left"><p>16 (0x10)</p></td>
</tr>
<tr class="even">
<td align="left"><p>9 to 16 bytes</p></td>
<td align="left"><p>24 (0x18)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>17 to 24 bytes</p></td>
<td align="left"><p>32 (0x20)</p></td>
</tr>
<tr class="even">
<td align="left"><p>...</p></td>
<td align="left"><p>...</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xFE9 to 0xFF0 bytes</p></td>
<td align="left"><p>0xFF8</p></td>
</tr>
</tbody>
</table>

 

For an x64 processor, PAGE\_SIZE is 0x1000 and the allocation size ranges are 16 bytes in length. To activate special pool for all allocations with sizes in this range, enter a number equal to the maximum of this range plus 16. (This number is always a multiple of 16.) The following table illustrates these values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Size range</th>
<th align="left">Enter this number in the Pool Tag text box</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1 to 16 bytes</p></td>
<td align="left"><p>32 (0x20)</p></td>
</tr>
<tr class="even">
<td align="left"><p>17 to 32 bytes</p></td>
<td align="left"><p>48 (0x30)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>33 to 48 bytes</p></td>
<td align="left"><p>64 (0x40)</p></td>
</tr>
<tr class="even">
<td align="left"><p>...</p></td>
<td align="left"><p>...</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xFD1 to 0xFE0 bytes</p></td>
<td align="left"><p>0xFF0</p></td>
</tr>
</tbody>
</table>

 

For an Itanium-based processor, PAGE\_SIZE is 0x2000 and the allocation size ranges are 16 bytes in length. To activate special pool for all allocations with sizes in this range, enter a number equal to the maximum of this range plus 16. (This number is always a multiple of 16.) The following table illustrates these values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Size range</th>
<th align="left">Enter this number in the Pool Tag text box</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1 to 16 bytes</p></td>
<td align="left"><p>32 (0x20)</p></td>
</tr>
<tr class="even">
<td align="left"><p>17 to 32 bytes</p></td>
<td align="left"><p>48 (0x30)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>33 to 48 bytes</p></td>
<td align="left"><p>64 (0x40)</p></td>
</tr>
<tr class="even">
<td align="left"><p>...</p></td>
<td align="left"><p>...</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1FD1 to 0x1FE0 bytes</p></td>
<td align="left"><p>0x1FF0</p></td>
</tr>
</tbody>
</table>

 

It is best to avoid using pool tags lower than PAGE\_SIZE. For example, if you put 0x30 into this text box on an Itanium-based processor, special pool will be used for all allocations between 17 and 32 bytes in size, and for allocations with the pool tag 0x0030.

**Note**   If Driver Verifier has enabled the special pool for a driver and the Global Flags utility has enabled the special pool for a pool tag or allocation size, the special pool will be used for all allocations meeting any of these criteria (subject to pool availability).

 

See [Special Pool](special-pool.md) for full details on the use of the special pool.

 

 





