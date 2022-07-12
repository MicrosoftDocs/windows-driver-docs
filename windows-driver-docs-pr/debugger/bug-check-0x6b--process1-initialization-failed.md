---
title: Bug Check 0x6B PROCESS1_INITIALIZATION_FAILED
description: The PROCESS1_INITIALIZATION_FAILED bug check has a value of 0x0000006B. This bug check indicates that the initialization of the Microsoft Windows operating system failed.
keywords: ["Bug Check 0x6B PROCESS1_INITIALIZATION_FAILED", "PROCESS1_INITIALIZATION_FAILED"]
ms.date: 06/27/2018
topic_type:
- apiref
api_name:
- PROCESS1_INITIALIZATION_FAILED
api_type:
- NA
---

# Bug Check 0x6B: PROCESS1\_INITIALIZATION\_FAILED


The PROCESS1\_INITIALIZATION\_FAILED bug check has a value of 0x0000006B. This bug check indicates that the initialization of the Microsoft Windows operating system failed.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


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
<td align="left"><p>0: Any failure of 2nd call to internal routine PsInitSystem </p>
<p> 2: Error when opening a system DLL </p>
<p> 3: Error when creating section for system DLL </p>
 <p> 4: Error when accessing section for system DLL </p>
 <p> 5: Error when mapping view of section for system DLL </p>
 <p> 6: Error finding any of one set of functions in system DLL </p>
 <p> 7: Error finding any of second set of functions in system DLL </p>
 <p> 8: Error finding any of third set of functions in system DLL </p>
 <p> Error getting section information for system DLL (Windows Vista and later) </p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>index to identify system DLL when the 2nd parameter is 2</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>0</p></td>
</tr>
</tbody>
</table>

 

## Cause

Any part of the disk subsystem can cause the PROCESS1\_INITIALIZATION\_FAILED bug check, including bad disks, bad or incorrect cables, mixing different ATA-type devices on the same chain, or drives that are not available because of hardware regeneration.

This bug check can also be caused by the system not being able to access to the file ntdll.dll, either because it is missing or corrupt, or if the catroot folder is missing, or by a driver that a user accidentally disabled in the **Drivers** tab.

 
## Resolution
The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause. 




