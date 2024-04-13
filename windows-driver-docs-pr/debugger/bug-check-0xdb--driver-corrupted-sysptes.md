---
title: Bug Check 0xDB DRIVER_CORRUPTED_SYSPTES
description: The DRIVER_CORRUPTED_SYSPTES bug check has a value of 0x000000DB. This indicates that an attempt was made to touch memory at an invalid IRQL, probably due to corruption of system PTEs.
keywords: ["Bug Check 0xDB DRIVER_CORRUPTED_SYSPTES", "DRIVER_CORRUPTED_SYSPTES"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- DRIVER_CORRUPTED_SYSPTES
api_type:
- NA
---

# Bug Check 0xDB: DRIVER\_CORRUPTED\_SYSPTES


The DRIVER\_CORRUPTED\_SYSPTES bug check has a value of 0x000000DB. This indicates that an attempt was made to touch memory at an invalid IRQL, probably due to corruption of system PTEs.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## DRIVER\_CORRUPTED\_SYSPTES Parameters


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
<td align="left"><p>Memory referenced</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>IRQL</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p><strong>0:</strong> Read</p>
<p><strong>1:</strong> Write</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Address in code which referenced memory</p></td>
</tr>
</tbody>
</table>

 

## Cause

A driver tried to access pageable (or completely invalid) memory at too high of an IRQL. This bug check is almost always caused by drivers that have corrupted system PTEs.

## Resolution

If this bug check occurs, the culprit can be detected by editing the registry. In the **\\\\HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management** registry key, create or edit the **TrackPtes** value, and set it equal to DWORD 3. Then reboot. The system will then save stack traces, and if the driver commits the same error, the system will issue [**bug check 0xDA**](bug-check-0xda--system-pte-misuse.md) (SYSTEM\_PTE\_MISUSE). Then the stack trace will identify the driver that caused the error.

 

 




