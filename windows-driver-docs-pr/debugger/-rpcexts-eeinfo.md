---
title: rpcexts.eeinfo
description: The rpcexts.eeinfo extension displays the extended error information chain.
ms.assetid: dc842236-bdbf-42aa-911d-6eb5eb1798ee
keywords: ["rpcexts.eeinfo Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- rpcexts.eeinfo
api_type:
- NA
ms.localizationpriority: medium
---

# !rpcexts.eeinfo


The **!rpcexts.eeinfo** extension displays the extended error information chain.

```dbgcmd
!rpcexts.eeinfo EEInfoAddress
```

## <span id="ddk__rpcexts_eeinfo_dbg"></span><span id="DDK__RPCEXTS_EEINFO_DBG"></span>Parameters


<span id="_______EEInfoAddress______"></span><span id="_______eeinfoaddress______"></span><span id="_______EEINFOADDRESS______"></span> *EEInfoAddress*   
Specifies the address of the extended error information.

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

 

 





