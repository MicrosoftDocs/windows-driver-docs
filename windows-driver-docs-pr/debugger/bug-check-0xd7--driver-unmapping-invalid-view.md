---
title: Bug Check 0xD7 DRIVER_UNMAPPING_INVALID_VIEW
description: The DRIVER_UNMAPPING_INVALID_VIEW bug check has a value of 0x000000D7. This indicates a driver is trying to unmap an address that was not mapped.
keywords: ["Bug Check 0xD7 DRIVER_UNMAPPING_INVALID_VIEW", "DRIVER_UNMAPPING_INVALID_VIEW"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- DRIVER_UNMAPPING_INVALID_VIEW
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xD7: DRIVER\_UNMAPPING\_INVALID\_VIEW


The DRIVER\_UNMAPPING\_INVALID\_VIEW bug check has a value of 0x000000D7. This indicates a driver is trying to unmap an address that was not mapped.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## DRIVER\_UNMAPPING\_INVALID\_VIEW Parameters


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
<td align="left"><p>Virtual address to unmap</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p><strong>1:</strong> The view is being unmapped</p>
<p><strong>2:</strong> The view is being committed</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>0</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause. Use the [**kb (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md)  command to get a stack trace: the driver that caused the error can be determined from the stack trace.

 

 




