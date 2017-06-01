---
title: .push (Save Debugger State)
description: The .push command saves the current state of the debugger.
ms.assetid: 2e0b45d6-35b8-4c86-9c54-df8d16b4dcc2
keywords: [".push (Save Debugger State) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .push (Save Debugger State)
api_type:
- NA
---

# .push (Save Debugger State)


The **.push** command saves the current state of the debugger.

```
.push
.push /r
.push /r /q
 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="________r______"></span><span id="________R______"></span> **/r**   
Specifies that the current values in the pseudo-registers **$t0** to **$t19** should be saved. If the **/r** parameter is not used, these values are not saved by the **.push** command.

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

This command is most useful when used with [scripts](using-script-files.md) and [debugger command programs](using-debugger-command-programs.md) so that they can work with one fixed state. To restore the debugger to a state that was previously saved using this command, use the [**.pop (Restore Debugger State)**](-pop--restore-debugger-state-.md) command. If the command is successful, no output is displayed.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.push%20%28Save%20Debugger%20State%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




