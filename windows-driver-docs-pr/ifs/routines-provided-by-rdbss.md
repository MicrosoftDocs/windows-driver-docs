---
title: Routines Provided by RDBSS
description: Routines Provided by RDBSS
keywords:
- RDBSS WDK file systems , routines
- Redirected Drive Buffering Subsystem WDK file systems , routines
- routines WDK RDBSS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Routines Provided by RDBSS


## <span id="ddk_functions_provided_by_rdbss_if"></span><span id="DDK_FUNCTIONS_PROVIDED_BY_RDBSS_IF"></span>


The following routines are exported by RDBSS.

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
<td align="left"><p><a href="/windows-hardware/drivers/ddi/mrxfcb/nf-mrxfcb-rxacquireexclusivefcbresourceinmrx" data-raw-source="[&lt;strong&gt;RxAcquireExclusiveFcbResourceInMRx&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrxfcb/nf-mrxfcb-rxacquireexclusivefcbresourceinmrx)"><strong>RxAcquireExclusiveFcbResourceInMRx</strong></a></p></td>
<td align="left"><p>This resource acquisition routine acquires the File Control Block (FCB) resource in exclusive mode. This routine will wait for the FCB resource to be free, so this routine does not return control until the resource has been acquired. This routine acquires the FCB resource even if the RX_CONTEXT associated with this FCB has been canceled.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/mrxfcb/nf-mrxfcb-rxacquiresharedfcbresourceinmrx" data-raw-source="[&lt;strong&gt;RxAcquireSharedFcbResourceInMRx&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrxfcb/nf-mrxfcb-rxacquiresharedfcbresourceinmrx)"><strong>RxAcquireSharedFcbResourceInMRx</strong></a></p></td>
<td align="left"><p>This resource acquisition routine acquires the FCB resource in shared mode. This routine will wait for the FCB resource to be free if it was previously acquired exclusively, so this routine does not return control until the resource has been acquired. This routine acquires the FCB resource even if the RX_CONTEXT associated with this FCB has been canceled.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ddi/mrxfcb/nf-mrxfcb-rxacquiresharedfcbresourceinmrxex" data-raw-source="[&lt;strong&gt;RxAcquireSharedFcbResourceInMRxEx&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrxfcb/nf-mrxfcb-rxacquiresharedfcbresourceinmrxex)"><strong>RxAcquireSharedFcbResourceInMRxEx</strong></a></td>
<td align="left"><p>This resource acquisition routine acquires the FCB resource in shared mode. This routine will wait for the FCB resource to be freed if it was previously acquired exclusively. This routine does not return control until the resource has been acquired. This routine acquires the FCB resource even if the RX_CONTEXT associated with this FCB has been canceled.</p>
<p>This routine is only available on Windows Server 2003 Service Pack 1 (SP1) and later.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ifs/rxassert" data-raw-source="[&lt;strong&gt;RxAssert&lt;/strong&gt;](./rxassert.md)"><strong>RxAssert</strong></a></p></td>
<td align="left"><p>This routine sends an assert string in RDBSS checked builds to a kernel debugger if one is installed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/midatlax/nf-midatlax-rxassociatecontextwithmid" data-raw-source="[&lt;strong&gt;RxAssociateContextWithMid&lt;/strong&gt;](/windows-hardware/drivers/ddi/midatlax/nf-midatlax-rxassociatecontextwithmid)"><strong>RxAssociateContextWithMid</strong></a></p></td>
<td align="left"><p>This routine associates the supplied opaque context with an available multiplex ID (MID) from a MID_ATLAS data structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxtimer/nf-rxtimer-rxcanceltimerrequest" data-raw-source="[&lt;strong&gt;RxCancelTimerRequest&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxtimer/nf-rxtimer-rxcanceltimerrequest)"><strong>RxCancelTimerRequest</strong></a></p></td>
<td align="left"><p>This routine cancels a timer request. The request to be canceled is identified by the routine and context.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxceallocateirpwithmdl" data-raw-source="[&lt;strong&gt;RxCeAllocateIrpWithMDL&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxceallocateirpwithmdl)"><strong>RxCeAllocateIrpWithMDL</strong></a></p></td>
<td align="left"><p>This routine allocates an IRP for use by the connection engine and associates an MDL with the IRP.</p>
<p>This routine is only available on Windows XP.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcebuildaddress" data-raw-source="[&lt;strong&gt;RxCeBuildAddress&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcebuildaddress)"><strong>RxCeBuildAddress</strong></a></p></td>
<td align="left"><p>This routine associates a transport address with a transport binding.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcebuildconnection" data-raw-source="[&lt;strong&gt;RxCeBuildConnection&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcebuildconnection)"><strong>RxCeBuildConnection</strong></a></p></td>
<td align="left"><p>This routine establishes a connection between a local RDBSS connection address and a given remote address. This routine should be called in the context of a system worker thread.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcebuildconnectionovermultipletransports" data-raw-source="[&lt;strong&gt;RxCeBuildConnectionOverMultipleTransports&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcebuildconnectionovermultipletransports)"><strong>RxCeBuildConnectionOverMultipleTransports</strong></a></p></td>
<td align="left"><p>This routine establishes a connection between a local RDBSS connection address and a given remote address and supports multiple transports. A set of local addresses are specified and this routine attempts to connect to the target server using all of the transports associated with the local addresses. One connection is chosen as the winner depending on the connection options. This routine must be called in the context of a system worker thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcebuildtransport" data-raw-source="[&lt;strong&gt;RxCeBuildTransport&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcebuildtransport)"><strong>RxCeBuildTransport</strong></a></p></td>
<td align="left"><p>This routine binds an RDBSS transport to a specified transport name.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcebuildvc" data-raw-source="[&lt;strong&gt;RxCeBuildVC&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcebuildvc)"><strong>RxCeBuildVC</strong></a></p></td>
<td align="left"><p>This routine adds a virtual circuit to a specified connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcecancelconnectrequest" data-raw-source="[&lt;strong&gt;RxCeCancelConnectRequest&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcecancelconnectrequest)"><strong>RxCeCancelConnectRequest</strong></a></p></td>
<td align="left"><p>This routine cancels a previously issued connection request.</p>
<p>Note that this routine is not currently implemented.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcefreeirp" data-raw-source="[&lt;strong&gt;RxCeFreeIrp&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcefreeirp)"><strong>RxCeFreeIrp</strong></a></p></td>
<td align="left"><p>This routine frees an IRP used by the connection engine.</p>
<p>This routine is only available on Windows XP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxceinitiatevcdisconnect" data-raw-source="[&lt;strong&gt;RxCeInitiateVCDisconnect&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxceinitiatevcdisconnect)"><strong>RxCeInitiateVCDisconnect</strong></a></p></td>
<td align="left"><p>This routine initiates a disconnect on the virtual circuit. This routine must be called in the context of a system worker thread.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcequeryadapterstatus" data-raw-source="[&lt;strong&gt;RxCeQueryAdapterStatus&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcequeryadapterstatus)"><strong>RxCeQueryAdapterStatus</strong></a></p></td>
<td align="left"><p>This routine returns the ADAPTER_STATUS structure for a given transport.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcequeryinformation" data-raw-source="[&lt;strong&gt;RxCeQueryInformation&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcequeryinformation)"><strong>RxCeQueryInformation</strong></a></p></td>
<td align="left"><p>This routine queries for information about a given virtual circuit.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcequerytransportinformation" data-raw-source="[&lt;strong&gt;RxCeQueryTransportInformation&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcequerytransportinformation)"><strong>RxCeQueryTransportInformation</strong></a></p></td>
<td align="left"><p>This routine queries a given transport for information about the connection count and quality of service.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcesend" data-raw-source="[&lt;strong&gt;RxCeSend&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcesend)"><strong>RxCeSend</strong></a></p></td>
<td align="left"><p>This routine sends a transport service data unit (TSDU) along the specified connection on a virtual circuit.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcesenddatagram" data-raw-source="[&lt;strong&gt;RxCeSendDatagram&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcesenddatagram)"><strong>RxCeSendDatagram</strong></a></p></td>
<td align="left"><p>This routine sends a TSDU to a specified transport address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxceteardownaddress" data-raw-source="[&lt;strong&gt;RxCeTearDownAddress&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxceteardownaddress)"><strong>RxCeTearDownAddress</strong></a></p></td>
<td align="left"><p>This routine removes a transport address from a transport binding.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxceteardownconnection" data-raw-source="[&lt;strong&gt;RxCeTearDownConnection&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxceteardownconnection)"><strong>RxCeTearDownConnection</strong></a></p></td>
<td align="left"><p>This routine tears down a given connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxceteardowntransport" data-raw-source="[&lt;strong&gt;RxCeTearDownTransport&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxceteardowntransport)"><strong>RxCeTearDownTransport</strong></a></p></td>
<td align="left"><p>This routine unbinds from the transport specified.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxceteardownvc" data-raw-source="[&lt;strong&gt;RxCeTearDownVC&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxceteardownvc)"><strong>RxCeTearDownVC</strong></a></p></td>
<td align="left"><p>This routine tears down a virtual connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxchangebufferingstate" data-raw-source="[&lt;strong&gt;RxChangeBufferingState&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxchangebufferingstate)"><strong>RxChangeBufferingState</strong></a></p></td>
<td align="left"><p>This routine is called to process a buffering state change request.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxcompleterequest" data-raw-source="[&lt;strong&gt;RxCompleteRequest&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxcompleterequest)"><strong>RxCompleteRequest</strong></a></p></td>
<td align="left"><p>This routine is used to complete an IRP associated with an RX_CONTEXT structure. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxcompleterequest_real" data-raw-source="[&lt;strong&gt;RxCompleteRequest_Real&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxcompleterequest_real)"><strong>RxCompleteRequest_Real</strong></a></p></td>
<td align="left"><p>This routine is used to complete an IRP associated with an RX_CONTEXT structure. This routine should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/midatlax/nf-midatlax-rxcreatemidatlas" data-raw-source="[&lt;strong&gt;RxCreateMidAtlas&lt;/strong&gt;](/windows-hardware/drivers/ddi/midatlax/nf-midatlax-rxcreatemidatlas)"><strong>RxCreateMidAtlas</strong></a></p></td>
<td align="left"><p>This routine allocates a new instance of a MID_ATLAS data structure and initializes it. RDBSS uses the multiplex ID (MID) defined in this data structure as a way that both the network client (mini-redirector) and the server can distinguish between the concurrently active requests on any connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxcreatenetfcb" data-raw-source="[&lt;strong&gt;RxCreateNetFcb&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxcreatenetfcb)"><strong>RxCreateNetFcb</strong></a></p></td>
<td align="left"><p>This routine allocates, initializes, and inserts a new FCB structure into the in-memory data structures for a NET_ROOT structure on which this FCB is opened. The structure allocated has space for a SRV_OPEN and an FOBX structure. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxcreatenetfobx" data-raw-source="[&lt;strong&gt;RxCreateNetFobx&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxcreatenetfobx)"><strong>RxCreateNetFobx</strong></a></p></td>
<td align="left"><p>This routine allocates, initializes, and inserts a new file object extension (FOBX) structure. Network mini-redirectors should call this routine to create an FOBX at the end of a successful create operation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxcreatenetroot" data-raw-source="[&lt;strong&gt;RxCreateNetRoot&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxcreatenetroot)"><strong>RxCreateNetRoot</strong></a></p></td>
<td align="left"><p>This routine builds a node representing a NET_ROOT structure and inserts the name into the net name table on the associated device object. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxcontx/nf-rxcontx-rxcreaterxcontext" data-raw-source="[&lt;strong&gt;RxCreateRxContext&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxcontx/nf-rxcontx-rxcreaterxcontext)"><strong>RxCreateRxContext</strong></a></p></td>
<td align="left"><p>This routine allocates a new RX_CONTEXT structure and initializes the data structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxcreatesrvcall" data-raw-source="[&lt;strong&gt;RxCreateSrvCall&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxcreatesrvcall)"><strong>RxCreateSrvCall</strong></a></p></td>
<td align="left"><p>This routine builds a node that represents a server call context and inserts the name into the net name table maintained by RDBSS. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxcreatesrvopen" data-raw-source="[&lt;strong&gt;RxCreateSrvOpen&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxcreatesrvopen)"><strong>RxCreateSrvOpen</strong></a></p></td>
<td align="left"><p>This routine allocates, initializes, and inserts a new SRV_OPEN structure into the in-memory data structures used by RDBSS. If a new structure has to be allocated, it has space for an FOBX structure. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxcreatevnetroot" data-raw-source="[&lt;strong&gt;RxCreateVNetRoot&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxcreatevnetroot)"><strong>RxCreateVNetRoot</strong></a></p></td>
<td align="left"><p>This routine builds a node that represents a V_NET_ROOT structure and inserts the name into the net name table. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ifs/rxdbgbreakpoint" data-raw-source="[&lt;strong&gt;RxDbgBreakPoint&lt;/strong&gt;](./rxdbgbreakpoint.md)"><strong>RxDbgBreakPoint</strong></a></p></td>
<td align="left"><p>This routine raises an exception that is handled by the kernel debugger if one is installed; otherwise, it is handled by the debug system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxdereference" data-raw-source="[&lt;strong&gt;RxDereference&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxdereference)"><strong>RxDereference</strong></a></p></td>
<td align="left"><p>This routine decrements the reference count on an instance of several of the reference-counted data structures used by RDBSS.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxcontx/nf-rxcontx-rxdereferenceanddeleterxcontext_real" data-raw-source="[&lt;strong&gt;RxDereferenceAndDeleteRxContext_Real&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxcontx/nf-rxcontx-rxdereferenceanddeleterxcontext_real)"><strong>RxDereferenceAndDeleteRxContext_Real</strong></a></p></td>
<td align="left"><p>This routine dereferences an RX_CONTEXT structure and if the reference count goes to zero, then it deallocates and removes the specified RX_CONTEXT structure from the RDBSS in-memory data structures.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/midatlax/nf-midatlax-rxdestroymidatlas" data-raw-source="[&lt;strong&gt;RxDestroyMidAtlas&lt;/strong&gt;](/windows-hardware/drivers/ddi/midatlax/nf-midatlax-rxdestroymidatlas)"><strong>RxDestroyMidAtlas</strong></a></p></td>
<td align="left"><p>This routine destroys an existing instance of a MID_ATLAS data structure and frees the memory allocated.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxworkq/nf-rxworkq-rxdispatchtoworkerthread" data-raw-source="[&lt;strong&gt;RxDispatchToWorkerThread&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxworkq/nf-rxworkq-rxdispatchtoworkerthread)"><strong>RxDispatchToWorkerThread</strong></a></p></td>
<td align="left"><p>This routine invokes a routine in the context of a worker thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxdriverentry" data-raw-source="[&lt;strong&gt;RxDriverEntry&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxdriverentry)"><strong>RxDriverEntry</strong></a></p></td>
<td align="left"><p>This routine is called by a monolithic network mini-redirector driver from its <strong>DriverEntry</strong> to initialize RDBSS.</p>
<p>For non-monolithic drivers, this initialization routine is equivalent to the <strong>DriverEntry</strong> routine of the <em>rdbss.sys</em> device driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxfinalizeconnection" data-raw-source="[&lt;strong&gt;RxFinalizeConnection&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxfinalizeconnection)"><strong>RxFinalizeConnection</strong></a></p></td>
<td align="left"><p>This routine deletes a connection to a share. Any files open on the connection are closed depending on the level of force specified. The network mini-redirector might choose to keep the transport connection open for performance reasons, unless some option is specified to force a close of connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxfinalizenetfcb" data-raw-source="[&lt;strong&gt;RxFinalizeNetFcb&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxfinalizenetfcb)"><strong>RxFinalizeNetFcb</strong></a></p></td>
<td align="left"><p>This routine finalizes the given FCB structure. The caller must have an exclusive lock on the NET_ROOT structure associated with FCB. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxfinalizenetfobx" data-raw-source="[&lt;strong&gt;RxFinalizeNetFobx&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxfinalizenetfobx)"><strong>RxFinalizeNetFobx</strong></a></p></td>
<td align="left"><p>This routine finalizes the given FOBX structure. The caller must have an exclusive lock on the FCB associated with this FOBX. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxfinalizenetroot" data-raw-source="[&lt;strong&gt;RxFinalizeNetRoot&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxfinalizenetroot)"><strong>RxFinalizeNetRoot</strong></a></p></td>
<td align="left"><p>This routine finalizes the given NET_ROOT structure. The caller should have exclusive access to the lock on the NetName table of the device object associated with this NET_ROOT structure (through the SRV_CALL structure). This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxfinalizesrvcall" data-raw-source="[&lt;strong&gt;RxFinalizeSrvCall&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxfinalizesrvcall)"><strong>RxFinalizeSrvCall</strong></a></p></td>
<td align="left"><p>This routine finalizes the given SRV_CALL structure. The caller should have exclusive access to the lock on the NetName table of the device object associated with this SRV_CALL structure. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxfinalizesrvopen" data-raw-source="[&lt;strong&gt;RxFinalizeSrvOpen&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxfinalizesrvopen)"><strong>RxFinalizeSrvOpen</strong></a></p></td>
<td align="left"><p>This routine finalizes the given SRV_OPEN structure. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
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
<td align="left"><p><a href="/windows-hardware/drivers/ddi/mrx/nf-mrx-rxfsddispatch" data-raw-source="[&lt;strong&gt;RxFsdDispatch&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nf-mrx-rxfsddispatch)"><strong>RxFsdDispatch</strong></a></p></td>
<td align="left"><p>This routine implements the file system driver (FSD) dispatch for RDBSS to process an I/O request packet (IRP). This routine is called by a network mini-redirector in the driver dispatch routines to initiate RDBSS processing of a request.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxfsdpostrequest" data-raw-source="[&lt;strong&gt;RxFsdPostRequest&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxfsdpostrequest)"><strong>RxFsdPostRequest</strong></a></p></td>
<td align="left"><p>This routine queues the I/O request packet (IRP) specified by an RX_CONTEXT structure to the worker queue for processing by the file system process (FSP).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxgetfilesizewithlock" data-raw-source="[&lt;strong&gt;RxGetFileSizeWithLock&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxgetfilesizewithlock)"><strong>RxGetFileSizeWithLock</strong></a></p></td>
<td align="left"><p>This routine gets the file size from the FCB structure using a lock to ensure that the 64-bit value is read consistently.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxstruc/nf-rxstruc-rxgetrdbssprocess" data-raw-source="[&lt;strong&gt;RxGetRDBSSProcess&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxstruc/nf-rxstruc-rxgetrdbssprocess)"><strong>RxGetRDBSSProcess</strong></a></p></td>
<td align="left"><p>This routine returns a pointer to the process of the main thread used by the RDBSS kernel process.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxindicatechangeofbufferingstate" data-raw-source="[&lt;strong&gt;RxIndicateChangeOfBufferingState&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxindicatechangeofbufferingstate)"><strong>RxIndicateChangeOfBufferingState</strong></a></p></td>
<td align="left"><p>This routine is called to register a buffering state change request (an oplock break indication, for example) for later processing.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxindicatechangeofbufferingstateforsrvopen" data-raw-source="[&lt;strong&gt;RxIndicateChangeOfBufferingStateForSrvOpen&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxindicatechangeofbufferingstateforsrvopen)"><strong>RxIndicateChangeOfBufferingStateForSrvOpen</strong></a></p></td>
<td align="left"><p>This routine is called to register a buffering state change request (an oplock break indication, for example) for later processing.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxinferfiletype" data-raw-source="[&lt;strong&gt;RxInferFileType&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxinferfiletype)"><strong>RxInferFileType</strong></a></p></td>
<td align="left"><p>This routine tries to infer the file type (directory or non-directory) from the <strong>CreateOptions</strong> ( <strong>Create.NtCreateParameters.CreateOptions</strong>) field in the RX_CONTEXT structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxcontx/nf-rxcontx-rxinitializecontext" data-raw-source="[&lt;strong&gt;RxInitializeContext&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxcontx/nf-rxcontx-rxinitializecontext)"><strong>RxInitializeContext</strong></a></p></td>
<td align="left"><p>This routine initializes a newly allocated RX_CONTEXT structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxisthisacscagentopen" data-raw-source="[&lt;strong&gt;RxIsThisACscAgentOpen&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxisthisacscagentopen)"><strong>RxIsThisACscAgentOpen</strong></a></p></td>
<td align="left"><p>This routine determines if a file open was made by a user-mode client-side caching agent.</p>
<p>This routine is only available on Windows Server 2003.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxlockenumerator" data-raw-source="[&lt;strong&gt;RxLockEnumerator&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxlockenumerator)"><strong>RxLockEnumerator</strong></a></p></td>
<td align="left"><p>This routine is called from a network mini-redirector to enumerate the file locks on an FCB.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxlogeventdirect" data-raw-source="[&lt;strong&gt;RxLogEventDirect&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxlogeventdirect)"><strong>RxLogEventDirect</strong></a></p></td>
<td align="left"><p>This routine is called to log an error to the I/O error log. It is recommended that the <strong>RxLogEvent</strong> or <strong>RxLogFailure</strong> macro be used instead of calling this routine directly.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxlogeventwithannotation" data-raw-source="[&lt;strong&gt;RxLogEventWithAnnotation&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxlogeventwithannotation)"><strong>RxLogEventWithAnnotation</strong></a></p></td>
<td align="left"><p>This routine allocates an I/O error log structure, fills in the log structure, and writes this structure to the I/O error log.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxlogeventwithbufferdirect" data-raw-source="[&lt;strong&gt;RxLogEventWithBufferDirect&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxlogeventwithbufferdirect)"><strong>RxLogEventWithBufferDirect</strong></a></p></td>
<td align="left"><p>This routine is called to log an error to an I/O error log. This routine encodes the line number and status into the data buffer stored in the I/O error log structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/lowio/nf-lowio-rxlowiocompletion" data-raw-source="[&lt;strong&gt;RxLowIoCompletion&lt;/strong&gt;](/windows-hardware/drivers/ddi/lowio/nf-lowio-rxlowiocompletion)"><strong>RxLowIoCompletion</strong></a></p></td>
<td align="left"><p>This routine must be called by the low I/O routines of a network mini-redirector driver when processing is complete, if the routine initially returned pending.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/lowio/nf-lowio-rxlowiogetbufferaddress" data-raw-source="[&lt;strong&gt;RxLowIoGetBufferAddress&lt;/strong&gt;](/windows-hardware/drivers/ddi/lowio/nf-lowio-rxlowiogetbufferaddress)"><strong>RxLowIoGetBufferAddress</strong></a></p></td>
<td align="left"><p>This routine returns the buffer that corresponds to the MDL from the <strong>LowIoContext</strong> structure of an RX_CONTEXT structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/mrx/nf-mrx-rxmakelatedeviceavailable" data-raw-source="[&lt;strong&gt;RxMakeLateDeviceAvailable&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nf-mrx-rxmakelatedeviceavailable)"><strong>RxMakeLateDeviceAvailable</strong></a></p></td>
<td align="left"><p>This routine modifies the device object to make a "late device" available. A late device is one that is not created in the driver's load routine.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/midatlax/nf-midatlax-rxmapanddissociatemidfromcontext" data-raw-source="[&lt;strong&gt;RxMapAndDissociateMidFromContext&lt;/strong&gt;](/windows-hardware/drivers/ddi/midatlax/nf-midatlax-rxmapanddissociatemidfromcontext)"><strong>RxMapAndDissociateMidFromContext</strong></a></p></td>
<td align="left"><p>This routine maps a MID to its associated context in a MID_ATLAS data structure and then disassociates the MID from the context.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/midatlax/nf-midatlax-rxmapmidtocontext" data-raw-source="[&lt;strong&gt;RxMapMidToContext&lt;/strong&gt;](/windows-hardware/drivers/ddi/midatlax/nf-midatlax-rxmapmidtocontext)"><strong>RxMapMidToContext</strong></a></p></td>
<td align="left"><p>This routine maps a MID to its associated context in a MID_ATLAS data structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxmapsystembuffer" data-raw-source="[&lt;strong&gt;RxMapSystemBuffer&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxmapsystembuffer)"><strong>RxMapSystemBuffer</strong></a></p></td>
<td align="left"><p>This routine returns the system buffer address from the I/O request packet (IRP).</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/namcache/nf-namcache-rxnamecacheactivateentry" data-raw-source="[&lt;strong&gt;RxNameCacheActivateEntry&lt;/strong&gt;](/windows-hardware/drivers/ddi/namcache/nf-namcache-rxnamecacheactivateentry)"><strong>RxNameCacheActivateEntry</strong></a></p></td>
<td align="left"><p>This routine takes a name cache entry and updates the expiration time and the network mini-redirector context. It then puts the entry on the active list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/namcache/nf-namcache-rxnamecachecheckentry" data-raw-source="[&lt;strong&gt;RxNameCacheCheckEntry&lt;/strong&gt;](/windows-hardware/drivers/ddi/namcache/nf-namcache-rxnamecachecheckentry)"><strong>RxNameCacheCheckEntry</strong></a></p></td>
<td align="left"><p>This routine checks a NAME_CACHE entry for validity.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/namcache/nf-namcache-rxnamecachecreateentry" data-raw-source="[&lt;strong&gt;RxNameCacheCreateEntry&lt;/strong&gt;](/windows-hardware/drivers/ddi/namcache/nf-namcache-rxnamecachecreateentry)"><strong>RxNameCacheCreateEntry</strong></a></p></td>
<td align="left"><p>This routine allocates and initializes a NAME_CACHE structure with the given name string. It is expected that the caller will then initialize any additional network mini-redirector elements of the name cache context and then put the entry on the name cache active list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/namcache/nf-namcache-rxnamecacheexpireentry" data-raw-source="[&lt;strong&gt;RxNameCacheExpireEntry&lt;/strong&gt;](/windows-hardware/drivers/ddi/namcache/nf-namcache-rxnamecacheexpireentry)"><strong>RxNameCacheExpireEntry</strong></a></p></td>
<td align="left"><p>This routine puts a NAME_CACHE entry on the free list.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/namcache/nf-namcache-rxnamecacheexpireentrywithshortname" data-raw-source="[&lt;strong&gt;RxNameCacheExpireEntryWithShortName&lt;/strong&gt;](/windows-hardware/drivers/ddi/namcache/nf-namcache-rxnamecacheexpireentrywithshortname)"><strong>RxNameCacheExpireEntryWithShortName</strong></a></p></td>
<td align="left"><p>This routine expires all of the NAME_CACHE entries whose name prefix matches the given short file name.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/namcache/nf-namcache-rxnamecachefetchentry" data-raw-source="[&lt;strong&gt;RxNameCacheFetchEntry&lt;/strong&gt;](/windows-hardware/drivers/ddi/namcache/nf-namcache-rxnamecachefetchentry)"><strong>RxNameCacheFetchEntry</strong></a></p></td>
<td align="left"><p>This routine looks for a match with a specified name string for a NAME_CACHE entry.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/namcache/nf-namcache-rxnamecachefinalize" data-raw-source="[&lt;strong&gt;RxNameCacheFinalize&lt;/strong&gt;](/windows-hardware/drivers/ddi/namcache/nf-namcache-rxnamecachefinalize)"><strong>RxNameCacheFinalize</strong></a></p></td>
<td align="left"><p>This routine releases the storage for all of the NAME_CACHE entries associated with a NAME_CACHE_CONTROL structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/namcache/nf-namcache-rxnamecachefreeentry" data-raw-source="[&lt;strong&gt;RxNameCacheFreeEntry&lt;/strong&gt;](/windows-hardware/drivers/ddi/namcache/nf-namcache-rxnamecachefreeentry)"><strong>RxNameCacheFreeEntry</strong></a></p></td>
<td align="left"><p>This routine releases the storage for a NAME_CACHE entry and decrements the count of NAME_CACHE cache entries associated with a NAME_CACHE_CONTROL structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/namcache/nf-namcache-rxnamecacheinitialize" data-raw-source="[&lt;strong&gt;RxNameCacheInitialize&lt;/strong&gt;](/windows-hardware/drivers/ddi/namcache/nf-namcache-rxnamecacheinitialize)"><strong>RxNameCacheInitialize</strong></a></p></td>
<td align="left"><p>This routine initializes a NAME_CACHE structure and associates it with a NAME_CACHE_CONTROL structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ifs/rxnewmapuserbuffer" data-raw-source="[&lt;strong&gt;RxNewMapUserBuffer&lt;/strong&gt;](./rxnewmapuserbuffer.md)"><strong>RxNewMapUserBuffer</strong></a></p></td>
<td align="left"><p>This routine returns the address of the user buffer used for low I/O.</p>
<p>This routine is only available on Windows XP and Windows 2000.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/prefix/nf-prefix-rxpacquireprefixtablelockexclusive" data-raw-source="[&lt;strong&gt;RxpAcquirePrefixTableLockExclusive&lt;/strong&gt;](/windows-hardware/drivers/ddi/prefix/nf-prefix-rxpacquireprefixtablelockexclusive)"><strong>RxpAcquirePrefixTableLockExclusive</strong></a></p></td>
<td align="left"><p>This routine acquires an exclusive lock on a prefix table used to catalog SRV_CALL and NET_ROOT names.</p>
<p>This routine is only available on Windows XP and Windows 2000. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/prefix/nf-prefix-rxpacquireprefixtablelockshared" data-raw-source="[&lt;strong&gt;RxpAcquirePrefixTableLockShared&lt;/strong&gt;](/windows-hardware/drivers/ddi/prefix/nf-prefix-rxpacquireprefixtablelockshared)"><strong>RxpAcquirePrefixTableLockShared</strong></a></p></td>
<td align="left"><p>This routine acquires a shared lock on a prefix table used to catalog SRV_CALL and NET_ROOT names.</p>
<p>This routine is only available on Windows XP and Windows 2000. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxpdereferenceandfinalizenetfcb" data-raw-source="[&lt;strong&gt;RxpDereferenceAndFinalizeNetFcb&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxpdereferenceandfinalizenetfcb)"><strong>RxpDereferenceAndFinalizeNetFcb</strong></a></td>
<td align="left"><p>This routine dereferences the reference count and finalizes an FCB.</p>
<p>This routine is only available on Windows Server 2003 Service Pack 1 (SP1) and later.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxpdereferencenetfcb" data-raw-source="[&lt;strong&gt;RxpDereferenceNetFcb&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxpdereferencenetfcb)"><strong>RxpDereferenceNetFcb</strong></a></p></td>
<td align="left"><p>This routine decrements the reference count on an FCB.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxtimer/nf-rxtimer-rxpostoneshottimerrequest" data-raw-source="[&lt;strong&gt;RxPostOneShotTimerRequest&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxtimer/nf-rxtimer-rxpostoneshottimerrequest)"><strong>RxPostOneShotTimerRequest</strong></a></p></td>
<td align="left"><p>This routine is used by drivers to initialize a one-shot timer request. The worker thread routine passed to this routine is called once when the timer expires.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxtimer/nf-rxtimer-rxpostrecurrenttimerrequest" data-raw-source="[&lt;strong&gt;RxPostRecurrentTimerRequest&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxtimer/nf-rxtimer-rxpostrecurrenttimerrequest)"><strong>RxPostRecurrentTimerRequest</strong></a></p></td>
<td align="left"><p>This routine is used to initialize a recurrent timer request. The worker thread routine passed to this routine is called at regular intervals when the recurrent timer fires based on the input parameters to this routine.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxworkq/nf-rxworkq-rxposttoworkerthread" data-raw-source="[&lt;strong&gt;RxPostToWorkerThread&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxworkq/nf-rxworkq-rxposttoworkerthread)"><strong>RxPostToWorkerThread</strong></a></p></td>
<td align="left"><p>This routine invokes the routine in the context of a worker thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxpreferencenetfcb" data-raw-source="[&lt;strong&gt;RxpReferenceNetFcb&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxpreferencenetfcb)"><strong>RxpReferenceNetFcb</strong></a></p></td>
<td align="left"><p>This routine increments the reference count on an FCB.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/prefix/nf-prefix-rxprefixtablelookupname" data-raw-source="[&lt;strong&gt;RxPrefixTableLookupName&lt;/strong&gt;](/windows-hardware/drivers/ddi/prefix/nf-prefix-rxprefixtablelookupname)"><strong>RxPrefixTableLookupName</strong></a></p></td>
<td align="left"><p>The routine looks up a name in a prefix table used to catalog SRV_CALL and NET_ROOT names and converts from the underlying pointer to the containing structure.</p>
<p>This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/prefix/nf-prefix-rxpreleaseprefixtablelock" data-raw-source="[&lt;strong&gt;RxpReleasePrefixTableLock&lt;/strong&gt;](/windows-hardware/drivers/ddi/prefix/nf-prefix-rxpreleaseprefixtablelock)"><strong>RxpReleasePrefixTableLock</strong></a></p></td>
<td align="left"><p>This routine releases a lock on a prefix table used to catalog SRV_CALL and NET_ROOT names.</p>
<p>This routine is only available on Windows XP and Windows 2000. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxcontx/nf-rxcontx-rxpreparecontextforreuse" data-raw-source="[&lt;strong&gt;RxPrepareContextForReuse&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxcontx/nf-rxcontx-rxpreparecontextforreuse)"><strong>RxPrepareContextForReuse</strong></a></p></td>
<td align="left"><p>This routine prepares an RX_CONTEXT structure for reuse by resetting all operation-specific allocations and acquisitions that have been made. The parameters obtained from the IRP are not modified. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxpreparetoreparsesymboliclink" data-raw-source="[&lt;strong&gt;RxPrepareToReparseSymbolicLink&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxpreparetoreparsesymboliclink)"><strong>RxPrepareToReparseSymbolicLink</strong></a></p></td>
<td align="left"><p>This routine sets up the file object name to facilitate a reparse. This routine is used by the network mini-redirectors to traverse symbolic links. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxptrackdereference" data-raw-source="[&lt;strong&gt;RxpTrackDereference&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxptrackdereference)"><strong>RxpTrackDereference</strong></a></p></td>
<td align="left"><p>This routine is used to track requests to dereference SRV_CALL, NET_ROOT, V_NET_ROOT, FOBX, FCB, and SRV_OPEN structures in checked builds. A log of these dereference requests can be accessed by the logging system and WMI.</p>
<p>For retail builds, this routine does nothing.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fcb/nf-fcb-rxptrackreference" data-raw-source="[&lt;strong&gt;RxpTrackReference&lt;/strong&gt;](/windows-hardware/drivers/ddi/fcb/nf-fcb-rxptrackreference)"><strong>RxpTrackReference</strong></a></p></td>
<td align="left"><p>This routine is used to track requests to reference SRV_CALL, NET_ROOT, V_NET_ROOT, FOBX, FCB, and SRV_OPEN structures in checked builds. A log of these reference requests can be accessed by the logging system and WMI.</p>
<p>For retail builds, this routine does nothing.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/mrx/nf-mrx-rxpunregisterminirdr" data-raw-source="[&lt;strong&gt;RxpUnregisterMinirdr&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nf-mrx-rxpunregisterminirdr)"><strong>RxpUnregisterMinirdr</strong></a></p></td>
<td align="left"><p>The routine is called by a network mini-redirector driver to unregister the driver with RDBSS and remove the registration information from the internal RDBSS registration table.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxpurgeallfobxs" data-raw-source="[&lt;strong&gt;RxPurgeAllFobxs&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxpurgeallfobxs)"><strong>RxPurgeAllFobxs</strong></a></p></td>
<td align="left"><p>This routine purges all the FOBX structures associated with a network mini-redirector.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/scavengr/nf-scavengr-rxpurgerelatedfobxs" data-raw-source="[&lt;strong&gt;RxPurgeRelatedFobxs&lt;/strong&gt;](/windows-hardware/drivers/ddi/scavengr/nf-scavengr-rxpurgerelatedfobxs)"><strong>RxPurgeRelatedFobxs</strong></a></p></td>
<td align="left"><p>This routine purges all of the FOBX structures associated with a NET_ROOT structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/midatlax/nf-midatlax-rxreassociatemid" data-raw-source="[&lt;strong&gt;RxReassociateMid&lt;/strong&gt;](/windows-hardware/drivers/ddi/midatlax/nf-midatlax-rxreassociatemid)"><strong>RxReassociateMid</strong></a></p></td>
<td align="left"><p>This routine reassociates a MID with an alternate context.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxreference" data-raw-source="[&lt;strong&gt;RxReference&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxreference)"><strong>RxReference</strong></a></p></td>
<td align="left"><p>This routine increments the reference count on an instance of several of the reference-counted data structures used by RDBSS.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/mrx/nf-mrx-rxregisterminirdr" data-raw-source="[&lt;strong&gt;RxRegisterMinirdr&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nf-mrx-rxregisterminirdr)"><strong>RxRegisterMinirdr</strong></a></p></td>
<td align="left"><p>This routine is called by a network mini-redirector driver to register the driver with RDBSS, which adds the registration information to an internal registration table. RDBSS also builds a device object for the network mini-redirector.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/mrxfcb/nf-mrxfcb-rxreleasefcbresourceinmrx" data-raw-source="[&lt;strong&gt;RxReleaseFcbResourceInMRx&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrxfcb/nf-mrxfcb-rxreleasefcbresourceinmrx)"><strong>RxReleaseFcbResourceInMRx</strong></a></p></td>
<td align="left"><p>This routine frees the FCB resource acquired using <strong>RxAcquireExclusiveFcbResourceInMRx</strong> or <strong>RxAcquireSharedFcbResourceInMRx</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ddi/mrxfcb/nf-mrxfcb-rxreleasefcbresourceforthreadinmrx" data-raw-source="[&lt;strong&gt;RxReleaseFcbResourceForThreadInMRx&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrxfcb/nf-mrxfcb-rxreleasefcbresourceforthreadinmrx)"><strong>RxReleaseFcbResourceForThreadInMRx</strong></a></td>
<td align="left"><p>This routine frees the FCB resource acquired using <a href="/windows-hardware/drivers/ddi/mrxfcb/nf-mrxfcb-rxacquiresharedfcbresourceinmrxex" data-raw-source="[&lt;strong&gt;RxAcquireSharedFcbResourceInMRxEx&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrxfcb/nf-mrxfcb-rxacquiresharedfcbresourceinmrxex)"><strong>RxAcquireSharedFcbResourceInMRxEx</strong></a></p>
<p>This routine is only available on Windows Server 2003 Service Pack 1 (SP1) and later.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxcontx/nf-rxcontx-rxresumeblockedoperations_serially" data-raw-source="[&lt;strong&gt;RxResumeBlockedOperations_Serially&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxcontx/nf-rxcontx-rxresumeblockedoperations_serially)"><strong>RxResumeBlockedOperations_Serially</strong></a></p></td>
<td align="left"><p>This routine wakes up the next waiting thread, if any, on the serialized blocking I/O queue.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxscavengeallfobxs" data-raw-source="[&lt;strong&gt;RxScavengeAllFobxs&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxscavengeallfobxs)"><strong>RxScavengeAllFobxs</strong></a></p></td>
<td align="left"><p>This routine scavenges all of the FOBX structures associated with a given network mini-redirector device object.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/scavengr/nf-scavengr-rxscavengefobxsfornetroot" data-raw-source="[&lt;strong&gt;RxScavengeFobxsForNetRoot&lt;/strong&gt;](/windows-hardware/drivers/ddi/scavengr/nf-scavengr-rxscavengefobxsfornetroot)"><strong>RxScavengeFobxsForNetRoot</strong></a></p></td>
<td align="left"><p>This routine scavenges all of the FOBX structures that pertain to the given NET_ROOT structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/mrx/nf-mrx-rxsetdomainformailslotbroadcast" data-raw-source="[&lt;strong&gt;RxSetDomainForMailslotBroadcast&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nf-mrx-rxsetdomainformailslotbroadcast)"><strong>RxSetDomainForMailslotBroadcast</strong></a></p></td>
<td align="left"><p>This routine is called by a network mini-redirector driver to set the domain used for mailslot broadcasts if mailslots are supported by the driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxcontx/nf-rxcontx-rxsetminirdrcancelroutine" data-raw-source="[&lt;strong&gt;RxSetMinirdrCancelRoutine&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxcontx/nf-rxcontx-rxsetminirdrcancelroutine)"><strong>RxSetMinirdrCancelRoutine</strong></a></p></td>
<td align="left"><p>This routine sets up a network mini-redirector cancel routine for an RX_CONTEXT structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxsetsrvcalldomainname" data-raw-source="[&lt;strong&gt;RxSetSrvCallDomainName&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxsetsrvcalldomainname)"><strong>RxSetSrvCallDomainName</strong></a></p></td>
<td align="left"><p>This routine sets the domain name associated with any given server (SRV_CALL structure).</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxworkq/nf-rxworkq-rxspindownmrxdispatcher" data-raw-source="[&lt;strong&gt;RxSpinDownMRxDispatcher&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxworkq/nf-rxworkq-rxspindownmrxdispatcher)"><strong>RxSpinDownMRxDispatcher</strong></a></p></td>
<td align="left"><p>This routine tears down the dispatcher context for a network mini-redirector.</p>
<p>This routine is only available on Windows XP and later.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/mrx/nf-mrx-rxstartminirdr" data-raw-source="[&lt;strong&gt;RxStartMinirdr&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nf-mrx-rxstartminirdr)"><strong>RxStartMinirdr</strong></a></p></td>
<td align="left"><p>This routine starts up a network mini-redirector that called to register itself. RDBSS will also register the network mini-redirector driver as a Universal Naming Convention (UNC) provider with the Multiple UNC Provider (MUP) if the driver indicates support for UNC names.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/mrx/nf-mrx-rxstopminirdr" data-raw-source="[&lt;strong&gt;RxStopMinirdr&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nf-mrx-rxstopminirdr)"><strong>RxStopMinirdr</strong></a></p></td>
<td align="left"><p>This routine stops a network mini-redirector driver. A driver that is stopped will no longer accept new commands.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxstruc/nf-rxstruc-rxunregisterminirdr" data-raw-source="[&lt;strong&gt;RxUnregisterMinirdr&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxstruc/nf-rxstruc-rxunregisterminirdr)"><strong>RxUnregisterMinirdr</strong></a></p></td>
<td align="left"><p>This routine is an inline function defined in <em>rxstruc.h</em> that is called by a network mini-redirector driver to unregister the driver with RDBSS and remove the registration information from the internal RDBSS registration table. The <strong>RxUnregisterMinirdr</strong> inline function internally calls <strong>RxpUnregisterMinirdr</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ifs/-rxallocatepoolwithtag" data-raw-source="[&lt;strong&gt;_RxAllocatePoolWithTag&lt;/strong&gt;](./-rxallocatepoolwithtag.md)"><strong>_RxAllocatePoolWithTag</strong></a></p></td>
<td align="left"><p>This routine allocates memory from a pool with a four-byte tag at the beginning of the block that can be used to help catch instances of memory problems.</p>
<p>It is recommended that the <strong>RxAllocatePoolWithTag</strong> macro be used instead of calling this routine directly.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ifs/-rxcheckmemoryblock" data-raw-source="[&lt;strong&gt;_RxCheckMemoryBlock&lt;/strong&gt;](./-rxcheckmemoryblock.md)"><strong>_RxCheckMemoryBlock</strong></a></p></td>
<td align="left"><p>This routine checks a memory block for a special RX_POOL_HEADER header signature. Note that a network mini-redirector driver would need to add this special signature block to memory allocated in order to use the routine.</p>
<p>This routine should not be used since this special header block has not been implemented.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ifs/-rxfreepool" data-raw-source="[&lt;strong&gt;_RxFreePool&lt;/strong&gt;](./-rxfreepool.md)"><strong>_RxFreePool</strong></a></p></td>
<td align="left"><p>This routine frees a memory pool.</p>
<p>It is recommended that the <strong>RxFreePool</strong> macro be used instead of calling this routine directly.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxlog/nf-rxlog-_rxlog" data-raw-source="[&lt;strong&gt;_RxLog&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxlog/nf-rxlog-_rxlog)"><strong>_RxLog</strong></a></p></td>
<td align="left"><p>This routine takes a format string and variable number of parameters and formats an output string for structureing as an I/O error log entry if logging is enabled.</p>
<p>It is recommended that the <a href="/windows-hardware/drivers/ddi/rxlog/nf-rxlog-_rxlog" data-raw-source="[&lt;strong&gt;RxLog&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxlog/nf-rxlog-_rxlog)"><strong>RxLog</strong></a> macro be used instead of calling this routine directly.</p>
<p>This routine is only available on checked builds of RDBSS on Windows Server 2003, Windows XP, and Windows 2000.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/mrx/nf-mrx-__rxfillandinstallfastiodispatch" data-raw-source="[&lt;strong&gt;__RxFillAndInstallFastIoDispatch&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nf-mrx-__rxfillandinstallfastiodispatch)"><strong>__RxFillAndInstallFastIoDispatch</strong></a></p></td>
<td align="left"><p>This routine fills out a fast I/O dispatch vector to be identical with the normal dispatch I/O vector and installs it into the driver object that is associated with the device object passed.</p>
<p>This routine is implemented only for non-monolithic drivers and does nothing on monolithic drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ddi/rxcontx/nf-rxcontx-__rxsynchronizeblockingoperations" data-raw-source="[&lt;strong&gt;__RxSynchronizeBlockingOperations&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxcontx/nf-rxcontx-__rxsynchronizeblockingoperations)"><strong>__RxSynchronizeBlockingOperations</strong></a></td>
<td align="left"><p>This routine is used to synchronize blocking I/O to the same work queue. This routine is used internally by RDBSS to synchronize named pipe operations. This routine may be used by a network mini-redirector to synchronize operations on a separate queue that is maintained by the network mini-redirector.</p>
<p>This routine is only available on Windows Server 2003.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/--rxsynchronizeblockingoperationsmaybedroppingfcblock" data-raw-source="[&lt;strong&gt;__RxSynchronizeBlockingOperationsMaybeDroppingFcbLock&lt;/strong&gt;](./--rxsynchronizeblockingoperationsmaybedroppingfcblock.md)"><strong>__RxSynchronizeBlockingOperationsMaybeDroppingFcbLock</strong></a></td>
<td align="left"><p>This routine is used to synchronize blocking I/O to the same work queue. This routine is used internally by RDBSS to synchronize named pipe operations. This routine may be used by a network mini-redirector to synchronize operations on a separate queue that is maintained by the network mini-redirector.</p>
<p>This routine is only available on Windows XP and Windows 2000.</p></td>
</tr>
</tbody>
</table>

 

