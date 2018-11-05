---
title: tls
description: The tls extension displays a thread local storage (TLS) slot.
ms.assetid: 43325322-8e6e-47fc-b1ec-8b1c304bb1e9
keywords: ["TLS (thread local storage)", "thread local storage (TLS)", "tls Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- tls
api_type:
- NA
ms.localizationpriority: medium
---

# !tls


The **!tls** extension displays a thread local storage (TLS) slot.

```dbgcmd
!tls Slot [TEB]
```

## <span id="ddk__tls_dbg"></span><span id="DDK__TLS_DBG"></span>Parameters


<span id="_______Slot______"></span><span id="_______slot______"></span><span id="_______SLOT______"></span> *Slot*   
Specifies the TLS slot. This can be any value between 0 and 1088 (decimal). If *Slot* is -1, all slots are displayed.

<span id="_______TEB______"></span><span id="_______teb______"></span> *TEB*   
Specifies the thread environment block (TEB). If this is 0 or omitted, the current thread is used.

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
<td align="left"><p>Exts.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Here is an example:

```dbgcmd
0:000> !tls -1
TLS slots on thread: c08.f54
0x0000 : 00000000
0x0001 : 003967b8
0:000> !tls 0
c08.f54: 00000000
```

 

 





