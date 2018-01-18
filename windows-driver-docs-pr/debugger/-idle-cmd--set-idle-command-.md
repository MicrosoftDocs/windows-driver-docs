---
title: .idle_cmd (Set Idle Command)
description: The .idle_cmd command sets the idle command. This is a command that is executed whenever control returns from the target to the debugger. 
ms.assetid: 8cfe7aa8-4e31-4e97-b61d-9e8bb1b7be61
keywords: [".idle_cmd (Set Idle Command) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .idle_cmd (Set Idle Command)
api_type:
- NA
---

# .idle\_cmd (Set Idle Command)


The **.idle\_cmd** command sets the *idle command*. This is a command that is executed whenever control returns from the target to the debugger. For example, when the target reaches a breakpoint, this command executes.

```
.idle_cmd
.idle_cmd String 
.idle_cmd /d
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______String______"></span><span id="_______string______"></span><span id="_______STRING______"></span> *String*   
Specifies the string to which the idle command should be set.

<span id="________d______"></span><span id="________D______"></span> **/d**   
Clears the idle command.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

This command cannot be used in script files.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

When **.idle\_cmd** is used with no parameters it displays the current idle command.

In WinDbg, idle commands are stored in workspaces.

Here is an example. The idle command is set to [**r eax**](r--registers-.md). Then, because the debugger is already idle, this command immediately executes, displaying the **eax** register:

```
windbg> .idle_cmd r eax 
Execute when idle: r eax
eax=003b0de8
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.idle_cmd%20%28Set%20Idle%20Command%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




