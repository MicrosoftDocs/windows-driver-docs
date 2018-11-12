---
title: Bug Check 0xD5 DRIVER_PAGE_FAULT_IN_FREED_SPECIAL_POOL
description: The DRIVER_PAGE_FAULT_IN_FREED_SPECIAL_POOL bug check has a value of 0x000000D5. This indicates that a driver has referenced memory which was earlier freed.
ms.assetid: b86e55d2-122f-40ac-adb3-092511d3274e
keywords: ["Bug Check 0xD5 DRIVER_PAGE_FAULT_IN_FREED_SPECIAL_POOL", "DRIVER_PAGE_FAULT_IN_FREED_SPECIAL_POOL"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- DRIVER_PAGE_FAULT_IN_FREED_SPECIAL_POOL
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xD5: DRIVER\_PAGE\_FAULT\_IN\_FREED\_SPECIAL\_POOL


The DRIVER\_PAGE\_FAULT\_IN\_FREED\_SPECIAL\_POOL bug check has a value of 0x000000D5. This indicates that a driver has referenced memory which was earlier freed.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## DRIVER\_PAGE\_FAULT\_IN\_FREED\_SPECIAL\_POOL Parameters


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

The Driver Verifier **Special Pool** option has caught the driver accessing memory which was earlier freed.

For information about the special pool, consult the Driver Verifier section of the Windows Driver Kit.

Remarks
-------

This cannot be protected by a **try - except** handler -- it can only be protected by a probe.

 

 




