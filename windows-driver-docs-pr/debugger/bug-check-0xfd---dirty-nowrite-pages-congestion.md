---
title: Bug Check 0xFD DIRTY_NOWRITE_PAGES_CONGESTION
description: The DIRTY_NOWRITE_PAGES_CONGESTION bug check has a value of 0x000000FD. This indicates that there are no free pages available to continue basic system operations.
ms.assetid: b657fffe-8331-4b4f-9d29-fea8ee1e1682
keywords: ["Bug Check 0xFD DIRTY_NOWRITE_PAGES_CONGESTION", "DIRTY_NOWRITE_PAGES_CONGESTION"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- DIRTY_NOWRITE_PAGES_CONGESTION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xFD: DIRTY\_NOWRITE\_PAGES\_CONGESTION


The DIRTY\_NOWRITE\_PAGES\_CONGESTION bug check has a value of 0x000000FD. This indicates that there are no free pages available to continue basic system operations.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## DIRTY\_NOWRITE\_PAGES\_CONGESTION Parameters


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
<td align="left"><p>Total number of dirty pages</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Number of non-writeable dirty pages</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Most recently modified write-error status</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

This bug check usually occurs because the component that owns the modified non-writeable pages failed to write out these pages after marking the relevant files as "do not write" to memory management. This indicates a driver bug.

Resolution
----------

For more information about which driver is causing the problem, use the [**!vm 3**](-vm.md) extension, followed by [**!memusage 1**](-memusage.md) .

 

 




