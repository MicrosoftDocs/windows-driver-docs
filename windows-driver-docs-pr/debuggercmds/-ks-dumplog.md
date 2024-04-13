---
title: "!ks.dumplog"
description: "The !ks.dumplog extension displays the internal kernel streaming debug log."
keywords: ["!ks.dumplog Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ks.dumplog
api_type:
- NA
---

# !ks.dumplog


The **!ks.dumplog** extension displays the internal kernel streaming debug log.

```dbgcmd
!ks.dumplog [Entries] 
```

## Parameters


<span id="_______Entries______"></span><span id="_______entries______"></span><span id="_______ENTRIES______"></span> *Entries*   
Optional. Specifies the number of log entries to display. If *Entries* is zero or omitted, the entire log is displayed.

## DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>winxp\Ks.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ks.dll</p></td>
</tr>
</tbody>
</table>

 

## Additional Information

For more information, see [Kernel Streaming Debugging](../debugger/kernel-streaming-debugging.md).

## Remarks

You can stop the log display by pressing [**CTRL+C**](../debugger/ctrl-c--break-.md).

This extension requires that the target computer be running a checked (debug) version of Ks.sys.

