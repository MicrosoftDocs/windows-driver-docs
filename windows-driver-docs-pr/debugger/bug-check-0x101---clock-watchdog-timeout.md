---
title: Bug Check 0x101 CLOCK_WATCHDOG_TIMEOUT
description: The CLOCK_WATCHDOG_TIMEOUT bug check has a value of 0x00000101 that indicates that an expected clock interrupt on a secondary processor, was not received within the allocated interval.
ms.assetid: 2e35d8c5-00b3-4722-b596-a76f38eb5179
keywords: ["Bug Check 0x101 CLOCK_WATCHDOG_TIMEOUT", "CLOCK_WATCHDOG_TIMEOUT"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- CLOCK_WATCHDOG_TIMEOUT
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x101: CLOCK\_WATCHDOG\_TIMEOUT


The CLOCK\_WATCHDOG\_TIMEOUT bug check has a value of 0x00000101. This indicates that an expected clock interrupt on a secondary processor, in a multi-processor system, was not received within the allocated interval.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## CLOCK\_WATCHDOG\_TIMEOUT Parameters


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
<td align="left"><p>Clock interrupt time-out interval, in nominal clock ticks</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The address of the processor control block (PRCB) for the unresponsive processor</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>0</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

The specified processor is not processing interrupts. Typically, this occurs when the processor is nonresponsive or is deadlocked.

 

 




