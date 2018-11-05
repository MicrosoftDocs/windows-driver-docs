---
title: Bug Check 0x188 CLUSTER_CSVFS_LIVEDUMP
description: The CLUSTER_CSVFS_LIVEDUMP bug check has a value of 0x00000188. This indicates that CSVFS initiated this livedump to help debug an inconsistent state.
ms.assetid: 220B0CDB-6E10-4262-A07C-042E8BA21D7F
keywords: ["Bug Check 0x188 CLUSTER_CSVFS_LIVEDUMP", "CLUSTER_CSVFS_LIVEDUMP"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- CLUSTER_CSVFS_LIVEDUMP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x188: CLUSTER\_CSVFS\_LIVEDUMP


The CLUSTER\_CSVFS\_LIVEDUMP bug check has a value of 0x00000188. This indicates that CSVFS initiated this livedump to help debug an inconsistent state.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

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

 

Cause
-----

First parameter contains the reason code When CSVFS detects that current state might cause data corruption or other sort of inconsistency it would generate live dump with this status code. Parameter1 has code pointing to what scenario this live dump is created for. Other parameters should be interpreted in context of the reason code.

 

 




