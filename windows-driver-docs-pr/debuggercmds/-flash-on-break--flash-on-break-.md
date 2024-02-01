---
title: .flash_on_break (Flash on Break)
description: The .flash_on_break command specifies whether the WinDbg taskbar entry flashes when WinDbg is minimized and the target breaks.
keywords: [".flash_on_break (Flash on Break) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .flash_on_break (Flash on Break)
api_type:
- NA
---

# .flash\_on\_break (Flash on Break)


The **.flash\_on\_break** command specifies whether the WinDbg taskbar entry flashes when WinDbg is minimized and the target breaks.

```dbgcmd
.flash_on_break on 
.flash_on_break off 
.flash_on_break 
```

## Parameters


<span id="_______on______"></span><span id="_______ON______"></span> **on**   
Causes the WinDbg taskbar entry to flash if WinDbg is minimized and the target breaks into the debugger. This is the default behavior for WinDbg.

<span id="_______off______"></span><span id="_______OFF______"></span> **off**   
Prevents the WinDbg taskbar entry from flashing.

### Environment

The **.flash\_on\_break** command is available only in WinDbg. You cannot use this command in script files.

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

If you use the **.flash\_on\_break** command without parameters, the debugger displays the current flash setting.

 

 





