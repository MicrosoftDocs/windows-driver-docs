---
title: Bug Check 0x190 WIN32K_CRITICAL_FAILURE_LIVEDUMP
description: The WIN32K_CRITICAL_FAILURE_LIVEDUMP live dump has a value of 0x00000190. This indicates that Win32k has encountered a critical failure. A live dump is captured to collect the debug information.
keywords: ["Bug Check 0x190 WIN32K_CRITICAL_FAILURE_LIVEDUMP", "WIN32K_CRITICAL_FAILURE_LIVEDUMP"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- WIN32K_CRITICAL_FAILURE_LIVEDUMP
api_type:
- NA
---

# Bug Check 0x190: WIN32K\_CRITICAL\_FAILURE\_LIVEDUMP


The WIN32K\_CRITICAL\_FAILURE\_LIVEDUMP live dump has a value of 0x00000190. This indicates that Win32k has encountered a critical failure. A live dump is captured to collect the debug information.

(This code can never be used for a real bug check; it is used to identify live dumps.)

## WIN32K\_CRITICAL\_FAILURE\_LIVEDUMP Parameters


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
<td align="left">1</td>
<td align="left"><p>Type of the failure</p>
<p>0x1 : REGION_VALIDATION_FAILURE - Region is out of surface bounds.</p>
2- Pointer to DC
3- Pointer to SURFACE
4- Pointer to REGION
<p>0x2 : OPERATOR_NEW_USED - Operator "new" is used to allocate memory.</p>
2 - Reserved
3 - Reserved
4 - Reserved</td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">See parameter 1</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left">See parameter 1</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">See parameter 1</td>
</tr>
</tbody>
</table>

 

 

 




