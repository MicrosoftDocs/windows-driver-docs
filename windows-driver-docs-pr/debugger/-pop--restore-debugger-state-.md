---
title: .pop (Restore Debugger State)
description: The .pop command restores the state of the debugger to a state that has previously been saved by using the .push (Save Debugger State) command.
ms.assetid: 31f94b2a-3597-40e4-845a-d686274e36c3
keywords: ["Restore Debugger State (.pop) command", ".pop (Restore Debugger State) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .pop (Restore Debugger State)
api_type:
- NA
---

# .pop (Restore Debugger State)


The **.pop** command restores the state of the debugger to a state that has previously been saved by using the [**.push (Save Debugger State)**](-push--save-debugger-state-.md) command.

```
.pop
.pop /r
.pop /r /q
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="________r______"></span><span id="________R______"></span> **/r**   
Specifies that the saved values of the pseudo-registers $t0 to $t19 should be restored. If **/r** is not included, these values are not affected by the **.pop** command.

<span id="________q______"></span><span id="________Q______"></span> **/q**   
Specifies that the command executes quietly. That is, the command executes without displaying any output.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

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

This command is most useful when used with [scripts](using-script-files.md) and [debugger command programs](using-debugger-command-programs.md) so that they can work with one fixed state. If the command is successful, no output is displayed.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.pop%20%28Restore%20Debugger%20State%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




