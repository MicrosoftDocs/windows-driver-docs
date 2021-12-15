---
title: Routines Implemented by the Kernel Network Mini-Redirector
description: Routines Implemented by the Kernel Network Mini-Redirector
keywords:
- mini-redirectors WDK , routines implemented
ms.date: 04/20/2017
---

# Routines Implemented by the Kernel Network Mini-Redirector


The following routines can be implemented by a network mini-redirector:

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
<td align="left"><a href="/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_chkfcb_calldown" data-raw-source="[&lt;strong&gt;MRxAreFilesAliased&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_chkfcb_calldown)"><strong>MRxAreFilesAliased</strong></a></td>
<td align="left"><p>RDBSS calls this routine to query the network mini-redirector if two file control block (FCB) structures represent the same file. RDBSS calls this routine when processing two files that appear to be the same but have different names (an MS-DOS short name and a long name, for example).</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff549841(v=vs.85)" data-raw-source="[&lt;strong&gt;MRxCleanupFobx&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff549841(v=vs.85))"><strong>MRxCleanupFobx</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector close a file system object extension structure. RDBSS issues this call in response to receiving an <a href="/windows-hardware/drivers/ifs/irp-mj-cleanup" data-raw-source="[&lt;strong&gt;IRP_MJ_CLEANUP&lt;/strong&gt;](./irp-mj-cleanup.md)"><strong>IRP_MJ_CLEANUP</strong></a> on a file object.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_calldown" data-raw-source="[&lt;strong&gt;MRxCloseSrvOpen&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_calldown)"><strong>MRxCloseSrvOpen</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector close a SRV_OPEN structure.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxcollapseopen" data-raw-source="[&lt;strong&gt;MRxCollapseOpen&lt;/strong&gt;](./mrxcollapseopen.md)"><strong>MRxCollapseOpen</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector collapse an open file system request onto an existing SRV_OPEN.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_change_buffering_state_calldown" data-raw-source="[&lt;strong&gt;MRxCompleteBufferingStateChangeRequest&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_change_buffering_state_calldown)"><strong>MRxCompleteBufferingStateChangeRequest</strong></a></td>
<td align="left"><p>RDBSS calls this routine to notify the network mini-redirector that a buffering state change request has been completed. For example, the SMB redirector uses this routine to send an oplock break response or to close the handle on an oplock break if the file is no longer in use. Byte range locks that need to be flushed out to the server are passed to the network mini-redirector in the <strong>LowIoContext.ParamsFor.Locks.LockList</strong> member of the RX_CONTEXT structure.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_compute_new_buffering_state" data-raw-source="[&lt;strong&gt;MRxComputeNewBufferingState&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_compute_new_buffering_state)"><strong>MRxComputeNewBufferingState</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector compute a new buffering state change.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxcreate" data-raw-source="[&lt;strong&gt;MRxCreate&lt;/strong&gt;](./mrxcreate.md)"><strong>MRxCreate</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector create a file system object. RDBSS issues this call in response to receiving an <a href="/windows-hardware/drivers/ifs/irp-mj-create" data-raw-source="[&lt;strong&gt;IRP_MJ_CREATE&lt;/strong&gt;](./irp-mj-create.md)"><strong>IRP_MJ_CREATE</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_create_srvcall" data-raw-source="[&lt;strong&gt;MRxCreateSrvCall&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_create_srvcall)"><strong>MRxCreateSrvCall</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector create a SRV_CALL structure and establish a connection with a server.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_create_v_net_root" data-raw-source="[&lt;strong&gt;MRxCreateVNetRoot&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_create_v_net_root)"><strong>MRxCreateVNetRoot</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector create a V_NET_ROOT structure.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_deallocate_for_fcb" data-raw-source="[&lt;strong&gt;MRxDeallocateForFcb&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_deallocate_for_fcb)"><strong>MRxDeallocateForFcb</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector deallocate an FCB. This call is in response to a request to close a file system object.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_deallocate_for_fobx" data-raw-source="[&lt;strong&gt;MRxDeallocateForFobx&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_deallocate_for_fobx)"><strong>MRxDeallocateForFobx</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector deallocate an FOBX structure. This call is in response to a request to close a file system object.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxdevfcbxxxcontrolfile" data-raw-source="[&lt;strong&gt;MRxDevFcbXXXControlFile&lt;/strong&gt;](./mrxdevfcbxxxcontrolfile.md)"><strong>MRxDevFcbXXXControlFile</strong></a></td>
<td align="left"><p>RDBSS calls this routine to pass a device FCB control request to the network mini-redirector. RDBSS issues this call in response to receiving an <a href="/windows-hardware/drivers/ifs/irp-mj-device-control" data-raw-source="[&lt;strong&gt;IRP_MJ_DEVICE_CONTROL&lt;/strong&gt;](./irp-mj-device-control.md)"><strong>IRP_MJ_DEVICE_CONTROL</strong></a>, <a href="/windows-hardware/drivers/ifs/irp-mj-file-system-control" data-raw-source="[&lt;strong&gt;IRP_MJ_FILE_SYSTEM_CONTROL&lt;/strong&gt;](./irp-mj-file-system-control.md)"><strong>IRP_MJ_FILE_SYSTEM_CONTROL</strong></a>, or <a href="/windows-hardware/drivers/ifs/irp-mj-internal-device-control" data-raw-source="[&lt;strong&gt;IRP_MJ_INTERNAL_DEVICE_CONTROL&lt;/strong&gt;](./irp-mj-internal-device-control.md)"><strong>IRP_MJ_INTERNAL_DEVICE_CONTROL</strong></a> on a device FCB.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_extendfile_calldown" data-raw-source="[&lt;strong&gt;MRxExtendForCache&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_extendfile_calldown)"><strong>MRxExtendForCache</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector extend a file when the file is being cached by the cache manager.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxextendfornoncache" data-raw-source="[&lt;strong&gt;MRxExtendForNonCache&lt;/strong&gt;](./mrxextendfornoncache.md)"><strong>MRxExtendForNonCache</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector extend a file when the file is not being cached by the cache manager.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_extract_netroot_name" data-raw-source="[&lt;strong&gt;MRxExtractNetRootName&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_extract_netroot_name)"><strong>MRxExtractNetRootName</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector extract the name of the NET_ROOT from a given pathname.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_finalize_net_root_calldown" data-raw-source="[&lt;strong&gt;MRxFinalizeNetRoot&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_finalize_net_root_calldown)"><strong>MRxFinalizeNetRoot</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector finalize a NET_ROOT object.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_finalize_srvcall_calldown" data-raw-source="[&lt;strong&gt;MRxFinalizeSrvCall&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_finalize_srvcall_calldown)"><strong>MRxFinalizeSrvCall</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector finalize a SRV_CALL structure used for establishing connection with a server.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_finalize_v_net_root_calldown" data-raw-source="[&lt;strong&gt;MRxFinalizeVNetRoot&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_finalize_v_net_root_calldown)"><strong>MRxFinalizeVNetRoot</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector finalize a V_NET_ROOT object.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxflush" data-raw-source="[&lt;strong&gt;MRxFlush&lt;/strong&gt;](./mrxflush.md)"><strong>MRxFlush</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector flush a file system object. RDBSS issues this call in response to receiving an <a href="/windows-hardware/drivers/ifs/irp-mj-flush-buffers" data-raw-source="[&lt;strong&gt;IRP_MJ_FLUSH_BUFFERS&lt;/strong&gt;](./irp-mj-flush-buffers.md)"><strong>IRP_MJ_FLUSH_BUFFERS</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_forceclosed_calldown" data-raw-source="[&lt;strong&gt;MRxForceClosed&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_forceclosed_calldown)"><strong>MRxForceClosed</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector force a close. This routine is called when the condition of the SRV_OPEN structure is bad or the SRV_OPEN structure is marked as closed.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_get_connection_id" data-raw-source="[&lt;strong&gt;MRxGetConnectionId&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_get_connection_id)"><strong>MRxGetConnectionId</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector return a connection ID for the connection which can be used for handling multiple sessions. If connection IDs are supported by the network mini-redirector, then the returned connection ID is appended to the connection structures stored in the name table. RDBSS considers the connection ID an opaque blob, and does a byte-by-byte comparison of the connection ID blob while looking up the net-name table for a given name.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_is_lock_realizable" data-raw-source="[&lt;strong&gt;MRxIsLockRealizable&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_is_lock_realizable)"><strong>MRxIsLockRealizable</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector indicate whether byte-range locks are supported on specific NET_ROOT structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_chkdir_calldown" data-raw-source="[&lt;strong&gt;MRxIsValidDirectory&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_chkdir_calldown)"><strong>MRxIsValidDirectory</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector indicate if a path is a valid directory.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxlowiosubmit-lowio-op-exclusivelock-" data-raw-source="[&lt;strong&gt;MRxLowIOSubmit[LOWIO_OP_EXCLUSIVELOCK]&lt;/strong&gt;](./mrxlowiosubmit-lowio-op-exclusivelock-.md)"><strong>MRxLowIOSubmit[LOWIO_OP_EXCLUSIVELOCK]</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector open an exclusive lock on a file object. RDBSS issues this call in response to receiving an <a href="/windows-hardware/drivers/ifs/irp-mj-lock-control" data-raw-source="[&lt;strong&gt;IRP_MJ_LOCK_CONTROL&lt;/strong&gt;](./irp-mj-lock-control.md)"><strong>IRP_MJ_LOCK_CONTROL</strong></a> with a minor code of IRP_MN_LOCK and when <strong>IrpSp-&gt;Flags</strong> has the SL_EXCLUSIVE_LOCK bit set.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxlowiosubmit-lowio-op-fsctl-" data-raw-source="[&lt;strong&gt;MRxLowIOSubmit[LOWIO_OP_FSCTL]&lt;/strong&gt;](./mrxlowiosubmit-lowio-op-fsctl-.md)"><strong>MRxLowIOSubmit[LOWIO_OP_FSCTL]</strong></a></td>
<td align="left"><p>RDBSS calls this routine to pass a file system control request to the network mini-redirector. RDBSS issues this call in response to receiving an <a href="/windows-hardware/drivers/ifs/irp-mj-file-system-control" data-raw-source="[&lt;strong&gt;IRP_MJ_FILE_SYSTEM_CONTROL&lt;/strong&gt;](./irp-mj-file-system-control.md)"><strong>IRP_MJ_FILE_SYSTEM_CONTROL</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxlowiosubmit-lowio-op-ioctl-" data-raw-source="[&lt;strong&gt;MRxLowIOSubmit[LOWIO_OP_IOCTL]&lt;/strong&gt;](./mrxlowiosubmit-lowio-op-ioctl-.md)"><strong>MRxLowIOSubmit[LOWIO_OP_IOCTL]</strong></a></td>
<td align="left"><p>RDBSS calls this routine to pass an I/O system control request to the network mini-redirector. RDBSS issues this call in response to receiving an <a href="/windows-hardware/drivers/ifs/irp-mj-device-control" data-raw-source="[&lt;strong&gt;IRP_MJ_DEVICE_CONTROL&lt;/strong&gt;](./irp-mj-device-control.md)"><strong>IRP_MJ_DEVICE_CONTROL</strong></a> or <a href="/windows-hardware/drivers/ifs/irp-mj-internal-device-control" data-raw-source="[&lt;strong&gt;IRP_MJ_INTERNAL_DEVICE_CONTROL&lt;/strong&gt;](./irp-mj-internal-device-control.md)"><strong>IRP_MJ_INTERNAL_DEVICE_CONTROL</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxlowiosubmit-lowio-op-notify-change-directory-" data-raw-source="[&lt;strong&gt;MRxLowIOSubmit[LOWIO_OP_NOTIFY_CHANGE_DIRECTORY]&lt;/strong&gt;](./mrxlowiosubmit-lowio-op-notify-change-directory-.md)"><strong>MRxLowIOSubmit[LOWIO_OP_NOTIFY_CHANGE_DIRECTORY]</strong></a></td>
<td align="left"><p>RDBSS calls this routine to issue a request to the network mini-redirector for a directory change notification operation. RDBSS issues this call in response to receiving an <a href="/windows-hardware/drivers/ifs/irp-mj-directory-control" data-raw-source="[&lt;strong&gt;IRP_MJ_DIRECTORY_CONTROL&lt;/strong&gt;](./irp-mj-directory-control.md)"><strong>IRP_MJ_DIRECTORY_CONTROL</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxlowiosubmit-lowio-op-read-" data-raw-source="[&lt;strong&gt;MRxLowIOSubmit[LOWIO_OP_READ]&lt;/strong&gt;](./mrxlowiosubmit-lowio-op-read-.md)"><strong>MRxLowIOSubmit[LOWIO_OP_READ]</strong></a></td>
<td align="left"><p>RDBSS calls this routine to issue a read request to the network mini-redirector. RDBSS issues this call in response to receiving an <a href="/windows-hardware/drivers/ifs/irp-mj-read" data-raw-source="[&lt;strong&gt;IRP_MJ_READ&lt;/strong&gt;](./irp-mj-read.md)"><strong>IRP_MJ_READ</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxlowiosubmit-lowio-op-sharedlock-" data-raw-source="[&lt;strong&gt;MRxLowIOSubmit[LOWIO_OP_SHAREDLOCK]&lt;/strong&gt;](./mrxlowiosubmit-lowio-op-sharedlock-.md)"><strong>MRxLowIOSubmit[LOWIO_OP_SHAREDLOCK]</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network redirector open a shared lock on a file object. RDBSS issues this call in response to receiving an <a href="/windows-hardware/drivers/ifs/irp-mj-lock-control" data-raw-source="[&lt;strong&gt;IRP_MJ_LOCK_CONTROL&lt;/strong&gt;](./irp-mj-lock-control.md)"><strong>IRP_MJ_LOCK_CONTROL</strong></a> with a minor code of IRP_MN_LOCK and when <strong>IrpSp-&gt;Flags</strong> has the SL_EXCLUSIVE_LOCK bit set.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxlowiosubmit-lowio-op-unlock-" data-raw-source="[&lt;strong&gt;MRxLowIOSubmit[LOWIO_OP_UNLOCK]&lt;/strong&gt;](./mrxlowiosubmit-lowio-op-unlock-.md)"><strong>MRxLowIOSubmit[LOWIO_OP_UNLOCK]</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector remove a single lock on a file object. RDBSS issues this call in response to receiving an IRP_MJ_LOCK_CONTROL with a minor code of IRP_MN_UNLOCK_SINGLE.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxlowiosubmit-lowio-op-unlock-multiple-" data-raw-source="[&lt;strong&gt;MRxLowIOSubmit[LOWIO_OP_UNLOCK_MULTIPLE]&lt;/strong&gt;](./mrxlowiosubmit-lowio-op-unlock-multiple-.md)"><strong>MRxLowIOSubmit[LOWIO_OP_UNLOCK_MULTIPLE]</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector remove multiple locks held on a file object. RDBSS issues this call in response to receiving an IRP_MJ_LOCK_CONTROL with a minor code of IRP_MN_UNLOCK_ALL or IRP_MN_UNLOCK_ALL_BY_KEY. The ranges to be unlocked are specified in the <strong>LowIoContext.ParamsFor.Locks.LockList</strong> member of the RX_CONTEXT.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxlowiosubmit-lowio-op-write-" data-raw-source="[&lt;strong&gt;MRxLowIOSubmit[LOWIO_OP_WRITE]&lt;/strong&gt;](./mrxlowiosubmit-lowio-op-write-.md)"><strong>MRxLowIOSubmit[LOWIO_OP_WRITE]</strong></a></td>
<td align="left"><p>RDBSS calls this routine to issue a write request to the network mini-redirector. RDBSS issues this call in response to receiving an <a href="/windows-hardware/drivers/ifs/irp-mj-write" data-raw-source="[&lt;strong&gt;IRP_MJ_WRITE&lt;/strong&gt;](./irp-mj-write.md)"><strong>IRP_MJ_WRITE</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_preparse_name" data-raw-source="[&lt;strong&gt;MRxPreparseName&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_preparse_name)"><strong>MRxPreparseName</strong></a></td>
<td align="left"><p>RDBSS calls this routine to give a network mini-redirector the opportunity to preparse a name.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxquerydirectory" data-raw-source="[&lt;strong&gt;MRxQueryDirectory&lt;/strong&gt;](./mrxquerydirectory.md)"><strong>MRxQueryDirectory</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query information on a file directory system object.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxqueryeainfo" data-raw-source="[&lt;strong&gt;MRxQueryEaInfo&lt;/strong&gt;](./mrxqueryeainfo.md)"><strong>MRxQueryEaInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query extended attribute information on a file system object. RDBSS issues this call in response to receiving an <a href="/windows-hardware/drivers/ifs/irp-mj-query-ea" data-raw-source="[&lt;strong&gt;IRP_MJ_QUERY_EA&lt;/strong&gt;](./irp-mj-query-ea.md)"><strong>IRP_MJ_QUERY_EA</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxqueryfileinfo" data-raw-source="[&lt;strong&gt;MRxQueryFileInfo&lt;/strong&gt;](./mrxqueryfileinfo.md)"><strong>MRxQueryFileInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query file information on a file system object. RDBSS issues this call in response to receiving an <a href="/windows-hardware/drivers/ifs/irp-mj-query-information" data-raw-source="[&lt;strong&gt;IRP_MJ_QUERY_INFORMATION&lt;/strong&gt;](./irp-mj-query-information.md)"><strong>IRP_MJ_QUERY_INFORMATION</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxqueryquotainfo" data-raw-source="[&lt;strong&gt;MRxQueryQuotaInfo&lt;/strong&gt;](./mrxqueryquotainfo.md)"><strong>MRxQueryQuotaInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query quota information on a file system object. RDBSS issues this call in response to receiving an <a href="/windows-hardware/drivers/ifs/irp-mj-query-quota" data-raw-source="[&lt;strong&gt;IRP_MJ_QUERY_QUOTA&lt;/strong&gt;](./irp-mj-query-quota.md)"><strong>IRP_MJ_QUERY_QUOTA</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxquerysdinfo" data-raw-source="[&lt;strong&gt;MRxQuerySdInfo&lt;/strong&gt;](./mrxquerysdinfo.md)"><strong>MRxQuerySdInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query security descriptor information on a file system object. RDBSS issues this call in response to receiving an <a href="/windows-hardware/drivers/ifs/irp-mj-query-security" data-raw-source="[&lt;strong&gt;IRP_MJ_QUERY_SECURITY&lt;/strong&gt;](./irp-mj-query-security.md)"><strong>IRP_MJ_QUERY_SECURITY</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxqueryvolumeinfo" data-raw-source="[&lt;strong&gt;MRxQueryVolumeInfo&lt;/strong&gt;](./mrxqueryvolumeinfo.md)"><strong>MRxQueryVolumeInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query volume information. RDBSS issues this call in response to receiving an <a href="/windows-hardware/drivers/ifs/irp-mj-query-volume-information" data-raw-source="[&lt;strong&gt;IRP_MJ_QUERY_VOLUME_INFORMATION&lt;/strong&gt;](./irp-mj-query-volume-information.md)"><strong>IRP_MJ_QUERY_VOLUME_INFORMATION</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxseteainfo" data-raw-source="[&lt;strong&gt;MRxSetEaInfo&lt;/strong&gt;](./mrxseteainfo.md)"><strong>MRxSetEaInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set extended attribute information on a file system object. RDBSS issues this call in response to receiving an <a href="/windows-hardware/drivers/ifs/irp-mj-set-ea" data-raw-source="[&lt;strong&gt;IRP_MJ_SET_EA&lt;/strong&gt;](./irp-mj-set-ea.md)"><strong>IRP_MJ_SET_EA</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxsetfileinfo" data-raw-source="[&lt;strong&gt;MRxSetFileInfo&lt;/strong&gt;](./mrxsetfileinfo.md)"><strong>MRxSetFileInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set file information on a file system object. RDBSS issues this call in response to receiving an <a href="/windows-hardware/drivers/ifs/irp-mj-set-information" data-raw-source="[&lt;strong&gt;IRP_MJ_SET_INFORMATION&lt;/strong&gt;](./irp-mj-set-information.md)"><strong>IRP_MJ_SET_INFORMATION</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxsetfileinfoatcleanup" data-raw-source="[&lt;strong&gt;MRxSetFileInfoAtCleanup&lt;/strong&gt;](./mrxsetfileinfoatcleanup.md)"><strong>MRxSetFileInfoAtCleanup</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set file information on a file system object at cleanup. RDBSS issues this call during cleanup when an application closes a handle but before the file object is closed by the I/O Manager.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxsetquotainfo" data-raw-source="[&lt;strong&gt;MRxSetQuotaInfo&lt;/strong&gt;](./mrxsetquotainfo.md)"><strong>MRxSetQuotaInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set quota information on a file system object. RDBSS issues this call in response to receiving an <a href="/windows-hardware/drivers/ifs/irp-mj-set-quota" data-raw-source="[&lt;strong&gt;IRP_MJ_SET_QUOTA&lt;/strong&gt;](./irp-mj-set-quota.md)"><strong>IRP_MJ_SET_QUOTA</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxsetsdinfo" data-raw-source="[&lt;strong&gt;MRxSetSdInfo&lt;/strong&gt;](./mrxsetsdinfo.md)"><strong>MRxSetSdInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set security descriptor information on a file system object. RDBSS issues this call in response to receiving an <a href="/windows-hardware/drivers/ifs/irp-mj-set-security" data-raw-source="[&lt;strong&gt;IRP_MJ_SET_SECURITY&lt;/strong&gt;](./irp-mj-set-security.md)"><strong>IRP_MJ_SET_SECURITY</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxsetvolumeinfo" data-raw-source="[&lt;strong&gt;MRxSetVolumeInfo&lt;/strong&gt;](./mrxsetvolumeinfo.md)"><strong>MRxSetVolumeInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set volume information. RDBSS issues this call in response to receiving an <a href="/windows-hardware/drivers/ifs/irp-mj-set-volume-information" data-raw-source="[&lt;strong&gt;IRP_MJ_SET_VOLUME_INFORMATION&lt;/strong&gt;](./irp-mj-set-volume-information.md)"><strong>IRP_MJ_SET_VOLUME_INFORMATION</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxshouldtrytocollapsethisopen" data-raw-source="[&lt;strong&gt;MRxShouldTryToCollapseThisOpen&lt;/strong&gt;](./mrxshouldtrytocollapsethisopen.md)"><strong>MRxShouldTryToCollapseThisOpen</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector indicate if RDBSS should try and collapse an open request onto an existing file system object.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_srvcall_winner_notify" data-raw-source="[&lt;strong&gt;MRxSrvCallWinnerNotify&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_srvcall_winner_notify)"><strong>MRxSrvCallWinnerNotify</strong></a></td>
<td align="left"><p>This routine was originally designed to be called by RDBSS to notify a network mini-redirector that it was "the winner" when multiple redirectors could fulfill the request. The winning network mini-redirector is expected to create the SRV_CALL structure and establish a connection with the server.</p>
<p>Under the current implementation of RDBSS, each network mini-redirector has its own copy of RDBSS, so there are no competing network redirectors at the RDBSS layer. This routine is called after every request to create a SRV_CALL structure.</p>
<p>When multiple redirectors are installed for handling the same Universal Naming Convention (UNC) namespace, the redirector to service a request is chosen by the Multiple UNC Provider (MUP) based on the order of redirectors specified in the registry.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_calldown_ctx" data-raw-source="[&lt;strong&gt;MRxStart&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_calldown_ctx)"><strong>MRxStart</strong></a></td>
<td align="left"><p>RDBSS calls this routine to start the network mini-redirector.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxstop" data-raw-source="[&lt;strong&gt;MRxStop&lt;/strong&gt;](./mrxstop.md)"><strong>MRxStop</strong></a></td>
<td align="left"><p>RDBSS calls this routine to stop the network mini-redirector.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxtruncate" data-raw-source="[&lt;strong&gt;MRxTruncate&lt;/strong&gt;](./mrxtruncate.md)"><strong>MRxTruncate</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector truncate a file system object.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxzeroextend" data-raw-source="[&lt;strong&gt;MRxZeroExtend&lt;/strong&gt;](./mrxzeroextend.md)"><strong>MRxZeroExtend</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector extend a file system object filling the file with zeros on cleanup if the file size is greater than the valid data length of the FCB.</p></td>
</tr>
</tbody>
</table>

 

