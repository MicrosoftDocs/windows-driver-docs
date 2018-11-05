---
title: Debugger Engine Overview
description: Debugger Engine Overview
ms.assetid: e3cd8a1d-dd07-480b-bc3b-4f6acc647167
keywords: ["Debugger Engine", "Debugger Engine, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debugger Engine Overview


The *debugger engine* (DbgEng.dll), typically referred to as the *engine*, provides an interface for examining and manipulating debugging targets in [*user mode*](https://msdn.microsoft.com/library/windows/hardware/ff556343#wdkgloss-user-mode) and [*kernel mode*](https://msdn.microsoft.com/library/windows/hardware/ff556299#wdkgloss-kernel-mode) on Microsoft Windows.

The debugger engine can acquire targets, set [breakpoints](multiprocessor-syntax.md#breakpoints), monitor [events](events.md#events), query [symbols](symbols.md#symbols), read and write to memory, and control [threads](controlling-threads-and-processes.md#threads) and [processes](controlling-threads-and-processes.md#processes) in a target.

You can use the debugger engine to write both debugger extension libraries and stand-alone applications. Such applications are referred to as *debugger engine applications*. A debugger engine application that uses the full functionality of the debugger engine is called a *debugger*. For example, WinDbg, CDB, NTSD, and KD are debuggers; the debugger engine provides the core of their functionality.

**Engine Concepts:**

[Debugging Session and Execution Model](debugging-session-and-execution-model.md)

[Client Objects](client-objects.md)

[Input and Output](input-and-output.md)

**Examining and Manipulating Targets:**

[Targets](targets.md)

[Events](events.md)

[Breakpoints](breakpoints3.md)

[Symbols](symbols.md)

[Memory](memory.md)

[Threads and Processes](threads-and-processes.md)

### <span id="incomplete_documentation"></span><span id="INCOMPLETE_DOCUMENTATION"></span>Incomplete Documentation

This is a preliminary document and is currently incomplete.

For many concepts relating to the debuggers and the debugger engine that are not yet documented here, look in the [Debugging Techniques](debugging-techniques.md) section of this documentation.

To obtain some of the currently undocumented functionality of the debugger engine API, use the [**Execute**](https://msdn.microsoft.com/library/windows/hardware/ff543208) method to execute individual debugger commands.

 

 





