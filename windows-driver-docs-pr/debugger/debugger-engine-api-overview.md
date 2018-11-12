---
title: Debugger Engine API Overview
description: Debugger Engine API Overview
ms.assetid: ea8beca6-93b7-4537-af89-78d599b8b982
keywords: ["Debugger Engine API, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debugger Engine API Overview


## <span id="ddk_debugger_engine_overview_dbx"></span><span id="DDK_DEBUGGER_ENGINE_OVERVIEW_DBX"></span>


This section includes:

[Interacting with the Engine](interacting-with-the-engine.md)

[Using Input and Output](using-input-and-output.md)

[Monitoring Events](monitoring-events.md)

[Using Breakpoints](using-breakpoints2.md)

[Memory Access](memory-access.md)

[Examining the Stack Trace](examining-the-stack-trace.md)

[Controlling Threads and Processes](controlling-threads-and-processes.md)

[Using Symbols](using-symbols.md)

[Using Source Files](using-source-files.md)

[Connecting to Targets](connecting-to-targets.md)

[Target Information](target-information.md)

[Target State](target-state.md)

[Calling Extensions and Extension Functions](calling-extensions-and-extension-functions.md)

[Assembling and Disassembling Instructions](assembling-and-disassembling-instructions.md)

**Important**  The IDebug\* interfaces such as [**IDebugEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff550550) interface, although COM like, are not proper COM APIs. Calling these interfaces from managed code is an unsupported scenario. Issues such as garbage collection and thread ownership, lead to system instability when the interfaces are called with managed code.

 

 

 





