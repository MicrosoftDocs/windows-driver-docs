---
title: Bug Check 0xCF TERMINAL_SERVER_DRIVER_MADE_INCORRECT_MEMORY_REFERENCE
description: The TERMINAL_SERVER_DRIVER_MADE_INCORRECT_MEMORY_REFERENCE bug check has a value of 0x000000CF. This indicates that a driver has been incorrectly ported to the terminal server.
ms.assetid: 1c3351d8-95df-4a12-a9c5-36aa6a5cf236
keywords: ["Bug Check 0xCF TERMINAL_SERVER_DRIVER_MADE_INCORRECT_MEMORY_REFERENCE", "TERMINAL_SERVER_DRIVER_MADE_INCORRECT_MEMORY_REFERENCE"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- TERMINAL_SERVER_DRIVER_MADE_INCORRECT_MEMORY_REFERENCE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xCF: TERMINAL\_SERVER\_DRIVER\_MADE\_INCORRECT\_MEMORY\_REFERENCE


The TERMINAL\_SERVER\_DRIVER\_MADE\_INCORRECT\_MEMORY\_REFERENCE bug check has a value of 0x000000CF. This indicates that a driver has been incorrectly ported to the terminal server.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## TERMINAL\_SERVER\_DRIVER\_MADE\_INCORRECT\_MEMORY\_REFERENCE Parameters


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
<td align="left"><p>Memory address referenced</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p><strong>0:</strong> Read</p>
<p><strong>1:</strong> Write</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Address that referenced memory (if known)</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

If the driver responsible for the error can be identified, its name is printed on the blue screen and stored in memory at the location (PUNICODE\_STRING) **KiBugCheckDriver**.

Cause
-----

The driver is referencing session space addresses from the system process context. This probably results from the driver queuing an item to a system worker thread.

This driver needs to comply with Terminal Server's memory management rules.

 

 




