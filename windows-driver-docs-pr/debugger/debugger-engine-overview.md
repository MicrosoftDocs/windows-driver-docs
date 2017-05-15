---
title: Debugger Engine Overview
description: Debugger Engine Overview
ms.assetid: e3cd8a1d-dd07-480b-bc3b-4f6acc647167
keywords: ["Debugger Engine", "Debugger Engine, overview"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugger%20Engine%20Overview%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




