---
title: Get RPC Endpoint Information
description: Get RPC Endpoint Information
ms.assetid: 8e852855-896c-4553-8a58-8ca49c7b2e0a
keywords: ["RPC endpoint Information"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Get RPC Endpoint Information


## <span id="ddk_get_rpc_endpoint_information_dbg"></span><span id="DDK_GET_RPC_ENDPOINT_INFORMATION_DBG"></span>


Endpoint information is displayed by the **!rpcexts.getendpointinfo** extension, or by DbgRpc when the **-e** switch is used.

If an endpoint number is specified, information about that endpoint is shown. If it is omitted, the endpoints for all processes on the system are displayed.

The following example displays all endpoints. This is often a useful way to obtain process IDs and cell numbers that can be used as arguments for additional commands:

```console
D:\wmsg>dbgrpc -e
Searching for endpoint info ...
## PID  CELL ID   ST PROTSEQ        ENDPOINT
-------------------------------------------------------
00a8 0000.0001 01            NMP \PIPE\InitShutdown
00a8 0000.0003 01            NMP \PIPE\SfcApi
00a8 0000.0004 01            NMP \PIPE\ProfMapApi
00a8 0000.0007 01            NMP \pipe\winlogonrpc
00a8 0000.0008 01           LRPC OLE5
00c4 0000.0001 01           LRPC ntsvcs
00c4 0000.0003 01            NMP \PIPE\ntsvcs
00c4 0000.0008 01            NMP \PIPE\scerpc
00d0 0000.0001 01            NMP \PIPE\lsass
00d0 0000.0004 01            NMP \pipe\WMIEP_d0
00d0 0000.000b 01            NMP \PIPE\POLICYAGENT
00d0 0000.000c 01           LRPC policyagent
0170 0000.0001 01           LRPC epmapper
0170 0000.0003 01            TCP 135
0170 0000.0005 01            SPX 34280
0170 0000.0006 01             NB 135
0170 0000.0007 01             NB 135
0170 0000.000b 01            NMP \pipe\epmapper
01b8 0000.0001 01            NMP \pipe\spoolss
01b8 0000.0003 01           LRPC spoolss
01b8 0000.0007 01           LRPC OLE7
00ec 0000.0001 01           LRPC OLE2
00ec 0000.0003 01           LRPC senssvc
00ec 0000.0007 01            NMP \pipe\tapsrv
00ec 0000.0008 01           LRPC tapsrvlpc
00ec 0000.000c 01            NMP \PIPE\ROUTER
00ec 0000.0010 01            NMP \pipe\WMIEP_ec
0214 0000.0001 01            NMP \PIPE\winreg
022c 0000.0001 01           LRPC LRPC0000022c.00000001
022c 0000.0003 01            TCP 1058
022c 0000.0005 01            SPX 24576
022c 0000.0006 01            NMP \PIPE\atsvc
02a8 0000.0001 01           LRPC OLE3
0370 0000.0001 01           LRPC OLE9
0278 0000.0001 01            TCP 1120
030c 0000.0001 01           LRPC OLE12
```

For details on the optional parameters, see [**DbgRpc Command-Line Options**](dbgrpc-command-line-options.md).

For a similar example using the RPC debugger extensions, see [**!rpcexts.getendpointinfo**](-rpcexts-getendpointinfo.md).

 

 





