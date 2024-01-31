---
title: Bug Check 0x198 UFX_LIVEDUMP
description: The UFX_LIVEDUMP live dump has a value of 0x00000198. This indicates that a UFX live dump occurred.
keywords: ["Bug Check 0x198 UFX_LIVEDUMP", "UFX_LIVEDUMP"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- UFX_LIVEDUMP
api_type:
- NA
---

# Bug Check 0x198: UFX\_LIVEDUMP

The UFX\_LIVEDUMP live dump has a value of 0x00000198. This indicates that a UFX live dump occurred.

(This code can never be used for a real bug check; it is used to identify live dumps.)

## UFX\_LIVEDUMP Parameters


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
<td align="left"><p>Failure type</p>
<p>0x1 : A class driver failed to activate the bus.</p>
2 - Mask of enumerated child PDOs
3 - Mask of activated child PDOs
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


## See Also

[Kernel Live Dump Code Reference](bug-check-code-reference-live-dump.md)

[Bug Check Code Reference](bug-check-code-reference2.md) 

