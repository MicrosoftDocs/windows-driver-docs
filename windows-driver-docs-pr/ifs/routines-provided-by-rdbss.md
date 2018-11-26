---
title: Routines Provided by RDBSS
description: Routines Provided by RDBSS
ms.assetid: 37631760-ac89-4ef0-ad7c-ed3e68aa1ceb
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553363" data-raw-source="[&lt;strong&gt;RxAcquireExclusiveFcbResourceInMRx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553363)"><strong>RxAcquireExclusiveFcbResourceInMRx</strong></a></p></td>
<td align="left"><p>This resource acquisition routine acquires the File Control Block (FCB) resource in exclusive mode. This routine will wait for the FCB resource to be free, so this routine does not return control until the resource has been acquired. This routine acquires the FCB resource even if the RX_CONTEXT associated with this FCB has been canceled.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553372" data-raw-source="[&lt;strong&gt;RxAcquireSharedFcbResourceInMRx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553372)"><strong>RxAcquireSharedFcbResourceInMRx</strong></a></p></td>
<td align="left"><p>This resource acquisition routine acquires the FCB resource in shared mode. This routine will wait for the FCB resource to be free if it was previously acquired exclusively, so this routine does not return control until the resource has been acquired. This routine acquires the FCB resource even if the RX_CONTEXT associated with this FCB has been canceled.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff553375" data-raw-source="[&lt;strong&gt;RxAcquireSharedFcbResourceInMRxEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553375)"><strong>RxAcquireSharedFcbResourceInMRxEx</strong></a></td>
<td align="left"><p>This resource acquisition routine acquires the FCB resource in shared mode. This routine will wait for the FCB resource to be freed if it was previously acquired exclusively. This routine does not return control until the resource has been acquired. This routine acquires the FCB resource even if the RX_CONTEXT associated with this FCB has been canceled.</p>
<p>This routine is only available on Windows Server 2003 Service Pack 1 (SP1) and later.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553384" data-raw-source="[&lt;strong&gt;RxAssert&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553384)"><strong>RxAssert</strong></a></p></td>
<td align="left"><p>This routine sends an assert string in RDBSS checked builds to a kernel debugger if one is installed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553388" data-raw-source="[&lt;strong&gt;RxAssociateContextWithMid&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553388)"><strong>RxAssociateContextWithMid</strong></a></p></td>
<td align="left"><p>This routine associates the supplied opaque context with an available multiplex ID (MID) from a MID_ATLAS data structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553395" data-raw-source="[&lt;strong&gt;RxCancelTimerRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553395)"><strong>RxCancelTimerRequest</strong></a></p></td>
<td align="left"><p>This routine cancels a timer request. The request to be canceled is identified by the routine and context.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553405" data-raw-source="[&lt;strong&gt;RxCeAllocateIrpWithMDL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553405)"><strong>RxCeAllocateIrpWithMDL</strong></a></p></td>
<td align="left"><p>This routine allocates an IRP for use by the connection engine and associates an MDL with the IRP.</p>
<p>This routine is only available on Windows XP.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553414" data-raw-source="[&lt;strong&gt;RxCeBuildAddress&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553414)"><strong>RxCeBuildAddress</strong></a></p></td>
<td align="left"><p>This routine associates a transport address with a transport binding.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553417" data-raw-source="[&lt;strong&gt;RxCeBuildConnection&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553417)"><strong>RxCeBuildConnection</strong></a></p></td>
<td align="left"><p>This routine establishes a connection between a local RDBSS connection address and a given remote address. This routine should be called in the context of a system worker thread.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553424" data-raw-source="[&lt;strong&gt;RxCeBuildConnectionOverMultipleTransports&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553424)"><strong>RxCeBuildConnectionOverMultipleTransports</strong></a></p></td>
<td align="left"><p>This routine establishes a connection between a local RDBSS connection address and a given remote address and supports multiple transports. A set of local addresses are specified and this routine attempts to connect to the target server using all of the transports associated with the local addresses. One connection is chosen as the winner depending on the connection options. This routine must be called in the context of a system worker thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553434" data-raw-source="[&lt;strong&gt;RxCeBuildTransport&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553434)"><strong>RxCeBuildTransport</strong></a></p></td>
<td align="left"><p>This routine binds an RDBSS transport to a specified transport name.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553439" data-raw-source="[&lt;strong&gt;RxCeBuildVC&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553439)"><strong>RxCeBuildVC</strong></a></p></td>
<td align="left"><p>This routine adds a virtual circuit to a specified connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553440" data-raw-source="[&lt;strong&gt;RxCeCancelConnectRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553440)"><strong>RxCeCancelConnectRequest</strong></a></p></td>
<td align="left"><p>This routine cancels a previously issued connection request.</p>
<p>Note that this routine is not currently implemented.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553448" data-raw-source="[&lt;strong&gt;RxCeFreeIrp&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553448)"><strong>RxCeFreeIrp</strong></a></p></td>
<td align="left"><p>This routine frees an IRP used by the connection engine.</p>
<p>This routine is only available on Windows XP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553454" data-raw-source="[&lt;strong&gt;RxCeInitiateVCDisconnect&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553454)"><strong>RxCeInitiateVCDisconnect</strong></a></p></td>
<td align="left"><p>This routine initiates a disconnect on the virtual circuit. This routine must be called in the context of a system worker thread.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553456" data-raw-source="[&lt;strong&gt;RxCeQueryAdapterStatus&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553456)"><strong>RxCeQueryAdapterStatus</strong></a></p></td>
<td align="left"><p>This routine returns the ADAPTER_STATUS structure for a given transport.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553461" data-raw-source="[&lt;strong&gt;RxCeQueryInformation&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553461)"><strong>RxCeQueryInformation</strong></a></p></td>
<td align="left"><p>This routine queries for information about a given virtual circuit.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553474" data-raw-source="[&lt;strong&gt;RxCeQueryTransportInformation&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553474)"><strong>RxCeQueryTransportInformation</strong></a></p></td>
<td align="left"><p>This routine queries a given transport for information about the connection count and quality of service.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553479" data-raw-source="[&lt;strong&gt;RxCeSend&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553479)"><strong>RxCeSend</strong></a></p></td>
<td align="left"><p>This routine sends a transport service data unit (TSDU) along the specified connection on a virtual circuit.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553482" data-raw-source="[&lt;strong&gt;RxCeSendDatagram&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553482)"><strong>RxCeSendDatagram</strong></a></p></td>
<td align="left"><p>This routine sends a TSDU to a specified transport address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553488" data-raw-source="[&lt;strong&gt;RxCeTearDownAddress&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553488)"><strong>RxCeTearDownAddress</strong></a></p></td>
<td align="left"><p>This routine removes a transport address from a transport binding.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554321" data-raw-source="[&lt;strong&gt;RxCeTearDownConnection&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554321)"><strong>RxCeTearDownConnection</strong></a></p></td>
<td align="left"><p>This routine tears down a given connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554328" data-raw-source="[&lt;strong&gt;RxCeTearDownTransport&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554328)"><strong>RxCeTearDownTransport</strong></a></p></td>
<td align="left"><p>This routine unbinds from the transport specified.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554332" data-raw-source="[&lt;strong&gt;RxCeTearDownVC&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554332)"><strong>RxCeTearDownVC</strong></a></p></td>
<td align="left"><p>This routine tears down a virtual connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554335" data-raw-source="[&lt;strong&gt;RxChangeBufferingState&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554335)"><strong>RxChangeBufferingState</strong></a></p></td>
<td align="left"><p>This routine is called to process a buffering state change request.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554340" data-raw-source="[&lt;strong&gt;RxCompleteRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554340)"><strong>RxCompleteRequest</strong></a></p></td>
<td align="left"><p>This routine is used to complete an IRP associated with an RX_CONTEXT structure. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554348" data-raw-source="[&lt;strong&gt;RxCompleteRequest_Real&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554348)"><strong>RxCompleteRequest_Real</strong></a></p></td>
<td align="left"><p>This routine is used to complete an IRP associated with an RX_CONTEXT structure. This routine should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554352" data-raw-source="[&lt;strong&gt;RxCreateMidAtlas&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554352)"><strong>RxCreateMidAtlas</strong></a></p></td>
<td align="left"><p>This routine allocates a new instance of a MID_ATLAS data structure and initializes it. RDBSS uses the multiplex ID (MID) defined in this data structure as a way that both the network client (mini-redirector) and the server can distinguish between the concurrently active requests on any connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554356" data-raw-source="[&lt;strong&gt;RxCreateNetFcb&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554356)"><strong>RxCreateNetFcb</strong></a></p></td>
<td align="left"><p>This routine allocates, initializes, and inserts a new FCB structure into the in-memory data structures for a NET_ROOT structure on which this FCB is opened. The structure allocated has space for a SRV_OPEN and an FOBX structure. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554358" data-raw-source="[&lt;strong&gt;RxCreateNetFobx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554358)"><strong>RxCreateNetFobx</strong></a></p></td>
<td align="left"><p>This routine allocates, initializes, and inserts a new file object extension (FOBX) structure. Network mini-redirectors should call this routine to create an FOBX at the end of a successful create operation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554366" data-raw-source="[&lt;strong&gt;RxCreateNetRoot&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554366)"><strong>RxCreateNetRoot</strong></a></p></td>
<td align="left"><p>This routine builds a node representing a NET_ROOT structure and inserts the name into the net name table on the associated device object. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554367" data-raw-source="[&lt;strong&gt;RxCreateRxContext&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554367)"><strong>RxCreateRxContext</strong></a></p></td>
<td align="left"><p>This routine allocates a new RX_CONTEXT structure and initializes the data structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554370" data-raw-source="[&lt;strong&gt;RxCreateSrvCall&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554370)"><strong>RxCreateSrvCall</strong></a></p></td>
<td align="left"><p>This routine builds a node that represents a server call context and inserts the name into the net name table maintained by RDBSS. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554376" data-raw-source="[&lt;strong&gt;RxCreateSrvOpen&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554376)"><strong>RxCreateSrvOpen</strong></a></p></td>
<td align="left"><p>This routine allocates, initializes, and inserts a new SRV_OPEN structure into the in-memory data structures used by RDBSS. If a new structure has to be allocated, it has space for an FOBX structure. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554380" data-raw-source="[&lt;strong&gt;RxCreateVNetRoot&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554380)"><strong>RxCreateVNetRoot</strong></a></p></td>
<td align="left"><p>This routine builds a node that represents a V_NET_ROOT structure and inserts the name into the net name table. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554385" data-raw-source="[&lt;strong&gt;RxDbgBreakPoint&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554385)"><strong>RxDbgBreakPoint</strong></a></p></td>
<td align="left"><p>This routine raises an exception that is handled by the kernel debugger if one is installed; otherwise, it is handled by the debug system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554388" data-raw-source="[&lt;strong&gt;RxDereference&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554388)"><strong>RxDereference</strong></a></p></td>
<td align="left"><p>This routine decrements the reference count on an instance of several of the reference-counted data structures used by RDBSS.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554393" data-raw-source="[&lt;strong&gt;RxDereferenceAndDeleteRxContext_Real&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554393)"><strong>RxDereferenceAndDeleteRxContext_Real</strong></a></p></td>
<td align="left"><p>This routine dereferences an RX_CONTEXT structure and if the reference count goes to zero, then it deallocates and removes the specified RX_CONTEXT structure from the RDBSS in-memory data structures.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554395" data-raw-source="[&lt;strong&gt;RxDestroyMidAtlas&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554395)"><strong>RxDestroyMidAtlas</strong></a></p></td>
<td align="left"><p>This routine destroys an existing instance of a MID_ATLAS data structure and frees the memory allocated.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554398" data-raw-source="[&lt;strong&gt;RxDispatchToWorkerThread&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554398)"><strong>RxDispatchToWorkerThread</strong></a></p></td>
<td align="left"><p>This routine invokes a routine in the context of a worker thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554404" data-raw-source="[&lt;strong&gt;RxDriverEntry&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554404)"><strong>RxDriverEntry</strong></a></p></td>
<td align="left"><p>This routine is called by a monolithic network mini-redirector driver from its <strong>DriverEntry</strong> to initialize RDBSS.</p>
<p>For non-monolithic drivers, this initialization routine is equivalent to the <strong>DriverEntry</strong> routine of the <em>rdbss.sys</em> device driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554409" data-raw-source="[&lt;strong&gt;RxFinalizeConnection&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554409)"><strong>RxFinalizeConnection</strong></a></p></td>
<td align="left"><p>This routine deletes a connection to a share. Any files open on the connection are closed depending on the level of force specified. The network mini-redirector might choose to keep the transport connection open for performance reasons, unless some option is specified to force a close of connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554412" data-raw-source="[&lt;strong&gt;RxFinalizeNetFcb&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554412)"><strong>RxFinalizeNetFcb</strong></a></p></td>
<td align="left"><p>This routine finalizes the given FCB structure. The caller must have an exclusive lock on the NET_ROOT structure associated with FCB. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554418" data-raw-source="[&lt;strong&gt;RxFinalizeNetFobx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554418)"><strong>RxFinalizeNetFobx</strong></a></p></td>
<td align="left"><p>This routine finalizes the given FOBX structure. The caller must have an exclusive lock on the FCB associated with this FOBX. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554421" data-raw-source="[&lt;strong&gt;RxFinalizeNetRoot&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554421)"><strong>RxFinalizeNetRoot</strong></a></p></td>
<td align="left"><p>This routine finalizes the given NET_ROOT structure. The caller should have exclusive access to the lock on the NetName table of the device object associated with this NET_ROOT structure (through the SRV_CALL structure). This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554426" data-raw-source="[&lt;strong&gt;RxFinalizeSrvCall&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554426)"><strong>RxFinalizeSrvCall</strong></a></p></td>
<td align="left"><p>This routine finalizes the given SRV_CALL structure. The caller should have exclusive access to the lock on the NetName table of the device object associated with this SRV_CALL structure. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554432" data-raw-source="[&lt;strong&gt;RxFinalizeSrvOpen&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554432)"><strong>RxFinalizeSrvOpen</strong></a></p></td>
<td align="left"><p>This routine finalizes the given SRV_OPEN structure. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554450" data-raw-source="[&lt;strong&gt;RxFinalizeVNetRoot&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554450)"><strong>RxFinalizeVNetRoot</strong></a></p></td>
<td align="left"><p>This routine finalizes the given V_NET_ROOT structure. The caller must have exclusive access to the lock on the NetName table of the device object associated with this V_NET_ROOT structure. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554454" data-raw-source="[&lt;strong&gt;RxFinishFcbInitialization&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554454)"><strong>RxFinishFcbInitialization</strong></a></p></td>
<td align="left"><p>This routine is used to finish initializing an FCB after the successful completion of a create operation by the network mini-redirector.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554463" data-raw-source="[&lt;strong&gt;RxForceFinalizeAllVNetRoots&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554463)"><strong>RxForceFinalizeAllVNetRoots</strong></a></p></td>
<td align="left"><p>This routine force finalizes all of the V_NET_ROOT structures associated with a given NET_ROOT structure. The caller must have exclusive access to the lock on the NetName table of the device object associated with this V_NET_ROOT structure. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554468" data-raw-source="[&lt;strong&gt;RxFsdDispatch&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554468)"><strong>RxFsdDispatch</strong></a></p></td>
<td align="left"><p>This routine implements the file system driver (FSD) dispatch for RDBSS to process an I/O request packet (IRP). This routine is called by a network mini-redirector in the driver dispatch routines to initiate RDBSS processing of a request.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554472" data-raw-source="[&lt;strong&gt;RxFsdPostRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554472)"><strong>RxFsdPostRequest</strong></a></p></td>
<td align="left"><p>This routine queues the I/O request packet (IRP) specified by an RX_CONTEXT structure to the worker queue for processing by the file system process (FSP).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554478" data-raw-source="[&lt;strong&gt;RxGetFileSizeWithLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554478)"><strong>RxGetFileSizeWithLock</strong></a></p></td>
<td align="left"><p>This routine gets the file size from the FCB structure using a lock to ensure that the 64-bit value is read consistently.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554481" data-raw-source="[&lt;strong&gt;RxGetRDBSSProcess&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554481)"><strong>RxGetRDBSSProcess</strong></a></p></td>
<td align="left"><p>This routine returns a pointer to the process of the main thread used by the RDBSS kernel process.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554485" data-raw-source="[&lt;strong&gt;RxIndicateChangeOfBufferingState&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554485)"><strong>RxIndicateChangeOfBufferingState</strong></a></p></td>
<td align="left"><p>This routine is called to register a buffering state change request (an oplock break indication, for example) for later processing.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554490" data-raw-source="[&lt;strong&gt;RxIndicateChangeOfBufferingStateForSrvOpen&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554490)"><strong>RxIndicateChangeOfBufferingStateForSrvOpen</strong></a></p></td>
<td align="left"><p>This routine is called to register a buffering state change request (an oplock break indication, for example) for later processing.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554493" data-raw-source="[&lt;strong&gt;RxInferFileType&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554493)"><strong>RxInferFileType</strong></a></p></td>
<td align="left"><p>This routine tries to infer the file type (directory or non-directory) from the <strong>CreateOptions</strong> ( <strong>Create.NtCreateParameters.CreateOptions</strong>) field in the RX_CONTEXT structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554502" data-raw-source="[&lt;strong&gt;RxInitializeContext&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554502)"><strong>RxInitializeContext</strong></a></p></td>
<td align="left"><p>This routine initializes a newly allocated RX_CONTEXT structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554508" data-raw-source="[&lt;strong&gt;RxIsThisACscAgentOpen&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554508)"><strong>RxIsThisACscAgentOpen</strong></a></p></td>
<td align="left"><p>This routine determines if a file open was made by a user-mode client-side caching agent.</p>
<p>This routine is only available on Windows Server 2003.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554511" data-raw-source="[&lt;strong&gt;RxLockEnumerator&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554511)"><strong>RxLockEnumerator</strong></a></p></td>
<td align="left"><p>This routine is called from a network mini-redirector to enumerate the file locks on an FCB.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554515" data-raw-source="[&lt;strong&gt;RxLogEventDirect&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554515)"><strong>RxLogEventDirect</strong></a></p></td>
<td align="left"><p>This routine is called to log an error to the I/O error log. It is recommended that the <strong>RxLogEvent</strong> or <strong>RxLogFailure</strong> macro be used instead of calling this routine directly.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554519" data-raw-source="[&lt;strong&gt;RxLogEventWithAnnotation&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554519)"><strong>RxLogEventWithAnnotation</strong></a></p></td>
<td align="left"><p>This routine allocates an I/O error log structure, fills in the log structure, and writes this structure to the I/O error log.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554524" data-raw-source="[&lt;strong&gt;RxLogEventWithBufferDirect&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554524)"><strong>RxLogEventWithBufferDirect</strong></a></p></td>
<td align="left"><p>This routine is called to log an error to an I/O error log. This routine encodes the line number and status into the data buffer stored in the I/O error log structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554525" data-raw-source="[&lt;strong&gt;RxLowIoCompletion&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554525)"><strong>RxLowIoCompletion</strong></a></p></td>
<td align="left"><p>This routine must be called by the low I/O routines of a network mini-redirector driver when processing is complete, if the routine initially returned pending.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554529" data-raw-source="[&lt;strong&gt;RxLowIoGetBufferAddress&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554529)"><strong>RxLowIoGetBufferAddress</strong></a></p></td>
<td align="left"><p>This routine returns the buffer that corresponds to the MDL from the <strong>LowIoContext</strong> structure of an RX_CONTEXT structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554532" data-raw-source="[&lt;strong&gt;RxMakeLateDeviceAvailable&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554532)"><strong>RxMakeLateDeviceAvailable</strong></a></p></td>
<td align="left"><p>This routine modifies the device object to make a &quot;late device&quot; available. A late device is one that is not created in the driver&#39;s load routine.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554541" data-raw-source="[&lt;strong&gt;RxMapAndDissociateMidFromContext&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554541)"><strong>RxMapAndDissociateMidFromContext</strong></a></p></td>
<td align="left"><p>This routine maps a MID to its associated context in a MID_ATLAS data structure and then disassociates the MID from the context.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554545" data-raw-source="[&lt;strong&gt;RxMapMidToContext&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554545)"><strong>RxMapMidToContext</strong></a></p></td>
<td align="left"><p>This routine maps a MID to its associated context in a MID_ATLAS data structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554549" data-raw-source="[&lt;strong&gt;RxMapSystemBuffer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554549)"><strong>RxMapSystemBuffer</strong></a></p></td>
<td align="left"><p>This routine returns the system buffer address from the I/O request packet (IRP).</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554552" data-raw-source="[&lt;strong&gt;RxNameCacheActivateEntry&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554552)"><strong>RxNameCacheActivateEntry</strong></a></p></td>
<td align="left"><p>This routine takes a name cache entry and updates the expiration time and the network mini-redirector context. It then puts the entry on the active list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554558" data-raw-source="[&lt;strong&gt;RxNameCacheCheckEntry&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554558)"><strong>RxNameCacheCheckEntry</strong></a></p></td>
<td align="left"><p>This routine checks a NAME_CACHE entry for validity.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554565" data-raw-source="[&lt;strong&gt;RxNameCacheCreateEntry&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554565)"><strong>RxNameCacheCreateEntry</strong></a></p></td>
<td align="left"><p>This routine allocates and initializes a NAME_CACHE structure with the given name string. It is expected that the caller will then initialize any additional network mini-redirector elements of the name cache context and then put the entry on the name cache active list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554569" data-raw-source="[&lt;strong&gt;RxNameCacheExpireEntry&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554569)"><strong>RxNameCacheExpireEntry</strong></a></p></td>
<td align="left"><p>This routine puts a NAME_CACHE entry on the free list.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554570" data-raw-source="[&lt;strong&gt;RxNameCacheExpireEntryWithShortName&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554570)"><strong>RxNameCacheExpireEntryWithShortName</strong></a></p></td>
<td align="left"><p>This routine expires all of the NAME_CACHE entries whose name prefix matches the given short file name.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554573" data-raw-source="[&lt;strong&gt;RxNameCacheFetchEntry&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554573)"><strong>RxNameCacheFetchEntry</strong></a></p></td>
<td align="left"><p>This routine looks for a match with a specified name string for a NAME_CACHE entry.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554575" data-raw-source="[&lt;strong&gt;RxNameCacheFinalize&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554575)"><strong>RxNameCacheFinalize</strong></a></p></td>
<td align="left"><p>This routine releases the storage for all of the NAME_CACHE entries associated with a NAME_CACHE_CONTROL structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554579" data-raw-source="[&lt;strong&gt;RxNameCacheFreeEntry&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554579)"><strong>RxNameCacheFreeEntry</strong></a></p></td>
<td align="left"><p>This routine releases the storage for a NAME_CACHE entry and decrements the count of NAME_CACHE cache entries associated with a NAME_CACHE_CONTROL structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554586" data-raw-source="[&lt;strong&gt;RxNameCacheInitialize&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554586)"><strong>RxNameCacheInitialize</strong></a></p></td>
<td align="left"><p>This routine initializes a NAME_CACHE structure and associates it with a NAME_CACHE_CONTROL structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554591" data-raw-source="[&lt;strong&gt;RxNewMapUserBuffer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554591)"><strong>RxNewMapUserBuffer</strong></a></p></td>
<td align="left"><p>This routine returns the address of the user buffer used for low I/O.</p>
<p>This routine is only available on Windows XP and Windows 2000.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554595" data-raw-source="[&lt;strong&gt;RxpAcquirePrefixTableLockExclusive&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554595)"><strong>RxpAcquirePrefixTableLockExclusive</strong></a></p></td>
<td align="left"><p>This routine acquires an exclusive lock on a prefix table used to catalog SRV_CALL and NET_ROOT names.</p>
<p>This routine is only available on Windows XP and Windows 2000. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554598" data-raw-source="[&lt;strong&gt;RxpAcquirePrefixTableLockShared&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554598)"><strong>RxpAcquirePrefixTableLockShared</strong></a></p></td>
<td align="left"><p>This routine acquires a shared lock on a prefix table used to catalog SRV_CALL and NET_ROOT names.</p>
<p>This routine is only available on Windows XP and Windows 2000. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff554603" data-raw-source="[&lt;strong&gt;RxpDereferenceAndFinalizeNetFcb&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554603)"><strong>RxpDereferenceAndFinalizeNetFcb</strong></a></td>
<td align="left"><p>This routine dereferences the reference count and finalizes an FCB.</p>
<p>This routine is only available on Windows Server 2003 Service Pack 1 (SP1) and later.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554608" data-raw-source="[&lt;strong&gt;RxpDereferenceNetFcb&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554608)"><strong>RxpDereferenceNetFcb</strong></a></p></td>
<td align="left"><p>This routine decrements the reference count on an FCB.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554612" data-raw-source="[&lt;strong&gt;RxPostOneShotTimerRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554612)"><strong>RxPostOneShotTimerRequest</strong></a></p></td>
<td align="left"><p>This routine is used by drivers to initialize a one-shot timer request. The worker thread routine passed to this routine is called once when the timer expires.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554615" data-raw-source="[&lt;strong&gt;RxPostRecurrentTimerRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554615)"><strong>RxPostRecurrentTimerRequest</strong></a></p></td>
<td align="left"><p>This routine is used to initialize a recurrent timer request. The worker thread routine passed to this routine is called at regular intervals when the recurrent timer fires based on the input parameters to this routine.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554620" data-raw-source="[&lt;strong&gt;RxPostToWorkerThread&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554620)"><strong>RxPostToWorkerThread</strong></a></p></td>
<td align="left"><p>This routine invokes the routine in the context of a worker thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554627" data-raw-source="[&lt;strong&gt;RxpReferenceNetFcb&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554627)"><strong>RxpReferenceNetFcb</strong></a></p></td>
<td align="left"><p>This routine increments the reference count on an FCB.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554632" data-raw-source="[&lt;strong&gt;RxPrefixTableLookupName&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554632)"><strong>RxPrefixTableLookupName</strong></a></p></td>
<td align="left"><p>The routine looks up a name in a prefix table used to catalog SRV_CALL and NET_ROOT names and converts from the underlying pointer to the containing structure.</p>
<p>This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554637" data-raw-source="[&lt;strong&gt;RxpReleasePrefixTableLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554637)"><strong>RxpReleasePrefixTableLock</strong></a></p></td>
<td align="left"><p>This routine releases a lock on a prefix table used to catalog SRV_CALL and NET_ROOT names.</p>
<p>This routine is only available on Windows XP and Windows 2000. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554643" data-raw-source="[&lt;strong&gt;RxPrepareContextForReuse&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554643)"><strong>RxPrepareContextForReuse</strong></a></p></td>
<td align="left"><p>This routine prepares an RX_CONTEXT structure for reuse by resetting all operation-specific allocations and acquisitions that have been made. The parameters obtained from the IRP are not modified. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554649" data-raw-source="[&lt;strong&gt;RxPrepareToReparseSymbolicLink&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554649)"><strong>RxPrepareToReparseSymbolicLink</strong></a></p></td>
<td align="left"><p>This routine sets up the file object name to facilitate a reparse. This routine is used by the network mini-redirectors to traverse symbolic links. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554655" data-raw-source="[&lt;strong&gt;RxpTrackDereference&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554655)"><strong>RxpTrackDereference</strong></a></p></td>
<td align="left"><p>This routine is used to track requests to dereference SRV_CALL, NET_ROOT, V_NET_ROOT, FOBX, FCB, and SRV_OPEN structures in checked builds. A log of these dereference requests can be accessed by the logging system and WMI.</p>
<p>For retail builds, this routine does nothing.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554659" data-raw-source="[&lt;strong&gt;RxpTrackReference&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554659)"><strong>RxpTrackReference</strong></a></p></td>
<td align="left"><p>This routine is used to track requests to reference SRV_CALL, NET_ROOT, V_NET_ROOT, FOBX, FCB, and SRV_OPEN structures in checked builds. A log of these reference requests can be accessed by the logging system and WMI.</p>
<p>For retail builds, this routine does nothing.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554662" data-raw-source="[&lt;strong&gt;RxpUnregisterMinirdr&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554662)"><strong>RxpUnregisterMinirdr</strong></a></p></td>
<td align="left"><p>The routine is called by a network mini-redirector driver to unregister the driver with RDBSS and remove the registration information from the internal RDBSS registration table.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554673" data-raw-source="[&lt;strong&gt;RxPurgeAllFobxs&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554673)"><strong>RxPurgeAllFobxs</strong></a></p></td>
<td align="left"><p>This routine purges all the FOBX structures associated with a network mini-redirector.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554679" data-raw-source="[&lt;strong&gt;RxPurgeRelatedFobxs&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554679)"><strong>RxPurgeRelatedFobxs</strong></a></p></td>
<td align="left"><p>This routine purges all of the FOBX structures associated with a NET_ROOT structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554686" data-raw-source="[&lt;strong&gt;RxReassociateMid&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554686)"><strong>RxReassociateMid</strong></a></p></td>
<td align="left"><p>This routine reassociates a MID with an alternate context.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554688" data-raw-source="[&lt;strong&gt;RxReference&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554688)"><strong>RxReference</strong></a></p></td>
<td align="left"><p>This routine increments the reference count on an instance of several of the reference-counted data structures used by RDBSS.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554693" data-raw-source="[&lt;strong&gt;RxRegisterMinirdr&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554693)"><strong>RxRegisterMinirdr</strong></a></p></td>
<td align="left"><p>This routine is called by a network mini-redirector driver to register the driver with RDBSS, which adds the registration information to an internal registration table. RDBSS also builds a device object for the network mini-redirector.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554699" data-raw-source="[&lt;strong&gt;RxReleaseFcbResourceInMRx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554699)"><strong>RxReleaseFcbResourceInMRx</strong></a></p></td>
<td align="left"><p>This routine frees the FCB resource acquired using <strong>RxAcquireExclusiveFcbResourceInMRx</strong> or <strong>RxAcquireSharedFcbResourceInMRx</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff554694" data-raw-source="[&lt;strong&gt;RxReleaseFcbResourceForThreadInMRx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554694)"><strong>RxReleaseFcbResourceForThreadInMRx</strong></a></td>
<td align="left"><p>This routine frees the FCB resource acquired using <a href="https://msdn.microsoft.com/library/windows/hardware/ff553375" data-raw-source="[&lt;strong&gt;RxAcquireSharedFcbResourceInMRxEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553375)"><strong>RxAcquireSharedFcbResourceInMRxEx</strong></a></p>
<p>This routine is only available on Windows Server 2003 Service Pack 1 (SP1) and later.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554701" data-raw-source="[&lt;strong&gt;RxResumeBlockedOperations_Serially&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554701)"><strong>RxResumeBlockedOperations_Serially</strong></a></p></td>
<td align="left"><p>This routine wakes up the next waiting thread, if any, on the serialized blocking I/O queue.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554707" data-raw-source="[&lt;strong&gt;RxScavengeAllFobxs&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554707)"><strong>RxScavengeAllFobxs</strong></a></p></td>
<td align="left"><p>This routine scavenges all of the FOBX structures associated with a given network mini-redirector device object.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554713" data-raw-source="[&lt;strong&gt;RxScavengeFobxsForNetRoot&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554713)"><strong>RxScavengeFobxsForNetRoot</strong></a></p></td>
<td align="left"><p>This routine scavenges all of the FOBX structures that pertain to the given NET_ROOT structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554718" data-raw-source="[&lt;strong&gt;RxSetDomainForMailslotBroadcast&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554718)"><strong>RxSetDomainForMailslotBroadcast</strong></a></p></td>
<td align="left"><p>This routine is called by a network mini-redirector driver to set the domain used for mailslot broadcasts if mailslots are supported by the driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554722" data-raw-source="[&lt;strong&gt;RxSetMinirdrCancelRoutine&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554722)"><strong>RxSetMinirdrCancelRoutine</strong></a></p></td>
<td align="left"><p>This routine sets up a network mini-redirector cancel routine for an RX_CONTEXT structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554728" data-raw-source="[&lt;strong&gt;RxSetSrvCallDomainName&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554728)"><strong>RxSetSrvCallDomainName</strong></a></p></td>
<td align="left"><p>This routine sets the domain name associated with any given server (SRV_CALL structure).</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554734" data-raw-source="[&lt;strong&gt;RxSpinDownMRxDispatcher&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554734)"><strong>RxSpinDownMRxDispatcher</strong></a></p></td>
<td align="left"><p>This routine tears down the dispatcher context for a network mini-redirector.</p>
<p>This routine is only available on Windows XP and later.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554736" data-raw-source="[&lt;strong&gt;RxStartMinirdr&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554736)"><strong>RxStartMinirdr</strong></a></p></td>
<td align="left"><p>This routine starts up a network mini-redirector that called to register itself. RDBSS will also register the network mini-redirector driver as a Universal Naming Convention (UNC) provider with the Multiple UNC Provider (MUP) if the driver indicates support for UNC names.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554743" data-raw-source="[&lt;strong&gt;RxStopMinirdr&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554743)"><strong>RxStopMinirdr</strong></a></p></td>
<td align="left"><p>This routine stops a network mini-redirector driver. A driver that is stopped will no longer accept new commands.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554744" data-raw-source="[&lt;strong&gt;RxUnregisterMinirdr&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554744)"><strong>RxUnregisterMinirdr</strong></a></p></td>
<td align="left"><p>This routine is an inline function defined in <em>rxstruc.h</em> that is called by a network mini-redirector driver to unregister the driver with RDBSS and remove the registration information from the internal RDBSS registration table. The <strong>RxUnregisterMinirdr</strong> inline function internally calls <strong>RxpUnregisterMinirdr</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557355" data-raw-source="[&lt;strong&gt;_RxAllocatePoolWithTag&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557355)"><strong>_RxAllocatePoolWithTag</strong></a></p></td>
<td align="left"><p>This routine allocates memory from a pool with a four-byte tag at the beginning of the block that can be used to help catch instances of memory problems.</p>
<p>It is recommended that the <strong>RxAllocatePoolWithTag</strong> macro be used instead of calling this routine directly.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557358" data-raw-source="[&lt;strong&gt;_RxCheckMemoryBlock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557358)"><strong>_RxCheckMemoryBlock</strong></a></p></td>
<td align="left"><p>This routine checks a memory block for a special RX_POOL_HEADER header signature. Note that a network mini-redirector driver would need to add this special signature block to memory allocated in order to use the routine.</p>
<p>This routine should not be used since this special header block has not been implemented.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557363" data-raw-source="[&lt;strong&gt;_RxFreePool&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557363)"><strong>_RxFreePool</strong></a></p></td>
<td align="left"><p>This routine frees a memory pool.</p>
<p>It is recommended that the <strong>RxFreePool</strong> macro be used instead of calling this routine directly.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557368" data-raw-source="[&lt;strong&gt;_RxLog&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557368)"><strong>_RxLog</strong></a></p></td>
<td align="left"><p>This routine takes a format string and variable number of parameters and formats an output string for structureing as an I/O error log entry if logging is enabled.</p>
<p>It is recommended that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557368" data-raw-source="[&lt;strong&gt;RxLog&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557368)"><strong>RxLog</strong></a> macro be used instead of calling this routine directly.</p>
<p>This routine is only available on checked builds of RDBSS on Windows Server 2003, Windows XP, and Windows 2000.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557374" data-raw-source="[&lt;strong&gt;__RxFillAndInstallFastIoDispatch&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557374)"><strong>__RxFillAndInstallFastIoDispatch</strong></a></p></td>
<td align="left"><p>This routine fills out a fast I/O dispatch vector to be identical with the normal dispatch I/O vector and installs it into the driver object that is associated with the device object passed.</p>
<p>This routine is implemented only for non-monolithic drivers and does nothing on monolithic drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff557377" data-raw-source="[&lt;strong&gt;__RxSynchronizeBlockingOperations&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557377)"><strong>__RxSynchronizeBlockingOperations</strong></a></td>
<td align="left"><p>This routine is used to synchronize blocking I/O to the same work queue. This routine is used internally by RDBSS to synchronize named pipe operations. This routine may be used by a network mini-redirector to synchronize operations on a separate queue that is maintained by the network mini-redirector.</p>
<p>This routine is only available on Windows Server 2003.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff557382" data-raw-source="[&lt;strong&gt;__RxSynchronizeBlockingOperationsMaybeDroppingFcbLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557382)"><strong>__RxSynchronizeBlockingOperationsMaybeDroppingFcbLock</strong></a></td>
<td align="left"><p>This routine is used to synchronize blocking I/O to the same work queue. This routine is used internally by RDBSS to synchronize named pipe operations. This routine may be used by a network mini-redirector to synchronize operations on a separate queue that is maintained by the network mini-redirector.</p>
<p>This routine is only available on Windows XP and Windows 2000.</p></td>
</tr>
</tbody>
</table>

 

 

 




