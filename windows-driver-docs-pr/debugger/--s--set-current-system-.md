---
title: s (Set Current System)
description: The s command sets or displays the current system number.
keywords: ["s (Set Current System) Windows Debugging"]
ms.date: 08/30/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- s (Set Current System)
api_type:
- NA
---

# ||s (Set Current System)

The **||s** command sets or displays the current system number.

```dbgcmd
||System s 
|| s 
```

Do not confuse this command with the [**s (Search Memory)**](s--search-memory-.md), [**~s (Change Current Processor)**](-s--change-current-processor-.md), [**~s (Set Current Thread)**](-s--set-current-thread-.md), or [**|s (Set Current Process)**](-s--set-current-process-.md) command.

## Parameters

*System*

Specifies the system number to activate. For more information about the syntax, see [System Syntax](system-syntax.md).

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes|Multiple target debugging|
|Targets|Live, crash dump|
|Platforms|All|

## Remarks

The **||s** command is useful when you are debugging multiple targets or working with multiple dump files.  For more information about these kinds of sessions, see [Debugging Multiple Targets](debugging-multiple-targets.md).

If you use the **||s** syntax, the debugger displays information about the current system.

This command also disassembles the current instruction for the current system, process, and thread.

**Note**  There are complications, when you debug live targets and dump targets together, because commands behave differently for each type of debugging. For example, if you use the **g (Go)** command when the current system is a dump file, the debugger begins executing, but you cannot break back into the debugger, because the break command is not recognized as valid for dump file debugging.
