---
title: Checking the Oplock State of an IRP_MJ_LOCK_CONTROL operation
description: Checking the Oplock State of an IRP_MJ_LOCK_CONTROL operation
ms.assetid: 6e0a5287-9a22-465f-b345-c9af556e6cdb
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Checking the Oplock State of an IRP_MJ_LOCK_CONTROL operation


The following applies on every byte range lock operation on the given stream.
<table>
<tr>
<th>Request Type</th>
<th>Conditions</th>
</tr>
<tr>
<td rowspan="2">
<p>Level 1</p>
<p>Batch</p>
<p>Read-Handle</p>
<p>Read-Write</p>
<p>Read-Write-Handle</p>
</td>
<td>
<p>Broken on IRP_MJ_LOCK_CONTROL when:</p>
<ul>
<li>
<p> The lock operation occurs on a FILE_OBJECT with a different oplock key from the FILE_OBJECT which owns the oplock.</p>
</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>If the oplock is broken:</p>
<ul>
<li>
<p> Break to None.</p>
</li>
<li>
<p>For the Handle request: Although acknowledgment of the break is required, the operation continues immediately (for example, without waiting for the acknowledgment).</p>
</li>
<li>
<p> For all other request types: An acknowledgment must be received before the operation continues.</p>
</li>
</ul>
</td>
</tr>
<tr>
<td rowspan="2">
<p>Read</p>
</td>
<td>
<p>Broken on IIRP_MJ_LOCK_CONTROL when:</p>
<ul>
<li>
<p> The lock operation occurs on a FILE_OBJECT with a different oplock key from the FILE_OBJECT which owns the oplock.</p>
</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>If the oplock is broken:</p>
<ul>
<li>
<p> Break to None.</p>
</li>
<li>
<p> No acknowledgment is required, the operation proceeds immediately.</p>
</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>Filter</p>
</td>
<td>
<ul>
<li>
<p> The oplock is not broken, no acknowledgment is required, and the operation proceeds immediately.</p>
</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>Level 2</p>
</td>
<td>
<ul>
<li>
<p> Always break to None.</p>
</li>
<li>
<p> No acknowledgment is required, the operation proceeds immediately.</p>
</li>
</ul>
</td>
</tr>
</table>

 

 




