---
title: rpcexts.thread
description: The rpcexts.thread extension displays the per-thread RPC information.This extension command should not be confused with the .thread command.
ms.assetid: eecc4eb6-7789-47ed-8b3f-5ec21cc6117c
keywords: ["rpcexts.thread Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- rpcexts.thread
api_type:
- NA
ms.localizationpriority: medium
---

# !rpcexts.thread


The **!rpcexts.thread** extension displays the per-thread RPC information.

This extension command should not be confused with the [**.thread (Set Register Context)**](-thread--set-register-context-.md) command or the [**!thread**](-thread.md) (!kdextx86.thread and !kdexts.thread) extension.

```dbgcmd
!rpcexts.thread TEB
```

## <span id="ddk__rpcexts_thread_dbg"></span><span id="DDK__RPCEXTS_THREAD_DBG"></span>Parameters


<span id="_______TEB______"></span><span id="_______teb______"></span> *TEB*   
Specifies the address of the thread environment block (TEB).

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Rpcexts.dll</p></td>
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

This extension displays the per-thread RPC information. A field in the per-thread RPC information is the extended error information for this thread.

Here is an example:

```dbgcmd
0:001> !rpcexts.thread 7ffdd000
RPC TLS at 692e70

HandleToThread - 0x6c
SavedProcedure - 0x0
SavedParameter - 0x0
ActiveCall - 0x0
Context - 0x0
CancelTimeout - 0xffffffff
SecurityContext - 0x0
ExtendedStatus - 0x0
ThreadEEInfo - 0xb015f0
ThreadEvent at - 0x00692E78
fCallCancelled - 0x0
buffer cache array at - 0x00692E84
fAsync - 0x0
```

 

 





