---
title: rpcexts.eerecord
description: The rpcexts.eerecord extension displays the contents of an extended error information record.
ms.assetid: 3c861842-d3ac-4c7d-88e3-d00233189b74
keywords: ["rpcexts.eerecord Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- rpcexts.eerecord
api_type:
- NA
ms.localizationpriority: medium
---

# !rpcexts.eerecord


The **!rpcexts.eerecord** extension displays the contents of an extended error information record.

```dbgcmd
!rpcexts.eerecord EERecordAddress
```

## <span id="ddk__rpcexts_eerecord_dbg"></span><span id="DDK__RPCEXTS_EERECORD_DBG"></span>Parameters


<span id="_______EERecordAddress______"></span><span id="_______eerecordaddress______"></span><span id="_______EERECORDADDRESS______"></span> *EERecordAddress*   
Specifies the address of the extended error record.

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

 

 





