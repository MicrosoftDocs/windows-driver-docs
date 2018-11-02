---
title: filetime
description: The filetime extension converts a 64-bit FILETIME structure into a human-readable time.
ms.assetid: 26ee9219-ad37-4b0e-b204-5ed6d93355b0
keywords: ["FILETIME", "filetime Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- filetime
api_type:
- NA
ms.localizationpriority: medium
---

# !filetime


The **!filetime** extension converts a 64-bit FILETIME structure into a human-readable time.

```dbgcmd
!filetime Time
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Time______"></span><span id="_______time______"></span><span id="_______TIME______"></span> *Time*   
Specifies a 64-bit FILETIME structure.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Kdextx86.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Here is an example of the output from this extension:

```dbgcmd
kd> !filetime 1c4730984712348
 7/26/2004 04:10:18.712 (Pacific Standard Time)
```

 

 





