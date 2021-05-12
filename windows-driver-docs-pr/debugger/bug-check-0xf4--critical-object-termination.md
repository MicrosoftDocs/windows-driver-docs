---
title: Bug Check 0xF4 CRITICAL_OBJECT_TERMINATION
description: The CRITICAL_OBJECT_TERMINATION bug check has a value of 0x000000F4. This indicates that a process or thread crucial to system operation has unexpectedly exited or been terminated.
keywords: ["Bug Check 0xF4 CRITICAL_OBJECT_TERMINATION", "CRITICAL_OBJECT_TERMINATION"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- CRITICAL_OBJECT_TERMINATION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xF4: CRITICAL\_OBJECT\_TERMINATION


The CRITICAL\_OBJECT\_TERMINATION bug check has a value of 0x000000F4. This indicates that a process or thread crucial to system operation has unexpectedly exited or been terminated.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## CRITICAL\_OBJECT\_TERMINATION Parameters


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
<td align="left"><p>The terminating object type:</p>
<p><strong>0x3:</strong> Process</p>
<p><strong>0x6:</strong> Thread</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The terminating object</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The process image file name</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Pointer to an ASCII string containing an explanatory message</p></td>
</tr>
</tbody>
</table>

 

## Cause

Several processes and threads are necessary for the operation of the system. When they are terminated for any reason, the system can no longer function.

 
## Resolution

The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.
 




