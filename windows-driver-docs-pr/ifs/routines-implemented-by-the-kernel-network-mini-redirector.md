---
title: Routines Implemented by the Kernel Network Mini-Redirector
description: Routines Implemented by the Kernel Network Mini-Redirector
ms.assetid: bd1a8989-100d-4b7b-9a61-521af6433b00
keywords: ["mini-redirectors WDK , routines implemented"]
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
<td align="left">[<strong>MRxAreFilesAliased</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549838)</td>
<td align="left"><p>RDBSS calls this routine to query the network mini-redirector if two file control block (FCB) structures represent the same file. RDBSS calls this routine when processing two files that appear to be the same but have different names (an MS-DOS short name and a long name, for example).</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxCleanupFobx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549841)</td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector close a file system object extension structure. RDBSS issues this call in response to receiving an [<strong>IRP_MJ_CLEANUP</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548608) on a file object.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxCloseSrvOpen</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549845)</td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector close a SRV_OPEN structure.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxCollapseOpen</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549847)</td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector collapse an open file system request onto an existing SRV_OPEN.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxCompleteBufferingStateChangeRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549850)</td>
<td align="left"><p>RDBSS calls this routine to notify the network mini-redirector that a buffering state change request has been completed. For example, the SMB redirector uses this routine to send an oplock break response or to close the handle on an oplock break if the file is no longer in use. Byte range locks that need to be flushed out to the server are passed to the network mini-redirector in the <strong>LowIoContext.ParamsFor.Locks.LockList</strong> member of the RX_CONTEXT structure.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxComputeNewBufferingState</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549856)</td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector compute a new buffering state change.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549862)</td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector create a file system object. RDBSS issues this call in response to receiving an [<strong>IRP_MJ_CREATE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548630).</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxCreateSrvCall</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549864)</td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector create a SRV_CALL structure and establish a connection with a server.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxCreateVNetRoot</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549869)</td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector create a V_NET_ROOT structure.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxDeallocateForFcb</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549871)</td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector deallocate an FCB. This call is in response to a request to close a file system object.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxDeallocateForFobx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549872)</td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector deallocate an FOBX structure. This call is in response to a request to close a file system object.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxDevFcbXXXControlFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549876)</td>
<td align="left"><p>RDBSS calls this routine to pass a device FCB control request to the network mini-redirector. RDBSS issues this call in response to receiving an [<strong>IRP_MJ_DEVICE_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548649), [<strong>IRP_MJ_FILE_SYSTEM_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548670), or [<strong>IRP_MJ_INTERNAL_DEVICE_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549241) on a device FCB.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxExtendForCache</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549878)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector extend a file when the file is being cached by the cache manager.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxExtendForNonCache</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549879)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector extend a file when the file is not being cached by the cache manager.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxExtractNetRootName</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550649)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector extract the name of the NET_ROOT from a given pathname.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxFinalizeNetRoot</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550653)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector finalize a NET_ROOT object.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxFinalizeSrvCall</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550656)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector finalize a SRV_CALL structure used for establishing connection with a server.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxFinalizeVNetRoot</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550663)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector finalize a V_NET_ROOT object.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxFlush</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550669)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector flush a file system object. RDBSS issues this call in response to receiving an [<strong>IRP_MJ_FLUSH_BUFFERS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549235).</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxForceClosed</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550677)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector force a close. This routine is called when the condition of the SRV_OPEN structure is bad or the SRV_OPEN structure is marked as closed.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxGetConnectionId</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550687)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector return a connection ID for the connection which can be used for handling multiple sessions. If connection IDs are supported by the network mini-redirector, then the returned connection ID is appended to the connection structures stored in the name table. RDBSS considers the connection ID an opaque blob, and does a byte-by-byte comparison of the connection ID blob while looking up the net-name table for a given name.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxIsLockRealizable</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550691)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector indicate whether byte-range locks are supported on specific NET_ROOT structure.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxIsValidDirectory</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550696)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector indicate if a path is a valid directory.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxLowIOSubmit[LOWIO_OP_EXCLUSIVELOCK]</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550703)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector open an exclusive lock on a file object. RDBSS issues this call in response to receiving an [<strong>IRP_MJ_LOCK_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549251) with a minor code of IRP_MN_LOCK and when <strong>IrpSp-&gt;Flags</strong> has the SL_EXCLUSIVE_LOCK bit set.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxLowIOSubmit[LOWIO_OP_FSCTL]</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550709)</td>
<td align="left"><p>RDBSS calls this routine to pass a file system control request to the network mini-redirector. RDBSS issues this call in response to receiving an [<strong>IRP_MJ_FILE_SYSTEM_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548670).</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxLowIOSubmit[LOWIO_OP_IOCTL]</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550715)</td>
<td align="left"><p>RDBSS calls this routine to pass an I/O system control request to the network mini-redirector. RDBSS issues this call in response to receiving an [<strong>IRP_MJ_DEVICE_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548649) or [<strong>IRP_MJ_INTERNAL_DEVICE_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549241).</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxLowIOSubmit[LOWIO_OP_NOTIFY_CHANGE_DIRECTORY]</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550721)</td>
<td align="left"><p>RDBSS calls this routine to issue a request to the network mini-redirector for a directory change notification operation. RDBSS issues this call in response to receiving an [<strong>IRP_MJ_DIRECTORY_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548658).</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxLowIOSubmit[LOWIO_OP_READ]</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550724)</td>
<td align="left"><p>RDBSS calls this routine to issue a read request to the network mini-redirector. RDBSS issues this call in response to receiving an [<strong>IRP_MJ_READ</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549327).</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxLowIOSubmit[LOWIO_OP_SHAREDLOCK]</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550734)</td>
<td align="left"><p>RDBSS calls this routine to request that a network redirector open a shared lock on a file object. RDBSS issues this call in response to receiving an [<strong>IRP_MJ_LOCK_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549251) with a minor code of IRP_MN_LOCK and when <strong>IrpSp-&gt;Flags</strong> has the SL_EXCLUSIVE_LOCK bit set.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxLowIOSubmit[LOWIO_OP_UNLOCK]</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550740)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector remove a single lock on a file object. RDBSS issues this call in response to receiving an IRP_MJ_LOCK_CONTROL with a minor code of IRP_MN_UNLOCK_SINGLE.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxLowIOSubmit[LOWIO_OP_UNLOCK_MULTIPLE]</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550745)</td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector remove multiple locks held on a file object. RDBSS issues this call in response to receiving an IRP_MJ_LOCK_CONTROL with a minor code of IRP_MN_UNLOCK_ALL or IRP_MN_UNLOCK_ALL_BY_KEY. The ranges to be unlocked are specified in the <strong>LowIoContext.ParamsFor.Locks.LockList</strong> member of the RX_CONTEXT.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxLowIOSubmit[LOWIO_OP_WRITE]</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550746)</td>
<td align="left"><p>RDBSS calls this routine to issue a write request to the network mini-redirector. RDBSS issues this call in response to receiving an [<strong>IRP_MJ_WRITE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549427).</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxPreparseName</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550750)</td>
<td align="left"><p>RDBSS calls this routine to give a network mini-redirector the opportunity to preparse a name.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxQueryDirectory</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550755)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query information on a file directory system object.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxQueryEaInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550759)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query extended attribute information on a file system object. RDBSS issues this call in response to receiving an [<strong>IRP_MJ_QUERY_EA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549279).</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxQueryFileInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550770)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query file information on a file system object. RDBSS issues this call in response to receiving an [<strong>IRP_MJ_QUERY_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549283).</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxQueryQuotaInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550773)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query quota information on a file system object. RDBSS issues this call in response to receiving an [<strong>IRP_MJ_QUERY_QUOTA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549293).</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxQuerySdInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550776)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query security descriptor information on a file system object. RDBSS issues this call in response to receiving an [<strong>IRP_MJ_QUERY_SECURITY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549298).</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxQueryVolumeInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550782)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query volume information. RDBSS issues this call in response to receiving an [<strong>IRP_MJ_QUERY_VOLUME_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549318).</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxSetEaInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550786)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set extended attribute information on a file system object. RDBSS issues this call in response to receiving an [<strong>IRP_MJ_SET_EA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549346).</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxSetFileInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550790)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set file information on a file system object. RDBSS issues this call in response to receiving an [<strong>IRP_MJ_SET_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549366).</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxSetFileInfoAtCleanup</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550796)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set file information on a file system object at cleanup. RDBSS issues this call during cleanup when an application closes a handle but before the file object is closed by the I/O Manager.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxSetQuotaInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550800)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set quota information on a file system object. RDBSS issues this call in response to receiving an [<strong>IRP_MJ_SET_QUOTA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549401).</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxSetSdInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550805)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set security descriptor information on a file system object. RDBSS issues this call in response to receiving an [<strong>IRP_MJ_SET_SECURITY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549407).</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxSetVolumeInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550810)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set volume information. RDBSS issues this call in response to receiving an [<strong>IRP_MJ_SET_VOLUME_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549415).</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxShouldTryToCollapseThisOpen</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550817)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector indicate if RDBSS should try and collapse an open request onto an existing file system object.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxSrvCallWinnerNotify</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550824)</td>
<td align="left"><p>This routine was originally designed to be called by RDBSS to notify a network mini-redirector that it was &quot;the winner&quot; when multiple redirectors could fulfill the request. The winning network mini-redirector is expected to create the SRV_CALL structure and establish a connection with the server.</p>
<p>Under the current implementation of RDBSS, each network mini-redirector has its own copy of RDBSS, so there are no competing network redirectors at the RDBSS layer. This routine is called after every request to create a SRV_CALL structure.</p>
<p>When multiple redirectors are installed for handling the same Universal Naming Convention (UNC) namespace, the redirector to service a request is chosen by the Multiple UNC Provider (MUP) based on the order of redirectors specified in the registry.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxStart</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550829)</td>
<td align="left"><p>RDBSS calls this routine to start the network mini-redirector.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxStop</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550833)</td>
<td align="left"><p>RDBSS calls this routine to stop the network mini-redirector.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxTruncate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550839)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector truncate a file system object.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxZeroExtend</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550844)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector extend a file system object filling the file with zeros on cleanup if the file size is greater than the valid data length of the FCB.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Routines%20Implemented%20by%20the%20Kernel%20Network%20Mini-Redirector%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




