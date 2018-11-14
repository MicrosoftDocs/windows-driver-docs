---
title: (System Status)
description: The double vertical bar ( ) command prints status for the specified system or for all systems that you are currently debugging.Do not confuse this command with the (Process Status) command.
ms.assetid: fcea61b1-2ec5-4c80-abd7-269b95d56cd4
keywords: ["(System Status) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- (System Status)
api_type:
- NA
ms.localizationpriority: medium
---

# || (System Status)


The double vertical bar (**||**) command prints status for the specified system or for all systems that you are currently debugging.

Do not confuse this command with the [**| (Process Status)**](---process-status-.md) command.

```dbgcmd
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

```dbgcmd
3:2:005> ||
```

The following command also displays all systems.

```dbgcmd
3:2:005> ||*
```

The following command displays the currently active system.

```dbgcmd
3:2:005> ||.
```

The following command displays the system that had the most recent exception or break.

```dbgcmd
3:2:005> ||#
```

The following command displays system number 2.

```dbgcmd
3:2:005> ||2
```

 

 





