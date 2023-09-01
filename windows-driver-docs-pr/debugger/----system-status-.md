---
title: (System Status)
description: The double vertical bar ( ) command prints status for the specified system or for all systems that you are currently debugging.Do not confuse this command with the (Process Status) command.
keywords: ["(System Status) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- (System Status)
api_type:
- NA
---

# || (System Status)

The double vertical bar (**||**) command prints status for the specified system or for all systems that you are currently debugging.

Do not confuse this command with the [**| (Process Status)**](---process-status-.md) command.

```dbgcmd
|| System 
```

## Parameters

*System*

Specifies the system to display. If you omit this parameter, all systems that you are debugging are displayed. For more information about the syntax, see [System Syntax](system-syntax.md).

### Environment

| Item      | Description               |
|-----------|---------------------------|
| Modes     | Multiple target debugging |
| Targets   | Live, crash dump          |
| Platforms | All                       |

## Remarks

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
