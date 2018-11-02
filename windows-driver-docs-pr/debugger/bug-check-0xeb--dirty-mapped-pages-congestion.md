---
title: Bug Check 0xEB DIRTY_MAPPED_PAGES_CONGESTION
description: The DIRTY_MAPPED_PAGES_CONGESTION bug check has a value of 0x000000EB. This indicates that no free pages are available to continue operations.
ms.assetid: 7a73dc74-fe40-4c0c-9c33-b0af3709bf43
keywords: ["Bug Check 0xEB DIRTY_MAPPED_PAGES_CONGESTION", "DIRTY_MAPPED_PAGES_CONGESTION"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- DIRTY_MAPPED_PAGES_CONGESTION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xEB: DIRTY\_MAPPED\_PAGES\_CONGESTION


The DIRTY\_MAPPED\_PAGES\_CONGESTION bug check has a value of 0x000000EB. This indicates that no free pages are available to continue operations.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## DIRTY\_MAPPED\_PAGES\_CONGESTION Parameters


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>The total number of dirty pages</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The number of dirty pages destined for the page file</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Windows Server 2003 only: The size of the nonpaged pool available at the time of the bug check (in pages)</p>
<p>Windows Vista and later versions: Reserved</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Windows Server 2003 only: The number of transition pages that are currently stranded</p>
<p>Windows Vista and later versions: The most recent modified write error status</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

The file system driver stack has deadlocked and most of the modified pages are destined for the file system. Because the file system is non-operational, the system has crashed because none of the modified pages can be reused without losing data. Any file system or filter driver in the stack may be at fault.

To see general memory statistics, use the [**!vm 3**](-vm.md) extension.

This bug check can occur for any of the following reasons:

-   A driver has blocked, deadlocking the modified or mapped page writers. Examples of this include mutex deadlocks or accesses to paged out memory in file system drivers or filter drivers. This indicates a driver bug.

    If Parameter 1 or Parameter 2 is large, this is a possibility. Use [**!vm 3**](-vm.md).

-   A storage driver is not processing requests. Examples of this are stranded queues and unresponsive drives. This indicates a driver bug.

    If Parameter 1 or Parameter 2 is large, this is a possibility. Use [**!process 0 7**](-process.md).

-   Windows Server 2003 only: Not enough pool is available for the storage stack to write out modified pages. This indicates a driver bug.

    If Parameter 3 is small, this is a possibility. Use [**!vm**](-vm.md) and [**!poolused 2**](-poolused.md).

 

 




