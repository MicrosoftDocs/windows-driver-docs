---
title: RPC State Information Internals
description: RPC State Information Internals
ms.assetid: fac4a1e4-e1ec-41f2-8de9-073a04a979be
keywords: ["RPC debugging, RPC state information internals"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# RPC State Information Internals


## <span id="ddk_rpc_state_information_internals_dbg"></span><span id="DDK_RPC_STATE_INFORMATION_INTERNALS_DBG"></span>


This section provides details of the internal structure of the state information gathered by the RPC Run-Time.

All RPC run-time state information is contained in cells. A cell is the smallest unit of information that can be viewed and updated individually.

Each key object in the RPC Run-Time will maintain one or more cells of information about its state. Each cell has a cell ID. When an objects refers to another object, it does so by specifying that object's cell ID. The key objects that the RPC Run-Time can maintain information about are endpoints, threads, connection objects, Server Call (SCALL) objects, and Client Call (CCALL) objects.

**When an RPC server is running**, the RPC Run-Time listens on a set of endpoints using one or more worker threads. Whenever data is transmitted to the server, a thread picks up the data and determines what the incoming request is. If the request is to create a connection, a Connection object is created, and this object then services all calls on the connection. When an RPC call is made on the connection, the Connection object instantiates a Server Call (SCALL) object corresponding to the Client Call (CCALL) object. This Server Call object then handles this particular call.

**When an RPC client is running**, the RPC Run-Time creates a Client Call object each time a call is made. This Client Call object contains information about this particular call.

### <span id="endpoint_cells"></span><span id="ENDPOINT_CELLS"></span>Endpoint Cells

From the RPC run-time's point of view, an endpoint is an entry point through which the particular server can be contacted. The endpoint is always associated with a given RPC transport. The endpoint state information is used to associate a client call with a particular process on the server.

The fields in an endpoint cell are:

<span id="ProtseqType"></span><span id="protseqtype"></span><span id="PROTSEQTYPE"></span>**ProtseqType**  
The protocol sequence for this endpoint.

<span id="Status"></span><span id="status"></span><span id="STATUS"></span>**Status**  
The status value: *allocated*, *active*, or *inactive*. Most endpoints are active. An endpoint has *allocated* status when the creation process has started, but is not complete yet. An endpoint is *inactive* if it is no longer in use (for example, when a protocol has been uninstalled).

<span id="EndpointName"></span><span id="endpointname"></span><span id="ENDPOINTNAME"></span>**EndpointName**  
The first 28 characters of the endpoint name.

### <span id="thread_cells"></span><span id="THREAD_CELLS"></span>Thread Cells

Server threads are worker threads (standard Win32 threads for use by RPC).

The fields in a thread cell are:

<span id="Status"></span><span id="status"></span><span id="STATUS"></span>**Status**  
The status value: *processing*, *dispatched*, *allocated*, or *idle*. A *processing* thread is one that is within the Run-Time and is processing information. A *dispatched* thread has already dispatched (called) to the server-provided manager routine (usually just called the *server routine*). An *allocated* thread has been cached. An *idle* thread is available to service requests.

<span id="LastUpdateTime"></span><span id="lastupdatetime"></span><span id="LASTUPDATETIME"></span>**LastUpdateTime**  
The time (in milliseconds after boot) when the information was last updated.

<span id="TID"></span><span id="tid"></span>**TID**  
The thread ID of this thread. This is useful when trying to correlate with the thread list in the debugger.

### <span id="connection_object_cells"></span><span id="CONNECTION_OBJECT_CELLS"></span>Connection Object Cells

The fields in a connection object cell are:

<span id="Flags"></span><span id="flags"></span><span id="FLAGS"></span>**Flags**  
Flag values include *exclusive*/*non-exclusive*, *authentication level*, and *authentication service*.

<span id="LastTransmitFragmentSize"></span><span id="lasttransmitfragmentsize"></span><span id="LASTTRANSMITFRAGMENTSIZE"></span>**LastTransmitFragmentSize**  
The size of the last fragment transmitted over the connection.

<span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>**Endpoint**  
The cell ID of the endpoint that this connection was picked up from.

<span id="LastSendTime"></span><span id="lastsendtime"></span><span id="LASTSENDTIME"></span>**LastSendTime**  
The last time data was sent on a connection.

<span id="LastReceiveTime"></span><span id="lastreceivetime"></span><span id="LASTRECEIVETIME"></span>**LastReceiveTime**  
The last time data was received on a connection.

### <span id="server_call_object_cells"></span><span id="SERVER_CALL_OBJECT_CELLS"></span>Server Call Object Cells

The fields in a Server Call (SCALL) object cell are:

<span id="Status"></span><span id="status"></span><span id="STATUS"></span>**Status**  
The status value: *allocated*, *active*, or *dispatched*. An *allocated* call is inactive and cached. When a call is *active*, the RPC Run-Time is processing information related to this call. When a call is *dispatched*, the manager routine (server routine) has been called and has not returned yet.

<span id="ProcNum"></span><span id="procnum"></span><span id="PROCNUM"></span>**ProcNum**  
The procedure number (operation number, in netmon capture files) of this call. The RPC Run-Time identifies individual routines from an interface by numbering them by position in the IDL file. The first routine in the interface will be number zero, the second number one, and so on.

<span id="InterfaceUUIDStart"></span><span id="interfaceuuidstart"></span><span id="INTERFACEUUIDSTART"></span>**InterfaceUUIDStart**  
The first DWORD of the interface UUID.

<span id="ServicingTID"></span><span id="servicingtid"></span><span id="SERVICINGTID"></span>**ServicingTID**  
The cell ID of the thread that is servicing this call. If the call is not *active* or *dispatched*, this contains stale information.

<span id="CallFlags"></span><span id="callflags"></span><span id="CALLFLAGS"></span>**CallFlags**  
These flag values indicate whether this is the cached call in an exclusive connection, whether this is an asynchronous call, whether this is a pipe call, and whether this is an LRPC or OSF call.

<span id="LastUpdateTime"></span><span id="lastupdatetime"></span><span id="LASTUPDATETIME"></span>**LastUpdateTime**  
The time (in milliseconds after boot) when the call object state information was last updated.

<span id="PID"></span><span id="pid"></span>**PID**  
The Process ID of the caller. Valid only for LRPC calls.

<span id="TID"></span><span id="tid"></span>**TID**  
The Thread ID of the caller. Valid only for LRPC calls.

### <span id="client_call_object_cells"></span><span id="CLIENT_CALL_OBJECT_CELLS"></span>Client Call Object Cells

A Client Call (CCALL) object is broken into two cells, because the information about a client call is too large to fit in one cell. The first cell is called *Client Call Information*, and the second is called *Call Target Information*. Most tools will show the information together, so you do not need to distinguish between them.

Information about client calls is not maintained unless you are gathering Full state information. There is one exception to this rule: information about client calls made within a server call is maintained even when only Server state information is being gathered. This allows you to trace calls spanning multiple hops.

The fields in the Client Call Information cell are:

<span id="ProcNum"></span><span id="procnum"></span><span id="PROCNUM"></span>**ProcNum**  
The procedure number (operation number, in netmon capture files) of the method being called. The RPC Run-Time identifies individual routines from an interface by numbering them by position in the IDL file. The first routine in the interface will be number zero, the second number one, and so on.

<span id="ServicingThread"></span><span id="servicingthread"></span><span id="SERVICINGTHREAD"></span>**ServicingThread**  
The cell ID of the thread on which this call is made.

<span id="IfStart"></span><span id="ifstart"></span><span id="IFSTART"></span>**IfStart**  
The first DWORD of the interface UUID on which the call is made.

<span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>**Endpoint**  
The first 12 characters of the endpoint on the server to which the call was made.

The fields in the Call Target Information cell are:

<span id="ProtocolSequence"></span><span id="protocolsequence"></span><span id="PROTOCOLSEQUENCE"></span>**ProtocolSequence**  
The protocol sequence for this call.

<span id="LastUpdateTime"></span><span id="lastupdatetime"></span><span id="LASTUPDATETIME"></span>**LastUpdateTime**  
The time (in milliseconds after boot) when the information about the client call or the call target was updated.

<span id="TargetServer"></span><span id="targetserver"></span><span id="TARGETSERVER"></span>**TargetServer**  
The first 24 characters of the name of the server to which the call is made.

 

 





