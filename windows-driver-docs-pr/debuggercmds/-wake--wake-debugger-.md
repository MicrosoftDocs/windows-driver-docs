---
title: ".wake (Wake Debugger)"
description: "The .wake command causes sleep mode to end. This command is used only when you are controlling the user-mode debugger from the kernel debugger."
keywords: ["Wake Debugger (.wake) command", "controlling the user-mode debugger from the kernel debugger, Wake Debugger (.wake) command", ".wake (Wake Debugger) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .wake (Wake Debugger)
api_type:
- NA
---

# .wake (Wake Debugger)

The **.wake** command causes sleep mode to end. This command is used only when you are controlling the user-mode debugger from the kernel debugger.

```dbgcmd
.wake PID
```

## Parameters

<span id="_______PID______"></span><span id="_______pid______"></span> *PID*   
The process ID of the user-mode debugger.

## Environment

|  Item       | Description               |
|--- |--- |
|Modes|controlling the user-mode debugger from the kernel debugger|
|Targets|live debugging only|
|Platforms|all|

## Additional Information

For more details, see [Controlling the User-Mode Debugger from the Kernel Debugger](../debugger/controlling-the-user-mode-debugger-from-the-kernel-debugger.md). For information about how to find the process ID of the debugger, see [Finding the Process ID](../debugger/finding-the-process-id.md).

## Remarks

When you are controlling the user-mode debugger from the kernel debugger and the system is in sleep mode, this command can be used to wake up the debugger before the sleep timer runs out.

This command is not issued in the user-mode debugger on the target machine, nor in the kernel debugger on the host machine. It must be issued from a third debugger (KD, CDB, or NTSD) running on the target machine.

This debugger can be started expressly for this purpose, or can be another debugger that happens to be running. However, if there is no other debugger already running, it is easier just to use CDB with the **-wake** [**command-line option**](../debugger/cdb-command-line-options.md).
