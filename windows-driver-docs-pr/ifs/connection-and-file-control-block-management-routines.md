---
title: Connection and File Control Block Management Routines
description: Connection and File Control Block Management Routines
keywords:
- blocks WDK RDBSS
- data structures WDK file systems
- RDBSS WDK file systems , connection and file structures
- Redirected Drive Buffering Subsystem WDK file systems , connection and file structures
- connection structures WDK RDBSS
- file structures WDK RDBSS
- structures WDK RDBSS
- connection information WDK RDBSS
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxcreatenetfcb" data-raw-source="[&lt;strong&gt;RxCreateNetFcb&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxcreatenetfcb)"><strong>RxCreateNetFcb</strong></a></p></td>
<td align="left"><p>This routine allocates, initializes, and inserts a new FCB structure into the in-memory data structures for a NET_ROOT structure on which this FCB is being opened. The structure allocated has space for a SRV_OPEN and an FOBX structure. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxcreatenetfobx" data-raw-source="[&lt;strong&gt;RxCreateNetFobx&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxcreatenetfobx)"><strong>RxCreateNetFobx</strong></a></p></td>
<td align="left"><p>This routine allocates, initializes, and inserts a new file object extension (FOBX) structure. Network mini-redirectors should call this routine to create an FOBX at the end of a successful create operation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxcreatenetroot" data-raw-source="[&lt;strong&gt;RxCreateNetRoot&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxcreatenetroot)"><strong>RxCreateNetRoot</strong></a></p></td>
<td align="left"><p>This routine builds a node that represents a NET_ROOT structure and inserts the name into the net name table on the associated device object. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxcreatesrvcall" data-raw-source="[&lt;strong&gt;RxCreateSrvCall&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxcreatesrvcall)"><strong>RxCreateSrvCall</strong></a></p></td>
<td align="left"><p>This routine builds a node that represents a server call context and inserts the name into the net name table maintained by RDBSS. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxcreatesrvopen" data-raw-source="[&lt;strong&gt;RxCreateSrvOpen&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxcreatesrvopen)"><strong>RxCreateSrvOpen</strong></a></p></td>
<td align="left"><p>This routine allocates, initializes, and inserts a new SRV_OPEN structure into the in-memory data structures used by RDBSS. If a new structure must be allocated, it has space for an FOBX structure. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxcreatevnetroot" data-raw-source="[&lt;strong&gt;RxCreateVNetRoot&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxcreatevnetroot)"><strong>RxCreateVNetRoot</strong></a></p></td>
<td align="left"><p>This routine builds a node that represents a V_NET_ROOT structure and inserts the name into the net name table. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxdereference" data-raw-source="[&lt;strong&gt;RxDereference&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxdereference)"><strong>RxDereference</strong></a></p></td>
<td align="left"><p>This routine decrements the reference count on an instance of several of the reference-counted data structures used by RDBSS.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxfinalizeconnection" data-raw-source="[&lt;strong&gt;RxFinalizeConnection&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxfinalizeconnection)"><strong>RxFinalizeConnection</strong></a></p></td>
<td align="left"><p>This routine deletes a connection to a share. Any files open on the connection are closed depending on the level of force specified. The network mini-redirector might choose to keep the transport connection open for performance reasons, unless some option is specified to force a close of the connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxfinalizenetfcb" data-raw-source="[&lt;strong&gt;RxFinalizeNetFcb&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxfinalizenetfcb)"><strong>RxFinalizeNetFcb</strong></a></p></td>
<td align="left"><p>This routine finalizes the given FCB structure. The caller must have an exclusive lock on the NET_ROOT structure associated with this FCB. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxfinalizenetfobx" data-raw-source="[&lt;strong&gt;RxFinalizeNetFobx&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxfinalizenetfobx)"><strong>RxFinalizeNetFobx</strong></a></p></td>
<td align="left"><p>This routine finalizes the given FOBX structure. The caller must have an exclusive lock on the FCB associated with this FOBX. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxfinalizenetroot" data-raw-source="[&lt;strong&gt;RxFinalizeNetRoot&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxfinalizenetroot)"><strong>RxFinalizeNetRoot</strong></a></p></td>
<td align="left"><p>This routine finalizes the given NET_ROOT structure. The caller should have exclusive lock on the NetName table of the device object associated with this NET_ROOT structure (through the SRV_CALL structure). This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxfinalizesrvcall" data-raw-source="[&lt;strong&gt;RxFinalizeSrvCall&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxfinalizesrvcall)"><strong>RxFinalizeSrvCall</strong></a></p></td>
<td align="left"><p>This routine finalizes the given SRV_CALL structure. The caller should have exclusive access to the lock on the NetName table of the device object associated with this SRV_CALL structure. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxfinalizesrvopen" data-raw-source="[&lt;strong&gt;RxFinalizeSrvOpen&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxfinalizesrvopen)"><strong>RxFinalizeSrvOpen</strong></a></p></td>
<td align="left"><p>This routine finalizes the given SRV_OPEN structure. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxfinalizevnetroot" data-raw-source="[&lt;strong&gt;RxFinalizeVNetRoot&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxfinalizevnetroot)"><strong>RxFinalizeVNetRoot</strong></a></p></td>
<td align="left"><p>This routine finalizes the given V_NET_ROOT structure. The caller must have exclusive access to the lock on the NetName table of the device object associated with this V_NET_ROOT structure. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxfinishfcbinitialization" data-raw-source="[&lt;strong&gt;RxFinishFcbInitialization&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxfinishfcbinitialization)"><strong>RxFinishFcbInitialization</strong></a></p></td>
<td align="left"><p>This routine is used to finish initializing an FCB after the successful completion of a create operation by the network mini-redirector.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxforcefinalizeallvnetroots" data-raw-source="[&lt;strong&gt;RxForceFinalizeAllVNetRoots&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxforcefinalizeallvnetroots)"><strong>RxForceFinalizeAllVNetRoots</strong></a></p></td>
<td align="left"><p>This routine force finalizes all of the V_NET_ROOT structures associated with a given NET_ROOT structure. The caller must have exclusive access to the lock on the NetName table of the device object associated with this V_NET_ROOT structure. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxgetfilesizewithlock" data-raw-source="[&lt;strong&gt;RxGetFileSizeWithLock&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxgetfilesizewithlock)"><strong>RxGetFileSizeWithLock</strong></a></p></td>
<td align="left"><p>This routine gets the file size in the FCB header, using a lock to ensure that the 64-bit value is read consistently.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxinferfiletype" data-raw-source="[&lt;strong&gt;RxInferFileType&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxinferfiletype)"><strong>RxInferFileType</strong></a></p></td>
<td align="left"><p>This routine tries to infer the file type (directory or non-directory) from a field in the RX_CONTEXT structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxlockenumerator" data-raw-source="[&lt;strong&gt;RxLockEnumerator&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxlockenumerator)"><strong>RxLockEnumerator</strong></a></p></td>
<td align="left"><p>This routine is called from a network mini-redirector to enumerate the file locks on an FCB.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxpdereferenceandfinalizenetfcb" data-raw-source="[&lt;strong&gt;RxpDereferenceAndFinalizeNetFcb&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxpdereferenceandfinalizenetfcb)"><strong>RxpDereferenceAndFinalizeNetFcb</strong></a></td>
<td align="left"><p>This routine decrements the reference count and finalizes an FCB.</p>
<p>This routine is only available on Windows Server 2003 Service Pack 1 (SP1) and later.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxpdereferencenetfcb" data-raw-source="[&lt;strong&gt;RxpDereferenceNetFcb&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxpdereferencenetfcb)"><strong>RxpDereferenceNetFcb</strong></a></p></td>
<td align="left"><p>This routine decrements the reference count on an FCB.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxpreferencenetfcb" data-raw-source="[&lt;strong&gt;RxpReferenceNetFcb&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxpreferencenetfcb)"><strong>RxpReferenceNetFcb</strong></a></p></td>
<td align="left"><p>This routine increments the reference count on an FCB.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxreference" data-raw-source="[&lt;strong&gt;RxReference&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxreference)"><strong>RxReference</strong></a></p></td>
<td align="left"><p>This routine increments the reference count on an instance of several of the reference-counted data structures used by RDBSS.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxsetsrvcalldomainname" data-raw-source="[&lt;strong&gt;RxSetSrvCallDomainName&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxsetsrvcalldomainname)"><strong>RxSetSrvCallDomainName</strong></a></p></td>
<td align="left"><p>This routine sets the domain name associated with any given server (SRV_CALL structure).</p></td>
</tr>
</tbody>
</table>

 

Note that a number of macros are also defined that provide wrappers around the [**RxReference**](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxreference) and [**RxDeference**](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxdereference) routines for debugging. For more information about these macros, see [Diagnostics and Debugging](diagnostics-and-debugging.md).

