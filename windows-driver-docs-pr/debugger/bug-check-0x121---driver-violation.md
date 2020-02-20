---
title: Bug Check 0x121 DRIVER_VIOLATION
description: The DRIVER_VIOLATION bug check has a value of 0x00000121. This bug check indicates that a driver has caused a violation.
ms.assetid: 4a5d1d84-a958-45a6-9511-b5b4ecd4c067
keywords: ["Bug Check 0x121 DRIVER_VIOLATION", "DRIVER_VIOLATION"]
ms.date: 10/08/2019
topic_type:
- apiref
api_name:
- DRIVER_VIOLATION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x121: DRIVER\_VIOLATION

The DRIVER\_VIOLATION bug check has a value of 0x00000121. This bug check indicates that a driver has caused a violation.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## DRIVER\_VIOLATION Parameters

Parameter 1 indicates the type of violation.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 1</th>
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Parameter 4</th>
<th align="left">Cause</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x1</p></td>
<td align="left"><p>The current IRQL.</p></td>
<td align="left"><p>The required IRQL.</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A driver has called a function which can only be called at a
	specific IRQL.</p></td>
</tr>
</tbody>
</table>

Remarks
-------

Use a kernel debugger and view the call stack to determine the name of the driver that caused the violation: the [**!analyze**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-analyze) debug extension displays information about the bug check and can be helpful in determining the root cause, then enter one of the [**k (Display Stack Backtrace)**](https://docs.microsoft.com/windows-hardware/drivers/debugger/k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-) commands to view the call stack.
