---
title: "~s (Change Current Processor)"
description: "The ~s command sets which processor is debugged on a multiprocessor system.In kernel mode, ~s changes the current processor."
keywords: ["Change Current Processor (~s) command", "multiprocessor computer, Change Current Processor (~s) command", "processors", "~s (Change Current Processor) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ~s (Change Current Processor)
api_type:
- NA
---

# ~s (Change Current Processor)

The **~s** command sets which processor is debugged on a multiprocessor system.

In kernel mode, **~s** changes the current processor. Do not confuse this command with the [**~s (Set Current Thread)**](-s--set-current-thread-.md) command (which works only in user mode), the [**|s (Set Current Process)**](-s--set-current-process-.md) command, the [**||s (Set Current System)**](--s--set-current-system-.md) command, or the [**s (Search Memory)**](s--search-memory-.md) command.

```dbgcmd
~Processor s
```

## Parameters

<span id="_______Processor______"></span><span id="_______processor______"></span><span id="_______PROCESSOR______"></span> *Processor*   
Specifies the number of the processor to debug.

## Environment

|  Item       | Description       |
|-----------|------------------|
| Modes     | kernel mode only |
| Targets   | live, crash dump |
| Platforms | all              |

## Remarks

You can specify processors only in kernel mode. In user mode, the tilde (~) refers to a thread.

You can immediately tell when you are working on a multiple processor system by the shape of the kernel debugging prompt. In the following example, 0: means that you are debugging the first processor in the computer.

```dbgcmd
0: kd>
```

Use the following command to switch between processors:

```dbgcmd
0: kd> ~1s
1: kd>
```

Now the second processor in the computer that is being debugged.

## See also

[Multiprocessor Syntax](multiprocessor-syntax.md)
