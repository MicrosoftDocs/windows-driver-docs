---
title: Checking the Oplock State of an IRP_MJ_CREATE operation
description: Checking the Oplock State of an IRP_MJ_CREATE operation
ms.assetid: 30684025-9da0-4f4c-a850-ab0390bef091
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Checking the Oplock State of an IRP_MJ_CREATE operation


The following only applies when an existing stream of a file is being opened (that is, newly created streams cannot have pre-existing oplocks on them).

**Note**  When processing IRP_MJ_CREATE for any oplock, if the desired access contains nothing other than FILE_READ_ATTRIBUTES, FILE_WRITE_ATTRIBUTES, or SYNCHRONIZE, the oplock does not break unless FILE_RESERVE_OPFILTER is specified. Specifying FILE_RESERVE_OPFILTER always results in an oplock break if the create succeeds. For brevity and simplicity, the following table omits the foregoing, since it applies to all oplocks.
<table>
<tr>
<th>Request Type</th>
<th>Conditions</th>
</tr>
<tr>
<td rowspan="2">
<p>Level 1</p>
</td>
<td>
<p>Broken on IRP_MJ_CREATE when:</p>
<ul>
<li>
<p> The oplock key associated with the FILE_OBJECT on which the open is occurring is different from the oplock key associated with the FILE_OBJECT that owns the oplock.</p>
</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>If the oplock is broken:</p>
<ul>
<li>
<p>Break to None <b>IF</b>:<ul>
<li>
<p>The FILE_RESERVE_OPFILTER flag is set</p>
<p><b>OR</b></p>
</li>
<li>Any of the following create disposition values are specified:<ul>
<li>FILE_SUPERSEDE</li>
<li>FILE_OVERWRITE</li>
<li>FILE_OVERWRITE_IF</li>
</ul>
</li>
</ul>
</p>
<p><b>ELSE:</b></p>
<ul>
<li>Break to Level 2.</li>
</ul>
</li>
<li>
<p>An acknowledgment must be received before the operation continues.</p>
</li>
</ul>
</td>
</tr>
<tr>
<td rowspan="2">
<p>Level 2</p>
</td>
<td>
<p>Broken on IRP_MJ_CREATE when:</p>
<ul>
<li>The oplock key associated with the FILE_OBJECT on which the open is occurring is different from the oplock key associated with the FILE_OBJECT that owns the oplock.</li>
<li><b>AND:</b><ul>
<li>
<p>The FILE_RESERVE_OPFILTER flag is set</p>
<p><b>OR</b></p>
</li>
<li> Any of the following create disposition values are specified:<ul>
<li>FILE_SUPERSEDE</li>
<li>FILE_OVERWRITE</li>
<li>FILE_OVERWRITE_IF</li>
</ul>
</li>
</ul>
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
<td rowspan="2">
<p>Batch</p>
</td>
<td>
<p>Broken on IRP_MJ_CREATE when:</p>
<ul>
<li>
<p> The oplock key associated with the FILE_OBJECT on which the open is occurring is different from the oplock key associated with the FILE_OBJECT that owns the oplock.</p>
</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>If the oplock is broken:</p>
<ul>
<li>
<p>Break to None <b>IF</b>:<ul>
<li>
<p>The FILE_RESERVE_OPFILTER flag is set.</p>
<p><b>OR</b></p>
</li>
<li>Any of the following create disposition values are specified:<ul>
<li>FILE_SUPERSEDE</li>
<li>FILE_OVERWRITE</li>
<li>FILE_OVERWRITE_IF</li>
</ul>
</li>
</ul>
</p>
<p><b>ELSE:</b></p>
<ul>
<li>Break to Level 2.</li>
</ul>
</li>
<li>
<p>An acknowledgment must be received before the operation continues.</p>
</li>
</ul>
</td>
</tr>
<tr>
<td rowspan="2">
<p>Filter</p>
</td>
<td>
<p>Broken on IRP_MJ_CREATE when:</p>
<ul>
<li>
<p> The oplock key associated with the FILE_OBJECT on which the open is occurring is different from the oplock key associated with the FILE_OBJECT that owns the oplock.</p>
</li>
<li><b>AND:</b><ul>
<li>
<p>A &quot;writable&quot; desired access was requested on the stream which was not opened for FILE_SHARE_READ access.  Note that &quot;writeable&quot; access is defined as any attribute other than:</p>
<ul>
<li>FILE_READ_ATTRIBUTES</li>
<li>FILE_WRITE_ATTRIBUTES</li>
<li>FILE_READ_DATA</li>
<li>FILE_READ_EA</li>
<li>FILE_EXECUTE</li>
<li>SYNCHRONIZE</li>
<li>READ_CONTROL</li>
</ul>
</li>
</ul>
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
<p> An acknowledgment must be received before the operation continues.</p>
</li>
</ul>
</td>
</tr>
<tr>
<td rowspan="2">
<p>Read</p>
</td>
<td>
<p>Broken on IRP_MJ_CREATE when:</p>
<ul>
<li>
<p>The oplock key associated with the FILE_OBJECT on which the open is occurring is different from the oplock key associated with the FILE_OBJECT that owns the oplock.</p>
</li>
<li><b>AND:</b><ul>
<li>
<p>The FILE_RESERVE_OPFILTER flag is set</p>
<p><b>OR</b></p>
</li>
<li> Any of the following create disposition values are specified:<ul>
<li>FILE_SUPERSEDE</li>
<li>FILE_OVERWRITE</li>
<li>FILE_OVERWRITE_IF</li>
</ul>
</li>
</ul>
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
<td rowspan="2">
<p>Read-Handle</p>
</td>
<td>
<p>Broken on IRP_MJ_CREATE when:</p>
<ul>
<li>
<p>The current open conflicts with an existing open such that a sharing violation would occur.</p>
<p><b>OR</b></p>
</li>
<li>
<p>The FILE_RESERVE_OPFILTER flag is set.</p>
<p><b>OR</b></p>
</li>
<li>
<p>Any of the following create disposition values are specified:<ul>
<li>FILE_SUPERSEDE</li>
<li>FILE_OVERWRITE</li>
<li>FILE_OVERWRITE_IF</li>
</ul>
</p>
<p><b>AND</b> (for any of the above three conditions)</p>
</li>
<li>
<p> The oplock key associated with the FILE_OBJECT on which the open is occurring is different from the oplock key associated with the FILE_OBJECT that owns the oplock.</p>
</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>If the oplock is broken:</p>
<ul>
<li>
<p>Break to None <b>IF</b>:<ul>
<li>
<p>The FILE_RESERVE_OPFILTER flag is set.</p>
<p><b>OR</b></p>
</li>
<li>Any of the following create disposition values are specified:<ul>
<li>FILE_SUPERSEDE</li>
<li>FILE_OVERWRITE</li>
<li>FILE_OVERWRITE_IF</li>
</ul>
</li>
</ul>
</p>
<p><b>ELSE:</b></p>
<ul>
<li>Break to Read.</li>
</ul>
</li>
<li>If the oplock broke because the current open conflicts with an existing open such that a sharing violation would occur, an acknowledgment must be received before the operation continues.
      </li>
<li>If the oplock broke for any other reason, although acknowledgment of the break is required, the operation continues immediately (for example, without waiting for the acknowledgment).</li>
</ul>
</td>
</tr>
<tr>
<td rowspan="2">
<p>Read-Write</p>
</td>
<td>
<p>Broken on IRP_MJ_CREATE when:</p>
<ul>
<li>
<p>The oplock key associated with the FILE_OBJECT on which the open is occurring is different from the oplock key associated with the FILE_OBJECT that owns the oplock.</p>
</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>If the oplock is broken:</p>
<ul>
<li>
<p>Break to None <b>IF</b>:<ul>
<li>
<p>The FILE_RESERVE_OPFILTER flag is set.</p>
<p><b>OR</b></p>
</li>
<li>Any of the following create disposition values are specified:<ul>
<li>FILE_SUPERSEDE</li>
<li>FILE_OVERWRITE</li>
<li>FILE_OVERWRITE_IF</li>
</ul>
</li>
</ul>
</p>
<p><b>ELSE:</b></p>
<ul>
<li>Break to Read.</li>
</ul>
</li>
<li>
<p>An acknowledgment must be received before the operation continues.</p>
</li>
</ul>
</td>
</tr>
<tr>
<td rowspan="2">
<p>Read-Write-Handle</p>
</td>
<td>
<p>Broken on IRP_MJ_CREATE when:</p>
<ul>
<li>
<p> The oplock key associated with the FILE_OBJECT on which the open is occurring is different from the oplock key associated with the FILE_OBJECT that owns the oplock.</p>
</li>
</ul>
</td>
</tr>
<tr>
<td>
<p>If the oplock is broken:</p>
<ul>
<li>
<p>Break to None <b>IF</b>:<ul>
<li>
<p>The FILE_RESERVE_OPFILTER flag is set.</p>
<p><b>OR</b></p>
</li>
<li>Any of the following create disposition values are specified:<ul>
<li>FILE_SUPERSEDE</li>
<li>FILE_OVERWRITE</li>
<li>FILE_OVERWRITE_IF</li>
</ul>
</li>
</ul>
</p>
<p><b>ELSE:</b></p>
<ul>
<li>
<p>Break to Read-Write if the current open conflicts with an existing open such that a sharing violation would occur.  Otherwise, break to Read-Handle.</p>
</li>
</ul>
</li>
<li>
<p>An acknowledgment must be received before the operation continues.</p>
</li>
</ul>
</td>
</tr>
</table>
 

The file system performs additional checks for Batch and Filter oplocks (rather than the oplock package itself) when processing an IRP_MJ_CREATE operation, which impact whether the file system asks the oplock package to perform oplock break processing. This is a case where operations on one data stream can impact the oplocks on other data streams of the same file (that is, the last two list items of the following criteria list). If one or more of the following criteria are met, the file system sends a request to the oplock package to perform oplock break processing:

-   Request a break if this is a network query open and a [KTM](http://go.microsoft.com/fwlink/p/?linkid=124745) transaction is present. Otherwise, do not request a break on network query open.

-   If a SUPERSEDE, OVERWRITE or OVERWRITE_IF operation is performed on an alternate data stream and FILE_SHARE_DELETE is not specified and there is a Batch or Filter oplock on the primary data stream, request a break of the Batch or Filter oplock on the primary data stream.

-   If a SUPERSEDE, OVERWRITE or OVERWRITE_IF operation is performed on the primary data stream and DELETE access has been requested and there are Batch or Filter oplocks on any alternate data stream, request a break of the Batch or Filter oplocks on all alternate data streams that have them.

When the file system decides to ask the oplock package to perform oplock break processing, the rules laid out in the preceding table apply.

The check to break Batch and Filter oplocks occurs before the share access checks are made. This means the Batch or Filter oplock is broken even if the open request ultimately fails due to a sharing violation.

 

 




