---
title: Debugger Engine API Overview
description: Debugger Engine API Overview
keywords: ["Debugger Engine API, overview"]
ms.date: 05/23/2017
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

**Important**  The IDebug\* interfaces such as [**IDebugEventCallbacks**](/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebugeventcallbacks) interface, although COM like, are not proper COM APIs. Calling these interfaces from managed code is an unsupported scenario. Issues such as garbage collection and thread ownership, lead to system instability when the interfaces are called with managed code.

 

 

