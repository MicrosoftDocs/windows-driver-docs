---
title: Debugging Targets on Multiple Computers
description: Debugging Targets on Multiple Computers
ms.assetid: 3c4fa2d9-1443-4460-b570-9415a3600393
keywords: ["multiple computer debugging", "system, targets on multiple computers", "remote debugging, multiple computers"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debugging Targets on Multiple Computers


## <span id="ddk_debugging_targets_on_multiple_computers_dbg"></span><span id="DDK_DEBUGGING_TARGETS_ON_MULTIPLE_COMPUTERS_DBG"></span>


The debugger can debug multiple dump files or live user-mode applications at the same time. See [Debugging Multiple Targets](debugging-multiple-targets.md) for details.

You can debug multiple live targets even if the processes are on different systems. Simply start a process server on each system, and then use the **-premote** parameter with [**.attach (Attach to Process)**](-attach--attach-to-process-.md) or [**.create (Create Process)**](-create--create-process-.md) to identify the proper process server.

The *current* or *active* system is the system currently being debugged. If you use the **.attach** or **.create** command again without specifying the **-premote** parameter, the debugger will attach to, or create, a process on the current system.

For details on how to control such a debugging session, see [Debugging Multiple Targets](debugging-multiple-targets.md).

 

 





