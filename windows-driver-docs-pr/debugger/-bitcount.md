---
title: bitcount
description: The !bitcount extension counts the number of "1" bits in a memory range.
ms.assetid: dacf3d63-6241-4779-afca-514905b37e26
keywords: ["bitcount Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- bitcount
api_type:
- NA
ms.localizationpriority: medium
---

# !bitcount


The **!bitcount** extension counts the number of "1" bits in a memory range.

```dbgcmd
!bitcount StartAddress TotalBits
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______StartAddress______"></span><span id="_______startaddress______"></span><span id="_______STARTADDRESS______"></span> *StartAddress*   
Specifies the starting address of the memory range whose "1" bits will be counted.

<span id="_______TotalBits______"></span><span id="_______totalbits______"></span><span id="_______TOTALBITS______"></span> *TotalBits*   
Specifies the size of the memory range, in bits.

<span id="_______-_______"></span> **-?**   
Displays some Help text for this extension in the [Debugger Command window](debugger-command-window.md).

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

 

 

 





