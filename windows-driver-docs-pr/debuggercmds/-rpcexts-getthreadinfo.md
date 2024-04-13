---
title: "!rpcexts.getthreadinfo"
description: "The !rpcexts.getthreadinfo extension searches the system's RPC state information for thread information."
keywords: ["!rpcexts.getthreadinfo Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- rpcexts.getthreadinfo
api_type:
- NA
---

# !rpcexts.getthreadinfo

The **!rpcexts.getthreadinfo** extension searches the system's RPC state information for thread information.

```dbgcmd
!rpcexts.getthreadinfo ProcessID [ThreadID] 
!rpcexts.getthreadinfo -? 
```

## Parameters

<span id="_______ProcessID______"></span><span id="_______processid______"></span><span id="_______PROCESSID______"></span> *ProcessID*   
Specifies the process ID (PID) of the process containing the desired thread.

<span id="_______ThreadID______"></span><span id="_______threadid______"></span><span id="_______THREADID______"></span> *ThreadID*   
Specifies the thread ID of the thread to be displayed. If omitted, all threads in the specified process will be displayed.

<span id="_______-_______"></span> **-?**   
Displays some brief Help text for this extension in the Command Prompt window.

## DLL

Rpcexts.dll

## Additional Information

For more information about debugging Microsoft Remote Procedure Call (RPC), see [RPC Debugging](../debugger/rpc-debugging.md).

## Remarks

This extension can only be used with CDB or with user-mode WinDbg.

Here is an example:

```dbgcmd
0:002> !rpcexts.getthreadinfo 26c
Searching for thread info ...
## PID  CELL ID   ST TID      LASTTIME
-----------------------------------
026c 0000.0002 01 000003c4 0004caa5
026c 0000.0005 03 00000254 0004ca9b
```

For a similar example using the DbgRpc tool, see [Get RPC Thread Information](../debugger/get-rpc-thread-information.md).
