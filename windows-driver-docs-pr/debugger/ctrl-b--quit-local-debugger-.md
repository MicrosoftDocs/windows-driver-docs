---
title: CTRL+B (Quit Local Debugger)
description: The CTRL+B key causes the debugger to terminate abruptly. This does not end a remote debugging session.
ms.assetid: f70f4c40-244f-4abf-982f-d738800ac621
keywords: ["CTRL+B (Quit Local Debugger) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- CTRL+B (Quit Local Debugger)
api_type:
- NA
---

# CTRL+B (Quit Local Debugger)


The CTRL+B key causes the debugger to terminate abruptly. This does not end a remote debugging session.

```
CTRL+B  ENTER 
```

## <span id="ddk_meta_ctrl_b_dbg"></span><span id="DDK_META_CTRL_B_DBG"></span>


### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Debuggers</strong></p></td>
<td align="left"><p>CDB and KD only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

In CDB, the [**q (Quit)**](q--qq--quit-.md) command should be used to exit. CTRL+B should only be used if the debugger is not responding.

In KD, the **q** command will end the debugging session and leave the target computer locked. If you need to preserve the debugging session (so a new debugger can connect to it), or if you need to leave the target computer running, you should use CTRL+B.

In WinDbg, the equivalent command is [File | Exit](file---exit.md) or ALT+F4.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20CTRL+B%20%28Quit%20Local%20Debugger%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




