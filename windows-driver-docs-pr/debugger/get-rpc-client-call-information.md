---
title: Get RPC Client Call Information
description: Get RPC Client Call Information
ms.assetid: 8b23428d-50e7-4613-a0ce-d1da5fa96ddf
keywords: ["RPC client call information", "CCALL (client call)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Get RPC Client Call Information


## <span id="ddk_get_rpc_client_call_information_dbg"></span><span id="DDK_GET_RPC_CLIENT_CALL_INFORMATION_DBG"></span>


Client call (CCALL) call information is displayed by the **!rpcexts.getclientcallinfo** extension, or by DbgRpc when the **-a** switch is used.

Four optional parameters are permitted. Three of these -- *CallID*, *IfStart*, and *ProcNum* -- are identifying information used by RPC to keep track of its calls. The fourth parameter, *ProcessID*, is the PID of the process that owns the call. You should supply whatever parameters you know to narrow down the search.

If no parameters are supplied, all known CCALLs in the system will be displayed. The following is an example of this (potentially long) display:

```console
D:\wmsg>dbgrpc -a
Searching for call info ...
## PID  CELL ID   PNO  IFSTART  TIDNUMBER CALLID   LASTTIME PS CLTNUMBER ENDPOINT
------------------------------------------------------------------------------
0390 0000.0001 0000 19bb5061 0000.0000 00000001 00072bff 07 0000.0002 1120
```

For details on the optional parameters, see [**DbgRpc Command-Line Options**](dbgrpc-command-line-options.md).

For a similar example using the RPC debugger extensions, see [**!rpcexts.getclientcallinfo**](-rpcexts-getclientcallinfo.md).

**Note**   Information about Client Call objects is only gathered if the **Full** state information is being gathered. See [Enabling RPC State Information](enabling-rpc-state-information.md) for details.

 

 

 





