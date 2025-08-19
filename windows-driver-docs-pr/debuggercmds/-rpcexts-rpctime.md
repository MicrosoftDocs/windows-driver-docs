---
title: "!rpcexts.rpctime"
description: "The !rpcexts.rpctime extension displays the current system time."
keywords: ["!rpcexts.rpctime Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- rpcexts.rpctime
api_type:
- NA
---

# !rpcexts.rpctime

The **!rpcexts.rpctime** extension displays the current system time.

```dbgcmd
!rpcexts.rpctime 
```

## DLL

Rpcexts.dll

## Remarks

This extension can only be used with CDB or with user-mode WinDbg.

Here is an example:

```dbgcmd
0:001> !rpcexts.rpctime
Current time is: 059931.126  (0x00ea1b.07e)
```
