---
title: Bug Check 0xF3 DISORDERLY_SHUTDOWN
description: The DISORDERLY_SHUTDOWN bug check has a value of 0x000000F3. This indicates that Windows was unable to shut down due to lack of memory.
ms.assetid: e113cd2f-96b2-43b8-a67e-a851cc5c0da8
keywords: ["Bug Check 0xF3 DISORDERLY_SHUTDOWN", "DISORDERLY_SHUTDOWN"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- DISORDERLY_SHUTDOWN
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xF3: DISORDERLY\_SHUTDOWN


The DISORDERLY\_SHUTDOWN bug check has a value of 0x000000F3. This indicates that Windows was unable to shut down due to lack of memory.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## DISORDERLY\_SHUTDOWN Parameters


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
<p>Windows Vista and later: Reserved</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Windows Server 2003 only: The current shut down stage</p>
<p>Windows Vista and later: The most recent modified write error status</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

Windows attempted to shut down, but there were no free pages available to continue operations.

Because applications were not terminated and drivers were not unloaded, they continued to access pages even after the modified writer had terminated. This causes the system to run out of pages, since the page files could be used.

 

 




