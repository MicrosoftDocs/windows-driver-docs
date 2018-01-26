---
title: Breakpoints
description: Breakpoints
ms.assetid: f805667c-7ee1-4f66-bfc5-7e3b90b35b86
keywords: ["Debugger Engine, breakpoints"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Breakpoints


The [debugger engine](introduction.md#debugger-engine) can create and monitor breakpoints in the target.

There are two types of breakpoints that the engine can insert into a target: software breakpoints and processor breakpoints.

-   *Software breakpoints* are inserted into the target's code by modifying the processor instruction at the breakpoint's location. The debugger engine keeps track of such breakpoints; they are invisible to the clients reading and writing memory at that location. A software breakpoint is triggered when the target executes the modified instruction.

-   *Processor breakpoints* are inserted into the target's processor by the debugger engine. A processor breakpoint can be triggered by different actions, for example, executing an instruction at the location (like software breakpoints), or reading or writing memory at the breakpoint's location. Support for processor breakpoints is dependent on the processor in the target's computer.

A breakpoint's address can be specified by an explicit address, by an expression that evaluates to an address, or by an expression that might evaluate to an address at a future time. In the last case, each time a module is loaded or unloaded in the target, the engine will attempt to reevaluate the expression and insert the breakpoint if it can determine the address; this makes it possible to set breakpoints in modules before they are loaded.

A number of parameters can be associated with a breakpoint to control its behavior:

-   A breakpoint can be associated with a particular thread in the target and will only be triggered by that thread.

-   A breakpoint can have debugger commands associated with it; these commands will automatically be executed when the breakpoint is triggered.

-   A breakpoint can be flagged as inactive until the target has passed it a specified number of times.

-   A breakpoint can be automatically removed the first time it is triggered.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For details about using breakpoints, see [Using Breakpoints](setting-breakpoints.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Breakpoints%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




