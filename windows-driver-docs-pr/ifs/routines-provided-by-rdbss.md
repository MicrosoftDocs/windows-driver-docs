---
title: Routines Provided by RDBSS
author: windows-driver-content
description: Routines Provided by RDBSS
ms.assetid: 37631760-ac89-4ef0-ad7c-ed3e68aa1ceb
keywords:
- RDBSS WDK file systems , routines
- Redirected Drive Buffering Subsystem WDK file systems , routines
- routines WDK RDBSS
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>[<strong>RxAcquireExclusiveFcbResourceInMRx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553363)</p></td>
<td align="left"><p>This resource acquisition routine acquires the File Control Block (FCB) resource in exclusive mode. This routine will wait for the FCB resource to be free, so this routine does not return control until the resource has been acquired. This routine acquires the FCB resource even if the RX_CONTEXT associated with this FCB has been canceled.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxAcquireSharedFcbResourceInMRx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553372)</p></td>
<td align="left"><p>This resource acquisition routine acquires the FCB resource in shared mode. This routine will wait for the FCB resource to be free if it was previously acquired exclusively, so this routine does not return control until the resource has been acquired. This routine acquires the FCB resource even if the RX_CONTEXT associated with this FCB has been canceled.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>RxAcquireSharedFcbResourceInMRxEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553375)</td>
<td align="left"><p>This resource acquisition routine acquires the FCB resource in shared mode. This routine will wait for the FCB resource to be freed if it was previously acquired exclusively. This routine does not return control until the resource has been acquired. This routine acquires the FCB resource even if the RX_CONTEXT associated with this FCB has been canceled.</p>
<p>This routine is only available on Windows Server 2003 Service Pack 1 (SP1) and later.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxAssert</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553384)</p></td>
<td align="left"><p>This routine sends an assert string in RDBSS checked builds to a kernel debugger if one is installed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxAssociateContextWithMid</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553388)</p></td>
<td align="left"><p>This routine associates the supplied opaque context with an available multiplex ID (MID) from a MID_ATLAS data structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCancelTimerRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553395)</p></td>
<td align="left"><p>This routine cancels a timer request. The request to be canceled is identified by the routine and context.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxCeAllocateIrpWithMDL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553405)</p></td>
<td align="left"><p>This routine allocates an IRP for use by the connection engine and associates an MDL with the IRP.</p>
<p>This routine is only available on Windows XP.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCeBuildAddress</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553414)</p></td>
<td align="left"><p>This routine associates a transport address with a transport binding.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxCeBuildConnection</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553417)</p></td>
<td align="left"><p>This routine establishes a connection between a local RDBSS connection address and a given remote address. This routine should be called in the context of a system worker thread.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCeBuildConnectionOverMultipleTransports</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553424)</p></td>
<td align="left"><p>This routine establishes a connection between a local RDBSS connection address and a given remote address and supports multiple transports. A set of local addresses are specified and this routine attempts to connect to the target server using all of the transports associated with the local addresses. One connection is chosen as the winner depending on the connection options. This routine must be called in the context of a system worker thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxCeBuildTransport</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553434)</p></td>
<td align="left"><p>This routine binds an RDBSS transport to a specified transport name.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCeBuildVC</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553439)</p></td>
<td align="left"><p>This routine adds a virtual circuit to a specified connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxCeCancelConnectRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553440)</p></td>
<td align="left"><p>This routine cancels a previously issued connection request.</p>
<p>Note that this routine is not currently implemented.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCeFreeIrp</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553448)</p></td>
<td align="left"><p>This routine frees an IRP used by the connection engine.</p>
<p>This routine is only available on Windows XP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxCeInitiateVCDisconnect</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553454)</p></td>
<td align="left"><p>This routine initiates a disconnect on the virtual circuit. This routine must be called in the context of a system worker thread.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCeQueryAdapterStatus</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553456)</p></td>
<td align="left"><p>This routine returns the ADAPTER_STATUS structure for a given transport.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxCeQueryInformation</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553461)</p></td>
<td align="left"><p>This routine queries for information about a given virtual circuit.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCeQueryTransportInformation</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553474)</p></td>
<td align="left"><p>This routine queries a given transport for information about the connection count and quality of service.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxCeSend</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553479)</p></td>
<td align="left"><p>This routine sends a transport service data unit (TSDU) along the specified connection on a virtual circuit.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCeSendDatagram</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553482)</p></td>
<td align="left"><p>This routine sends a TSDU to a specified transport address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxCeTearDownAddress</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553488)</p></td>
<td align="left"><p>This routine removes a transport address from a transport binding.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCeTearDownConnection</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554321)</p></td>
<td align="left"><p>This routine tears down a given connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxCeTearDownTransport</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554328)</p></td>
<td align="left"><p>This routine unbinds from the transport specified.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCeTearDownVC</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554332)</p></td>
<td align="left"><p>This routine tears down a virtual connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxChangeBufferingState</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554335)</p></td>
<td align="left"><p>This routine is called to process a buffering state change request.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCompleteRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554340)</p></td>
<td align="left"><p>This routine is used to complete an IRP associated with an RX_CONTEXT structure. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxCompleteRequest_Real</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554348)</p></td>
<td align="left"><p>This routine is used to complete an IRP associated with an RX_CONTEXT structure. This routine should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCreateMidAtlas</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554352)</p></td>
<td align="left"><p>This routine allocates a new instance of a MID_ATLAS data structure and initializes it. RDBSS uses the multiplex ID (MID) defined in this data structure as a way that both the network client (mini-redirector) and the server can distinguish between the concurrently active requests on any connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxCreateNetFcb</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554356)</p></td>
<td align="left"><p>This routine allocates, initializes, and inserts a new FCB structure into the in-memory data structures for a NET_ROOT structure on which this FCB is opened. The structure allocated has space for a SRV_OPEN and an FOBX structure. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCreateNetFobx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554358)</p></td>
<td align="left"><p>This routine allocates, initializes, and inserts a new file object extension (FOBX) structure. Network mini-redirectors should call this routine to create an FOBX at the end of a successful create operation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxCreateNetRoot</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554366)</p></td>
<td align="left"><p>This routine builds a node representing a NET_ROOT structure and inserts the name into the net name table on the associated device object. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCreateRxContext</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554367)</p></td>
<td align="left"><p>This routine allocates a new RX_CONTEXT structure and initializes the data structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxCreateSrvCall</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554370)</p></td>
<td align="left"><p>This routine builds a node that represents a server call context and inserts the name into the net name table maintained by RDBSS. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCreateSrvOpen</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554376)</p></td>
<td align="left"><p>This routine allocates, initializes, and inserts a new SRV_OPEN structure into the in-memory data structures used by RDBSS. If a new structure has to be allocated, it has space for an FOBX structure. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxCreateVNetRoot</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554380)</p></td>
<td align="left"><p>This routine builds a node that represents a V_NET_ROOT structure and inserts the name into the net name table. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxDbgBreakPoint</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554385)</p></td>
<td align="left"><p>This routine raises an exception that is handled by the kernel debugger if one is installed; otherwise, it is handled by the debug system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxDereference</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554388)</p></td>
<td align="left"><p>This routine decrements the reference count on an instance of several of the reference-counted data structures used by RDBSS.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxDereferenceAndDeleteRxContext_Real</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554393)</p></td>
<td align="left"><p>This routine dereferences an RX_CONTEXT structure and if the reference count goes to zero, then it deallocates and removes the specified RX_CONTEXT structure from the RDBSS in-memory data structures.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxDestroyMidAtlas</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554395)</p></td>
<td align="left"><p>This routine destroys an existing instance of a MID_ATLAS data structure and frees the memory allocated.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxDispatchToWorkerThread</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554398)</p></td>
<td align="left"><p>This routine invokes a routine in the context of a worker thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxDriverEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554404)</p></td>
<td align="left"><p>This routine is called by a monolithic network mini-redirector driver from its <strong>DriverEntry</strong> to initialize RDBSS.</p>
<p>For non-monolithic drivers, this initialization routine is equivalent to the <strong>DriverEntry</strong> routine of the <em>rdbss.sys</em> device driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxFinalizeConnection</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554409)</p></td>
<td align="left"><p>This routine deletes a connection to a share. Any files open on the connection are closed depending on the level of force specified. The network mini-redirector might choose to keep the transport connection open for performance reasons, unless some option is specified to force a close of connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxFinalizeNetFcb</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554412)</p></td>
<td align="left"><p>This routine finalizes the given FCB structure. The caller must have an exclusive lock on the NET_ROOT structure associated with FCB. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxFinalizeNetFobx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554418)</p></td>
<td align="left"><p>This routine finalizes the given FOBX structure. The caller must have an exclusive lock on the FCB associated with this FOBX. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxFinalizeNetRoot</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554421)</p></td>
<td align="left"><p>This routine finalizes the given NET_ROOT structure. The caller should have exclusive access to the lock on the NetName table of the device object associated with this NET_ROOT structure (through the SRV_CALL structure). This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxFinalizeSrvCall</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554426)</p></td>
<td align="left"><p>This routine finalizes the given SRV_CALL structure. The caller should have exclusive access to the lock on the NetName table of the device object associated with this SRV_CALL structure. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxFinalizeSrvOpen</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554432)</p></td>
<td align="left"><p>This routine finalizes the given SRV_OPEN structure. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
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
<td align="left"><p>[<strong>RxFsdDispatch</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554468)</p></td>
<td align="left"><p>This routine implements the file system driver (FSD) dispatch for RDBSS to process an I/O request packet (IRP). This routine is called by a network mini-redirector in the driver dispatch routines to initiate RDBSS processing of a request.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxFsdPostRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554472)</p></td>
<td align="left"><p>This routine queues the I/O request packet (IRP) specified by an RX_CONTEXT structure to the worker queue for processing by the file system process (FSP).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxGetFileSizeWithLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554478)</p></td>
<td align="left"><p>This routine gets the file size from the FCB structure using a lock to ensure that the 64-bit value is read consistently.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxGetRDBSSProcess</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554481)</p></td>
<td align="left"><p>This routine returns a pointer to the process of the main thread used by the RDBSS kernel process.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxIndicateChangeOfBufferingState</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554485)</p></td>
<td align="left"><p>This routine is called to register a buffering state change request (an oplock break indication, for example) for later processing.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxIndicateChangeOfBufferingStateForSrvOpen</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554490)</p></td>
<td align="left"><p>This routine is called to register a buffering state change request (an oplock break indication, for example) for later processing.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxInferFileType</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554493)</p></td>
<td align="left"><p>This routine tries to infer the file type (directory or non-directory) from the <strong>CreateOptions</strong> ( <strong>Create.NtCreateParameters.CreateOptions</strong>) field in the RX_CONTEXT structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxInitializeContext</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554502)</p></td>
<td align="left"><p>This routine initializes a newly allocated RX_CONTEXT structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxIsThisACscAgentOpen</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554508)</p></td>
<td align="left"><p>This routine determines if a file open was made by a user-mode client-side caching agent.</p>
<p>This routine is only available on Windows Server 2003.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxLockEnumerator</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554511)</p></td>
<td align="left"><p>This routine is called from a network mini-redirector to enumerate the file locks on an FCB.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxLogEventDirect</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554515)</p></td>
<td align="left"><p>This routine is called to log an error to the I/O error log. It is recommended that the <strong>RxLogEvent</strong> or <strong>RxLogFailure</strong> macro be used instead of calling this routine directly.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxLogEventWithAnnotation</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554519)</p></td>
<td align="left"><p>This routine allocates an I/O error log structure, fills in the log structure, and writes this structure to the I/O error log.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxLogEventWithBufferDirect</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554524)</p></td>
<td align="left"><p>This routine is called to log an error to an I/O error log. This routine encodes the line number and status into the data buffer stored in the I/O error log structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxLowIoCompletion</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554525)</p></td>
<td align="left"><p>This routine must be called by the low I/O routines of a network mini-redirector driver when processing is complete, if the routine initially returned pending.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxLowIoGetBufferAddress</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554529)</p></td>
<td align="left"><p>This routine returns the buffer that corresponds to the MDL from the <strong>LowIoContext</strong> structure of an RX_CONTEXT structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxMakeLateDeviceAvailable</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554532)</p></td>
<td align="left"><p>This routine modifies the device object to make a &quot;late device&quot; available. A late device is one that is not created in the driver's load routine.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxMapAndDissociateMidFromContext</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554541)</p></td>
<td align="left"><p>This routine maps a MID to its associated context in a MID_ATLAS data structure and then disassociates the MID from the context.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxMapMidToContext</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554545)</p></td>
<td align="left"><p>This routine maps a MID to its associated context in a MID_ATLAS data structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxMapSystemBuffer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554549)</p></td>
<td align="left"><p>This routine returns the system buffer address from the I/O request packet (IRP).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxNameCacheActivateEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554552)</p></td>
<td align="left"><p>This routine takes a name cache entry and updates the expiration time and the network mini-redirector context. It then puts the entry on the active list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxNameCacheCheckEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554558)</p></td>
<td align="left"><p>This routine checks a NAME_CACHE entry for validity.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxNameCacheCreateEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554565)</p></td>
<td align="left"><p>This routine allocates and initializes a NAME_CACHE structure with the given name string. It is expected that the caller will then initialize any additional network mini-redirector elements of the name cache context and then put the entry on the name cache active list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxNameCacheExpireEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554569)</p></td>
<td align="left"><p>This routine puts a NAME_CACHE entry on the free list.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxNameCacheExpireEntryWithShortName</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554570)</p></td>
<td align="left"><p>This routine expires all of the NAME_CACHE entries whose name prefix matches the given short file name.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxNameCacheFetchEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554573)</p></td>
<td align="left"><p>This routine looks for a match with a specified name string for a NAME_CACHE entry.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxNameCacheFinalize</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554575)</p></td>
<td align="left"><p>This routine releases the storage for all of the NAME_CACHE entries associated with a NAME_CACHE_CONTROL structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxNameCacheFreeEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554579)</p></td>
<td align="left"><p>This routine releases the storage for a NAME_CACHE entry and decrements the count of NAME_CACHE cache entries associated with a NAME_CACHE_CONTROL structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxNameCacheInitialize</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554586)</p></td>
<td align="left"><p>This routine initializes a NAME_CACHE structure and associates it with a NAME_CACHE_CONTROL structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxNewMapUserBuffer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554591)</p></td>
<td align="left"><p>This routine returns the address of the user buffer used for low I/O.</p>
<p>This routine is only available on Windows XP and Windows 2000.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxpAcquirePrefixTableLockExclusive</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554595)</p></td>
<td align="left"><p>This routine acquires an exclusive lock on a prefix table used to catalog SRV_CALL and NET_ROOT names.</p>
<p>This routine is only available on Windows XP and Windows 2000. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxpAcquirePrefixTableLockShared</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554598)</p></td>
<td align="left"><p>This routine acquires a shared lock on a prefix table used to catalog SRV_CALL and NET_ROOT names.</p>
<p>This routine is only available on Windows XP and Windows 2000. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>RxpDereferenceAndFinalizeNetFcb</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554603)</td>
<td align="left"><p>This routine dereferences the reference count and finalizes an FCB.</p>
<p>This routine is only available on Windows Server 2003 Service Pack 1 (SP1) and later.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxpDereferenceNetFcb</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554608)</p></td>
<td align="left"><p>This routine decrements the reference count on an FCB.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxPostOneShotTimerRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554612)</p></td>
<td align="left"><p>This routine is used by drivers to initialize a one-shot timer request. The worker thread routine passed to this routine is called once when the timer expires.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxPostRecurrentTimerRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554615)</p></td>
<td align="left"><p>This routine is used to initialize a recurrent timer request. The worker thread routine passed to this routine is called at regular intervals when the recurrent timer fires based on the input parameters to this routine.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxPostToWorkerThread</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554620)</p></td>
<td align="left"><p>This routine invokes the routine in the context of a worker thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxpReferenceNetFcb</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554627)</p></td>
<td align="left"><p>This routine increments the reference count on an FCB.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxPrefixTableLookupName</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554632)</p></td>
<td align="left"><p>The routine looks up a name in a prefix table used to catalog SRV_CALL and NET_ROOT names and converts from the underlying pointer to the containing structure.</p>
<p>This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxpReleasePrefixTableLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554637)</p></td>
<td align="left"><p>This routine releases a lock on a prefix table used to catalog SRV_CALL and NET_ROOT names.</p>
<p>This routine is only available on Windows XP and Windows 2000. This routine is used internally by RDBSS and should not be used by network mini-redirector drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxPrepareContextForReuse</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554643)</p></td>
<td align="left"><p>This routine prepares an RX_CONTEXT structure for reuse by resetting all operation-specific allocations and acquisitions that have been made. The parameters obtained from the IRP are not modified. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxPrepareToReparseSymbolicLink</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554649)</p></td>
<td align="left"><p>This routine sets up the file object name to facilitate a reparse. This routine is used by the network mini-redirectors to traverse symbolic links. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxpTrackDereference</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554655)</p></td>
<td align="left"><p>This routine is used to track requests to dereference SRV_CALL, NET_ROOT, V_NET_ROOT, FOBX, FCB, and SRV_OPEN structures in checked builds. A log of these dereference requests can be accessed by the logging system and WMI.</p>
<p>For retail builds, this routine does nothing.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxpTrackReference</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554659)</p></td>
<td align="left"><p>This routine is used to track requests to reference SRV_CALL, NET_ROOT, V_NET_ROOT, FOBX, FCB, and SRV_OPEN structures in checked builds. A log of these reference requests can be accessed by the logging system and WMI.</p>
<p>For retail builds, this routine does nothing.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxpUnregisterMinirdr</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554662)</p></td>
<td align="left"><p>The routine is called by a network mini-redirector driver to unregister the driver with RDBSS and remove the registration information from the internal RDBSS registration table.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxPurgeAllFobxs</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554673)</p></td>
<td align="left"><p>This routine purges all the FOBX structures associated with a network mini-redirector.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxPurgeRelatedFobxs</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554679)</p></td>
<td align="left"><p>This routine purges all of the FOBX structures associated with a NET_ROOT structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxReassociateMid</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554686)</p></td>
<td align="left"><p>This routine reassociates a MID with an alternate context.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxReference</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554688)</p></td>
<td align="left"><p>This routine increments the reference count on an instance of several of the reference-counted data structures used by RDBSS.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxRegisterMinirdr</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554693)</p></td>
<td align="left"><p>This routine is called by a network mini-redirector driver to register the driver with RDBSS, which adds the registration information to an internal registration table. RDBSS also builds a device object for the network mini-redirector.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxReleaseFcbResourceInMRx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554699)</p></td>
<td align="left"><p>This routine frees the FCB resource acquired using <strong>RxAcquireExclusiveFcbResourceInMRx</strong> or <strong>RxAcquireSharedFcbResourceInMRx</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>RxReleaseFcbResourceForThreadInMRx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554694)</td>
<td align="left"><p>This routine frees the FCB resource acquired using [<strong>RxAcquireSharedFcbResourceInMRxEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553375)</p>
<p>This routine is only available on Windows Server 2003 Service Pack 1 (SP1) and later.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxResumeBlockedOperations_Serially</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554701)</p></td>
<td align="left"><p>This routine wakes up the next waiting thread, if any, on the serialized blocking I/O queue.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxScavengeAllFobxs</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554707)</p></td>
<td align="left"><p>This routine scavenges all of the FOBX structures associated with a given network mini-redirector device object.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxScavengeFobxsForNetRoot</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554713)</p></td>
<td align="left"><p>This routine scavenges all of the FOBX structures that pertain to the given NET_ROOT structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxSetDomainForMailslotBroadcast</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554718)</p></td>
<td align="left"><p>This routine is called by a network mini-redirector driver to set the domain used for mailslot broadcasts if mailslots are supported by the driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxSetMinirdrCancelRoutine</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554722)</p></td>
<td align="left"><p>This routine sets up a network mini-redirector cancel routine for an RX_CONTEXT structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxSetSrvCallDomainName</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554728)</p></td>
<td align="left"><p>This routine sets the domain name associated with any given server (SRV_CALL structure).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxSpinDownMRxDispatcher</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554734)</p></td>
<td align="left"><p>This routine tears down the dispatcher context for a network mini-redirector.</p>
<p>This routine is only available on Windows XP and later.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxStartMinirdr</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554736)</p></td>
<td align="left"><p>This routine starts up a network mini-redirector that called to register itself. RDBSS will also register the network mini-redirector driver as a Universal Naming Convention (UNC) provider with the Multiple UNC Provider (MUP) if the driver indicates support for UNC names.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxStopMinirdr</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554743)</p></td>
<td align="left"><p>This routine stops a network mini-redirector driver. A driver that is stopped will no longer accept new commands.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxUnregisterMinirdr</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554744)</p></td>
<td align="left"><p>This routine is an inline function defined in <em>rxstruc.h</em> that is called by a network mini-redirector driver to unregister the driver with RDBSS and remove the registration information from the internal RDBSS registration table. The <strong>RxUnregisterMinirdr</strong> inline function internally calls <strong>RxpUnregisterMinirdr</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>_RxAllocatePoolWithTag</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557355)</p></td>
<td align="left"><p>This routine allocates memory from a pool with a four-byte tag at the beginning of the block that can be used to help catch instances of memory problems.</p>
<p>It is recommended that the <strong>RxAllocatePoolWithTag</strong> macro be used instead of calling this routine directly.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>_RxCheckMemoryBlock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557358)</p></td>
<td align="left"><p>This routine checks a memory block for a special RX_POOL_HEADER header signature. Note that a network mini-redirector driver would need to add this special signature block to memory allocated in order to use the routine.</p>
<p>This routine should not be used since this special header block has not been implemented.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>_RxFreePool</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557363)</p></td>
<td align="left"><p>This routine frees a memory pool.</p>
<p>It is recommended that the <strong>RxFreePool</strong> macro be used instead of calling this routine directly.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>_RxLog</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557368)</p></td>
<td align="left"><p>This routine takes a format string and variable number of parameters and formats an output string for structureing as an I/O error log entry if logging is enabled.</p>
<p>It is recommended that the [<strong>RxLog</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557368) macro be used instead of calling this routine directly.</p>
<p>This routine is only available on checked builds of RDBSS on Windows Server 2003, Windows XP, and Windows 2000.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>__RxFillAndInstallFastIoDispatch</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557374)</p></td>
<td align="left"><p>This routine fills out a fast I/O dispatch vector to be identical with the normal dispatch I/O vector and installs it into the driver object that is associated with the device object passed.</p>
<p>This routine is implemented only for non-monolithic drivers and does nothing on monolithic drivers.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>__RxSynchronizeBlockingOperations</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557377)</td>
<td align="left"><p>This routine is used to synchronize blocking I/O to the same work queue. This routine is used internally by RDBSS to synchronize named pipe operations. This routine may be used by a network mini-redirector to synchronize operations on a separate queue that is maintained by the network mini-redirector.</p>
<p>This routine is only available on Windows Server 2003.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>__RxSynchronizeBlockingOperationsMaybeDroppingFcbLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557382)</td>
<td align="left"><p>This routine is used to synchronize blocking I/O to the same work queue. This routine is used internally by RDBSS to synchronize named pipe operations. This routine may be used by a network mini-redirector to synchronize operations on a separate queue that is maintained by the network mini-redirector.</p>
<p>This routine is only available on Windows XP and Windows 2000.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------


