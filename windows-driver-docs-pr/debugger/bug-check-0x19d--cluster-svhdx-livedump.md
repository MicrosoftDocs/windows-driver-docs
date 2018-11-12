---
title: Bug Check 0x19D CLUSTER_SVHDX_LIVEDUMP
description: The CLUSTER_SVHDX_LIVEDUMP bug check has a value of 0x0000019D. This indicates that SVHDX initiated this livedump to help debug an inconsistent state.
ms.assetid: E261617D-E84A-4644-8854-53A189395637
keywords: ["Bug Check 0x19D CLUSTER_SVHDX_LIVEDUMP", "CLUSTER_SVHDX_LIVEDUMP"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- CLUSTER_SVHDX_LIVEDUMP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x19D: CLUSTER\_SVHDX\_LIVEDUMP


The CLUSTER\_SVHDX\_LIVEDUMP bug check has a value of 0x0000019D. This indicates that SVHDX initiated this livedump to help debug an inconsistent state.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## CLUSTER\_SVHDX\_LIVEDUMP Parameters


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
<td align="left"><p>Reason code</p>
<p>0x1 : Mounting a Shared Virtual disk has failed</p>
2 - Address of Svhdxflt!_SVHDX_VIRTUALDISK_CONTEXT
3 - Address of nt!_FILE_OBJECT
4 - NTSTATUS</td>
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

 

Cause
-----

When SVHDX detects that current state might cause some sort of inconsistency it will generate live dump with this status code. Parameter1 has code pointing to what scenario this live dump is created for. Other parameters should be interpreted in context of the reason code.

 

 




