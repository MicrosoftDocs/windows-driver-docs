---
title: rpcexts.rpcreadstack
description: The rpcexts.rpcreadstack extension reads an RPC client-side stack and retrieves the call information.
ms.assetid: e0988ac9-dc6e-4a4f-9096-6af2e70dcd42
keywords: ["rpcexts.rpcreadstack Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- rpcexts.rpcreadstack
api_type:
- NA
ms.localizationpriority: medium
---

# !rpcexts.rpcreadstack


The **!rpcexts.rpcreadstack** extension reads an RPC client-side stack and retrieves the call information.

```dbgcmd
!rpcexts.rpcreadstack ThreadStackPointer
```

## <span id="ddk__rpcexts_rpcreadstack_dbg"></span><span id="DDK__RPCEXTS_RPCREADSTACK_DBG"></span>Parameters


<span id="_______ThreadStackPointer______"></span><span id="_______threadstackpointer______"></span><span id="_______THREADSTACKPOINTER______"></span> *ThreadStackPointer*   
Specifies the pointer to the thread stack.

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

For a common use of this extension, see [Analyzing a Stuck Call Problem](analyzing-a-stuck-call-problem.md).

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

 

 





