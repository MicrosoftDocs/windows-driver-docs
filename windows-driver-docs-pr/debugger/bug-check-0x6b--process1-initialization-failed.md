---
title: Bug Check 0x6B PROCESS1_INITIALIZATION_FAILED
description: The PROCESS1_INITIALIZATION_FAILED bug check has a value of 0x0000006B. This bug check indicates that the initialization of the Microsoft Windows operating system failed.
keywords: ["Bug Check 0x6B PROCESS1_INITIALIZATION_FAILED", "PROCESS1_INITIALIZATION_FAILED"]
ms.date: 06/27/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- PROCESS1_INITIALIZATION_FAILED
api_type:
- NA
---

# Bug Check 0x6B: PROCESS1\_INITIALIZATION\_FAILED


The PROCESS1\_INITIALIZATION\_FAILED bug check has a value of 0x0000006B. This bug check indicates that the initialization of the Microsoft Windows operating system failed.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## PROCESS1\_INITIALIZATION\_FAILED Parameters


The following parameters appear on the blue screen.

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
<td align="left"><p>The NT status code that caused the failure</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

## Cause

Any part of the disk subsystem can cause the PROCESS1\_INITIALIZATION\_FAILED bug check, including bad disks, bad or incorrect cables, mixing different ATA-type devices on the same chain, or drives that are not available because of hardware regeneration.

This bug check can also be caused by a missing file from the boot partition or by a driver that a user accidentally disabled in the **Drivers** tab.

 
## Resolution
The [**!analyze**](../debuggercmds/-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause. 




