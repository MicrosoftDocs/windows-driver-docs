---
title: Connection and File Control Block Management Routines
author: windows-driver-content
description: Connection and File Control Block Management Routines
ms.assetid: e56c0cba-7352-4964-b067-57bc90c7f911
keywords: ["blocks WDK RDBSS", "data structures WDK file systems", "RDBSS WDK file systems , connection and file structures", "Redirected Drive Buffering Subsystem WDK file systems , connection and file structures", "connection structures WDK RDBSS", "file structures WDK RDBSS", "structures WDK RDBSS", "connection information WDK RDBSS"]
---

# Connection and File Control Block Management Routines


The connection and file control block management routines are used by RDBSS to manage structures used to represent connections and file control blocks.

RDBSS provides the following routines for connection and file control block management that can be used by network mini-redirector drivers:

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
<td align="left"><p>[<strong>RxCreateNetFcb</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554356)</p></td>
<td align="left"><p>This routine allocates, initializes, and inserts a new FCB structure into the in-memory data structures for a NET_ROOT structure on which this FCB is being opened. The structure allocated has space for a SRV_OPEN and an FOBX structure. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCreateNetFobx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554358)</p></td>
<td align="left"><p>This routine allocates, initializes, and inserts a new file object extension (FOBX) structure. Network mini-redirectors should call this routine to create an FOBX at the end of a successful create operation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxCreateNetRoot</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554366)</p></td>
<td align="left"><p>This routine builds a node that represents a NET_ROOT structure and inserts the name into the net name table on the associated device object. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCreateSrvCall</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554370)</p></td>
<td align="left"><p>This routine builds a node that represents a server call context and inserts the name into the net name table maintained by RDBSS. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxCreateSrvOpen</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554376)</p></td>
<td align="left"><p>This routine allocates, initializes, and inserts a new SRV_OPEN structure into the in-memory data structures used by RDBSS. If a new structure must be allocated, it has space for an FOBX structure. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCreateVNetRoot</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554380)</p></td>
<td align="left"><p>This routine builds a node that represents a V_NET_ROOT structure and inserts the name into the net name table. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxDereference</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554388)</p></td>
<td align="left"><p>This routine decrements the reference count on an instance of several of the reference-counted data structures used by RDBSS.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxFinalizeConnection</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554409)</p></td>
<td align="left"><p>This routine deletes a connection to a share. Any files open on the connection are closed depending on the level of force specified. The network mini-redirector might choose to keep the transport connection open for performance reasons, unless some option is specified to force a close of the connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxFinalizeNetFcb</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554412)</p></td>
<td align="left"><p>This routine finalizes the given FCB structure. The caller must have an exclusive lock on the NET_ROOT structure associated with this FCB. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxFinalizeNetFobx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554418)</p></td>
<td align="left"><p>This routine finalizes the given FOBX structure. The caller must have an exclusive lock on the FCB associated with this FOBX. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxFinalizeNetRoot</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554421)</p></td>
<td align="left"><p>This routine finalizes the given NET_ROOT structure. The caller should have exclusive lock on the NetName table of the device object associated with this NET_ROOT structure (through the SRV_CALL structure). This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxFinalizeSrvCall</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554426)</p></td>
<td align="left"><p>This routine finalizes the given SRV_CALL structure. The caller should have exclusive access to the lock on the NetName table of the device object associated with this SRV_CALL structure. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxFinalizeSrvOpen</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554432)</p></td>
<td align="left"><p>This routine finalizes the given SRV_OPEN structure. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxFinalizeVNetRoot</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554450)</p></td>
<td align="left"><p>This routine finalizes the given V_NET_ROOT structure. The caller must have exclusive access to the lock on the NetName table of the device object associated with this V_NET_ROOT structure. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxFinishFcbInitialization</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554454)</p></td>
<td align="left"><p>This routine is used to finish initializing an FCB after the successful completion of a create operation by the network mini-redirector.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxForceFinalizeAllVNetRoots</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554463)</p></td>
<td align="left"><p>This routine force finalizes all of the V_NET_ROOT structures associated with a given NET_ROOT structure. The caller must have exclusive access to the lock on the NetName table of the device object associated with this V_NET_ROOT structure. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxGetFileSizeWithLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554478)</p></td>
<td align="left"><p>This routine gets the file size in the FCB header, using a lock to ensure that the 64-bit value is read consistently.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxInferFileType</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554493)</p></td>
<td align="left"><p>This routine tries to infer the file type (directory or non-directory) from a field in the RX_CONTEXT structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxLockEnumerator</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554511)</p></td>
<td align="left"><p>This routine is called from a network mini-redirector to enumerate the file locks on an FCB.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>RxpDereferenceAndFinalizeNetFcb</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554603)</td>
<td align="left"><p>This routine decrements the reference count and finalizes an FCB.</p>
<p>This routine is only available on Windows Server 2003 Service Pack 1 (SP1) and later.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxpDereferenceNetFcb</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554608)</p></td>
<td align="left"><p>This routine decrements the reference count on an FCB.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxpReferenceNetFcb</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554627)</p></td>
<td align="left"><p>This routine increments the reference count on an FCB.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxReference</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554688)</p></td>
<td align="left"><p>This routine increments the reference count on an instance of several of the reference-counted data structures used by RDBSS.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxSetSrvCallDomainName</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554728)</p></td>
<td align="left"><p>This routine sets the domain name associated with any given server (SRV_CALL structure).</p></td>
</tr>
</tbody>
</table>

 

Note that a number of macros are also defined that provide wrappers around the [**RxReference**](https://msdn.microsoft.com/library/windows/hardware/ff554688) and [**RxDeference**](https://msdn.microsoft.com/library/windows/hardware/ff554388) routines for debugging. For more information about these macros, see [Diagnostics and Debugging](diagnostics-and-debugging.md).

 

 


--------------------


