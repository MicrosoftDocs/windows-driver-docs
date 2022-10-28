---
title: Bug Check 0x1E0 INVALID_ALTERNATE_SYSTEM_CALL_HANDLER_REGISTRATION
description: The INVALID_ALTERNATE_SYSTEM_CALL_HANDLER_REGISTRATION live dump has a value of 0x000001E0. This indicates that an invalid operation has been performed with regard to alternate system call handling registration.
keywords: ["Bug Check 0x1E0 INVALID_ALTERNATE_SYSTEM_CALL_HANDLER_REGISTRATION", "INVALID_ALTERNATE_SYSTEM_CALL_HANDLER_REGISTRATION"]
ms.date: 10/10/2022
topic_type:
- apiref
api_name:
- INVALID_ALTERNATE_SYSTEM_CALL_HANDLER_REGISTRATION
api_type:
- NA
---

# Bug Check 0x1E0: INVALID\_ALTERNATE\_SYSTEM\_CALL\_HANDLER\_REGISTRATION

The INVALID\_ALTERNATE\_SYSTEM\_CALL\_HANDLER\_REGISTRATION live dump has a value of 0x000001E0. This indicates that an invalid operation has been performed with regard to alternate system call handling registration. 

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## INVALID\_ALTERNATE\_SYSTEM\_CALL\_HANDLER\_REGISTRATION Parameters

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
<td align="left"><p>Reserved</p>
</td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">Reserved</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left">Reserved</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">Reserved</td>
</tr>
</tbody>
</table>

## Resolution

The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.

## See also

[Bug Check Code Reference](bug-check-code-reference2.md)
