---
title: .restart (Restart Kernel Connection)
description: The .restart command restarts the kernel connection.Do not confuse this command with the .restart (Restart Target Application) command, which works only in user mode.
ms.assetid: 2c81625b-d75f-4c5f-9437-9619bf33b500
keywords: [".restart (Restart Kernel Connection) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .restart (Restart Kernel Connection)
api_type:
- NA
---

# .restart (Restart Kernel Connection)


The **.restart** command restarts the kernel connection.

Do not confuse this command with the [**.restart (Restart Target Application)**](-restart--restart-target-application-.md) command, which works only in user mode.

```
.restart 
```

## <span id="ddk_meta_restart_kernel_connection_dbg"></span><span id="DDK_META_RESTART_KERNEL_CONNECTION_DBG"></span>


### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

You can use the **.restart** command only in KD.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>Kernel mode only</p></td>
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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about reestablishing contact with the target, see [Synchronizing with the Target Computer](synchronizing-with-the-target-computer.md).

Remarks
-------

The **.restart** command is similar to the [**CTRL+R (Re-synchronize)**](ctrl-r--re-synchronize-.md) command, except that **.restart** is even more extensive in its effect. This command is equivalent to ending the debugger and then attaching a new debugger to the target computer.

The **.restart** command is most useful when you are performing [remote debugging through remote.exe](remote-debugging-through-remote-exe.md) and ending and restarting the debugger might be difficult. However, you cannot use **.restart** from a debugging client if you are performing remote debugging through the debugger.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.restart%20%28Restart%20Kernel%20Connection%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




