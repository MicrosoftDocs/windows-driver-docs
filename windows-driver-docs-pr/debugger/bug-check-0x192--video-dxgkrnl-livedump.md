---
title: Bug Check 0x193 VIDEO_DXGKRNL_LIVEDUMP
description: The VIDEO_DXGKRNL_LIVEDUMP live dump has a value of 0x00000193. This indicates a livedump triggered by dxgkrnl occurred.
keywords: ["Bug Check 0x193 VIDEO_DXGKRNL_LIVEDUMP", "VIDEO_DXGKRNL_LIVEDUMP"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- VIDEO_DXGKRNL_LIVEDUMP
api_type:
- NA
---

# Bug Check 0x193: VIDEO\_DXGKRNL\_LIVEDUMP


The VIDEO\_DXGKRNL\_LIVEDUMP live dump has a value of 0x00000193. This indicates a live dump triggered by dxgkrnl occurred.

(This code can never be used for a real bug check; it is used to identify live dumps.)

## VIDEO\_DXGKRNL\_LIVEDUMP Parameters


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
<td align="left"><p>Reason Code</p>
0x100 Internal</td>
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
 

 ## See Also

[Kernel Live Dump Code Reference](bug-check-code-reference-live-dump.md)

[Bug Check Code Reference](bug-check-code-reference2.md)

 




