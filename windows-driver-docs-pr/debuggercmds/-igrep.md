---
title: "!igrep (WinDbg)"
description: "The !igrep extension searches for a pattern in disassembly."
keywords: ["!igrep Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- igrep
api_type:
- NA
---

# !igrep

The **!igrep** extension searches for a pattern in disassembly.

```dbgcmd
!igrep [Pattern [StartAddress]] 
```

## <span id="ddk__igrep_dbg"></span><span id="DDK__IGREP_DBG"></span>Parameters


<span id="_______Pattern______"></span><span id="_______pattern______"></span><span id="_______PATTERN______"></span> *Pattern*   
Specifies the pattern to search for. If omitted, the last *Pattern* is used.

<span id="_______StartAddress______"></span><span id="_______startaddress______"></span><span id="_______STARTADDRESS______"></span> *StartAddress*   
Specifies the hexadecimal address at which to begin searching. If omitted, the current program counter is used.

## DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Ntsdexts.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
</tbody>
</table>
