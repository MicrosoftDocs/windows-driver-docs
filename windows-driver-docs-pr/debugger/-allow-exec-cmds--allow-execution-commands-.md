---
title: .allow\_exec\_cmds (Allow Execution Commands)
description: The .allow\_exec\_cmds command controls whether execution commands can be used.
ms.assetid: c6e37cf1-42cc-4f82-9eb8-d252f0b6e196
keywords: [".allow_exec_cmds (Allow Execution Commands) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .allow_exec_cmds (Allow Execution Commands)
api_type:
- NA
---

# .allow\_exec\_cmds (Allow Execution Commands)


The **.allow\_exec\_cmds** command controls whether execution commands can be used.

``` syntax
    .allow_exec_cmds 0 
.allow_exec_cmds 1 
.allow_exec_cmds 
```

## <span id="ddk_meta_allow_execution_commands_dbg"></span><span id="DDK_META_ALLOW_EXECUTION_COMMANDS_DBG"></span>Parameters


<span id="_______0______"></span> **0**   
Prevents execution commands from being used.

<span id="_______1______"></span> **1**   
Allows execution commands to be used.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode and kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For a complete list of execution commands, see [Controlling the Target](controlling-the-target.md).

Remarks
-------

With no parameters, **.allow\_exec\_cmds** will display whether execution commands are currently permitted.

Execution commands include [**g (Go)**](g--go-.md), [**t (Trace)**](t--trace-.md), [**p (Step)**](p--step-.md), and any other command or WinDbg graphical interface action that would cause the target to execute.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.allow_exec_cmds%20%28Allow%20Execution%20Commands%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




