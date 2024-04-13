---
title: "!rpcexts.eeinfo"
description: "The !rpcexts.eeinfo extension displays the extended error information chain."
keywords: ["!rpcexts.eeinfo Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- rpcexts.eeinfo
api_type:
- NA
---

# !rpcexts.eeinfo

The **!rpcexts.eeinfo** extension displays the extended error information chain.

```dbgcmd
!rpcexts.eeinfo EEInfoAddress
```

## Parameters

<span id="_______EEInfoAddress______"></span><span id="_______eeinfoaddress______"></span><span id="_______EEINFOADDRESS______"></span> *EEInfoAddress*   
Specifies the address of the extended error information.

## DLL

Rpcexts.dll

## Additional Information

For more information about debugging Microsoft Remote Procedure Call (RPC), see [RPC Debugging](../debugger/rpc-debugging.md).

## Remarks

This extension displays the contents of all records in the extended error information chain.

The records are displayed in order, with the most recent records first. The records are separated by a line of dashes.

Here is an example (in which there is only one record):

```dbgcmd
0:001> !rpcexts.eeinfo 0xb015f0
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

If the chain is very long and you wish to see only one record, use [**!rpcexts.eerecord**](-rpcexts-eerecord.md) instead.
