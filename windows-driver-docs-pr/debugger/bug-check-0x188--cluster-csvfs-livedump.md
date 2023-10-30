---
title: Bug Check 0x188 CLUSTER_CSVFS_LIVEDUMP
description: The CLUSTER_CSVFS_LIVEDUMP live dump has a value of 0x00000188. This indicates that CSVFS initiated this livedump to help debug an inconsistent state.
keywords: ["Bug Check 0x188 CLUSTER_CSVFS_LIVEDUMP", "CLUSTER_CSVFS_LIVEDUMP"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- CLUSTER_CSVFS_LIVEDUMP
api_type:
- NA
---

# Bug Check 0x188: CLUSTER\_CSVFS\_LIVEDUMP


The CLUSTER\_CSVFS\_LIVEDUMP live dump has a value of 0x00000188. This indicates that CSVFS initiated this livedump to help debug an inconsistent state.

(This code can never be used for a real bug check; it is used to identify live dumps.)

## CLUSTER\_CSVFS\_LIVEDUMP Parameters


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
0x1 : Cache purge on oplock downgrade to none has failed
<p>2- address of CSVFS!_SCB</p>
0x2 : Cache purge on oplock upgrade from none has failed
<p>2- address of CSVFS!_SCB</p>
0x3 : Cache purge on set purge failure mode
<p>2- address of CSVFS!_SCB</p>
0x4 : Cache flush on oplock downgrade to none failed
<p>2- address of CSVFS!_SCB</p></td>
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

 

## Cause

First parameter contains the reason code When CSVFS detects that current state might cause data corruption or other sort of inconsistency it would generate live dump with this status code. Parameter1 has code pointing to what scenario this live dump is created for. Other parameters should be interpreted in context of the reason code.

 
## See Also

[Kernel Live Dump Code Reference](bug-check-code-reference-live-dump.md)

[Bug Check Code Reference](bug-check-code-reference2.md)
 




