---
title: symsrv extension command
description: The symsrv extension closes the symbol server client.
ms.assetid: 666fa9d7-f723-4745-95fc-17aa20993b42
keywords: ["symsrv Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- symsrv
api_type:
- NA
ms.localizationpriority: medium
---

# !symsrv


The **!symsrv** extension closes the symbol server client.

```dbgcmd
!symsrv close
```

## <span id="ddk__symsrv_dbg"></span><span id="DDK__SYMSRV_DBG"></span>


### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Dbghelp.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Dbghelp.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **!symsrv close** extension will close any active symbol server client.

This can be useful if you need to re-synchronize your connection.

If you have previously refused an internet authentication request, you will need to use **!symsrv close** to reconnect to the symbol store. See [Firewalls and Proxy Servers](firewalls-and-proxy-servers.md) for details.

 

 





