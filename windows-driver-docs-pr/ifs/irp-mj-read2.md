---
title: Checking the Oplock State of an IRP_MJ_READ operation
description: Checking the Oplock State of an IRP_MJ_READ operation
ms.assetid: 9b4d1ba9-0838-44f1-8328-f60bfb3910ee
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Checking the Oplock State of an IRP_MJ_READ operation


The following only applies when a *stream* is being read. If a TxF transacted reader performs the read, this check is not made since a transacted reader excludes a writer (that is, a writer holding an oplock cannot be present at all).
<table>
<tr>
<th>Request Type</th>
<th>Conditions</th>
</tr>
<tr>
<td rowspan="2">
<p>Level 1</p>
<p>Batch</p>
</td>
<td>
<p>Broken on IRP_MJ_READ when:</p>
<ul>
<li>
<p> The read operation occurs on a FILE_OBJECT with a different oplock key from the FILE_OBJECT which owns the oplock.</p>
</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>If the oplock is broken:</p>
<ul>
<li>
<p> Break to Level 2.</p>
</li>
<li>
<p> An acknowledgment must be received before the operation continues.</p>
</li>
</ul>
</td>
</tr>
<tr>
<td rowspan="2">
<p>Read-Write</p>
</td>
<td>
<p>Broken on IRP_MJ_READ when:</p>
<ul>
<li>
<p> The read operation occurs on a FILE_OBJECT with a different oplock key from the FILE_OBJECT which owns the oplock.</p>
</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>If the oplock is broken:</p>
<ul>
<li>
<p> Break to Read.</p>
</li>
<li>
<p> An acknowledgment must be received before the operation continues.</p>
</li>
</ul>
</td>
</tr>
<tr>
<td rowspan="2">
<p>Read-Write-Handle</p>
</td>
<td>
<p>Broken on IRP_MJ_READ when:</p>
<ul>
<li>
<p> The read operation occurs on a FILE_OBJECT with a different oplock key from the FILE_OBJECT which owns the oplock.</p>
</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>If the oplock is broken:</p>
<ul>
<li>
<p> Break to Read-Handle.</p>
</li>
<li>
<p> An acknowledgment must be received before the operation continues.</p>
</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>Level 2</p>
<p>Filter</p>
<p>Read</p>
<p>Read-Handle</p>
</td>
<td>
<ul>
<li>
<p> The oplock is not broken, no acknowledgment is required, and the operation proceeds immediately.</p>
</li>
</ul>
</td>
</tr>
</table>

 




