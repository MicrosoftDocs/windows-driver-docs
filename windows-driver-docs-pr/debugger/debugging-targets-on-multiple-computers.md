---
title: Debugging Targets on Multiple Computers
description: Debugging Targets on Multiple Computers
keywords: ["multiple computer debugging", "system, targets on multiple computers", "remote debugging, multiple computers"]
ms.date: 05/23/2017
---

# Debugging Targets on Multiple Computers


## <span id="ddk_debugging_targets_on_multiple_computers_dbg"></span><span id="DDK_DEBUGGING_TARGETS_ON_MULTIPLE_COMPUTERS_DBG"></span>


The debugger can debug multiple dump files or live user-mode applications at the same time. See [Debugging Multiple Targets](debugging-multiple-targets.md) for details.

You can debug multiple live targets even if the processes are on different systems. Simply start a process server on each system, and then use the **-premote** parameter with [**.attach (Attach to Process)**](../debuggercmds/-attach--attach-to-process-.md) or [**.create (Create Process)**](../debuggercmds/-create--create-process-.md) to identify the proper process server.

The *current* or *active* system is the system currently being debugged. If you use the **.attach** or **.create** command again without specifying the **-premote** parameter, the debugger will attach to, or create, a process on the current system.

For details on how to control such a debugging session, see [Debugging Multiple Targets](debugging-multiple-targets.md).

 

 





