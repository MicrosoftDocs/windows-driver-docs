---
title: Debugger Engine API Overview
description: Debugger Engine API Overview
ms.assetid: ea8beca6-93b7-4537-af89-78d599b8b982
keywords: ["Debugger Engine API, overview"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugger%20Engine%20API%20Overview%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




