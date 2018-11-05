---
title: Bug Check 0x6B PROCESS1_INITIALIZATION_FAILED
description: The PROCESS1_INITIALIZATION_FAILED bug check has a value of 0x0000006B. This bug check indicates that the initialization of the Microsoft Windows operating system failed.
ms.assetid: 8680d924-3041-4927-a228-52b281bbc267
keywords: ["Bug Check 0x6B PROCESS1_INITIALIZATION_FAILED", "PROCESS1_INITIALIZATION_FAILED"]
ms.author: domars
ms.date: 06/27/2018
topic_type:
- apiref
api_name:
- PROCESS1_INITIALIZATION_FAILED
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x6B: PROCESS1\_INITIALIZATION\_FAILED


The PROCESS1\_INITIALIZATION\_FAILED bug check has a value of 0x0000006B. This bug check indicates that the initialization of the Microsoft Windows operating system failed.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

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

 

Cause
-----

Any part of the disk subsystem can cause the PROCESS1\_INITIALIZATION\_FAILED bug check, including bad disks, bad or incorrect cables, mixing different ATA-type devices on the same chain, or drives that are not available because of hardware regeneration.

This bug check can also be caused by a missing file from the boot partition or by a driver that a user accidentally disabled in the **Drivers** tab.

 

 




