---
title: Enable pool tagging
description: Enable pool tagging
ms.assetid: e88f97a0-a8c3-4162-871a-b78671b902bb
keywords: ["Enable pool tagging (global flag)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Enable pool tagging


## <span id="ddk_enable_pool_tagging_dtools"></span><span id="DDK_ENABLE_POOL_TAGGING_DTOOLS"></span>


The **Enable pool tagging** flag collects data and calculates statistics about pool memory allocations sorted by pool tag value.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>ptg</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>0x400</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>FLG_POOL_ENABLE_TAGGING</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>System-wide registry entry</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

This flag is permanently set in Windows Server 2003 and later versions of Windows. On these systems, the **Enable pool tagging** check box in the Global Flags dialog box is dimmed and commands to enable or disable pool tagging fail.

Use **ExAllocatePoolWithTag** or **ExAllocatePoolWithQuotaTag** to set the tag value. When no tag value is specified (**ExAllocatePool**, **ExAllocatePoolWithQuota**), Windows creates a tag with the default value of "None." Because data for all allocations with a "None" tag is combined, you cannot distinguish the data for a specific allocation. For information about these routines, see the Windows Driver Kit (WDK).

In Windows XP and earlier systems, this flag also directs Windows to attach a pool tag even when the pool memory is allocated by using **ExAllocatePoolWithQuotaTag**. Otherwise, the tag bytes are used to store the quota values. In Windows Server 2003, tag values and quota values are stored in separate fields that are attached to every pool memory allocation.

**Note**   To display the data that Windows collects about a tagged allocation, use PoolMon, a tool that is included in the Windows Driver Kit.
The description of the **Enable Pool Tagging** flag in the Windows XP Support Tools documentation is incomplete. This flag directs Windows to collect and process data by tag value.

 

 

 





