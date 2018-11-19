---
title: Checking the Oplock State of an IRP_MJ_CLEANUP operation
description: Checking the Oplock State of an IRP_MJ_CLEANUP operation
ms.assetid: 5e078575-cbb8-4460-9986-4c546b8c20be
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Checking the Oplock State of an IRP_MJ_CLEANUP operation


The following only applies when a *stream* is being closed.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Request Type</th>
<th align="left">Conditions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Level 1</p>
<p>Batch</p>
<p>Filter</p>
<p>Read-Handle</p>
<p>Read-Write</p>
<p>Read-Write-Handle</p></td>
<td align="left"><ul>
<li><p>Always break to None.</p></li>
<li><p>No acknowledgment is required, the operation proceeds immediately. Note that any I/O operations (IRPs) waiting for an acknowledgment from a pending break request are completed immediately.</p></li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p>Level 2</p>
<p>Read</p></td>
<td align="left"><ul>
<li><p>Always break to None. Note that other Level 2 or Read oplocks on the same stream are not affected; only the Level 2 or Read oplock associated with this FILE_OBJECT is broken.</p></li>
<li><p>No acknowledgment is required, the operation proceeds immediately.</p></li>
</ul></td>
</tr>
</tbody>
</table>

 

 

 




