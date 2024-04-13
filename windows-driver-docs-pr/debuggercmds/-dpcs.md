---
title: "!dpcs (WinDbg)"
description: "The !dpcs extension displays the deferred procedure call (DPC) queues for a specified processor."
keywords: ["DPC (deferred procedure call)", "!dpcs Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- dpcs
api_type:
- NA
---

# !dpcs


The **!dpcs** extension displays the deferred procedure call (DPC) queues for a specified processor.

```dbgcmd
!dpcs [Processor]
```

## Parameters


<span id="_______Processor______"></span><span id="_______processor______"></span><span id="_______PROCESSOR______"></span> *Processor*   
Specifies a processor. If *Processor* is omitted, then the DPC queues for all processors are displayed.

## DLL

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
<td align="left"><p><strong>Windows XP</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Windows Server 2003 and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

## Additional Information

For information about DPCs, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

