---
title: "!rpcexts.eerecord"
description: "The !rpcexts.eerecord extension displays the contents of an extended error information record."
keywords: ["!rpcexts.eerecord Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- rpcexts.eerecord
api_type:
- NA
---

# !rpcexts.eerecord

The **!rpcexts.eerecord** extension displays the contents of an extended error information record.

```dbgcmd
!rpcexts.eerecord EERecordAddress
```

## Parameters

<span id="_______EERecordAddress______"></span><span id="_______eerecordaddress______"></span><span id="_______EERECORDADDRESS______"></span> *EERecordAddress*   
Specifies the address of the extended error record.

## DLL

Rpcexts.dll

## Additional Information

For more information about debugging Microsoft Remote Procedure Call (RPC), see [RPC Debugging](../debugger/rpc-debugging.md).

## Remarks

This extension displays the contents of one extended error information record in the debugger. In most cases, it is easier to use [**!rpcexts.eeinfo**](-rpcexts-eeinfo.md), which displays the whole chain. If the chain is very long and you wish to see only one record, use **!eerecord** instead.

Here is an example:

```dbgcmd
0:001> !rpcexts.eerecord 0xb015f0
Computer Name: (null)
ProcessID: 708 (0x2C4)
System Time is: 3/21/2000 4:3:0:264
Generating component: 8
Status: 14
Detection Location: 311
Flags:
Parameter 0:(Long value) : -30976 (0xFFFF8700)
Parameter 1:(Long value) : 16777343 (0x100007F)
```
