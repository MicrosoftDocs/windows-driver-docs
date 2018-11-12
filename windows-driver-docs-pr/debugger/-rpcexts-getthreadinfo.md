---
title: rpcexts.getthreadinfo
description: The rpcexts.getthreadinfo extension searches the system's RPC state information for thread information.
ms.assetid: 904605e7-c53b-4e29-874f-7a055fc7a02b
keywords: ["rpcexts.getthreadinfo Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- rpcexts.getthreadinfo
api_type:
- NA
ms.localizationpriority: medium
---

# !rpcexts.getthreadinfo


The **!rpcexts.getthreadinfo** extension searches the system's RPC state information for thread information.

```dbgcmd
!rpcexts.getthreadinfo ProcessID [ThreadID] 
!rpcexts.getthreadinfo -? 
```

## <span id="ddk__rpcexts_getthreadinfo_dbg"></span><span id="DDK__RPCEXTS_GETTHREADINFO_DBG"></span>Parameters


<span id="_______ProcessID______"></span><span id="_______processid______"></span><span id="_______PROCESSID______"></span> *ProcessID*   
Specifies the process ID (PID) of the process containing the desired thread.

<span id="_______ThreadID______"></span><span id="_______threadid______"></span><span id="_______THREADID______"></span> *ThreadID*   
Specifies the thread ID of the thread to be displayed. If omitted, all threads in the specified process will be displayed.

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
0:002> !rpcexts.getthreadinfo 26c
Searching for thread info ...
## PID  CELL ID   ST TID      LASTTIME
-----------------------------------
026c 0000.0002 01 000003c4 0004caa5
026c 0000.0005 03 00000254 0004ca9b
```

For a similar example using the DbgRpc tool, see [Get RPC Thread Information](get-rpc-thread-information.md).

 

 





