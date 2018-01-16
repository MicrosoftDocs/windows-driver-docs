---
title: .noshell (Prohibit Shell Commands)
description: The .noshell command prevents you from using .shell commands.
ms.assetid: 49a83e46-1390-4b60-bd61-a5da80c513e3
keywords: [".noshell (Prohibit Shell Commands) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .noshell (Prohibit Shell Commands)
api_type:
- NA
---

# .noshell (Prohibit Shell Commands)


The **.noshell** command prevents you from using [**.shell**](-shell--command-shell-.md) commands.

```
.noshell 
```

## <span id="ddk_meta_prohibit_shell_commands_dbg"></span><span id="DDK_META_PROHIBIT_SHELL_COMMANDS_DBG"></span>


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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about the command shell and for other ways to disable shell commands, see [Using Shell Commands](using-shell-commands.md).

Remarks
-------

If you use the **.noshell** command, you cannot use [**.shell (Command Shell)**](-shell--command-shell-.md) commands as long as the debugger is running, even if you start a new debugging session.

If you are performing remote debugging, this command is useful for security purposes.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.noshell%20%28Prohibit%20Shell%20Commands%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




