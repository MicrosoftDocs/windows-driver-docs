---
title: "~u (Unfreeze Thread)"
description: "The ~u command unfreezes the specified thread.Do not confuse this command with the U (Unassemble) command."
keywords: ["~u (Unfreeze Thread) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ~u (Unfreeze Thread)
api_type:
- NA
---

# ~u (Unfreeze Thread)

The **~u** command unfreezes the specified thread.

Do not confuse this command with the [**U (Unassemble)**](u--unassemble-.md) command.

```dbgcmd
~Thread u 
```

## Parameters

<span id="_______Thread______"></span><span id="_______thread______"></span><span id="_______THREAD______"></span> *Thread*   
Specifies the thread or threads to unfreeze. For more information about the syntax, see [Thread Syntax](thread-syntax.md).

## Environment

| Item      | Description      |
|-----------|------------------|
| Modes     | User mode only   |
| Targets   | Live, crash dump |
| Platforms | All              |

## Additional Information

For more information about how frozen threads behave and a list of other commands that control the freezing and suspending of threads, see [Controlling Processes and Threads](../debugger/controlling-processes-and-threads.md).

## Remarks

You can specify threads only in user mode. In kernel mode, the tilde (~) refers to a processor.

The following examples show you how to use the ~ commands.

The following command displays the current status of all threads.

```dbgcmd
0:000> ~* k
```

The following command freeze the thread that caused the current exception.

```dbgcmd
0:000> ~# f
```

The following command checks that the status of this thread is suspended.

```dbgcmd
0:000> ~* k
```

The following command unfreezes thread number 123.

```dbgcmd
0:000> ~123 u
```
