---
title: "!rpcexts.rpcreadstack"
description: "The !rpcexts.rpcreadstack extension reads an RPC client-side stack and retrieves the call information."
keywords: ["!rpcexts.rpcreadstack Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- rpcexts.rpcreadstack
api_type:
- NA
---

# !rpcexts.rpcreadstack

The **!rpcexts.rpcreadstack** extension reads an RPC client-side stack and retrieves the call information.

```dbgcmd
!rpcexts.rpcreadstack ThreadStackPointer
```

## Parameters

<span id="_______ThreadStackPointer______"></span><span id="_______threadstackpointer______"></span><span id="_______THREADSTACKPOINTER______"></span> *ThreadStackPointer*   
Specifies the pointer to the thread stack.

## DLL

Rpcexts.dll

## Additional Information

For more information about debugging Microsoft Remote Procedure Call (RPC), see [RPC Debugging](../debugger/rpc-debugging.md).

## Remarks

For a common use of this extension, see [Analyzing a Stuck Call Problem](../debugger/analyzing-a-stuck-call-problem.md).

Here is an example:

```dbgcmd
0:001> !rpcexts.rpcreadstack 68fba4
CallID: 1
IfStart: 19bb5061
ProcNum: 0
        Protocol Sequence:      "ncacn_ip_tcp"  (Address: 00692ED8)
        NetworkAddress: ""      (Address: 00692F38)
        Endpoint:       "1120"  (Address: 00693988)
```
