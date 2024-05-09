---
title: ".ttime (Display Thread Times)"
description: "The .ttime command displays the running times for a thread."
keywords: [".ttime (Display Thread Times) Windows Debugging"]
ms.date: 08/01/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- .ttime (Display Thread Times)
api_type:
- NA
---

# .ttime (Display Thread Times)

The **.ttime** command displays the running times for a thread.

```dbgcmd
.ttime 
```

## Environment

| Item      | Description      |
|-----------|------------------|
| Modes     | user mode only   |
| Targets   | live, crash dump |
| Platforms | x86 only         |

## Remarks

This command only works in user mode. In kernel mode you should use [**!thread**](-thread.md) instead. This command works with user-mode minidumps as long as they were created with the **/mt** or **/ma** options; see [User-Mode Dump Files](../debugger/user-mode-dump-files.md) for details.

The **.ttime** command shows the creation time of the thread, as well as the amount of time it has been running in kernel mode and in user mode.

Here is an example:

```dbgcmd
0:000> .ttime
Created: Sat Jun 28 17:58:42 2003
Kernel:  0 days 0:00:00.131
User:    0 days 0:00:02.109
```
