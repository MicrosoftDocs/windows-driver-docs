---
title: Miscellaneous Network Mini-Redirector Routines
description: Miscellaneous Network Mini-Redirector Routines
keywords:
- mini-redirectors WDK , miscellaneous routines
- connection IDs WDK network redirectors
- buffering state WDK network redirectors
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Miscellaneous Network Mini-Redirector Routines


A few other routines implemented by a network mini-redirector deal with buffering state management and connection IDs. The buffering state management routines can be used by a network mini-redirector to handle various buffering schemes implemented in the redirector and the server and to communicate any changes in buffering state. For example, the [**MRxCompleteBufferingStateChangeRequest**](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_change_buffering_state_calldown) routine is used by the SMB redirector as part of the mechanism to send an oplock break to the server.

Connection IDs can be used for multiplexing multiple connections. It is unnecessary for a network mini-redirector to support connection IDs, so [**MRxGetConnectionId**](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_get_connection_id) is optional.

The following table lists the routines that can be implemented by a network mini-redirector for miscellaneous operations.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Routine</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_change_buffering_state_calldown" data-raw-source="[&lt;strong&gt;MRxCompleteBufferingStateChangeRequest&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_change_buffering_state_calldown)"><strong>MRxCompleteBufferingStateChangeRequest</strong></a></td>
<td align="left"><p>RDBSS calls this routine to notify the network mini-redirector that a buffering state change request has been completed. For example, the SMB redirector uses this routine to send an oplock break response or to close the handle on an oplock break if the file is no longer in use. Byte range locks that need to be flushed out to the server are passed to the network mini-redirector in the <strong>LowIoContext.ParamsFor.Locks.LockList</strong> member of the RX_CONTEXT.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_compute_new_buffering_state" data-raw-source="[&lt;strong&gt;MRxComputeNewBufferingState&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_compute_new_buffering_state)"><strong>MRxComputeNewBufferingState</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector compute a new buffering state change.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_get_connection_id" data-raw-source="[&lt;strong&gt;MRxGetConnectionId&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_get_connection_id)"><strong>MRxGetConnectionId</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector return a connection ID for the connection which can be used for handling multiple sessions. If connection IDs are supported by the network mini-redirector, then the returned connection ID is appended to the connection structures stored in the name table. RDBSS considers the connection ID as an opaque blob, and does a byte-by-byte comparison of the connection ID blob while looking up the net-name table for a given name.</p></td>
</tr>
</tbody>
</table>

 

