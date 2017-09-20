---
title: .flash_on_break (Flash on Break)
description: The .flash_on_break command specifies whether the WinDbg taskbar entry flashes when WinDbg is minimized and the target breaks.
ms.assetid: b2f0a8c5-5b32-44f4-9546-c75859476ce0
keywords: [".flash_on_break (Flash on Break) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .flash_on_break (Flash on Break)
api_type:
- NA
---

# .flash\_on\_break (Flash on Break)


The **.flash\_on\_break** command specifies whether the WinDbg taskbar entry flashes when WinDbg is minimized and the target breaks.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.flash_on_break%20%28Flash%20on%20Break%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




