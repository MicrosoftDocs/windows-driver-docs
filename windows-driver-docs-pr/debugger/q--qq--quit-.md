---
title: q, qq (Quit)
description: The q and qq commands end the debugging session.
ms.assetid: 94d35997-8b21-4d25-b2ae-4b2a78240153
keywords: ["q, qq (Quit) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- q, qq (Quit)
api_type:
- NA
---

# q, qq (Quit)


The **q** and **qq** commands end the debugging session. (In CDB and KD, this command also exits the debugger itself. In WinDbg, this command returns the debugger to dormant mode.)

```
q 
qq 
```

## <span id="ddk_cmd_quit_dbg"></span><span id="DDK_CMD_QUIT_DBG"></span>


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

In user-mode debugging, the **q** command ends the debugging session and closes the target application.

In kernel-mode debugging, the **q** command saves the log file and ends the debugging session. The target computer remains locked.

If this command does not work in KD, press [**CTRL+R+ENTER**](ctrl-r--re-synchronize-.md) on the debugger keyboard, and then retry the **q** command. If this action does not work, you must use CTRL+B+ENTER to exit the debugger.

The **qq** command behaves exactly like the **q** command, unless you are performing remote debugging. During remote debugging, the **q** command has no effect, but the **qq** command ends the debugging server. For more information about this effect, see [Remote Debugging Through the Debugger](remote-debugging-through-the-debugger.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20q,%20qq%20%28Quit%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




