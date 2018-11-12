---
title: ks.dumplog
description: The ks.dumplog extension displays the internal kernel streaming debug log.
ms.assetid: 09829517-c01c-4cbd-bd0f-2ad0c1554f39
keywords: ["ks.dumplog Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ks.dumplog
api_type:
- NA
ms.localizationpriority: medium
---

# !ks.dumplog


The **!ks.dumplog** extension displays the internal kernel streaming debug log.

```dbgcmd
!ks.dumplog [Entries] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Entries______"></span><span id="_______entries______"></span><span id="_______ENTRIES______"></span> *Entries*   
Optional. Specifies the number of log entries to display. If *Entries* is zero or omitted, the entire log is displayed.

### <span id="DLL"></span><span id="dll"></span>DLL

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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel Streaming Debugging](kernel-streaming-debugging.md).

Remarks
-------

You can stop the log display by pressing [**CTRL+C**](ctrl-c--break-.md).

This extension requires that the target computer be running a checked (debug) version of Ks.sys.

 

 





