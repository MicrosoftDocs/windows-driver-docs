---
title: DbgRpc Command-Line Options
description: The DbgRpc command line must always contain exactly one of the -l, -e, -t, -c, or -a switches. The options following these switches depend on the switch used. 
ms.assetid: 1c90f97c-f054-402d-a559-2459528029b9
keywords: ["DbgRpc Command-Line Options Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- DbgRpc Command-Line Options
api_type:
- NA
ms.localizationpriority: medium
---

# DbgRpc Command-Line Options


The DbgRpc command line must always contain exactly one of the -l, -e, -t, -c, or -a switches. The options following these switches depend on the switch used. The -s, -p, and -r options can be used with any other options.

```console
 dbgrpc [-s Server -p ProtSeq] [-r Radix] -l -P ProcessID -L CellID1.CellID2 

dbgrpc [-s Server -p ProtSeq] [-r Radix] -e [-E EndpointName] 

dbgrpc [-s Server -p ProtSeq] [-r Radix] -t -P ProcessID [-T ThreadID] 

dbgrpc [-s Server -p ProtSeq] [-r Radix] [-c|-a] [-C CallID] [-I IfStart] [-N ProcNum] [-P ProcessID] 

dbgrpc -? 
```

## <span id="ddk_dbgrpc_command_line_options_dbg"></span><span id="DDK_DBGRPC_COMMAND_LINE_OPTIONS_DBG"></span>Parameters


<span id="_______-s_______Server______"></span><span id="_______-s_______server______"></span><span id="_______-S_______SERVER______"></span> **-s** *Server*   
Allows DbgRpc to view information from a remote machine. The server name should not be preceded by slash marks. For more information about using DbgRpc remotely, see [Using the DbgRpc Tool](using-the-dbgrpc-tool.md).

<span id="_______-p_______ProtSeq______"></span><span id="_______-p_______protseq______"></span><span id="_______-P_______PROTSEQ______"></span> **-p** *ProtSeq*   
Specifies the remote transport to be used. The possible values of *ProtSeq* are **ncacn\_ip\_tcp** (TCP protocol) and **ncacn\_np** (named pipe protocol). TCP protocol is recommended. For more information about using DbgRpc remotely, see [Using the DbgRpc Tool](using-the-dbgrpc-tool.md).

<span id="_______-r_______Radix______"></span><span id="_______-r_______radix______"></span><span id="_______-R_______RADIX______"></span> **-r** *Radix*   
Specifies the radix to be used for the command parameters. The default is base 16. If the **-r** parameter is used, it should be placed first on the line, since it only affects parameters listed after itself. It does not affect the output of the DbgRpc tool.

<span id="_______-l______"></span><span id="_______-L______"></span> **-l**   
Displays RPC state information for the specified cell. For an example, see [Get RPC Cell Information](get-rpc-cell-information.md).

<span id="_______ProcessID______"></span><span id="_______processid______"></span><span id="_______PROCESSID______"></span> *ProcessID*   
Specifies the process ID (PID) of a process. When the **-l** option is being used, this should be the process whose server contains the desired cell. When the **-t** option is being used, this should be the process containing the desired thread. When the **-c** or **-a** options are being used, this parameter is optional; it should be the server process that owns the calls you wish to display.

<span id="cellid1.cellid2______"></span><span id="CELLID1.CELLID2______"></span>*CellID1*.*CellID2*   
Specifies the number of the cell to be displayed.

<span id="_______-e______"></span><span id="_______-E______"></span> **-e**   
Searches the system's RPC state information for endpoint information. For an example, see [Get RPC Endpoint Information](get-rpc-endpoint-information.md).

<span id="_______EndpointName______"></span><span id="_______endpointname______"></span><span id="_______ENDPOINTNAME______"></span> *EndpointName*   
Specifies the number of the endpoint to be displayed. If omitted, the endpoints for all processes on the system are displayed.

<span id="_______-t______"></span><span id="_______-T______"></span> **-t**   
Searches the system's RPC state information for thread information. For an example, see [Get RPC Thread Information](get-rpc-thread-information.md).

<span id="_______ThreadID______"></span><span id="_______threadid______"></span><span id="_______THREADID______"></span> *ThreadID*   
Specifies the thread ID of the thread to be displayed. If omitted, all threads in the specified process will be displayed.

<span id="_______-c______"></span><span id="_______-C______"></span> **-c**   
Searches the system's RPC state information for server-side call (SCALL) information. For an example, see [Get RPC Call Information](get-rpc-call-information.md).

<span id="_______-a______"></span><span id="_______-A______"></span> **-a**   
Searches the system's RPC state information for client call (CCALL) information. For an example, see [Get RPC Client Call Information](get-rpc-client-call-information.md). This option requires full RPC state information.

<span id="_______CallID______"></span><span id="_______callid______"></span><span id="_______CALLID______"></span> *CallID*   
Specifies the call ID. This parameter is optional; include it only if you want to display calls matching a specific *CallID* value.

<span id="_______IfStart______"></span><span id="_______ifstart______"></span><span id="_______IFSTART______"></span> *IfStart*   
Specifies the first DWORD of the interface's universally unique identifier (UUID) on which the call was made. This parameter is optional; include it only if you want to display calls matching a specific *IfStart* value.

<span id="_______ProcNum______"></span><span id="_______procnum______"></span><span id="_______PROCNUM______"></span> *ProcNum*   
Specifies the procedure number of this call. (The RPC Run-Time identifies individual routines from an interface by numbering them by position in the IDL file -- the first routine in the interface is 0, the second 1, and so on.) This parameter is optional; include it only if you want to display calls matching a specific *ProcNum* value.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about debugging Microsoft Remote Procedure Call (RPC), see [RPC Debugging](rpc-debugging.md).

 

 





