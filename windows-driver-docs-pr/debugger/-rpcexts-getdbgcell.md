---
title: rpcexts.getdbgcell
description: The rpcexts.getdbgcell extension displays RPC state information for the specified cell.
ms.assetid: 28be074f-6756-4610-aa86-1162b83fd0a7
keywords: ["rpcexts.getdbgcell Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- rpcexts.getdbgcell
api_type:
- NA
ms.localizationpriority: medium
---

# !rpcexts.getdbgcell


The **!rpcexts.getdbgcell** extension displays RPC state information for the specified cell.

```dbgcmd
!rpcexts.getdbgcell ProcessID CellID1.CellID2 
!rpcexts.getdbgcell -?
```

## <span id="ddk__rpcexts_getdbgcell_dbg"></span><span id="DDK__RPCEXTS_GETDBGCELL_DBG"></span>Parameters


<span id="_______ProcessID______"></span><span id="_______processid______"></span><span id="_______PROCESSID______"></span> *ProcessID*   
Specifies the process ID (PID) of the process whose server contains the desired cell.

<span id="_______cellid1.cellid2______"></span><span id="_______CELLID1.CELLID2______"></span> *CellID1*.*CellID2*   
Specifies the number of the cell to be displayed.

<span id="_______-_______"></span> **-?**   
Displays some brief Help text for this extension in the Command Prompt window.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Rpcexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about debugging Microsoft Remote Procedure Call (RPC), see [RPC Debugging](rpc-debugging.md).

Remarks
-------

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

For a similar example using the DbgRpc tool, see [Get RPC Cell Information](get-rpc-cell-information.md).

 

 





