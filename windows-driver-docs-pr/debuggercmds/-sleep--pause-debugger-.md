---
title: ".sleep (Pause Debugger)"
description: "The .sleep command causes the user-mode debugger to pause and the target computer to become active. This command is only used when you are controlling the user-mode debugger from the kernel debugger."
keywords: ["Pause Debugger (.sleep) command", "controlling the user-mode debugger from the kernel debugger, Pause Debugger (.sleep) command", ".sleep (Pause Debugger) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .sleep (Pause Debugger)
api_type:
- NA
---

# .sleep (Pause Debugger)

The **.sleep** command causes the user-mode debugger to pause and the target computer to become active. This command is only used when you are controlling the user-mode debugger from the kernel debugger.

```dbgcmd
.sleep milliseconds
```

## Parameters

<span id="_______milliseconds______"></span><span id="_______MILLISECONDS______"></span> *milliseconds*   
Specifies the length of the pause, in milliseconds.

## Environment

|  Item       | Description               |
|--- |--- |
|Modes|controlling the user-mode debugger from the kernel debugger|
|Targets|live debugging only|
|Platforms|all|

## Additional Information

For details and information about how to wake up a debugger in sleep mode, see [Controlling the User-Mode Debugger from the Kernel Debugger](../debugger/controlling-the-user-mode-debugger-from-the-kernel-debugger.md).

## Remarks

When you are controlling the user-mode debugger from the kernel debugger, and the user-mode debugger prompt is visible in the kernel debugger, this command will activate sleep mode. The kernel debugger, the user-mode debugger, and the target application will all freeze, but the rest of the target computer will become active.

If you use this command in any other scenario, it will simply freeze the debugger for a period of time.

The sleep time is in milliseconds and interpreted according to the default radix, unless a prefix such as **0n** is used. Thus, if the default radix is 16, the following command will cause about 65 seconds of sleep:

```dbgcmd
0:000> .sleep 10000
```
