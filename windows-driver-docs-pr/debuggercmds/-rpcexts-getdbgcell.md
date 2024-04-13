---
title: "!rpcexts.getdbgcell"
description: "The !rpcexts.getdbgcell extension displays RPC state information for the specified cell."
keywords: ["!rpcexts.getdbgcell Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- rpcexts.getdbgcell
api_type:
- NA
---

# !rpcexts.getdbgcell

The **!rpcexts.getdbgcell** extension displays RPC state information for the specified cell.

```dbgcmd
!rpcexts.getdbgcell ProcessID CellID1.CellID2 
!rpcexts.getdbgcell -?
```

## Parameters

<span id="_______ProcessID______"></span><span id="_______processid______"></span><span id="_______PROCESSID______"></span> *ProcessID*   
Specifies the process ID (PID) of the process whose server contains the desired cell.

<span id="_______cellid1.cellid2______"></span><span id="_______CELLID1.CELLID2______"></span> *CellID1*.*CellID2*   
Specifies the number of the cell to be displayed.

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
0:002> !rpcexts.getdbgcell c4 0.19
Getting cell info ...
Call
Status: Active
Procedure Number: 11
Interface UUID start (first DWORD only): 82273FDC
Call ID: 0x0 (0)
Servicing thread identifier: 0x0.3E
Call Flags: cached, LRPC
Last update time (in seconds since boot):1453.459 (0x5AD.1CB)
Caller (PID/TID) is: d0.1ac (208.428)
```

For a similar example using the DbgRpc tool, see [Get RPC Cell Information](../debugger/get-rpc-cell-information.md).
