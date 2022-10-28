---
title: Bug Check 0x195 SMB_SERVER_LIVEDUMP
description: The SMB_SERVER_LIVEDUMP live dump has a value of 0x00000195. This indicates the SMB server detected a problem and has captured a kernel dump to collect debug information.
keywords: ["Bug Check 0x195 SMB_SERVER_LIVEDUMP", "SMB_SERVER_LIVEDUMP"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- SMB_SERVER_LIVEDUMP
api_type:
- NA
---

# Bug Check 0x195: SMB\_SERVER\_LIVEDUMP


The SMB\_SERVER\_LIVEDUMP live dump has a value of 0x00000195. This indicates the SMB server detected a problem and has captured a kernel dump to collect debug information.

(This code can never be used for a real bug check; it is used to identify live dumps.)

## SMB\_SERVER\_LIVEDUMP Parameters


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
<td align="left"><p>0x1 : An I/O failed to complete in a reasonable amount of time.</p>
2 - Pointer to the I/O's SRV2_WORK_ITEM</td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">See parameter 1</td>
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

## See Also

[Kernel Live Dump Code Reference](bug-check-code-reference-live-dump.md)

[Bug Check Code Reference](bug-check-code-reference2.md) 

 

 




