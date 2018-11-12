---
title: Bug Check 0x4D NO_PAGES_AVAILABLE
description: The NO_PAGES_AVAILABLE bug check has a value of 0x0000004D. This indicates that no free pages are available to continue operations.
ms.assetid: c1f8fb33-a01c-4455-87a7-59aa6ba7cb37
keywords: ["Bug Check 0x4D NO_PAGES_AVAILABLE", "NO_PAGES_AVAILABLE"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- NO_PAGES_AVAILABLE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x4D: NO\_PAGES\_AVAILABLE


The NO\_PAGES\_AVAILABLE bug check has a value of 0x0000004D. This indicates that no free pages are available to continue operations.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## NO\_PAGES\_AVAILABLE Parameters


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
<td align="left"><p><strong>Windows XP and Windows 2000:</strong> The size of the nonpaged pool available at the time the bug check occurred</p>
<p><strong>Windows Server 2003 and later:</strong> Reserved</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p><strong>Windows 2000:</strong> The number of transition pages that are currently stranded</p>
<p><strong>Windows XP and later:</strong> The most recent modified write error status.</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

To see general memory statistics, use the [**!vm 3**](-vm.md) extension.

This bug check can occur for any of the following reasons:

-   A driver has blocked, deadlocking the modified or mapped page writers. Examples of this include mutex deadlocks or accesses to paged out memory in file system drivers or filter drivers. This indicates a driver bug.

    If Parameter 1 or Parameter 2 is large, then this is a possibility. Use [**!vm 3**](-vm.md).

-   A storage driver is not processing requests. Examples of this are stranded queues and non-responding drives. This indicates a driver bug.

    If Parameter 1 or Parameter 2 is large, then this is a possibility. Use [**!vm 8**](-vm.md), followed by [**!process 0 7**](-process.md).

-   A high-priority realtime thread has starved the balance set manager from trimming pages from the working set, or starved the modified page writer from writing them out. This indicates a bug in the component that created this thread.

    This situation is difficult to analyze. Try using [**!ready**](-ready.md). Try also [**!process 0 7**](-process.md) to list all threads and see if any have accumulated excessive kernel time as well as what their current priorities are. Such processes may have blocked out the memory management threads from making pages available.

-   **Windows XP and Windows 2000:** Not enough pool is available for the storage stack to write out modified pages. This indicates a driver bug.

    If Parameter 3 is small, then this is a possibility. Use [**!vm**](-vm.md) and [**!poolused 2**](-poolused.md).

-   **Windows 2000:** All the processes have been trimmed to their minimums and all modified pages written, but still no memory is available. The freed memory must be stuck in transition pages with non-zero reference counts -- thus they cannot be put on the freelist.

    A driver is neglecting to unlock the pages preventing the reference counts from going to zero which would free the pages. This may be due to transfers that never finish, causing the driver routines to run endlessly, or to other driver bugs.

    If Parameter 4 is large, then this is a possibility. But it is very hard to find the driver. Try the [**!process 0 1**](-process.md) extension and look for any drivers that have a lot of locked pages.

If the problem cannot be found, then try booting with a kernel debugger attached from the beginning, and monitor the situation.

 

 




