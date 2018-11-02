---
title: rpcexts.rpctime
description: The rpcexts.rpctime extension displays the current system time.
ms.assetid: 72d54357-6b16-4d53-9909-ba201bb33519
keywords: ["rpcexts.rpctime Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- rpcexts.rpctime
api_type:
- NA
ms.localizationpriority: medium
---

# !rpcexts.rpctime


The **!rpcexts.rpctime** extension displays the current system time.

```dbgcmd
!rpcexts.rpctime 
```

## <span id="ddk__rpcexts_rpctime_dbg"></span><span id="DDK__RPCEXTS_RPCTIME_DBG"></span>


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

 

Remarks
-------

This extension can only be used with CDB or with user-mode WinDbg.

Here is an example:

```dbgcmd
0:001> !rpcexts.rpctime
Current time is: 059931.126  (0x00ea1b.07e)
```

 

 





