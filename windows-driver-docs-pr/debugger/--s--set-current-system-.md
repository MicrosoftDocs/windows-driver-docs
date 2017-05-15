---
title: s (Set Current System)
description: The s command sets or displays the current system number.Do not confuse this command with the s (Search Memory), ~s (Change Current Processor), ~s (Set Current Thread), or s (Set Current Process) command.
ms.assetid: 33ad3a63-166f-4669-868c-49100c9b4d8c
keywords: ["s (Set Current System) Windows Debugging"]
topic_type:
- apiref
api_name:
- s (Set Current System)
api_type:
- NA
---

# ||s (Set Current System)


The **||s** command sets or displays the current system number.

Do not confuse this command with the [**s (Search Memory)**](s--search-memory-.md), [**~s (Change Current Processor)**](-s--change-current-processor-.md), [**~s (Set Current Thread)**](-s--set-current-thread-.md), or [**|s (Set Current Process)**](-s--set-current-process-.md) command.

``` syntax
||System s 
|| s 
```

## <span id="ddk_cmd_set_current_system_dbg"></span><span id="DDK_CMD_SET_CURRENT_SYSTEM_DBG"></span>Parameters


<span id="_______System______"></span><span id="_______system______"></span><span id="_______SYSTEM______"></span> *System*   
Specifies the system to activate. For more information about the syntax, see [System Syntax](system-syntax.md).

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>Multiple target debugging</p></td>
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

The **||s** command is useful only when you are debugging multiple targets. Many, but not all, multiple-target debugging sessions involve multiple systems. For more information about these kinds of sessions, see [Debugging Multiple Targets](debugging-multiple-targets.md).

If you use the **||s** syntax, the debugger displays information about the current system.

This command also disassembles the current instruction for the current system, process, and thread.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20||s%20%28Set%20Current%20System%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




