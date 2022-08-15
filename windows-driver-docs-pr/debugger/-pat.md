---
title: pat (WinDbg)
description: The pat extension displays the Page Attribute Table (PAT) registers for the target processor.
keywords: ["PAT", "pat Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- pat
api_type:
- NA
---

# !pat


The **!pat** extension displays the Page Attribute Table (PAT) registers for the target processor.

```dbgcmd
!pat Flag 
!pat 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Flag______"></span><span id="_______flag______"></span><span id="_______FLAG______"></span> *Flag*   
If *Flag* is set, the debugger verifies that the PAT feature is present before the PAT is displayed.

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

 

This extension command can only be used with an x86-based target computer.

 

 





