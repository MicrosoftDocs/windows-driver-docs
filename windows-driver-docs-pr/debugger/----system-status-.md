---
title: (System Status)
description: The double vertical bar ( ) command prints status for the specified system or for all systems that you are currently debugging.Do not confuse this command with the (Process Status) command.
ms.assetid: fcea61b1-2ec5-4c80-abd7-269b95d56cd4
keywords: ["(System Status) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- (System Status)
api_type:
- NA
---

# || (System Status)


The double vertical bar (**||**) command prints status for the specified system or for all systems that you are currently debugging.

Do not confuse this command with the [**| (Process Status)**](---process-status-.md) command.

```
|| System 
```

## <span id="ddk_cmd_system_status_dbg"></span><span id="DDK_CMD_SYSTEM_STATUS_DBG"></span>Parameters


<span id="_______System______"></span><span id="_______system______"></span><span id="_______SYSTEM______"></span> *System*   
Specifies the system to display. If you omit this parameter, all systems that you are debugging are displayed. For more information about the syntax, see [System Syntax](system-syntax.md).

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

The **||** command is useful only when you are debugging multiple targets. Many, but not all, multiple-target debugging sessions involve multiple systems. For more information about these sessions, see [Debugging Multiple Targets](debugging-multiple-targets.md).

Each system listing includes the server name and the protocol details. The system that the debugger is running on is identified as **&lt;Local&gt;**.

The following examples show you how to use this command. The following command displays all systems.

```
3:2:005> ||
```

The following command also displays all systems.

```
3:2:005> ||*
```

The following command displays the currently active system.

```
3:2:005> ||.
```

The following command displays the system that had the most recent exception or break.

```
3:2:005> ||#
```

The following command displays system number 2.

```
3:2:005> ||2
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20||%20%28System%20Status%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




