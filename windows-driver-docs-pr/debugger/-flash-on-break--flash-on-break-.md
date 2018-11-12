---
title: .flash_on_break (Flash on Break)
description: The .flash_on_break command specifies whether the WinDbg taskbar entry flashes when WinDbg is minimized and the target breaks.
ms.assetid: b2f0a8c5-5b32-44f4-9546-c75859476ce0
keywords: [".flash_on_break (Flash on Break) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .flash_on_break (Flash on Break)
api_type:
- NA
ms.localizationpriority: medium
---

# .flash\_on\_break (Flash on Break)


The **.flash\_on\_break** command specifies whether the WinDbg taskbar entry flashes when WinDbg is minimized and the target breaks.

```dbgcmd
.flash_on_break on 
.flash_on_break off 
.flash_on_break 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______on______"></span><span id="_______ON______"></span> **on**   
Causes the WinDbg taskbar entry to flash if WinDbg is minimized and the target breaks into the debugger. This is the default behavior for WinDbg.

<span id="_______off______"></span><span id="_______OFF______"></span> **off**   
Prevents the WinDbg taskbar entry from flashing.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

The **.flash\_on\_break** command is available only in WinDbg. You cannot use this command in script files.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

If you use the **.flash\_on\_break** command without parameters, the debugger displays the current flash setting.

 

 





