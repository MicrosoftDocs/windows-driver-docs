---
title: bth
description: The bth extension displays the Itanium-based branch traces history for the specified processor.
ms.assetid: e6bf1452-adb7-4b1d-8614-03fcf0306c70
keywords: ["branch trace history", "bth Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- bth
api_type:
- NA
ms.localizationpriority: medium
---

# !bth


The **!bth** extension displays the Itanium-based branch traces history for the specified processor.

```dbgcmd
!bth [Processor]
```

**Important**  This command has been deprecated in the Windows Debugger Version 10.0.14257 and later, and is no longer available.

 

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Processor______"></span><span id="_______processor______"></span><span id="_______PROCESSOR______"></span> *Processor*   
Specifies a processor. If *Processor* is omitted, then the branch trace history for all of processors is displayed.

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
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

This extension command can only be used with an Itanium-based target computer.

 

 





