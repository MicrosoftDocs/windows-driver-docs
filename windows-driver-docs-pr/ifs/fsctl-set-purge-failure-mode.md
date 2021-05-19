---
title: FSCTL_SET_PURGE_FAILURE_MODE control code
description: Filter Manager uses FSCTL\_SET\_PURGE\_FAILURE\_MODE control code to orchestrate the syncrhonization of operations during the lifetime of a section created for [data scan](windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatesectionfordatascan).
keywords: ["FSCTL_SET_PURGE_FAILURE_MODE control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_SET_PURGE_FAILURE_MODE
api_location:
- ntifs.h
api_type:
- HeaderDef
---

# FSCTL\_SET\_PURGE\_FAILURE\_MODE control code

Filter Manager uses the  **FSCTL\_SET\_PURGE\_FAILURE\_MODE** control code to orchestrate the syncrhonization of operations during the lifetime of a section created for [data scan](windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatesectionfordatascan).

Filter Manager brackets the life of the section with IRP\_MJ\_FILE\_SYSTEM\_CONTROL calls using this control code.  These serve to instruct a File System (and, rarely, File System MiniFilters) to behave differently if it fails to purge the CacheManager caches.  See the remarks section for more details.

Filters should never issue this control code.

## Parameters

The parameter for the operation will be a SET\_PURGE\_FAILURE\_MODE\_INPUT structure (_I'll leave it to you to document that bit because you have tools_)

## Remarks
For every FSCTL\_SET\_PURGE\_FAILURE\_MODE with the SET\_PURGE\_FAILURE\_MODE\_ENABLED bit set, another one will be issued with the SET\_PURGE\_FAILURE\_MODE\_DISABLED set.   Whilst there is an unbalanced SET\_PURGE\_FAILURE\_MODE\_ENABLED outstanding, filter manager responds to certain failure statuses from certain types of operations by pending the  operation, expediting the close of the section (where possible) and then requeueing the operation to the MiniFilter or File System that issued the failure.

In order to trigger the filter manager to do this the file system (or filter) responds to a failure to purge a section in the following ways.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Operation</th>
<th align="left">Required return status</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>IRP_MJ_CREATE (destructive operations)</p></td>
<td align="left"><p>STATUS_USER_MAPPED_FILE</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MJ_WRITE (unbuffered operations <strong>only</strong>)</p></td>
<td align="left"><p>STATUS_PURGE_FAILED</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IRP_MJ_SET_INFORMATION</p></td>
<td align="left"><p>STATUS_PURGE_FAILED</p></td>
</tr>
</tbody>
</table>

These statuses should only be returned  while there is a SET\_PURGE\_FAILURE\_MODE\_ENABLED outstanding (no balancing SET\_PURGE\_FAILURE\_MODE\_DISABLED received) - in all other cases error statuses will be returned to the application.

For any other operation (for instances a cached write), if the filesystem (or filter) fails to purge a section whilst there is an FSCTL\_SET\_PURGE\_FAILURE\_MODE outstanding then it is responsbile for pending the operation and reissuing it when the count of outstanding FSCTL\_SET\_PURGE\_FAILURE\_MODE drops to zero.  If it just returns a failure status (including those listed above) they will be returned to the application.

It should be noted that the error status is processed entirely within Filter Manager as is the requeuing of the failed operation.  This means that neither are visible to filters.  This in turn has has two important implications:

* File system monitoring tools such as [Process Monitor](sysinternals/downloads/procmon) will not report these operations
* If an upper filter is required to be involved in order for the re-issued operation to succeed, then the requeued operation will fail.  In this situation filter writers are required to ensure that this second filter returns the failure status (_I appreciate that this is a super edge case, but it bit me_)

## OTHER NOTES

_I happen to know that you can help things along in the "Pend and post yourself because filter manager won't" case by issuing a non cached zero length write to yourself and arrage to fail it  STATUS\_PURGE\_FAILED, but that probably doesn't need to be documented._


## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ntifs.h (include Ntifs.h or Fltkernel.h)</td>
</tr>
</tbody>
</table>

## See also

